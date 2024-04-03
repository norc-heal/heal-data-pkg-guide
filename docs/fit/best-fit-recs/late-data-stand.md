# LATE, DATASET-SHARING, STANDARD

## GRAPHIC AT TOP


### What to do **right away**   

{{ external_markdown('https://raw.githubusercontent.com/norc-heal/heal-data-pkg-guide/modules/docs/fit/best-fit-recs/modules/set-success.md', '## Late') }}


* Initialize your [Data Package](../../terms/index.md#data-package)  
  * Create a ["dsc-pkg" folder/directory](../../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../../terms/index.md#standard-data-package-metadata-files) for your data package
    * If all [study files/resources](../../terms/index.md#study-filesresources) are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
    * If not, create this folder/directory in a disk location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package 


### What to do **when your dataset-of-interest is finalized**

* Audit the full set of study experiments/activities that produced supporting data or other support for the final dataset-of-interest
* Start your [Experiment Tracker](../../terms/index.md#experiment-tracker) 
  * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-experiment-tracker.csv)
    * Save your Experiment Tracker in your ["dsc-pkg" folder](../../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
  * Add all experiments or other study activities that produced supporting data or other support for the final dataset-of-interest to your Experiment Tracker
    * Use the [Experiment Tracker schema](../../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
* Audit the full set of [associated files/dependencies](../../terms/index.md#associated-filesdependencies) for the final dataset-of-interest (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
* If the dataset-of-interest, or any associated file/dependency of the dataset-of-interest is a [tabular data file](../../terms/index.md#tabular-data-file), create a [Data Dictionary](../../terms/index.md#data-dictionary) for the tabular dataset-of-interest and for each associated file/dependency that is a tabular data file, AND add these Data Dictionaries to the list of associated files/dependencies for the dataset-of-interest
  * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../../csv-templates/heal-csv-data-dictionary.csv)
    * Save your Data Dictionary in your ["dsc-pkg" folder](../../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
    * Add all variables in the tabular data file to your Data Dictionary
      * Use the [Data Dictionary schema](../../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
* Start your [Resource Tracker](../../terms/index.md#resource-tracker)
  * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-resource-tracker.csv)
    * Save your Resource Tracker in your ["dsc-pkg" folder](../../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
  * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
    * Use the [Resource Tracker schema](../../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
    * The Resource Tracker will ask you to list [associated files/dependencies](../../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
* Add your finalized dataset-of-interest to your Resource Tracker 
* Add each of the associated files/dependencies for the final dataset-of-interest to your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies 
  * Check that all [associated files/dependencies](../../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies - Add any that are missing 