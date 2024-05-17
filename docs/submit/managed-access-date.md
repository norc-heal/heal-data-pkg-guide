---
hide:
  - toc
full-width: true
---

# Creating a Managed-Access by Specified Date Shareable Data Package

  ![](../assets/prepare-sub-managed-date.drawio)


<br>


---

--8<-- "submit/modules/remind.md"


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px;">


<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

--8<-- "submit/modules/set.md"

--8<-- "submit/modules/intro/man-acc-date.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Identify resources that meet sharing requirements

1. Navigate to your dsc-pkg folder and open your Resource Tracker. 
2. The two fields most important to this step are "access" and "access-date." You will use the values in these columns to determine which files will go into your shareable data package folder.
3. Identify all study files/resources that are designated as managed-access as of the date you are planning to share your data package at a repository. For reference, the requirements for access and access-date are below:
  1. **"open-access" in access AND "temporary-private" not in access** OR
  2. **"open-access" in access AND "temporary-private" in access AND date planned for sharing at a repository >= access date**
  3. **"managed-access" in access AND "temporary-private" not in access** OR
  4. **"managed-access" in access AND "temporary-private" in access AND date planned for sharing at a repository >= access-date** OR

  !!! warning

      These files **should not** be copied into your shareable data package folder:
    
      * A file designated as temporary private with an access date later than the intended sharing date for this data package
      * A file designated as permanent private

4. In addition to your study files, you will need to identify which standard data package metadata should be copied into your shareable data package. Standard data package metadata includes the Experiment Tracker, Resource Tracker, Results Tracker(s), and Data Dictionary(ies)
  1. You should automatically copy the Resource Tracker and Experiment Tracker into any shareable data package you create.
  2. Results Tracker(s) and Data Dictionary(ies) have similar restrictions as other files/resources - you should only copy each over if it meets the requirements listed above.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Copy open-access and managed-access files into your 'managed-access-by-date' shareable data package folder

--8<-- "submit/modules/copyover.md"
        
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare Resource and Results Trackers

--8<-- "submit/modules/restrackpath.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Zip up your shareable data package

--8<-- "submit/modules/zipup.md"

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Prepare other materials for submission

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### Overview Resource Tracker

1. Navigate to the edited Resource Tracker you saved in your "my-study-share-current-date" directory in the previous step.
1. Add a column to the Resource Tracker called "managed-access-by-date-shareable-data-pkg." Replace "date" with the applicable date on which you intend to share your data package at a repository.
  2. For each row, enter a 1 if the file will be shared in this "managed-access-by-date" shareable data package. If not shared in this shareable data package, enter a 0.

</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### README File

--8<-- "submit/modules/readme1.md"

</div>
</div>

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

#### Upload your shareable data package to your repository

**Congratulations! You are ready to upload your "managed-access-by-date" shareable data package.**

1. Your final "managed-access-by-date" shareable data package should include 3 items:
  1. Your zipped "managed-access-by-date" shareable data package
  2. Two open-access files
    1. Your edited Resource Tracker, which designates which files are included in the zipped data package.
    2. Your README.
2. You should share the edited Resource Tracker and README at your chosen data repository as open-access files and the zipped "managed-access-by-date" shareable data package as managed-access with embargo restrictions applied through the repository until the date intended for sharing.

</div>
</div>

