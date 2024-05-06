---
hide:
  - toc
full-width: true
---

# Creating an Open-Access Shareable Data Package

  ![](../assets/prepare-sub-open.drawio)


<br>


---
!!! note "Reminder"

    **These instructions apply to studies that have a centralized study folder where all study files are saved.**


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Create your shareable data package folder

You will need to create a folder to hold all data and non-data supporting files that you have designated as shareable from your study. You can create your folder however you see fit, but a recommended structure follow below. The following instructions will refer to recommended folder names throughout.

* Create a folder called "my-study-share-current date." (*Note: You can name this folder whatever you would like - this is just a recommended name.*)
  * This folder will hold your shareable data package as well as some supporting documentation.
* Within that folder, create another folder called "my-study-share-open-access-now." This is where your data package will live. 
  * In this folder, you will want to mirror the folder structure of your current internal centralized study folder where all your files and supporting documentation are held. **All folders you create here should be empty right now.**
    * Mirroring the structure of your centralized study folder will allow a secondary user to find files referenced in the Resource Tracker in the folder based on their provided file path.
    * This is where you will copy in the files from your centralized study folder that are meant to be shared in your "open-access now" shareable data package. Continue to the next step for more information on this.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Identify resources that meet sharing requirements

1. Navigate to your dsc-pkg folder and open your Resource Tracker. 
2. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files will go into your "open-access now" shareable data package.
3. Identify all study files/resources that are designated as open-access as of today's date. For reference, the requirements for access and access-date are below:
  1. **"open-access" in access AND "temporary-private" not in access** OR
  2. **"open-access" in access AND "temporary-private" in access AND today's date >= access-date**
4. In addition to your study files, you will need to identify which standard data package metadata should be copied into your "open-access now" shareable data package. Standard data package metadata includes the Experiment Tracker, Resource Tracker, Results Tracker(s), and Data Dictionary(ies)
  1. The Resource Tracker and Experiment Tracker should be copied into any shareable data package you create.
  2. Results Tracker(s) and Data Dictionary(ies) have similar restrictions as other files/resources - you should only copy each over if it meets the requirements for "open-access now" listed above.

  !!! warning

      These files **should not** be copied into your shareable data package folder:
    
      * A file designated as temporary private as of today's date
      * A file designated as managed access
      * A file designated as permanent private

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Copy open-access files into your "open-access now" shareable data package folder

1. After identifying the resources that meet the requirements, copy each of those resources from your study folder into your "my-study-share-open-access-now" folder.
  1. This any data or non-data supporting files as well as Results Tracker(s) or Data Dictionary(ies) in the Resource Tracker that meet the requirements for sharing as open-access at this time.
2. Copy your Resource Tracker and Experiment Tracker into this folder.
        
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare Resource and Results Tracker(s)

Next, you will need to make adjustments to your Resource Tracker and Results Tracker(s) that you copied into your "my-study-share-open-access-now" folder from full paths to paths relative to the dsc-pkg folder.

* Adjusting the paths within these trackers to be relative to the dsc-pkg folder protects your study team's privacy, as it means people won't see your local folder structure, while also increasing utility for secondary users.
* As mentioned previously, this method works best when all files and the dsc-pkg folder are saved within a centralized study folder. Every path disclosed will be in relation to your dsc-pkg folder and within your centralized study folder.

See below for information on adjustments to make within each tracker. ***Reminder:** You will be making these adjustments to the Resource Tracker and Results Tracker(s) within your shareable data package folder.*

##### Resource Tracker

You will likely have to make adjustments to file paths within each of the below columns (if they are not empty): 

* path
* associatedFileDataDict
* associatedFileProtocol
* associatedFileResultsTracker
* associatedFileDependsOn
* associatedFileResultsDependOn
* associatedFileMultiLikeFiles

##### Results Tracker(s)

You will likely have to make adjustments to file paths within each of the below columns (if they are not empty):

* associatedFilePublication
* associatedFileDependsOn

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Zip up your shareable data package

1. After you have edited your Resource Tracker to reflect relative file paths, you will need to make another copy. This copy should be moved into your one-level-up "my-study-share-current date" directory. You will add some additional information to this version of the Resource Tracker in the coming steps. This version of the Resource Tracker will act as supporting documentation for your zipped shareable data package.
2. Examine your "my-study-share-open-access-now" folder to ensure that you have shared the files and resources you want to share and have not shared anything you don't want to share.
3. Now, your "open-access now" shareable data package folder is ready to zip up for submission. 
  1. You can zip it up in whichever way you choose.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare other materials for submission

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### Overview Resource Tracker

1. Navigate to the edited Resource Tracker you saved in your "my-study-share-current-date" directory in the previous step.
1. Add a column to the Resource Tracker called "open-access-shareable-data-pkg."
  2. For each row, enter a 1 if the file will be shared in this open-access now shareable data package. If not shared in this shareable data package, enter a 0.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### README File

1. Create a README file, which will provide a brief, structured description of the shareable data packages included in the "my-study-share-current-date" folder. 
  1. You can find a README template [here](readme.md).
2. Save the README file in the "my-study-share-current-date" folder.

</div>
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Upload your shareable data package to your repository

**Congratulations! You are ready to upload your "open-access now" shareable data package.**

1. Your final "open-access now" shareable data package should include 3 open-access items:
  1. Your zipped "open-access now" shareable data package
  2. Your edited Resource Tracker, which designates which files are included in the zipped data package.
  3. Your README file.
2. You should share these at your chosen data repository as open access files.

</div>
</div>

