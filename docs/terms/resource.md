## About the Resource Tracker

## Study-Level Metadata

The resource tracker is an inventory and annotated list of all data and supporting/non-data files for the study. Each row of the resource tracker corresponds to one data or non-data resource. Information in the tracker about each resource includes file path, description, access restrictions, format and corresponding software, and dependencies. The resource tracker is where you will also list and annotate any associated results trackers documenting multi-result files.

See [LINK: Resource Tracker: Associated Files/Dependencies] for more information on how you should document your dependencies, depending on the type and amount of data you are sharing.

For detailed information on the name and definition of each field in the resource tracker, please refer to the [LINK: resource tracker schema].

## Associated Data Dictionary

This is a field within the resource tracker. Wherever possible, you should document data dictionary files for your study using the associated data dictionary field (assoc.file.dd) rather than in associated files/dependencies.

## Associated Protocol

This is a field within the resource tracker. Wherever possible, you should document protocols for your study using the associated protocol field (assoc.file.protocol) rather than in associated files/dependencies.

## Associated Results Tracker

This is a field within the resource tracker. You should document your results tracker(s) using the associated results tracker field (assoc.file.results.tracker) rather than in associated files/dependencies.

## Associated Files/Dependencies

Any file that the study artefact being annotated depends on to be produced, interpreted, or used (e.g. a processed tabular data file may depend on a raw data file(s), plus a code file that implements the statistical analysis plan to be produced, and require a data dictionary to interpret/use)

!!! note
    Data dictionaries and protocols should be shared in the more specific Associated data dictionary, Associated protocol fields in the resource tracker wherever possible

How you annotate the dependencies of a file in the resource tracker will depend on whether you are annotating wholistically or minimally.

<details>
<summary> If you are annotating artefacts wholistically</summary>
    
   <b> Use the 'one layer deep' approach</b>: list only the immediate dependencies needed to produce/interpret/use the artefact.<br>
   <br>
    <li> List each dependency in the resource tracker in its own row/entry</li>
    <li> For each row, list dependencies of that file one layer deep</li>
    <li> Continue until you are annotating files with no dependencies</li>

</details>

<details>
<summary> If you are annotating artefacts minimally</summary>
    
   <b> Use the 'liberal' approach</b>: list all dependencies.<br>
   <br>
    <li> For a resource, list immediate dependencies needed to produce/interpret/use the artefact plus dependencies of those dependencies</li>
    <li> Continue until you are listing files with no dependencies</li>

</details>


### Example
A processed tabular data file may depend on a raw data file(s), plus a code file that implements the statistical analysis plan to be produced, and require a data dictionary to interpret/use.

| 'One layer deep' Dependencies            | Liberal Dependencies                             |
| :----------------------------------------| :-----------------------------------------------|
|<ul><li>Immediately underlying raw data files,<br> plus a code file that implements the<br> statistical analysis plan and 'transforms'<br> the raw data files into the processed data<br> file, plus the data dictionary for the<br> processed data file</li> | <li>All immediate/one layer deep files, plus</li><li>The statistical analysis plan that was used<br> to produce the code, the data dictionary<br>  for the raw underlying data file(s), a <br> protocol for collection of the raw underlying<br> data file(s), etc.</li><li>If possible, list liberal dependencies in order<br> from most immediate to least immediate.</li>