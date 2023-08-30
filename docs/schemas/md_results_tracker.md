# HEAL Results Tracker

*HEAL DSC Core Metadata piece to track and provide basic information about results statements or figures in a multi-result file (e.g. a publication) that presents results from your HEAL study. Objective is to list at least all results that have been/will be published in order to describe each result, the data/non-data files each result depends on, and how to use these data/non-data files to reproduce published results.*

## Properties

- **`result.id`** *(string)*: Unique ID assigned to each result; If using the DSC Packaging application to annotate your resource(s), these IDs will be auto-assigned when you use the Add Result Tracker button above the form to add your Result Tracker Directory. Auto-assignment of IDs occurs by searching the directory for any result annotation files already saved, identifying the result ID with the highest result ID number, and adding 1 to that number to get the result ID number and unique result ID for the current result.
- **`description`** *(string)*: A description of your result. For figure results this may be the figure caption. For text results, it is recommended that this text be identical or very similar to the text of result as shared in text of the multi-result file that is published or provided as part of the data package.
- **`category`** *(string)*: Broad category your result falls into; Generally, these categories are: figure, or text. Must be one of: `["", "figure", "table", "text"]`.
- **`assoc.multi.result.file`** *(array)*: The multi-result file(s) in which this result has been shared.
  - **Items** *(string)*
- **`figure.number`** *(array)*: If the result is a figure result, provide the number of the figure as it appears in the corresponding multi-result file; Examples include '1' if the result is in figure 1, or '1a' if the result is in figure 1A. If the result is included in more than one multi-result file, use the Associated Multi-Result File(s) field above to specify all multi-result files in which the result appears, and add the figure number at which the result appears in each of those files in this field, using the same order (e.g. file-1, file-2; figure-number-in-file-1, figure-number-in-file-2).
  - **Items** *(string)*
- **`table.number`** *(array)*: If the result is a table result, provide the number of the table as it appears in the corresponding multi-result file; Examples include '1' if the result is in table 1, or '1a' if the result is in table 1A. If the result is included in more than one multi-result file, use the Associated Multi-Result File(s) field above to specify all multi-result files in which the result appears, and add the table number at which the result appears in each of those files in this field, using the same order (e.g. file-1, file-2; table-number-in-file-1, table-number-in-file-2).
  - **Items** *(string)*
- **`assoc.file.depends.on`** *(array)*: Data and/or non-data supporting files the result depends upon (e.g. data, analysis plan/code, etc.). If you are using the DSC Packaging App and have many result dependencies to add, you can use the Add Multiple Result Dependencies button above the form to reveal an interface where you can drag and drop many files at once. If documenting resources wholistically (i.e. documenting all resources related to a study), only list dependencies one layer deep; if documenting resources minimally (i.e. only documenting resources that will be publicly shared), list dependencies liberally; dependencies can be data, code, protocol, etc.
  - **Items** *(string)*
- **`result.supports`** *(array)*: Describe a larger claim(s) that this result is used to support in text that is published or provided as part of the data package.
  - **Items** *(string)*
- **`restrk.create.date.time`** *(string)*: Date time at which the result annotation file for the result was created; auto-inferred.
- **`restrk.mod.date.time`** *(string)*: Date time at which the result annotation file for the result was last modified; auto-inferred.

