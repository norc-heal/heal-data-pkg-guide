# Submitting RNA-seq data to Sequence Read Archive (SRA)

This page provides step-by-step guidance on how to submit RNA-seq data to the Sequence Read Archive (SRA), a HEAL-compliant repository.

**There are a few reasons why it may be useful to submit your RNA-seq or other sequencing data to SRA.** 

* Submitting this type of data to SRA, a repository explicitly reserved for sequencing data, will greatly increase your data’s discoverability and accessibility over a generalist repository. 
* SRA will also prompt you to provide standardized metadata that is appropriate and tailored to your data type and population of study, which generalist repositories may not. 
* You may run into issues submitting RNA-seq and other sequencing data to repositories not specifically geared towards this type of data. Sequencing files are often very large, and you may run into size restrictions and/or fees in trying to upload files.

**SRA submission does have some limitations.**

* SRA does not have the capacity to store other data types/documents beyond sequencing files. 
  * Therefore, we recommend you package and submit other data types/documents related to your study to a different repository, making sure to link your studies between the two repositories (to the extent possible).

Throughout this step-by-step guidance, we will refer you to find more information/detail from an [existing step-by-step guide](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"} on submission to SRA (referred to as "step-by-step guide" in the instructions below). This is a very good resource with detailed information and definitions, including screenshots. **We recommend you have it open as you work through the steps below.** There are also additional [resources](#resources) listed at the bottom of this document that may be useful to review ahead of working through these steps.

## Create an NCBI Account

1. Navigate to the [SRA website](https://www.ncbi.nlm.nih.gov/sra){:target="_blank"}.
2. Create an NCBI Account. You can use a single account for all submissions you make to SRA. 
  1. NOTE: You may already have an account with an affiliate (e.g., ORCID, NIH, Gmail) that would enable you to sign in to NCBI without explicitly creating an NCBI account.

## Register Your BioProject

1. First, you will need to [create a BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/){:target="_blank"}. This BioProject will contain all of the BioSamples that you will create in the next step and all the corresponding RNA-seq data. To create your BioProject, you will need to fill out information in each of 7 tabs. For detailed information on how to complete the fields, please see the ["step-by-step guide"](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"}.
  1. Submitter
  2. Project Type
  3. Target
  4. General Info
    1. **Note**: This step provides an opportunity to link your SRA data to a submission at another repository in the *External Links* field.
      1. For example, if you have a data package shared (or in progress) at Harvard Dataverse, you would enter the link to your Harvard Dataverse dataset in the *External links* field, including a brief explanation of the fact that other data for the project is contained in the linked project at the Harvard Dataverse repository. This will mean that whenever someone accesses your BioProject page, they will be able to quickly find the rest of your data at Harvard Dataverse.
  5. BioSample
    3. **Note**: Although there is a BioSample tab in this step, you will not include BioSample information here, as you have not yet registered the BioSample(s) (that will happen in the next step). You will be able to link your BioSample(s) and BioProject later, in the "Submit your Data" section (i.e., when submitting raw reads).
  6. Publications
  7. Overview
2. After you create a BioProject, you will be provided with a **BioProject ID**. This will be in the format of PRJNAXXXXXX.

  !!! note

      It is difficult to edit the information entered in this step after submission; any changes require you to get in touch with SRA via email. Therefore, it is advised to ensure that details provided are accurate prior to submission.

## Register Your BioSample(s)

1. Go to the [BioSample submission page](https://submit.ncbi.nlm.nih.gov/subs/biosample/){:target="_blank"}. Click on the BioSample link and choose New Submission.
  1. You can submit information on multiple BioSamples at once. If you have multiple BioSamples, you will likely want to batch add all BioSamples for the same BioProject at once.
  2. You will be asked to provide metadata about the BioSamples you want to batch add. You will need to complete seven tabs of information:
    1. Submitter
    2. General info
    3. Sample type
    4. Attributes
      1. **Note**: This is where you will be prompted to download and fill out a metadata template to batch add the BioSamples. Make sure you download the correct Excel template for your BioSample Type. This Excel contains tooltips for each column to explain what should go in each cell for the BioSample metadata.
        1. For additional detailed information on how to fill out this template, refer to the [step-by-step guide](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"}.
      2. Each of the BioSample rows must be unique, so although many of the characteristics of your BioSamples may be similar, it is important to ensure that they are distinguishable on some of the data entered into the metadata template.
    5. BioProject
      1. **Note**: This is where you can enter your registered BioProject number created in the previous step; you can also wait until the next step ("Submit your Data") to associate your BioSamples and BioProject.
    6. Description
    7. Overview
2. Once you submit your BioSample(s), you will be provided with **BioSample ID(s)**. These will be in the format of SAMNXXXX.

  !!! note

      It is difficult to edit the information entered in this step after submission; any changes require you to get in touch with SRA via email. Therefore, it is advised to ensure that details provided are accurate prior to submission.

## Submit Your Data

1. The next step is submission. Navigate to the [SRA submission portal](https://submit.ncbi.nlm.nih.gov/subs/sra/){:target="_blank"} and select new submission.
2. As part of submission, you will need to do an additional round of metadata creation, where you will provide information about the sequencing. You will need to fill out information in five tabs:
  1. Submitter
  2. General info
    1. **Note**: This is where you would add your BioProject ID if you did not do so in the previous step.
  3. SRA metadata
    1. **Note**: This involves preparation of an external file, which you will be prompted to download, fill out, and upload.
      1. This template is set up as one row per raw read/sequencing experiment (e.g., there could be more than one row/sequencing experiment per BioSample if you split a BioSample into multiple aliquots and performed different sequencing on each aliquot).
    2. Detailed information on how to fill out the Excel metadata template is included in the linked ["step-by-step guide."](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"}
    3. Once you complete the template, you must save it as a **tab-delimited txt file** to upload.
  5. Files
    1. **Note**: This is the step where you will upload the raw reads.
    2. You can upload the raw reads in a number of ways, depending on the number and size of files you are submitting as well as your personal comfort with using command line tools. Please refer to the ["step-by-step guide"](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"} and the [SRA File Upload page](https://www.ncbi.nlm.nih.gov/sra/docs/submitfiles/){:target="_blank"} in the SRA submission quick start guide for information on the options and how to select the one that fits best with your data.
    3. When selecting files to upload (regardless of upload method), ensure that the files you select to upload completely align with the files inventoried in the SRA metadata spreadsheet in the previous step.
      1. If the SRA metadata spreadsheet does not match the files uploaded in this step, you will receive an error that you uploaded one or more files that are not in your metadata table.
  6. Overview
3. Upon submission, you will receive email confirmation regarding your submission title, submission ID, and BioProject ID.

## Linking Repository Submissions

1. As mentioned previously, if you submit the rest of your study files/documentation at another repository, we recommend creating a linkage between your SRA submission and your other repository using the *External links* field in the SRA submission process. We also recommend, where possible, creating a similar linkage to your SRA submission from your other repository. 
  1. This might mean linking to your SRA study from your other repository, including the BioProject ID within the study description at your other repository, or something else.
  2. The way to operationalize this will depend on the repository, so we recommend you review your repository's documentation for guidance.

## Resources
Here are some additional resources that may be helpful as you work through the steps above:

* [Good Citizenship Made Easy: A Step-by-Step Guide to Submitting RNA-Seq Data to NCBI](https://www.researchgate.net/profile/Sara-Oppenheim/publication/328919194_Good_Citizenship_Made_Easy_A_Step-by-Step_Guide_to_Submitting_RNA-Seq_Data_to_NCBI/links/611c2aa61ca20f6f862cb526/Good-Citizenship-Made-Easy-A-Step-by-Step-Guide-to-Submitting-RNA-Seq-Data-to-NCBI.pdf){:target="_blank"}: This article contains step-by-step guidance including screenshots of how to submit RNA-seq data to SRA. This is the "step-by-step guide" document referenced throughout the above instructions.
* [SRA Submission Guide](https://www.ncbi.nlm.nih.gov/sra/docs/submit/){:target="_blank"}: Contains helpful guidance on the steps of submitting to SRA including information on BioProjects, BioSamples, file formats, file upload, and more.
* [Troubleshooting SRA submission in the SRA Submission Portal Wizard](https://www.ncbi.nlm.nih.gov/sra/docs/submitspfiles/){:target="_blank"}: Contains information on common errors that you may encounter in submitting to SRA and how to resolve them.