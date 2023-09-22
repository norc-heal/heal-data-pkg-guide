# Best fit annotation recommendations

## Early



#### Early, Results-support, Standard 

??? note "Study stage == Early <br> Data-sharing goal == Results-support <br> Data-sharing resources == Standard"

        
    Use an ["As-you-go"](../terms/index.md#as-you-go-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#as-you-go-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>
    
    * Start annotating "As-you-go" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to these files now, and to future files as they are created
        * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all study files/resources are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disc location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package  
    * Create a [Data Dictionary](../terms/index.md#data-dictionary) for each existing [tabular data file](../terms/index.md#tabular-data-file)
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add all files already produced by/for your study to your Resource Tracker
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities which have already been designed to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field 
        

    <font size="3"> What to do **continuously, as-you-go**</font>
        
    * **As you create/collect new study files:** 
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to study files/resources as they are created
            * If you came up with file organization and naming conventions based on HEAL recommendations at the start of or earlier in your study, continue to consistently apply those conventions as you create/collect new study files
        * Add new study files/resources to your [Resource Tracker](../terms/index.md#resource-tracker) as they are created/collected (as soon as possible)
    * **As you create/collect new tabular data files:**
        * Create a [Data Dictionary](../terms/index.md#data-dictionary) for tabular data files as they are created
    * **As you design new study experiments/activities:**
        * Add new study experiments/activities to your [Experiment Tracker](../terms/index.md#experiment-tracker) as they are designed (as soon as possible)


    <font size="3"> What to do **when you start to create [final result products](../terms/index.md#final-result-products)** </font>

    
    * For each final result product (e.g. figure, figure panel, table, text statement), as you create it, audit the full subset of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for that final result product (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies 
    * Start your [Results Tracker(s)](../terms/index.md#results-tracker) - one per manuscript or other multi-result file
        * Start to create a Results Tracker to document the final result products (e.g. figures, tables) that will, or may, be published as part of a [multi-result file](../terms/index.md#multi-result-file) (e.g. report or manuscript)
        * Start your Results Tracker by initializing an empty Results Tracker file based on the [Results Tracker csv template](../csv-templates/heal-csv-results-tracker.csv)
            * Save your Results Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-results-tracker-my-manuscript-file.csv" (i.e. the file name starts with the prefix "heal-csv-results-tracker-", you append the name of the manuscript or other multi-result file to which the Results Tracker applies, and save as a csv file)
        * Add all final result products already produced by/for your study to a Results Tracker
            * Use the [Results Tracker schema](../schemas/md_results_tracker.md) to understand what each "question"/field in the Results Tracker means and how to "answer"/complete each "question"/field 
            * The Results Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each final result product (i.e. files that are required to interpret, replicate, or use the result)
        * **As you produce more final result products** add them to a Results Tracker as soon as possible

    <font size="3"> What to do **when your manuscript is finalized** </font>

    * Finalize the Results Tracker for the completed manuscript (or other [multi-result file](../terms/index.md#multi-result-file))
        * Audit the [final result products](../terms/index.md#final-result-products) (e.g. figure, figure panel, table, text statement) produced by your study that are shared in the manuscript - create a list of final result products
        * Check that all final result products shared in the manuscript or other multi-result file are listed in the associated Results Tracker - Add any that are missing
        * Check that figure/table numbers for all final result products shared in the manuscript are accurately reflected in the final result product entry in the manuscript's associated Results Tracker - Correct any that need to be updated
    * Add your manuscript and its [associated Results Tracker](../terms/index.md#associated-results-tracker) to your Resource Tracker 
    * Check that all final result product [associated files/dependencies](../terms/index.md#associated-filesdependencies) (listed in the associated files/dependencies fields for each final result product listed in the Results Tracker) are also listed as study resource/files in your Resource Tracker - Add any that are missing 
      

#### Early, Results-support, Low

??? note "Study stage == Early <br> Data-sharing goal == Results-support <br> Data-sharing resources == Low"

    <font size="3"> What to do **right away**</font>
    
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to these files now, and to future files as they are created
        * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
    * <mark>Then follow best fit annotation recommendations for</mark>: [Late, Results-support, Low](#late-results-support-low)



#### Early, Dataset-sharing, Standard

??? note "Study stage == Early <br> Data-sharing goal == Dataset-sharing <br> Data-sharing resources == Standard"

        
    Use an ["As-you-go"](../terms/index.md#as-you-go-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#as-you-go-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>
    
    * Start annotating "As-you-go" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to these files now, and to future files as they are created
        * Where possible, organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all study files/resources are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disc location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package  
    * Create a [Data Dictionary](../terms/index.md#data-dictionary) for each existing [tabular data file](../terms/index.md#tabular-data-file)
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add all files already produced by/for your study to your Resource Tracker
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities which have already been designed to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field 
        

    <font size="3"> What to do **continuously, as-you-go**</font>
        
    * **As you create/collect new study files:** 
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to study files/resources as they are created
            * If you came up with file organization and naming conventions based on HEAL recommendations at the start of or earlier in your study, continue to consistently apply those conventions as you create/collect new study files
        * Add new study files/resources to your [Resource Tracker](../terms/index.md#resource-tracker) as they are created/collected (as soon as possible)
    * **As you create/collect new tabular data files:**
        * Create a [Data Dictionary](../terms/index.md#data-dictionary) for tabular data files as they are created
    * **As you design new study experiments/activities:**
        * Add new study experiments/activities to your [Experiment Tracker](../terms/index.md#experiment-tracker) as they are designed (as soon as possible)

    <font size="3"> What to do **when your dataset-of-interest is finalized** </font>

    * Add your finalized dataset-of-interest to your Resource Tracker 
    * Check that all [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker - Add any that are missing 

#### Early, Dataset-sharing, Low

??? note "Study stage == Early <br> Data-sharing goal == Dataset-sharing <br> Data-sharing resources == Low"

    <font size="3"> What to do **right away**</font>
    
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * Consider applying [HEAL recommendations for file organization and naming](../file-o-and-n/index.md) to these files now, and to future files as they are created
        * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
    * <mark>Then follow best fit annotation recommendations for</mark>: [Late, Dataset-sharing, Low](#late-dataset-sharing-low)

    
## Late

#### Late, Results-support, Standard

??? note "Study stage == Late <br> Data-sharing goal == Results-support <br> Data-sharing resources == Standard"

        
    Use a ["Top-down"](../terms/index.md#top-down-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#top-down-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>

    * Start annotating "Top-down" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * If you are late in your study and have accumulated many study files already, establishing file naming and organization conventions now and back-applying them may be quite burdensome and potentially prone to error
        * Therefore, we generally recommend that you leave file names and organization as is - However, we do request that you consider the following exceptions: 
            * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
            * If you have sets of "like" files (e.g. a similarly formatted tabular data file or brain imaging file per study subject per study timepoint), it may be well worth establishing file naming and organization conventions based on [HEAL recommendations for organizing and naming study files/resources](../file-o-and-n/index.md) now and back-applying them just for these file sets - doing so may make it possible/easier to annotate these file sets in one go instead of annotating them singly one at a time, and so may substantially reduce annotation/data-sharing burden for the study group
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all [study files/resources](../terms/index.md#study-filesresources) are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disk location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package 
    
     
    <font size="3"> What to do **when your manuscript is finalized** </font>

    * Audit the [final result products](../terms/index.md#final-result-products) (e.g. figure, figure panel, table, text statement) produced by your study that are shared in the manuscript - create a list of final result products
    * For each final result product shared in your manuscript, 
        * Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for that final result product (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
        * Audit the full set of study experiments/activities that produced supporting data or other support for that final result product
    * If any associated file/dependency for any of the final result products is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for each associated file/dependency that is a tabular data file, AND add this Data Dictionary to the list of associated files/dependencies for that final result product
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Results Tracker(s)](../terms/index.md#results-tracker) - one per manuscript or other multi-result file
        * Start to create a Results Tracker to document the [final result products](../terms/index.md#final-result-products) (e.g. figures, tables) that will be published as part of your manuscript or other [multi-result file](../terms/index.md#multi-result-file) (e.g. report or manuscript)
        * Start your Results Tracker by initializing an empty Results Tracker file based on the [Results Tracker csv template](../csv-templates/heal-csv-results-tracker.csv)
            * Save your Results Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-results-tracker-my-manuscript-file.csv" (i.e. the file name starts with the prefix "heal-csv-results-tracker-", you append the name of the manuscript or other multi-result file to which the Results Tracker applies, and save as a csv file)
        * Add all final result products shared in the manuscript or other multi-result file to a Results Tracker
            * Use the [Results Tracker schema](../schemas/md_results_tracker.md) to understand what each "question"/field in the Results Tracker means and how to "answer"/complete each "question"/field 
            * The Results Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each final result product (i.e. files that are required to interpret, replicate, or use the result)
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities that produced supporting data or other support for any of the final result products shared in your manuscript to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
    * Finalize the Results Tracker for the completed manuscript (or other [multi-result file](../terms/index.md#multi-result-file))
        * Check that all final result products shared in the manuscript or other multi-result file are listed in the associated Results Tracker - Add any that are missing
        * Check that figure/table numbers for all final result products shared in the manuscript are accurately reflected in the final result product entry in the manuscript's associated Results Tracker - Correct any that need to be updated
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Add your manuscript and its [associated Results Tracker](../terms/index.md#associated-results-tracker) to your Resource Tracker 
        * Do not add the Results Tracker for your manuscript to your Resource Tracker until it is finalized 
    * For each final result product shared in your manuscript, add each of the associated files/dependencies for that final result product to your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies 
        * Check that all final result product [associated files/dependencies](../terms/index.md#associated-filesdependencies) (listed in the associated files/dependencies fields for each final result product listed in the Results Tracker) are also listed as study resource/files in your Resource Tracker - Add any that are missing
        

          

#### Late, Results-support, Low

??? note "Study stage == Late <br> Data-sharing goal == Results-support <br> Data-sharing resources == Low"

        
    Use a ["Top-down"](../terms/index.md#top-down-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#top-down-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>

    * Start annotating "Top-down" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * If you are late in your study and have accumulated many study files already, establishing file naming and organization conventions now and back-applying them may be quite burdensome and potentially prone to error
        * Therefore, we generally recommend that you leave file names and organization as is - However, we do request that you consider the following exceptions: 
            * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
            * If you have sets of "like" files (e.g. a similarly formatted tabular data file or brain imaging file per study subject per study timepoint), it may be well worth establishing file naming and organization conventions based on [HEAL recommendations for organizing and naming study files/resources](../file-o-and-n/index.md) now and back-applying them just for these file sets - doing so may make it possible/easier to annotate these file sets in one go instead of annotating them singly one at a time, and so may substantially reduce annotation/data-sharing burden for the study group
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all [study files/resources](../terms/index.md#study-filesresources) are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disk location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package 
    
     
    <font size="3"> What to do **when your manuscript is finalized** </font>

    * Audit the [final result products](../terms/index.md#final-result-products) (e.g. figure, figure panel, table, text statement) produced by your study that are shared in the manuscript - create a list of final result products
    * For each final result product shared in your manuscript, 
        * Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for that final result product (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
        * Audit the full set of study experiments/activities that produced supporting data or other support for that final result product
    * If any associated file/dependency for any of the final result products is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for each associated file/dependency that is a tabular data file, AND add this Data Dictionary to the list of associated files/dependencies for that final result product
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Results Tracker(s)](../terms/index.md#results-tracker) - one per manuscript or other multi-result file
        * Start to create a Results Tracker to document the [final result products](../terms/index.md#final-result-products) (e.g. figures, tables) that will be published as part of your manuscript or other [multi-result file](../terms/index.md#multi-result-file) (e.g. report or manuscript)
        * Start your Results Tracker by initializing an empty Results Tracker file based on the [Results Tracker csv template](../csv-templates/heal-csv-results-tracker.csv)
            * Save your Results Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-results-tracker-my-manuscript-file.csv" (i.e. the file name starts with the prefix "heal-csv-results-tracker-", you append the name of the manuscript or other multi-result file to which the Results Tracker applies, and save as a csv file)
        * Add all final result products shared in the manuscript or other multi-result file to a Results Tracker
            * Use the [Results Tracker schema](../schemas/md_results_tracker.md) to understand what each "question"/field in the Results Tracker means and how to "answer"/complete each "question"/field 
            * The Results Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each final result product (i.e. files that are required to interpret, replicate, or use the result)
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities that produced supporting data or other support for any of the final result products shared in your manuscript to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
    * Finalize the Results Tracker for the completed manuscript (or other [multi-result file](../terms/index.md#multi-result-file))
        * Check that all final result products shared in the manuscript or other multi-result file are listed in the associated Results Tracker - Add any that are missing
        * Check that figure/table numbers for all final result products shared in the manuscript are accurately reflected in the final result product entry in the manuscript's associated Results Tracker - Correct any that need to be updated
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Add your manuscript and its [associated Results Tracker](../terms/index.md#associated-results-tracker) to your Resource Tracker 
        * Do not add the Results Tracker for your manuscript to your Resource Tracker until it is finalized 
    * For each final result product shared in your manuscript, review your audit list of associated files/dependencies for that result product (including associated files/dependencies of immediate dependencies), and determine which of these files will be shared in a public repository 
    * For each final result product shared in your manuscript, add each of the associated files/dependencies for that final result product to your Resource Tracker (including associated files/dependencies of immediate associated files/dependencies) **ONLY if the file will be shared in a public repository** 
        * Check that all final result product [associated files/dependencies](../terms/index.md#associated-filesdependencies) (listed in the associated files/dependencies fields for each final result product listed in the Results Tracker) are also listed as study resource/files in your Resource Tracker **ONLY if the file will be shared in a public repository** - Add any that are missing
        

#### Late, Dataset-sharing, Standard

??? note "Study stage == Late <br> Data-sharing goal == Dataset-sharing <br> Data-sharing resources == Standard"

        
    Use a ["Top-down"](../terms/index.md#top-down-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#top-down-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>

    * Start annotating "Top-down" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * If you are late in your study and have accumulated many study files already, establishing file naming and organization conventions now and back-applying them may be quite burdensome and potentially prone to error
        * Therefore, we generally recommend that you leave file names and organization as is - However, we do request that you consider the following exceptions: 
            * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
            * If you have sets of "like" files (e.g. a similarly formatted tabular data file or brain imaging file per study subject per study timepoint), it may be well worth establishing file naming and organization conventions based on [HEAL recommendations for organizing and naming study files/resources](../file-o-and-n/index.md) now and back-applying them just for these file sets - doing so may make it possible/easier to annotate these file sets in one go instead of annotating them singly one at a time, and so may substantially reduce annotation/data-sharing burden for the study group
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all [study files/resources](../terms/index.md#study-filesresources) are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disk location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package 
    
    
    <font size="3"> What to do **when your dataset-of-interest is finalized** </font>

    * Audit the full set of study experiments/activities that produced supporting data or other support for the final dataset-of-interest
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities that produced supporting data or other support for the final dataset-of-interest to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
    * Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the final dataset-of-interest (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
    * If the dataset-of-interest, or any associated file/dependency of the dataset-of-interest is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for the tabular dataset-of-interest and for each associated file/dependency that is a tabular data file, AND add these Data Dictionaries to the list of associated files/dependencies for the dataset-of-interest
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Add your finalized dataset-of-interest to your Resource Tracker 
    * Add each of the associated files/dependencies for the final dataset-of-interest to your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies 
        * Check that all [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies - Add any that are missing 
    
    
     

#### Late, Dataset-sharing, Low

??? note "Study stage == Late <br> Data-sharing goal == Dataset-sharing <br> Data-sharing resources == Low"

    
    Use a ["Top-down"](../terms/index.md#top-down-annotation) annotation approach; a **detailed overview** of what this involves can be found [here](../terms/index.md#top-down-annotation); a **brief overview** of what this involves follows below:

    <font size="3"> What to do **right away**</font>

    * Start annotating "Top-down" as soon as possible
    * Audit all [study files/resources](../terms/index.md#study-filesresources) already produced by or for your study
        * If you are late in your study and have accumulated many study files already, establishing file naming and organization conventions now and back-applying them may be quite burdensome and potentially prone to error
        * Therefore, we generally recommend that you leave file names and organization as is - However, we do request that you consider the following exceptions: 
            * Where practicable to implement (without duplicating original files), organize all study files/resources into a single study folder/directory (study folder/directory may of course have sub-directories; see [here](../guidance/file-org.md) for guidance on and examples of recommended study folder/directory structure)
            * If you have sets of "like" files (e.g. a similarly formatted tabular data file or brain imaging file per study subject per study timepoint), it may be well worth establishing file naming and organization conventions based on [HEAL recommendations for organizing and naming study files/resources](../file-o-and-n/index.md) now and back-applying them just for these file sets - doing so may make it possible/easier to annotate these file sets in one go instead of annotating them singly one at a time, and so may substantially reduce annotation/data-sharing burden for the study group
    * Initialize your [Data Package](../terms/index.md#data-package)  
        * Create a ["dsc-pkg" folder/directory](../terms/index.md#dsc-pkg-folder) that will hold all [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) for your data package
            * If all [study files/resources](../terms/index.md#study-filesresources) are organized into a single study folder/directory, create this folder/directory as a direct sub-directory of your study folder/directory, and name it "dsc-pkg"; consistency in naming and location of this folder/directory relative to your overall study folder/directory will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package
            * If not, create this folder/directory in a disk location that makes sense for you; name it "dsc-pkg", optionally appending a suffix to the name that will make it easy to recognize as "belonging" to a specific study (e.g. "dsc-pkg-study-1" or "dsc-pkg-mindfulness-for-oud"); consistency in naming (i.e. including the "dsc-pkg" prefix) and appending a suffix to the name that is a human-recongnizable identifier for the relevant study will make it easy to recognize as the folder that contains the Standard Data Package Metadata files for your study's data package 
    
    
    <font size="3"> What to do **when your dataset-of-interest is finalized** </font>

    * Audit the full set of study experiments/activities that produced supporting data or other support for the final dataset-of-interest
    * Start your [Experiment Tracker](../terms/index.md#experiment-tracker) 
        * Start your Experiment Tracker by initializing an empty Experiment Tracker file based on the [Experiment Tracker csv template](../csv-templates/heal-csv-experiment-tracker.csv)
            * Save your Experiment Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-experiment-tracker.csv"
        * Add all experiments or other study activities that produced supporting data or other support for the final dataset-of-interest to your Experiment Tracker
            * Use the [Experiment Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Experiment Tracker means and how to "answer"/complete each "question"/field
    * Audit the full set of [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the final dataset-of-interest (i.e. all study files/resources required to interpret, replicate, or use the final result product), including associated files/dependencies of immediate associated files/dependencies
    * If the dataset-of-interest, or any associated file/dependency of the dataset-of-interest is a [tabular data file](../terms/index.md#tabular-data-file), create a [Data Dictionary](../terms/index.md#data-dictionary) for the tabular dataset-of-interest and for each associated file/dependency that is a tabular data file, AND add these Data Dictionaries to the list of associated files/dependencies for the dataset-of-interest
        * Start a Data Dictionary for a tabular data file by initializing an empty Data Dictionary file based on the [Data Dictionary csv template](../csv-templates/heal-csv-data-dictionary.csv)
            * Save your Data Dictionary in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-dd-my-datafile.csv" (i.e. the file name starts with the prefix "heal-csv-dd-", you append the name of the data file to which the Data Dictionary applies, and save as a csv file)
            * Add all variables in the tabular data file to your Data Dictionary
                * Use the [Data Dictionary schema](../schemas/md_data_dictionary_fields.md) to understand what each "question"/field in the Data Dictionary means and how to "answer"/complete each "question"/field 
    * Start your [Resource Tracker](../terms/index.md#resource-tracker)
        * Start your Resource Tracker by initializing an empty Resource Tracker file based on the [Resource Tracker csv template](../csv-templates/heal-csv-resource-tracker.csv)
            * Save your Resource Tracker in your ["dsc-pkg" folder](../terms/index.md#dsc-pkg-folder) as "heal-csv-resource-tracker.csv"
        * Add files produced by/for your study to your Resource Tracker (see next bullet for guidance on which files to add and where to start)
            * Use the [Resource Tracker schema](../schemas/md_resource_tracker.md) to understand what each "question"/field in the Resource Tracker means and how to "answer"/complete each "question"/field  
            * The Resource Tracker will ask you to list [associated files/dependencies](../terms/index.md#associated-filesdependencies) for each study file/resource (i.e. files that are required to interpret, replicate, or use the study file/resource)
    * Add your finalized dataset-of-interest to your Resource Tracker 
    * Review your audit list of associated files/dependencies for the final dataset-of-interest (including associated files/dependencies of immediate dependencies), and determine which of these files will be shared in a public repository 
    * Add each of the associated files/dependencies for the final dataset-of-interest to your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies **ONLY if the file will be shared in a public repository**
        * Check that all [associated files/dependencies](../terms/index.md#associated-filesdependencies) for the finalized dataset-of-interest (i.e. files required to interpret, replicate, or use the finalized dataset-of-interest) are also listed as study resource/files in your Resource Tracker, including associated files/dependencies of immediate associated files/dependencies **ONLY if the file will be shared in a public repository** - Add any that are missing 
    
    
    
   