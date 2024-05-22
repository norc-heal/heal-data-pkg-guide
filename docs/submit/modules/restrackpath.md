<!-- File path updates for Resource and Results Trackers -->

Next, you will need to make one adjustment to the Resource Tracker and any Results Tracker(s) in your shareable data package folder. 

* All local file paths to study files/resources listed in the Resource Tracker or any Results Tracker to be included in a shareable data package should be converted to relative file paths for the modified Tracker versions included in any shareable data package.
  * Every path disclosed will be in relation to your dsc-pkg folder.
  * This is to protect the privacy of local computer systems and to make navigation of study files easier for secondary users.
  * As mentioned previously, this method works best when your local data package is centralized (i.e., all study files and your dsc-pkg folder containing standard data package metadata are in a single, centralized local data package or my-study folder). 

See below for information on which fields in your Resource Tracker or Results Tracker(s) may hold file paths that will need to be adjusted. ***Reminder:** You will be making these adjustments to the Resource Tracker and Results Tracker(s) within your shareable data package folder (copied over from your local data package), not to the versions of these files in your local data package's dsc-pkg folder.*

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

##### [Resource Tracker](link to schema)

* path
* associatedFileDataDict
* associatedFileProtocol
* associatedFileResultsTracker
* associatedFileDependsOn
* associatedFileResultsDependOn
* associatedFileMultiLikeFiles

##### [Results Tracker(s)](link to schema)

* associatedFilePublication
* associatedFileDependsOn

</div>