---
hide:
  - toc
full-width: true
---

# Creating an Open-Access Now Shareable Data Package

  ![](../assets/prepare-sub-open.drawio)


<br>


---

--8<-- "submit/modules/remind.md"


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">


--8<-- "submit/modules/set.md"

--8<-- "submit/modules/intro/open-acc-now.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Identify resources and standard data package metadata that meet sharing requirements

1. Use the [Resource Tracker](../terms/index.md#resource-tracker) from your local data package to identify study files/resources and standard data package metadata that meet sharing requirements.
2. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files will go into your shareable data package folder.
3. Identify all study files/resources that are designated as open-access as of today's date. For reference, the requirements for access and access-date fields are below:
  1. **"open-access" value in access field AND "temporary-private" value not in access field** OR
  2. **"open-access" value in access field AND "temporary-private" value in access field AND today's date >= access-date field value**

  !!! warning

      These files **should not** be copied into your shareable data package folder:
    
      * A file with an access date after today's date in your Resource Tracker
      * A file designated as managed access in your Resource Tracker
      * A file designated as permanent private in your Resource Tracker
      * A file that is not listed in your Resource Tracker

4. In addition to your study files, you will need to identify which standard data package metadata should be copied from the dsc-pkg folder in your local data package into the dsc-pkg folder in your shareable data package. Standard data package metadata includes the Experiment Tracker, Resource Tracker, Results Tracker(s), and Data Dictionary(ies).
  1. You should automatically copy the Resource Tracker and Experiment Tracker into any shareable data package you create. These standard data package metadata files are not listed in your Resource Tracker. This is the only exception to the general rule that you should not share any files that are not listed in your Resource Tracker in a shareable data package.
  2. Results Tracker(s) and Data Dictionary(ies) have similar restrictions as other study files/resources. Results Tracker(s) and Data Dictionary(ies) should be listed in your Resource Tracker. 
    1. Use the "access" and "access-date" fields for your Results Tracker(s) and Data Dictionary(ies) to determine whether they should be copied into your shareable data package, based on the requirements listed above in step 3.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Copy files that meet sharing requirements into your shareable data package folder

--8<-- "submit/modules/copyover.md"
        
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare Resource and Results Trackers

--8<-- "submit/modules/restrackpath.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Review your shareable data package

--8<-- "submit/modules/review.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare other materials for submission

Prepare the accessory files that you will submit along with your shareable data package - This includes the 1) "Overview" Resource Tracker, and 2) Readme file. 

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### Overview Resource Tracker

1. Create a copy of the Resource Tracker in your shareable data package folder and move that copy into your "my-study-share" folder. This will be your "Overview" Resource Tracker, which will indicate whether or not each file in the Resource Tracker is shared in the shareable data package.
2. Add a column to this Resource Tracker. A suggested name for this column might be "share-open-access-now."
  1. For each row, enter a 1 if the file will be shared in this "open-access-now" shareable data package. If not shared in this shareable data package, enter a 0.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### README File

--8<-- "submit/modules/readme1.md"

</div>
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Zip up your shareable data package

--8<-- "submit/modules/zipup.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Upload your shareable data package to your repository

**Congratulations! You are ready to upload your "open-access now" shareable data package.**

1. Submit your "open-access-now" zipped up shareable data package along with your "overview" Resource Tracker and README file accessory files at the data repository you've selected. The full inventory of items you will submit, and under what access conditions to share them at your repository, include: 
  1. Zipped "open-access now" shareable data package: share as open-access without embargo restrictions
  2. "Overview" Resource Tracker: share as open-access without embargo restrictions
  3. README: share as open-access without embargo restrictions

</div>
</div>

