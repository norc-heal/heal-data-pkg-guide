If you are planning to share only files that are necessary to support the results in a multi-result file, such as a manuscript or presentation:

1. Use ['top-down'](../../terms/addtop.md#top-down-annotation-of-study-artefacts) annotation. Do not use 'add-as-you-go' annotation.
    <ol type="a">
        <li><u>Audit multi-result file(s)</u> that need support</li>
        <li><u>Aduit supporting files</u> for each result in multi-result file(s), including sharing status and access level
        <ol class="lower-roman">
            <li><u>Audit dependencies</u> of supporting files, including sharing status and access level</li>
            <li><u>Add data dictionary</u> for any tabular supporting files or dependencies
        </ol>
        <li><u>Create result tracker</u> for each multi-result file (list supporting files for each result in the result tracker 'depends on' field). To determine what approach you should take to listing supporting files for each result, [click here](../../terms/filelevel.md#results-tracker).</li>
        <li><u>Add result tracker</u> to resource tracker
        <li><u>Add supporting files</u> to resource tracker (list dependencies for each supporting resource tracker 'depends on' field)
        <li><b>Notes on wholistic vs. minimal annotation</b>
        <ol class="lower-roman">
            <li><b>If using [wholistic annotation](../../terms/holmin.md#wholistic-annotation-of-study-artefacts):</b>
            <ol type="a">
                <li>When adding supporting files for results in the results tracker, add ['one-layer-deep' dependencies](../../terms/depend.md#one-layer-deep-dependencies).</li>
                <li>When adding dependencies of supporting files in the resource tracker, add ['one-layer-deep' dependencies](../../terms/depend.md#one-layer-deep-dependencies).</li>
            </ol>
            <li><b>If using [minimal annotation](../../terms/holmin.md#minimal-annotation-of-study-artefacts)</b>
            <ol type="a">
                <li>When adding supporting files for results in the results tracker, add ['liberal' dependencies](../../terms/depend.md#liberal-dependencies).</li>
                <li>When adding dependencies of supporting files in the resource tracker, add ['liberal' dependencies](../../terms/depend.md#liberal-dependencies).</li>
            </ol>
        </ol>
    </ol>