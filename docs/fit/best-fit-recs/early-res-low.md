# EARLY, RESULTS-SUPPORT, LOW RESOURCES


## GRAPHIC AT TOP


### What to do **right away**    
    
{{ external_markdown('https://raw.githubusercontent.com/norc-heal/heal-data-pkg-guide/modules/docs/fit/best-fit-recs/modules/set-success.md', '## Early') }}

* Initialize your [Data Package](../terms/index.md#data-package)  
  * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
    * If all study files/resources are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
    * If not, create this folder/directory in a disc location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package  

### What to do **when your manuscript is finalized**

* Audit the [final result products](../terms/index.md#final-result-products) (e.g. figure, figure panel, table, text statement) produced by your study that are shared in the manuscript - create a list of final result products
* For each final result product shared in your manuscript, 
  * Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for that final result product (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
  * Audit the full set of study experiments/activities that produced supporting data or other support for that final result product
* If any associated file/dependency for any of the final result products is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for each associated file/dependency that is a tabular data file, AND add this Data Dictionary to the list of associated files/dependencies for that final result product
  * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
    * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
    * Add all variables in the tabular data file to your Data Dictionary
      * Use the [Data Dictionary schema](../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
* Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
  * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-experiment-tracker.csv)
    * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
  * Add all experiments or other study activities that produced supporting data or other support for any of the final result products shared in your manuscript to your Experiment Tracker
    * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
* Start your [Results Tracker(s)](../terms/index.md#results-tracker) - one per manuscript
  * Start to create a Results Tracker to document the [final result products](../terms/index.md#final-result-products) (e.g. figures, tables) that will be published as part of your manuscript or report
    * Start your Results Tracker by initializing an empty Results Tracker file based on the [Results Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-results-tracker.csv)
      * Save your Results Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-results-tracker-my-manuscript-file.csv" (i.e. the file name starts with the prefix "heal-csv-results-tracker-", you append the name of the manuscript or report to which the Results Tracker applies, and save as a csv file)
    * Add all final result products shared in the manuscript or report to a Results Tracker
      * Use the [Results Tracker schema](../schemas/md_results_tracker.md) to understand what each "question"/field in the Results Tracker means and how to "answer"/complete each "question"/field 
      * The Results Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each final result product (i.e. files that are required to interpret, replicate, or use the result)
* Finalize the Results Tracker for the completed manuscript or report
  * Check that all final result products shared in the manuscript or report are listed in the associated Results Tracker - Add any that are missing
  * Check that figure/table numbers for all final result products shared in the manuscript are accurately reflected in the final result product entry in the manuscript's associated Results Tracker - Correct any that need to be updated
* Start your [Resource Tracker](../terms/index.md#resource-tracker)
  * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](https://raw.githubusercontent.com/norc-heal/heal-data-pkg-tool/main/heal-csv-resource-tracker.csv)
    * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
  * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
    * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
    * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
* Add your manuscript and its [associated Results Tracker](../terms/index.md#associated-results-tracker) to your Resource Tracker 
  * Do not add the Results Tracker for your manuscript to your Resource Tracker until it is finalized 
* For each final result product shared in your manuscript, review your audit list of associated files/dependencies for that result product (including associated files/dependencies of immediate dependencies), and determine which of these files will be shared in a public repository 
* For each final result product shared in your manuscript, add each of the associated files/dependencies for that final result product to your Resource Tracker (including associated files/dependencies of immediate associated files/dependencies) **ONLY if the file will be shared in a public repository** 
  * Check that all final result product [associated files/dependencies](../terms/index.md#associated-filesdependencies) (listed in the associated files/dependencies fields for each final result product listed in the Results Tracker) are also listed as study resource/files in your Resource Tracker **ONLY if the file will be shared in a public repository** - Add any that are missing