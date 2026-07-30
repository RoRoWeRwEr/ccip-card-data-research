# Consolidated Master Data Reference

Generated: 2026-07-30. This is the continuation document for the Saudi payment-card working dataset.

## Purpose and scope boundary

The deliverable consolidates inherited workbook records, the prior Claude reference, Chrome V4 official-site research, and the available document corpus without claiming final currency or completeness. It does not modify or feed the main CCIP platform.

## Current state

- Original master: 196 card records, 19 issuer names, 11 original worksheets.
- Original `calcTier`: precise 65, estimated 98, unavailable 33.
- Chrome V4: 165 card-guide records and 443 structured detail rows across nine bank sections.
- Exact `card_id` links: 67.
- Unmatched/new identifier records preserved provisionally: 98.
- Conflicts preserved: 146 (48 inherited workbook entries; 98 field-level differences detected during exact-ID reconciliation).
- Missing-field backlog rows: 74.
- Consolidated workbook: `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`.

## Sources and authority

See `docs/REPOSITORY_INVENTORY.md` for hashes, sizes, extractability, and bank mappings. The provisional priority is: current tariff; product T&Cs; current product page; rewards terms; FAQ/campaign; payment network; traceable prior research; unsupported workbook value; secondary source. Conflicts are preserved regardless of rank until applicability and date are established.

## Workbook structure

All original sheets remain. Six additive sheets were created: Chrome card guide, Chrome detail staging, reconciliation, source registry, missing fields, and decisions/conflicts. Original formulas, formatting objects, tables, filters, comments, hyperlinks, validations, merged cells, hidden states, and frozen panes are compared during validation.

## Banks

Al Rajhi Bank, Alinma Bank, Alinma Pay, American Express Saudi Arabia, Arab National Bank, Bank Albilad, Bank Aljazira, Banque Saudi Fransi, Barq (Bank Aljazira digital wallet), D360 Bank, Emirates NBD KSA, Gulf International Bank Saudi Arabia (meem), Mobily Pay, Riyad Bank, STC Bank, Saudi Awwal Bank, Saudi Investment Bank (SAIB), Saudi National Bank, TIQMO

## Card categories in the original master

بطاقة ائتمانية, بطاقة ائتمانية (مرابحة), بطاقة حسم شهري (Charge), بطاقة خصم (ليست مدى — شبكة Visa خصم مباشر), بطاقة متخصصة (رواتب/غير استهلاكية), بطاقة مسبقة الدفع, غير مؤكَّد (Charge أم ائتمانية), مسبقة الدفع (Prepaid)

## Data conventions and decisions

- `precise`, `estimated`, and `unavailable` retain the inherited definitions below.
- Direct evidence, normalization, inference, conflict, missing data, provisional decisions, and confirmed decisions are distinct states.
- Exact IDs link evidence; only blank fields are candidates for safe enrichment. Populated differences become conflict rows.
- Mismatched namespaces are not force-mapped. The 98 unmatched Chrome records remain source records with `unresolved_identity_do_not_merge` in machine exports.
- No card, historical record, or source file was deleted. No populated master value was silently overwritten.

## Completed work

- Reconstructed repository and workbook state.
- Read all Markdown sources and programmatically inspected all worksheets and document files.
- Parsed Chrome V4 card-guide and detail tables.
- Created additive reconciliation and provenance layers.
- Generated missing-data, conflict, collection-status, audit, change, and final-validation reports.
- Generated CSV/JSON exports without flattening or replacing the original workbook structure.

## Partially completed and outstanding work

- Identifier mapping for unmatched Chrome V4 records requires bank-by-bank identity review.
- Conflicting official values require date/applicability checks.
- Image-only or layout-dependent PDF tables require visual/OCR review where extraction is weak.
- Product availability, fees, APR, rewards, limits, eligibility, and benefits still require final current-source validation.
- Machine exports preserve rich text values; they do not decompose every narrative fee/benefit into atomic database fields.

## Instructions for the next agent

Read `AGENTS.md`, this file, `CONFLICTS_AND_DECISIONS.md`, and `MISSING_INFORMATION.md`. Rerun the scripts before editing. Work bank-by-bank, establish explicit ID aliases, add evidence rather than replacing it, and update counts. Do not restart research or assume unmatched IDs are new products.

## Final-validation plan

Follow `outputs/reports/FINAL_VALIDATION_PLAN.md`. The next recommended action is an explicit identity-mapping pass for the unmatched Chrome namespaces, starting with the highest-volume banks, before selecting any conflicting values.

---

# Inherited Claude master reference (carried forward verbatim)

# تدقيق ملف بطاقات الائتمان الموحَّد (Excel) — الملف المرجعي الرئيسي

**آخر تحديث:** 2026-07-29 · **الغرض:** أي جلسة Claude تعمل على تدقيق/تحديث ملف `saudi-credit-cards-unified V3.xlsx` تقرأ **هذا الملف أولاً** فقط، بدل فتح كل ملفات PDF/docx المصدر أو كل مستندات المشروع الأخرى من جديد. المستندات الأخرى (تدقيقات بنك ببنك) تبقى أرشيفًا للتفاصيل الحرفية عند الحاجة فقط.

## ⚠ قاعدة نطاق ثابتة — لا تُخالَف
هذا المسار **منفصل كليًا** عن أي عمل يخص `index.html` أو مستودع BICC على GitHub أو أداة المقارنة الفعلية للمستخدم النهائي. **لا تلمس GitHub أو index.html أو CARD_DB من هذا المسار إطلاقًا** — ذاك مسار مختلف تمامًا موثَّق بملف `claude/BICC-CURRENT-STATE.md` المنفصل. هذا الملف وملف الإكسل يخصان **فقط** ضمان سلامة/دقة قاعدة بيانات البطاقات كمصدر بيانات مستقل.

---

## 1) هوية الملف

- **الاسم:** `saudi-credit-cards-unified V3.xlsx`
- **الموقع:** مجلد "Credit Cards Terms and Conditions" على جهاز المستخدم (OneDrive — KAPSARC)، متصل عبر device bridge.
- **11 ورقة:** دليل الرموز، دليل البطاقات (الجدول الرئيسي)، معدلات الاكتساب (عام)، اكتساب تفصيلي (دقيق)، الرسوم والAPR (دقيق)، مراحل البونص (دقيق)، المزايا (دقيق)، سجل التعارضات، لوحة التغطية، المنهجية، بنوك متبقية ومستبعدة.
- **الحالة الحالية (2026-07-29):** 196 بطاقة عبر 19 بنك/جهة. توزيع `calcTier`: **precise=65، estimated=98، unavailable=33**.

## 2) المنهجية الثابتة (لا تُعاد صياغتها، تُطبَّق كما هي)

- **calcTier ثلاثي:** `precise` (رقم مباشر مؤكَّد من مصدر أساسي حرفي) / `estimated` (معدل عام تقريبي) / `unavailable` (لا رقم، تُستبعد من الحاسبة).
- **لا اختراع:** أي حقل غير مؤكَّد يُترك فارغًا أو يُعلَّم ⚠ تعارض — لا تقريب يُعرض كحقيقة.
- **لا حذف صامت:** أي بطاقة مكتشفة تُدرج ولو ناقصة البيانات كليًا. الاستثناء الوحيد الدائم: **BSF-13، BSF-14، ALJAZIRA-04** (مستبعدة نهائيًا بقرار سابق مؤكَّد).
- **توثيق التعارضات حرفيًا:** كل تعارض في ورقة "سجل التعارضات" يذكر الرقمين/المصدرين حرفيًا، حالة (مفتوح/محسوم)، وخطوة الحسم المطلوبة.
- **قاعدة "estimated" للعرض النهائي (ملاحظة للمستقبل، وليست قيدًا على الإكسل):** في أداة المقارنة النهائية (index.html)، أي نتيجة محسوبة تلمس مُدخلًا واحدًا estimated تُعرض للمستخدم كـ"تقديري" كاملة، حتى لو بقية المُدخلات precise. **هذا لا يمنع ترقية حقل بعينه بالإكسل من estimated إلى precise متى توفر تأكيد مباشر حرفي من المصدر** — القيدان منفصلان (عرض للمستخدم ≠ تصنيف داخلي بالإكسل).
- **أسلوب التقارير:** بعد كل خطوة، تحديث قصير بنقاط ("سويت كذا" / "أحتاج منك كذا") — بدون تقارير طويلة أو توقف غير ضروري.

## 3) الجدول الزمني المختصر (من الأقدم للأحدث)

| التاريخ | الحدث |
|---|---|
| 2026-07-24 وما قبل | القاعدة الأصلية: 168 بطاقة من CARD_DB الحي بمستودع BICC (GitHub) — أساس البناء الأول. |
| 2026-07-27 | تصحيح ANB-17/18 (unavailable→estimated) + ترقية 11 بطاقة فرسان لـ precise عبر 6 بنوك. |
| 2026-07-28 (جولة 2) | RIYAD-01/02 → precise. إضافة بنك جديد كليًا: **ENBD KSA** (12 بطاقة). |
| 2026-07-28 (جولة 3) | تغطية شاملة لـ11 بنكًا (27 ملف PDF/docx جديد) → 183 بطاقة، 24 ترقية precise جديدة (الراجحي +7، البلاد +12، SAIB +3، ANB +2). 3 اكتشافات جديدة: BALAD-19، SAIB-08، SNB-16. |
| 2026-07-28 (جولة 4) | بنك الجزيرة كامل (12 بطاقة) عبر **Claude in Chrome فعلي** (يحل حجب 403 على WebFetch لهذا النطاق) → كل بطاقاته precise. حُسم تعارض هوية ALJAZIRA-02. |
| 2026-07-29 (هذه الجلسة) | انظر القسم 4 أدناه — التحديثات الأحدث. |

## 4) تحديثات 2026-07-29 (هذه الجلسة تحديدًا)

1. **إضافة بنك كامل كان غائبًا كليًا: American Express Saudi Arabia.** 13 بطاقة (AMEX-01 إلى AMEX-13) أُضيفت عبر كل الأوراق الست، من مصدرين: التدقيق السابق (`claude/card-data-amex-audit-2026-07-27.md`، عبر WebFetch) + قراءة مباشرة لملف الاتفاقية المحلي (`AMERICAN EXPRESS ...v6-en.pdf`، شاملة Annex A/B).
   - **حُسم تعارض قديم:** AMEX-03 (Gold Credit Card، 460 ريال/APR 40.85%) مقابل AMEX-08 (The Gold Card، 1,104 ريال/APR 42.43%) — Annex A الرسمي يفصل الاسمين بوضوح كمنتجين مختلفين. كلاهما الآن precise.
   - **تعارضان جديدان اكتُشفا** (لم يظهرا بالتدقيق السابق): AMEX-01 رسوم سنوية (0 مقابل 345 ريال)، AMEX-09 وجود APR 48.21% رغم تصنيفها Charge.
   - **بطاقة 13 مكتشَفة حديثًا:** "The American Express Card" (اسم مجرَّد) ظهرت فقط بـAnnex A — لم تُذكر بالتدقيق السابق ولا بأي مصدر آخر — بيانات ناقصة جدًا (unavailable).
   - 4 بطاقات Amex مرخَّصة لبنوك أخرى (SABB/SAB/SAIB) سُجِّلت في "بنوك متبقية ومستبعدة" دون تدقيق (خارج نطاق أمكس المباشر).
2. **تصحيح RAJHI-ALFURSAN-INF:** كانت 4.25/3.5 ريال لكل ميل (محلي/دولي) — خطأ استخراج (anb-type error، نسخ من عمود Platinum المجاور). صُحِّحت لـ 3/2 ريال لكل ميل عبر `pdfplumber.extract_tables()` على الجدول الرسمي.
3. **ترقية SNB-16** من estimated إلى precise (نقاط 2.0/2.5 محلي/دولي مؤكَّدة حرفيًا بجدول (3.3) الرسمي).
4. **قرار تصنيف جديد — فئة "فائقة التميز / دعوة حصرية" (Super-Premium / Invitation-Only):** بموافقة صريحة من المستخدم، طُبِّق على **12 بطاقة عبر 6 بنوك** (كل بطاقات World Elite / World Legend / World Legend Exclusive / Infinite Privilege بالملف): SNB-16، ALJAZIRA-10، ANB-01/10/11/12/13، BSF-04، RIYAD-09/11، SAB-08/11. ملاحظة تحليلية مهمة: SNB-16 يحمل نفس معدل نقاط Wessam Platinum الأدنى — التميز هنا بالرسوم/الأهلية لا بمضاعف النقاط.
5. **ترقية RIYAD-10/11/12** (بطاقات الهلال كاش باك) من estimated إلى precise — جدول استرداد نقدي رسمي مصوَّر يؤكد الأرقام تمامًا + يضيف فئتي إنترنت/ألعاب إلكترونية غير موثقتين سابقًا + سقف شهري (10,000 ريال عام، 500 ريال ألعاب).
6. **تحقق نهائي لـSAIB-04:** أُعيدت محاذاة جدول الكاش باك الشرائحي بدقة (بلا فقد بيانات) — النتيجة مطابقة تمامًا لما كان بالملف. أُغلقت كفجوة "تحتاج تحقق".
7. **ملفا ANB المتشابهان** ("ANB Al Fursan Credit Cards.pdf" و"ANB Alfursan Cards contract_EN.pdf"): تأكَّد أنهما **ليسا مكررين فعليًا** (فروق حقيقية بالمحتوى) — **بقرار المستخدم: لا حذف، كلاهما مرجع.** سُحبت منهما البيانات الناقصة المفيدة (رسوم البطاقة الإضافية بالتفصيل: مجانية لأول بطاقتين ثم 50% لكل بطاقة إضافية) وأُضيفت لـANB-17/18.
8. **ملفات SAB الثلاثة** (qatar/noon مكررتان فعليًا، 9jan25 نسخة أقدم مختلفة): **بقرار المستخدم: لا حذف لأي منها — تبقى مرجعًا حتى لو مكررة، لا تأثير على البيانات.**

## 5) فجوات/تعارضات مفتوحة تحتاج قرارًا (لم تُحسم بعد)

| البند | الوصف | الحالة |
|---|---|---|
| AMEX-01 | رسوم سنوية 0 مقابل 345 ريال (Annex A مقابل الموقع الحي) | مفتوح |
| AMEX-08 | 1,104 ريال مقابل 908.5/241.50 (أي رقم يخص Charge تحديدًا) | مفتوح جزئيًا |
| AMEX-09 | APR 48.21% مذكور رغم تصنيف Charge — تناقض غير مفسَّر | مفتوح |
| AMEX-10 | رسوم 1,150 دولار بمصدر واحد فقط | مفتوح |
| AMEX-13 | بطاقة مكتشفة حديثًا، حالة توفرها الفعلية غير مؤكدة | يحتاج بحث مباشر (Chrome) |
| بنك البلاد (تمكين بلس) | تعارضات رسوم تصل لفروق 2.5× بين PDF 2025 وموقع حي 2026 | مفتوح — أولوية |
| SAIB Visa Platinum (SAIB-03) | 300 ريال مقابل مجاني، مؤرَّخ بدقة | مفتوح |
| الراجحي — بونص Marriott | 50,000 نقطة (PDF) مقابل 150,000 عبر 3 مراحل (الموقع الحي) | مفتوح |
| بنك الجزيرة | آلية تحويل النقاط لقيمة نقدية غير منشورة؛ شروط الأهلية غير مذكورة | مفتوح (لا يمنع precise) |
| GIB (meem) | لا يوجد أي ملف/تدقيق مصدري بعد — 4 بطاقات estimated بالكامل | لم يبدأ |
| BSF docx جديد | `BSF EF.01.021.03_Credit_Card_Agreement.docx` ظهر بالمجلد، لم يُفحص إن كان مطابقًا للـPDF المدقَّق | لم يبدأ |
| ~130 بطاقة estimated/unavailable متبقية | التحقق المزدوج (PDF + موقع حي) لم يبدأ بعد لمعظمها | المرحلة القادمة (انظر قسم 6) |

## 6) الخطوة التالية المخطَّطة

بناء برومبت Claude in Chrome احترافي (ملف منفصل: `claude/chrome-prompt-earning-rates-collection.md` — راجعه، قد يحتاج تحديثًا ليطابق هذا الملف) يسمح بإعطاء اسم البنك + رابط الموقع **مرة واحدة فقط**، وتقوم الجلسة تلقائيًا بجمع بيانات كل بطاقات ذلك البنك (رسوم، معدلات اكتساب، APR، بونص، مزايا) بنفس منهجية calcTier/لا اختراع/لا حذف صامت، ثم كتابتها مباشرة بنفس هيكل هذا الإكسل.

## 7) فهرس مستندات المشروع الأخرى (للتفاصيل الحرفية فقط، لا تُقرأ إلا عند الحاجة)

- `claude/card-data-*-audit-*.md` (بنك ببنك): التفاصيل الحرفية الكاملة خلف كل رقم precise لكل بنك.
- `claude/card-data-amex-audit-2026-07-27.md`: التدقيق الأصلي لأمكس (12 بطاقة، قبل إضافة AMEX-13 والتصحيحات أعلاه).
- `claude/index-update-manifest-2026-07-28.md` و`claude/unified-workbook-build-2026-07-28.md`: سجل بناء الإكسل حتى 2026-07-28 (تاريخي، لا حاجة لإعادة قراءته بعد هذا الملف).
- `claude/BICC-CURRENT-STATE.md`: **مسار منفصل تمامًا (GitHub/index.html) — لا علاقة له بهذا المسار، لا تخلط بينهما.**
- `claude/chrome-prompt-earning-rates-collection.md`: مسودة برومبت Chrome سابقة — يُراجَع/يُحدَّث بالخطوة القادمة (قسم 6).
