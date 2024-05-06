---
hide:
  - toc
full-width: true
---

# Preparing your Data Package for Submission

  ![](share.drawio)

Once you have finished preparing your data package locally, you will need to prepare your data package for submission to a repository. This section will walk through the different types of shareable data packages you can consider, how to determine which files should go into your final shareable data package, and how to finalize this data package for submission to a data repository.

You should start by thinking about what sorts of shareable data packages you want to produce. You likely have some files designated as open access and some managed access. Other files may be embargoed until a certain date, at which point they will become open or managed access. You may also have some files that are permanent private, which you will not be sharing. This step will help you determine which files will go into your final shareable data package(s) and how to create them.

## Determining what your shareable data package will look like

Depending on your specific study situation, you may not want to share all your files in a public data repository (e.g., if you collected human subjects data, you would not want to share fully identified versions of this data publicly) or you may not want to share all files in the same way or at the same time.

!!! example ""
    === "Sharing study files with different levels of protection"

        Your study may have generated sensitive data (e.g., deidentified human subjects data with some level of disclosure risk).

        In this case, you may want to share the sensitive data as managed access while sharing study data that are not sensitive (e.g., non-human subject data) or non-data supporting files such as data dictionaries, protocols, and code as open access.

    === "Sharing study files at different times"

        Certain data and results related to your study may not be able to be shared right away. 
        
        You may want to wait for study milestones that will allow you to share your data publicly such as when your study team publishes a manuscript based on this data or secures intellectual property rights. In these cases, you may want to embargo all or some of the data until that date.

How and when you want to share all or some of your study files will determine the approach you take to preparing your data package for submission. 

### Shareable data packages come in multiple "flavors"

| Flavor                   | Process                |
| -------------------------| ----------------------------|
| **open access now** | <ul><li> Create a version of shareable data package that only includes study files that you want to share right away (i.e., no embargo or embargo has already expired) and that you have indicated will be shared as open access</li><li>Share this shareable data package at your data repository as **open access without embargo restrictions**</li><li>Data repository users will be able to see/use these files right away with a low barrier</li> |
| **managed access now** | <ul><li>Create a version of shareable data package that only includes study files that you want to share right away (i.e., no embargo or embargo has already expired) and that you have indicated will be shared as either open access or managed access</li><li>Share this shareable data package at your data repository as **managed access without embargo restrictions**</li><li>Data repository users will be able to see/use these files after completing the (relatively high barrier) process of requesting access in accordance with repository policies|
| **open access by date** | <ul><li>Create a version of shareable data package that includes study files that you want to share right away as well as study files that you will share once a specific date has passed (i.e., under embargo until a specific date in the future) and that you have indicated will be shared as open access</li><li>Share this shareable data package at your data repository as **open access with embargo restrictions**</li><li>Data repository users will be able to see/use the open access now files right away and the date-restricted files once the embargo date has passed with a low barrier |
| **managed access by date** | <ul><li>Create a version of shareable data package that includes study files that you want to share right away as well as study files that you will share once a specific date has passed (i.e., under embargo until a specific date in the future) and that you have indicated will be shared either as open access or managed access</li><li>Share this shareable data package at your data repository as **managed access with embargo restrictions**</li><li>Data repository users will be able to see/use the managed access now files after completing the (relatively high barrier) process of requesting access in accordance with repository policies; for embargoed files, they will be able to begin the process of requesting access once the embargo date passes |

Depending on how and when you are sharing your data, you may want to create more than one "flavor" of shareable data package for your data. 

Situations in which you may want to create and share multiple shareable data packages of different "flavors" at your data repository may include:

* You want to share some files as open access and some as managed access
  * Because it is easiest and fastest for secondary users to get access to an "open access now" (versus "managed access now") shareable data package, creating and sharing both an open access now and managed access now shareable data package maximizes access to your valuable study files.
* You want to share some files right away and others after you've published or secured intellectual property rights
  * Because it will be faster for secondary users to get access to an "open access now" (versus "open access by date," where the data has not yet passed) shareable data package, creating and sharing both an open access now and open access by date shareable data package will allow researchers to access some of your data and supporting files now, maximizing access to your valuable study files

## Creating your shareable data package(s)

Creating a shareable data package largely consists of starting with your local data package and filtering in study files you've indicated you want to share and filtering out study files you've indicated you do not want to share.

* The Resource Tracker and Experiment Tracker should be included by default in any shareable data package created.
* Results Tracker(s) and data dictionary(ies) will only be inlcuded in a shareable data package if they are listed in the Resource Tracker as shareable

Once the shareable data package has been reviewed and approved by the study PI or other appropriate study staff, the shareable data package should be zipped up into a zip archive. The full shareable data package submitted to a public repository will include:
* Zipped data package
* An edited version of your study's Resource Tracker, which designates which files are included in the zipped data package
* A README

Finally, once the full shareable data package is complete, it can be submitted to the data repository selected by the study group.

### First steps to creating a shareable data package

Before you can begin creating your shareable data package, you should make sure your data and metadata are organized and annotated appropriately to facilitate this process.

#### Using standard data package metadata

If you have set up your local data package by adding standard data package metadata (including a resource tracker), **you have already specified which files you will share as well as how and when you will share them** using the "access" and "access date" fields in the Resource Tracker.

!!! info "Key shareable data package fields"
    === "Access"

        See the table below for an refresher on the "access" fields:

        | Field    | Description                 |
        | ----------------| ----------------------------|
        | **open access** | Share with very low barrier to access |
        | **managed access** | Share with relatively high barrier to access, managed either by<br>repository staff or by study staff depending on the repository |
        | **temporary private** | Share after the access date specified |
        | **permanent private** | Do not share |

    === "Access date"

        Access date field is a date value that specifies when a file should be shared.

        This field will only be used if the file to be shared is currently marked as temporary private.


#### Ensuring your study files are shareable

For a file to be considered shareable, each of the following must be true:

1. The file is listed as a resource in the Resource Tracker
2. The access field for that resource is complete
3. If the access field value is temporary private, 1) the access date (which specifies when the file will become shareable) is complete, and 2) there is a second value in "access" of either open or managed access (the way you want to share a file once it is no longer temporary private)

Check that all of the appropriate files are annotated and fields are complete before starting to perpare your data package for submission.

## Next steps

After you decide what "flavor(s)" of shareable data packages you will create for repository submission and confirm your Resource Tracker has the appropriate information for shareable data package creation, see below for instructions on how to create each type of shareable data package.

## Creating a shareable data package

[Creating an open-access shareable data package](open-access.md){ .md-button}

[Creating a managed-access shareable data package](managed-access.md){ .md-button}


