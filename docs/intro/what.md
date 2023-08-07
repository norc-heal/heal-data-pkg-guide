# What is a data package? 

Data sharing requirement often only mention sharing data (e.g. "You must share all data underlying published results"). Aside from the data itself, it is important for investigators to provide context and usability information, including: what questions was the study group trying to answer in collecting the data, how did they design study experiment(s)/activity(s) to answer those questions, how was data collected, what data was collected, what is in each data file, how to use it, how it relates to other data files, how it relates to published results, etc. 

**In fact, supporting or metadata files that include this context and usability information are arguably as or more important than the data itself**. Without the context information, it is difficult for potential secondary data users or collaborators to get even a high-level sense of whether it may be productive to request access to study data or to reach out regarding a collaboration with the originating study group. Without the usability information, it is difficult for potential secondary data users or collaborators to get a more granular view of whether the collected data may be usable for their secondary data use purposes, and it may be difficult or impossible to actually use the data for their secondary data use purposed. 

## A data package includes:

1. Data produced/collected by the study 
2. Non-data supporting files produced for/by the study 
3. Standard data package metadata files (study-level and file-level)

## Standard data package metadata - Study-level  

* **Experiment Tracker**: one per study; an inventory of experiments or activities included in the study; for a clinical trial, this may be simply one experiment equal to the registered clinical trial activity; for a basic biology study, this may be a listing of several orthogonal experiments used altogether to address and advance the study aims, 
* **Resource Tracker**: one per study; an inventory of all data and non-data supporting files produced during the course of the study (or, in some cases, only those which will be shared in a public data repository), including a description of what is in the file or what the file represents, file relationships and dependencies, and whether/how each file is shareable in a public repository or not  

## Standard data package metadata - File-level 

* **Data Dictionary**: one per tabular data file; an inventory of variables included in a tabular data file 
* **Results Tracker**: one per multi-result file (e.g. manuscript); an inventory of figure, table, and text results included in a multi-result file 