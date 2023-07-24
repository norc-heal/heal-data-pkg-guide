
## Results Tracker

The results tracker provider detailed information and annotation for [multi-result files](files.md#multi-result-file) (e.g., manuscript, presentation). Each multi-result file will have a corresponding results tracker. The purpose of this tracker is to track and annotate each single result (e.g., a figure or textual statement) within each multi-result file as well as the data and supporting files upone which each single result depends. Within the result tracker, each row corresponds to one result from the multi-result file. Information eabout each result includes type of result (figure or text), description, and supported claims.

Each results tracker should additionally be listed and annotated as its own row in the [resource tracker](resource.md).

For detailed information on the name and definition of each field in the results tracker, please refer to the [LINK: results tracker schema].

### Associated Files/Dependencies

Any file that the study artefact being annotated depends on to be produced, interpreted, or used (e.g. a processed tabular data file may depend on a raw data file(s), plus a code file that implements the statistical analysis plan to be produced, and require a data dictionary to interpret/use)

How you annotate the dependencies of a file in the result tracker will depend on whether you are annotating wholistically or minimally.

<details>
<summary> If you are annotating artefacts wholistically</summary>
    
   <b> Use the 'one layer deep' approach</b>: list only the immediate dependencies needed to produce/interpret/use the result.<br>
   <br>
    <li> List each dependency in the result tracker in its own row/entry</li>
    <li> For each row, list dependencies of that file one layer deep</li>
    <li> Continue until you are annotating files with no dependencies</li>

</details>

<details>
<summary> If you are annotating artefacts minimally</summary>
    
   <b> Use the 'liberal' approach</b>: list all dependencies.<br>
   <br>
    <li> For a result, list immediate dependencies needed to produce/interpret/use the artefact plus dependencies of those dependencies</li>
    <li> Continue until you are listing files with no dependencies</li>

</details>
mkdo

### Example
A processed tabular data file may depend on a raw data file(s), plus a code file that implements the statistical analysis plan to be produced, and require a data dictionary to interpret/use. For more information on 'one layer deep' and 'liberal' dependency documentation, click here.

| 'One layer deep' Dependencies            | Liberal Dependencies                             |
| :----------------------------------------| :-----------------------------------------------|
|<ul><li>Immediately underlying raw data files,<br> plus a code file that implements the<br> statistical analysis plan and 'transforms'<br> the raw data files into the processed data<br> file, plus the data dictionary for the<br> processed data file</li> | <ul><li>All immediate/one layer deep files, AND</li><li>The statistical analysis plan that was used<br> to produce the code, the data dictionary<br>  for the raw underlying data file(s), a <br> protocol for collection of the raw underlying<br> data file(s), etc.</li><li>If possible, list liberal dependencies in order<br> from most immediate to least immediate.</li></ul>

## Data Dictionary

Each [tabular data file](files.md#tabular-data-file) should have its own data dictionary. The data dictionary describes the content, format, and structure of the data file. Within the data dictionary, each row contains information about each variable such as the name, description, type, format, and encodings. The data dictionary is a critical piece in re-use of the data by future researchers, as it contains information about how to read, format, and interpret the data.

For detailed information on the name and definition of each field in the data dictionary, please refer to the [LINK: data dictionary schema].

!!! note "Helpful tip"
    If you are creating data dictionaries, save the data dictionary with the same filename as the data file, with a "dd-" prefix.

        Example: dd-my-data-1.csv