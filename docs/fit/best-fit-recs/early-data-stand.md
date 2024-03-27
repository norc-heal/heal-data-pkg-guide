# EARLY, DATA-SHARING, STANDARD


## GRAPHIC AT TOP


### What to do **right away**
    
    
* Set yourself up for success
  * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
  * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to these files now, and to future files as they are created
  * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
  * All [study files/resources](../terms/index.md#study-filesresources) should be stored in a location where the person(s)  who will be creating/contributing to your data package documentation can access them all at the same time (e.g. you can have files located on different network drives as long as all network drives can be mounted and accessed at the same time by the person documenting; you CANNOT have files located on two different local computer drives, even if the person documenting can access both computers separately)
* Initialize your [Data Package](../terms/index.md#data-package)  
  * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
    * If all study files/resources are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
    * If not, create this folder/directory in a disc location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package  
* Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
  * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-experiment-tracker.csv)
    * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
  * Add all experiments or other study activities which have already been designed to your Experiment Tracker
    * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field 
* Create a [Data Dictionary](../terms/index.md#data-dictionary) for each existing [tabular data file](../terms/index.md#tabular-data-file)
  * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
    * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
    * Add all variables in the tabular data file to your Data Dictionary
      * Use the [Data Dictionary schema](../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
* Start your [Resource Tracker](../terms/index.md#resource-tracker)
  * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-resource-tracker.csv)
    * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
  * Add all files already produced by/for your study to your Resource Tracker
    * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
    * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource; for tabular data files, this will include a data dictionary for the file)

        

### What to do **continuously, as-you-go**
        
* **As you design new study experiments/activities:**
  * Add new study experiments/activities to your [Experiment Tracker](../terms/index.md#experiment-tracker) as they are designed (as soon as possible)
* **As you create/collect new tabular data files:**
  * Create a [Data Dictionary](../terms/index.md#data-dictionary) for tabular data files as they are created
* **As you create/collect new study files/resources:** 
  * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to study files/resources as they are created
    * If you came up with file organization and naming conventions based on HEAL recommendations at the start of or earlier in your study, continue to consistently apply those conventions as you create/collect new study files
  * Add new study files/resources to your [Resource Tracker](../terms/index.md#resource-tracker) as they are created/collected (as soon as possible), including study analysis/result files

### What to do **when your dataset-of-interest is finalized**

* Add your finalized dataset-of-interest to your Resource Tracker 
* Check that all [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker - Add any that are missing 