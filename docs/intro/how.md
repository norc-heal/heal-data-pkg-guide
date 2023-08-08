# How should I go about creating my data package? 

In general, an overview of the process looks like: 

1. Audit relevant files
2. Organize and consistently name your files and folders
3. Add Standard data package metadata - File-level
4. Add Standard data package metadata - Study-level

However, when and exactly how you approach each of these steps will depend on a few factors, including how early on you are in your study, what your data sharing goals are, and the preferences of you and your study group - See below for details OR [Skip ahead to find the best fit for you](../guide/index.md)

## Audit relevant files - all or a subset 
If you are early in your study, you may want to audit all files created/produced by or for the study. If you are later in your study, you may want to audit only files that are needed to support (e.g. interpret, use, or replicate) results you share in a manuscript, or datasets you share in a public data repository.  

## Organize and consistently name your files and folders - HEAL recommendations or not
If you are early in your study, you may want to consider following HEAL recommendations and guidance re: file naming and organization. In order to do this, you may need to change the location of and rename files. This may increase human interpretability and make it easier especially to create and complete your data package's Resource Tracker. 

If you are late in your study, applying HEAL guidance may be too burdensome to be realistic and it may make more sense to leave naming and organization as is.

## Add Standard data package metadata (File-level) - if, when, and how
Currently, file-level standard data package metadata files are the data dictionary (heal-formatted-data-dictionary; one per tabular data file) and the results tracker (heal-formatted-results-tracker; one per multi-result file - e.g. manuscript, poster).

**Data Dictionary**: If your study has not and will not produce any tabular data files, you will not need to create a data dictionary. If your study has or will produce any tabular data files, you will need to create a data dictionary per tabular data file (if multiple tabular data files have the same format with the same variables, you can create a single data dictionary that applies across all of these files). In many cases, the best approach nearly universally will be to go ahead and create a data dictionary for each of your tabular datasets as the dataset is created. Please see here [add link to cli tools and/or desktop tool approach] for instructions on how to create (or at least get a head start on creating) a HEAL formatted data dictionary using just your tabular data file as input.     
**Results Tracker**: If your study is most interested in sharing a dataset of general interest to the scientific/research community, and is less interested in specifically providing clear support for results you share in a manuscript, you may not need to create a results tracker. If your study is interested in providing clear support for results you share in a manuscript, you should create a results tracker. If you are late in your study and have already produced/published a manuscript or result(s) in another format (e.g. poster, white paper, NIH report), you may want to consider starting your results tracker right away. If you are early in your study and have not yet formulated final results text, tables or figures or drafted you may want to consider waiting to start your results tracker until you have reached the study stage of formulating final results text, tables, or figures.   

## Add Standard data package metadata (Study-level) - when, and how
Currently, study-level standard data package metadata files are the experiment tracker (heal-formatted-experiment-tracker; one per study) and the resource tracker (heal-formatted-resource-tracker; one per study).

**Experiment Tracker**: If your study has not and will not produce any tabular data files, you will not need to create a data dictionary. If your study has or will produce any tabular data files, you will need to create a data dictionary per tabular data file (if multiple tabular data files have the same format with the same variables, you can create a single data dictionary that applies across all of these files). You should go ahead and create a data dictionaryPlease see here for instructions on how to  
**Resource Tracker**: If your study is most interested in sharing a dataset of general interest to the scientific/research community, and is less interested in specifically providing clear support for results you share in a manuscript, you may not need to create a results tracker. If your study is interested in providing clear support for results you share in a manuscript, you should create a results tracker. If you are late in your study and have already produced/published a manuscript or result(s) in another format (e.g. poster, white paper, NIH report), you may want to consider starting your results tracker right away. If you are early in your study and have not yet formulated final results text, tables or figures or drafted you may want to consider waiting to start your results tracker until you have reached the study stage of formulating final results text, tables, or figures.  

## Find the best fit for you
See [here](../guide/index.md) for some guidance on determining the best fit for your study group