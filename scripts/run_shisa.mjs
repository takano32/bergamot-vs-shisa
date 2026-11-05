// pyodide-llm の公開サイトをヘッドレス Chrome で開き、Shisa V2.1c LFM2 350M に data/sentences.jsonl を1文ずつ訳させる。
//   node scripts/run_shisa.mjs [url] [出力 jsonl] [件数の上限]
// 環境変数 SHISA_SITE で既定のサイト、SHISA_CHROME で Chrome の実行ファイルを変えられる。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const site = process.argv[2] || process.env.SHISA_SITE || "https://takano32.github.io/pyodide-llm/";
const outFile = process.argv[3] ?? path.join(root, "results/shisa.jsonl");
const limit = Number(process.argv[4] ?? 1e9);
const MODEL = "hf-shisa-v2.1c-lfm2-350m";
const NAMES = { ja: "Japanese", en: "English" };
const rows = fs.readFileSync(path.join(root, "data/sentences.jsonl"), "utf8").trim().split("\n").map((l) => JSON.parse(l)).slice(0, limit);
// 指示文は2種類。SHISA_PROMPT=strict で厳しい版（ノートや説明を付けない、原文の言語に戻さない）。
const prompt = process.env.SHISA_PROMPT === "strict"
  ? (r) => `Translate the following ${NAMES[r.src_lang]} sentence into ${NAMES[r.tgt_lang]}. The output must be written in ${NAMES[r.tgt_lang]}, not in ${NAMES[r.src_lang]}. Reply with the translation only: no notes, no explanations, no alternatives.\n\n${r.src}`
  : (r) => `Translate the following ${NAMES[r.src_lang]} text into ${NAMES[r.tgt_lang]}. Output only the translation.\n\n${r.src}`;

fs.mkdirSync(path.dirname(outFile), { recursive: true });
const browser = await chromium.launch({ headless: true, executablePath: process.env.SHISA_CHROME ?? "/usr/bin/google-chrome", args: ["--no-sandbox"] });
const page = await browser.newPage({ viewport: { width: 900, height: 900 } });
page.on("dialog", (d) => d.accept());
page.on("pageerror", (e) => console.log("[pageerror]", String(e)));
const t0 = Date.now();
const log = (...a) => console.log(`${((Date.now() - t0) / 1000).toFixed(0)}s`, ...a);
await page.goto(`${site}?model=${MODEL}`);
// 初回訪問は一度リロードする（Service Worker がスレッド用のヘッダーを付ける）。リロード中の待ちは続行。
const across = async (fn) => { for (;;) { try { return await fn(); } catch (e) { if (!/destroyed|navigat|detached/i.test(String(e.message))) throw e; } } };
let last = "";
const poll = setInterval(async () => { const s = await page.evaluate(() => document.getElementById("status-text")?.textContent ?? "").catch(() => ""); if (s && s !== last) { last = s; log("[status]", s); } }, 3000);
await across(() => page.waitForFunction(() => document.getElementById("run")?.disabled === false || document.querySelector(".error"), null, { timeout: 0 }));
clearInterval(poll);
log("ready:", await page.evaluate(() => document.getElementById("status-text").textContent));
// 設定: 温度 0（貪欲）、最大 300 トークン。ページを読み込み直さず、見えているスライダーに値を入れる。
const settings = await page.evaluate(() => {
  const set = (id, v) => { const e = document.getElementById(id); if (!e) return null; e.value = v; e.dispatchEvent(new Event("input", { bubbles: true })); e.dispatchEvent(new Event("change", { bubbles: true })); return e.value; };
  return { temperature: set("temperature", "0"), steps: set("steps", "300"), seed: set("seed", "1") };
});
log("settings:", JSON.stringify(settings));

const out = fs.createWriteStream(outFile);
for (const r of rows) {
  const before = await page.evaluate(() => document.querySelectorAll(".model .meta").length);
  await page.fill("#prompt", prompt(r));
  const s = Date.now();
  await page.press("#prompt", "Control+Enter");
  await page.waitForFunction((n) => document.querySelectorAll(".model .meta").length > n || document.querySelector(".error"), before, { timeout: 0 });
  const got = await page.evaluate(() => {
    const bubbles = [...document.querySelectorAll(".model .bubble")];
    const b = bubbles.at(-1);
    return { text: b?.textContent ?? "", answer: b?.querySelector(".answer")?.textContent ?? null, meta: [...document.querySelectorAll(".model .meta summary")].at(-1)?.textContent ?? "", error: document.querySelector(".error .bubble")?.textContent ?? "" };
  });
  const rec = { ...r, hyp: (got.answer ?? got.text).trim(), raw: got.text, meta: got.meta, error: got.error, seconds: +((Date.now() - s) / 1000).toFixed(1) };
  out.write(JSON.stringify(rec) + "\n");
  log(r.id, rec.seconds + "s", JSON.stringify(rec.hyp), "|", got.meta);
}
out.end();
await browser.close();
