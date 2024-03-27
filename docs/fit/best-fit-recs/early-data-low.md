# EARLY, DATA-SHARING, STANDARD


## GRAPHIC AT TOP

``` mermaid
timeline
    title Timeline of Industrial Revolution
    section 17th-20th century
        Industry 1.0 : Machinery, Water power, Steam <br>power
        Industry 2.0 : Electricity, Internal combustion engine, Mass production
        Industry 3.0 : Electronics, Computers, Automation
    section 21st century
        Industry 4.0 : Internet, Robotics, Internet of Things
        Industry 5.0 : Artificial intelligence, Big data, 3D printing
```


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

### What to do when your dataset-of-interest is finalized

* Audit the full set of study experiments/activities that produced supporting data or other support for the final dataset-of-interest
* Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
  * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-experiment-tracker.csv)
    * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
  * Add all experiments or other study activities that produced supporting data or other support for the final dataset-of-interest to your Experiment Tracker
    * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
* Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the final dataset-of-interest (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
* If the dataset-of-interest, or any associated file/dependency of the dataset-of-interest is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for the tabular dataset-of-interest and for each associated file/dependency that is a tabular data file, AND add these Data Dictionaries to the list of associated files/dependencies for the dataset-of-interest
  * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
    * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
    * Add all variables in the tabular data file to your Data Dictionary
      * Use the [Data Dictionary schema](../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
* Start your [Resource Tracker](../terms/index.md#resource-tracker)
  * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-resource-tracker.csv)
    * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
  * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
    * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
    * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
* Add your finalized dataset-of-interest to your Resource Tracker 
* Add each of the associated files/dependencies for the final dataset-of-interest to your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies **ONLY if the file will be shared in a public repository**  
  * Check that all [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies **ONLY if the file will be shared in a public repository** - Add any that are missing 