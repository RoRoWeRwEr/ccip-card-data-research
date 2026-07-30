import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const inputPath = path.join(root, "outputs/excel/saudi-credit-cards-unified-consolidated.xlsx");
const outputDir = path.join(root, "working/previews");
await fs.mkdir(outputDir, { recursive: true });
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const summary = await workbook.inspect({ kind: "sheet", include: "id,name", maxChars: 12000 });
await fs.writeFile(path.join(outputDir, "sheet-inspection.ndjson"), summary.ndjson, "utf8");
const names = [
  "دليل الرموز", "دليل البطاقات", "معدلات الاكتساب (عام)", "اكتساب تفصيلي (دقيق)",
  "الرسوم والAPR (دقيق)", "مراحل البونص (دقيق)", "المزايا (دقيق)", "سجل التعارضات",
  "لوحة التغطية", "المنهجية", "بنوك متبقية ومستبعدة", "Chrome V4 - دليل",
  "Chrome V4 - تفاصيل", "مطابقة وتوحيد", "مصادر ومراجع", "حقول مفقودة", "قرارات وتعارضات",
];
let rendered = 0;
const failures = [];
for (let i = 0; i < names.length; i++) {
  try {
    const sheet = workbook.worksheets.getItem(names[i]);
    const used = sheet.getUsedRange();
    const maxRows = Math.min(used?.rowCount ?? 30, 30);
    const maxCols = Math.min(used?.columnCount ?? 12, 12);
    const range = sheet.getRangeByIndexes(0, 0, maxRows, maxCols).address;
    const blob = await workbook.render({ sheetName: names[i], range, scale: 0.8, format: "png" });
    const safe = String(i + 1).padStart(2, "0") + "-" + names[i].replaceAll("/", "-") + ".png";
    await fs.writeFile(path.join(outputDir, safe), new Uint8Array(await blob.arrayBuffer()));
    rendered++;
  } catch (error) {
    failures.push({ sheet: names[i], error: String(error?.message ?? error).slice(0, 500) });
  }
}
console.log(JSON.stringify({ rendered, failures, outputDir }));
if (failures.length) process.exitCode = 1;
