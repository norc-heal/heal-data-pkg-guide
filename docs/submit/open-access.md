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

    **These directions apply to studies that have a centralized study folder where all study files are saved.**


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">


#### Create your shareable data package folder

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Create a new folder with the same folder structure as your centralized study folder. This is where you will create your open-access now shareable data package.

</div>

#### Copy open-access files into your shareable data package folder

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

2. Navigate to your dsc-pkg folder and open your Resource Tracker. 
  1. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files will go into your open-access shareable data package.
  2. Identify all study files/resources that are designated as open-access as of today's date. For reference, the requirements for access and access-date are below:
    1. "open-access" in access AND "temporary-private" not in access OR
    2. "open-access" in access AND "temporary-private" in access AND today's date >= access-date
3. After identifying the resources that meet the requirements, copy each of those resources from your study folder into the new shareable data package folder you created.
        
  !!! warning

      These files **should not** be copied into your new shareable data package folder:
    
      * A file designated as temporary private as of today's date
      * A file designated as managed access
      * A file designated as permanent private

</div>

#### Prepare and copy over standard data package metadata

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Next, you will need to make some adjustments to your standard data package metadata (specifically, your Resource Tracker and Results Tracker, if applicable). You will need to adjust all file paths within the Resource Tracker and Results Tracker from full paths to paths relative to the dsc-pkg folder.

* Editing the resource file paths to be relative to the dsc-pkg folder will help future users to better understand the relationship of the files within the folder.
  * It will also keep you from having to share informatin about the structure of your study team's network drive, Box, or other folder structure.
  * This method works best when all files and the dsc-pkg folder are saved within a centralized study folder. Every path disclosed will be in relation to your dsc-pkg folder within your centralized study folder.

4. Open your Resource Tracker. You will be need to adjust all file paths within the tracker from full paths to paths relative to the dsc-pkg folder within your centralized study folder.
  1. You will likely have to make adjustments to file paths within each of the below columns (if they are not empty): 
    * path
    * associatedFileDataDict
    * associatedFileProtocol
    * associatedFileResultsTracker
    * associatedFileDependsOn
    * associatedFileResultsDependOn
    * associatedFileMultiLikeFiles

5. After setting up your relative file paths, copy your edited Resource Tracker and your Experiment Tracker into your new open-access now shareable data package folder. No edits should need to be made to the Experiment Tracker before copying over to the shareable data package folder.

5. If your Results Tracker is included in the files able to be shared as open-access as of today's date, open your Results Tracker.

  !!! warning

      For your Results Tracker to be included in your open-access now shareable data package, it must also meet the requirements listed above in its Resource Tracker entry:
    
      1. "open-access" in access AND "temporary-private" not in access OR
      2. "open-access" in access AND "temporary-private" in access AND today's date >= access-date

      If your Results Tracker **does not meet** one of the above requirements, you will not include your Results Tracker in your open-access now shareable data package. You may skip to the next step.

  1. You will also need to adjust any file paths included within the Results Tracker from full paths to paths relative to the dsc-pkg folder.
    1. You will likely have to make adjustments to file paths within each of the below columns (if they are not empty):
      * associatedFilePublication
      * associatedFileDependsOn

6. After adjusting to relative file paths, copy your edited Results Tracker into your new open-access now shareable data package folder.

</div>

#### Zip up your shareable data package

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Your open-access now shareable data package folder is ready to zip up for submission. You can zip it up in whatever way is most comfortable for you.

</div>


#### Prepare other materials for submission

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

8. Return to your original dsc-pkg folder. 
9. Make a copy of your edited Resource Tracker (the version with relative paths).
  1. Add a column to the Resource Tracker called "open-access-shareable-data-pkg."
  2. For each row, enter a 1 if the file will be shared in this open-access now shareable data package. If not shared in this shareable data package, enter a 0.
10. Create a README.
  1. You can find a README template [here](readme.md).

</div>

#### Upload your shareable data package to your repository

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

**Congratulations! You are ready to upload your open-access now shareable data package.**

1. If you have other shareable data packages you need to create, you may want to complete those first. For more information on additional shareable data packages you may want to create based on your study files, see [prepare your data package for submission](index.md)
2. Your final submission should include 3 open-access items:
  1. Your zipped open-access now shareable data package
  2. Your edited Resource Tracker, which designates which files are included in the zipped data package.
  3. Your README.

</div>
</div>

