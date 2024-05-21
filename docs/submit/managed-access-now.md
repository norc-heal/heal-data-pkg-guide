---
hide:
  - toc
full-width: true
---

# Creating a Managed-Access Now Shareable Data Package

  ![](../assets/prepare-sub-managed.drawio)

<br>

---

--8<-- "submit/modules/remind.md"

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">


--8<-- "submit/modules/set.md"

--8<-- "submit/modules/intro/man-acc-date.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Identify resources and standard data package metadata that meet sharing requirements

1. Navigate to your dsc-pkg folder and open your Resource Tracker. 
2. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files will go into your shareable data package folder.
3. Identify all study files/resources that are designated as managed-access or open-access as of today's date. For reference, the requirements for access and access-date are below:
  1. **"open-access" in access AND "temporary-private" not in access** OR
  2. **"open-access" in access AND "temporary-private" in access AND today's date >= access-date** OR
  3. **"managed-access" in access AND "temporary-private" not in access** OR
  4. **"managed-access" in access AND "temporary-private" in access AND today's date >= access-date**

  !!! warning

      These files **should not** be copied into your new shareable data package folder:
    
      * A file designated as temporary private as of today's date
      * A file designated as permanent private

4. In addition to your study files, you will need to identify which standard data package metadata should be copied into your shareable data package. Standard data package metadata includes the Experiment Tracker, Resource Tracker, Results Tracker(s), and Data Dictionary(ies)
  1. You should automatically copy the Resource Tracker and Experiment Tracker into any shareable data package you create.
  2. Results Tracker(s) and Data Dictionary(ies) have similar restrictions as other files/resources - you should only copy each over if it meets the requirements listed above.

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

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### Overview Resource Tracker

1. Create a copy of the Resource Tracker in your shareable data package folder and move that copy into your "my-study-share" folder. This will be your "Overview" Resource Tracker, which will indicate whether or not each file in the Resource Tracker is shared in the shareable data package.
1. Add a column to the Resource Tracker. A suggested name for this column might be "managed-access-now-shareable-data-pkg."
  2. For each row, enter a 1 if the file will be shared in this "managed-access now" shareable data package. If not shared in this shareable data package, enter a 0.

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

**Congratulations! You are ready to upload your "managed-access now" shareable data package.**

1. Submit your "managed-access-now" zipped up shareable data package along with your "overview" Resource Tracker and README file accessory files at the data repository you've selected. The full inventory of items you will submit, and under what access conditions to share them at your repository, include: 
  1. Zipped "managed-access now": share as managed-access without embargo restrictions
  2. "Overview" Resource Tracker: share as open-access without embargo restrictions
  3. Your README: share as open-access without embargo restrictions

</div>
</div>
