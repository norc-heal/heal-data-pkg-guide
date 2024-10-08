<!-- Early standard -->

* Create a Data Dictionary for each [tabular data file](../../terms/index.md#tabular-data-file) already produced by or for your study
* Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](https://raw.githubusercontent.com/norc-heal/healdata-utils/pr-integration/data/templates/twofields.csv)
  * Save your Data Dictionary in your ["dsc-pkg" folder](../../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
  * Each row in your Data Dictionary will represent a variable that is collected/populated in your tabular data file 
  * Use the [Data Dictionary schema](../../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field
* Add all variables in the tabular data file to your Data Dictionary
     