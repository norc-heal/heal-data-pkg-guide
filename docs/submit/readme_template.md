# Suggested README Template for Submission Along with Shareable Data Package

Get Started

This catalog includes:

* Data packaged according to HEAL Data Sharing Consultancy (DSC) specifications
  * Data packaging specifications: link
  * Resource tracker specifications: [link](https://norc-heal.github.io/heal-data-pkg-guide/schemas/md_resource_tracker/)
  * Experiment tracker specifications: [link](https://norc-heal.github.io/heal-data-pkg-guide/schemas/md_experiment_tracker/)
  * Results tracker specifications: [link](https://norc-heal.github.io/heal-data-pkg-guide/schemas/md_results_tracker/)
  * Data dictionary specifications: [link](https://norc-heal.github.io/heal-data-pkg-guide/schemas/md_data_dictionary/)

* README
  * file-name: readme.txt
  * description: this file provides an overview of the shareable data package(s) shared and how to determine which files are shared in each shareable data package

* Resource tracker
  * file-name: heal-csv-resource-tracker.csv
  * description: this file provides an overview of study files, whether shared or not (denoted by indicator variable), as well as file dependencies; originating study group may provide description and other information about files that are not shared in a public data repository, especially if these unshared files are dependencies of a shared file

* Shareable data package(s)
  * Description: Includes study files shared by the originating study group under specific access regime(s) (e.g., open-access now, managed-access now, open-access after a specified dat, managed-access after a specific date)
  * Shareable data packages:
    * my-study-open-access
      * access-regime: open-access now
      * created: [insert creation date and time]
      * file-name: [insert file name of zip file]
      * files-included:
        * instructions: files with a value of 1 in [resource-tracker-flag-name: open-access-shareable-data-package OR managed-access-shareable-data-package] column of heal-csv-resource-tracker file are included in the shareable data package
    * my-study-managed-access
      * access-regime: managed-access now
      * created: [insert creation date and time]
      * file-name: [insert file name of zip file]
      * files included:
        * instructions: files with a value of 1 in [resource-tracker-flag-name: open-access-shareable-data-package OR managed-access-shareable-data-package] column of heal-csv-resource-tracker file are included in the shareable data package
