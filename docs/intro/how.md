# How should I go about creating my data package? 

In general, an overview of the process looks like: 

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

1. Audit relevant files
2. Organize and consistently name your files and folders - using HEAL recommendations for organizing and naming study files/resources
3. Add Standard data package metadata - File-level
4. Add Standard data package metadata - Study-level

</div>

However, when and exactly how you approach each of these steps will depend on a few factors, including how early on you are in your study, what your data sharing goals are, and the preferences of you and your study group - See below for details OR [Skip ahead to find the best fit for you](../guide/index.md)

## Audit relevant files

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

**Variations:** All, or a subset of study files

If you are early in your study, you may want to start auditing your study files rights away AND you may want to audit all files already created/produced by or for the study. 

If you are later in your study, you may want to wait until you are at the study stage of producing the result(s) and/or dataset(s) your study group aims to share before auditing your study files AND you may want to audit only files that are needed to support (e.g. interpret, use, or replicate) results you will share in a manuscript, or datasets you will share in a public data repository.  

</div>

## Organize and consistently name your files and folders 

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

**Variations:** follow HEAL recommendations for organization and naming of study files/resources, or not

If you are early in your study, you may want to consider following HEAL recommendations and guidance re: file naming and organization. In order to do this, you may need to change the location of and rename files. You should start this process right away in order to establish file naming and organizational conventions that you can apply to all study files as they are created/produced. Establishing file naming and organizational conventions based on HEAL recommendations early in your study may increase human interpretability of your files and file structure and make it easier especially to create and complete your data package's Resource Tracker. 

If you are late in your study, applying HEAL recommendations and guidance re: file naming and organization may be too burdensome to be realistic and it may make more sense to leave naming and organization as is.

</div>

## Add Standard data package metadata (File-level)  

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

**Variations:** If, when, and how

Currently, file-level standard data package metadata files are the data dictionary (heal-formatted-data-dictionary; one per tabular data file) and the results tracker (heal-formatted-results-tracker; one per multi-result file - e.g. manuscript, poster).

**Data Dictionary**: 

If your study has not and will not produce any tabular data files, you will not need to create a data dictionary. 

If your study has or will produce any tabular data files, you will need to create a data dictionary per tabular data file (if multiple tabular data files have the same format with the same variables, you can create a single data dictionary that applies across all of these files). In many cases, the best approach nearly universally will be to go ahead and create a data dictionary for each of your tabular datasets as the dataset is created. Please see here [add link to cli tools and/or desktop tool approach] for instructions on how to create (or at least get a head start on creating) a HEAL formatted data dictionary using just your tabular data file as input.     

**Results Tracker**: 

If your study is interested in providing clear support for results you share in a manuscript (required by many journals and funding agen cies), you should create a results tracker. 

* If you are late in your study and have already produced/published a manuscript or result(s) in another format (e.g. poster, white paper, NIH report), you may want to consider starting your results tracker right away. 
* If you are early in your study and have not yet formulated final results text, tables or figures or drafted you may want to consider waiting to start your results tracker until you have reached the study stage of formulating final results text, tables, or figures. 

If your study is most interested in sharing a dataset of general interest to the scientific/research community, and is less interested in specifically providing clear support for results you share in a manuscript, you may not need to create a results tracker. 

</div>

## Add Standard data package metadata (Study-level) - when, and how

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

**Variations:** When, and how

Currently, study-level standard data package metadata files are the experiment tracker (heal-formatted-experiment-tracker; one per study) and the resource tracker (heal-formatted-resource-tracker; one per study).

**Experiment Tracker**: Each study should create and complete an experiment tracker; it is meant to be an inventory of each component experiment or activity that is part of your study. It is expected that some studies (e.g. clinical trials) may have just a single component study experiment/activity, whereas others may have many (e.g. many basic science studies). 

* If you are early on in your study and all component study experiments/activities are already known/designed, go ahead and complete the experiment tracker right away. 
* If you are early on in your study and all component study experiments/activities are NOT already known/designed, you may want to consider starting your experiment tracker right away, adding the experiments/activities that are already known/designed, and then moving forward add each new experiment/activity as it is designed ("as you go" annotation). 
* If you are later on in your study, you may want to wait until you are at the study stage of producing the result(s) and/or dataset(s) your study group aims to share before starting your experiment tracker; this will allow you to pick and choose, adding only the experiments/activities that produced items that support the result(s) or dataset(s) you will share.   

**Resource Tracker**: Each study should create and complete a resource tracker; it is meant to be an inventory of each data or non-data supporting file collected/produced by or for the study, plus all standard data package metadata files added during the data packaging process. 

* If you are early on in your study, you may want to consider starting your resource tracker right away, adding the study files/resources that have already been created, and then moving forward, adding each new study file/resource as it is created ("as you go" annotation). 
* If you are later on in your study, you may want to wait until you are at the study stage of producing the result(s) and/or dataset(s) your study group aims to share before starting your resource tracker; this will allow you to pick and choose, adding only the study resources/files that support the result(s) or dataset(s) you will share. 

</div>

## Find the best fit for you

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

See [here](../guide/index.md) for some guidance on determining the best fit for your study group

</div>