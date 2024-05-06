---
hide:
  - toc
full-width: true
---

# Creating an Managed-Access Shareable Data Package

  ![](../assets/prepare-sub-managed.drawio)

<br>


---
!!! note "Reminder"

    **These instructions apply to studies that have a centralized study folder where all study files are saved.**

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">


#### Create your shareable data package folder

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Create a new folder with the same folder structure as your centralized study folder. This is where you will create your managed-access shareable data package.

</div>

#### Copy open-access files into your shareable data package folder

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

2. Navigate to your dsc-pkg folder and open your Resource Tracker. 
  1. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files you put in your managed-access shareable data package.
  2. Identify all study files/resources that are designated as managed-access or open-access as of today's date. For reference, the requirements for access and access-date are below:
    1. "open-access" in access AND "temporary-private" not in access OR
    2. "open-access" in access AND "temporary-private" in access AND today's date >= access-date OR
    3. "managed-access" in access AND "temporary-private" not in access OR
    4. "managed-access" in access AND "temporary-private" in access AND today's date >= access-date
3. After identifying the resources that meet the requirements, copy each of those resources from your study folder into the new shareable data package folder you created.
        
  !!! warning

      These files **should not** be copied into your new shareable data package folder:
    
      * A file designated as temporary private as of today's date
      * A file designated as permanent private

</div>

#### Prepare and copy over standard data package metadata

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Next, you will need to make adjustments to your standard data package metadata, specifically you will need to adjust all file paths within the Resource Tracker and Results Tracker from full paths to paths relative to the dsc-pkg folder.

* Showing all file paths as relative to the dsc-pkg folder will help future users to better understand the relationship of the resources without having to share information about the structure of your internal study team's network drive, Box, or other folder structure.
* As mentioned previously, this method works best when all files and the dsc-pkg folder are saved within a centralized study folder. Every path disclosed will be in relation to your dsc-pkkg folder and within your centralized study folder.

##### Resource Tracker

4. Open your Resource Tracker. You will be need to adjust all file paths within the tracker from full paths to paths relative to the dsc-pkg folder within your centralized study folder.
  1. You will have to make adjustments within each of the below columns if they are not empty: 
    * path
    * associatedFileDataDict
    * associatedFileProtocol
    * associatedFileResultsTracker
    * associatedFileDependsOn
    * associatedFileResultsDependOn
    * associatedFileMultiLikeFiles

5. Copy your edited Resource Tracker and your Experiment Tracker into your new managed-access shareable data package folder. No edits should need to be made to the Experiment Tracker before copying over to the shareable data package folder.

##### Results Tracker(s)

5. If your Results Tracker is able to be shared as open-access or managed-access as of today's date, open your Results Tracker.

  !!! warning

      For your Results Tracker to be included in your managed-access shareable data package, it must also meet the requirements above in its Resource Tracker entry:
    
      1. "open-access" in access AND "temporary-private" not in access OR
      2. "open-access" in access AND "temporary-private" in access AND today's date >= access-date OR
      3. "managed-access" in access AND "temporary-private" not in access OR
      4. "managed-access" in access AND "temporary-private" in access AND today's date >= access-date

      If your Results Tracker **does not meet** one of the above requirements, you will not include your Results Tracker in your managed-access shareable data package. You may skip to the next step.

  1. You will need to adjust all file paths within the Results Tracker from full paths to paths relative to the dsc-pkg folder within your centralized study folder.
    1. You will likely have to make adjustments within each of the below columns if they are not empty:
      * associatedFilePublication
      * associatedFileDependsOn

6. Copy your edited Results Tracker into your new managed-access shareable data package folder.

</div>

#### Zip up your shareable data package

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Your managed-access shareable data package folder is ready to zip up for submission. You can zip it up in whatever way is most comfortable for you.

</div>

#### Prepare other materials for submission

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

8. Return to your original dsc-pkg folder. 
9. Make a copy of your edited Resource Tracker (with relative paths to files).
  1. Add a column to the Resource Tracker called "managed-access-shareable-data-pkg."
  2. For each row, if the file will be shared in this managed-access shareable data package, enter a 1. If not shared in this shareable data package, enter a 0.
10. Create a README.
  1. You can find a README template [here](readme.md).

</div>

#### Upload your shareable data package to your repository

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

**Congratulations! You are ready to upload your managed-access shareable data package.**

1. If you have other shareable data packages you need to create, you may want to complete those first. For more information on additional shareable data packages you may want to create based on your study files, see [prepare your data package for submission](index.md)
2. Your final submission should include 3 items:
  1. Your zipped managed-access now shareable data package
  2. Two open-access files
    1. Your edited Resource Tracker, which designates which files are included in the zipped data package.
    2. Your README.

</div>
</div>
