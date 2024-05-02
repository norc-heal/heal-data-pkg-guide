<!-- Dataset sharing early low and late both -->

* You should create a data dictionary for any tabular data files that you will be sharing a public repository
* If the dataset-of-interest is a [tabular data file](../../terms/index.md#tabular-data-file), create a [Data Dictionary](../../terms/index.md#data-dictionary) for the dataset; this will be a dependency of your dataset-of-interest because it is necessary for interpretation
* Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../../csv-templates/heal-csv-data-dictionary.csv)
  * Save your Data Dictionary in your ["dsc-pkg" folder](../../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
  * Add all variables in the tabular data file to your Data Dictionary
    * Use the [Data Dictionary schema](../../schemas/md_data_dictionary.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 