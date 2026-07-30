# Workbook Audit

Generated: 2026-07-30.

## Structure

- Original workbook: `Credit Cards Terms and Conditions/01. saudi-credit-cards-unified V3.xlsx`
- Sheets: 11
- Card records: 196
- Defined names: 0
- Duplicate card IDs: 0
- Duplicate normalized bank/card-name candidates: 0
- Formula cells: 0
- Comments: 0
- Hyperlinks: 0

| sheet | state | rows | columns | formulas | comments | hyperlinks | merged_ranges | hidden_rows | hidden_columns | tables | data_validations | conditional_formatting_ranges | freeze_panes | auto_filter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| دليل الرموز | visible | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| دليل البطاقات | visible | 197 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | C2 |  |
| معدلات الاكتساب (عام) | visible | 148 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| اكتساب تفصيلي (دقيق) | visible | 168 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| الرسوم والAPR (دقيق) | visible | 69 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| مراحل البونص (دقيق) | visible | 27 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| المزايا (دقيق) | visible | 45 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| سجل التعارضات | visible | 49 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | B2 |  |
| لوحة التغطية | visible | 27 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| المنهجية | visible | 40 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |
| بنوك متبقية ومستبعدة | visible | 30 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |

## Quality findings and risks

- The workbook contains no formulas, so there are no formula-reference errors to repair; this also means coverage summaries are static and can drift.
- The main card guide has 196 records and no duplicate `card_id` values.
- Blank mandatory/expected fields are enumerated in `MISSING_INFORMATION.md` rather than inferred.
- Similar card names and changed ID namespaces are identity candidates, not confirmed duplicates.
- Narrative fee, APR, bonus, and benefit fields contain mixed units and composite values. Machine exports preserve them as text to avoid lossy parsing.
- The original master has one Excel table and no named ranges. Generated sheets use filters and frozen headers.
- No original row, column, sheet, formula, comment, hyperlink, validation, merge, or hidden state is intentionally removed.

## Duplicate-name candidates

```json
{}
```
