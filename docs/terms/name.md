## Organize study-related files into folders with consistent naming conventions

* Organize all your files (whether you will share them or not), into folders.
* In general, **minimize the number of folders** at each level, and the number of 'layers' of your whole directory.
    *   File naming conventions can often be used quite effectively to 'organize' files and to provide clues as to what the files are and how they relate to each other without resorting to using separation into different directories to serve that purpose.
* However, there is a limit to naming conventions, and you may want to separate your files into directors based on some type of logical groupings and/or based on th elevel or timing of access to the files you expect to provide. See below for further details.

    !!! note "Reminder"
        Before creating more directories or directory layers, consider whether file-naming conventions may be used more efficiently to create this organization.

## Create logical groupings
There are a number of ways to group files logically. Below are some examples of how you can logically group your files in folder structures:

| Grouping strategy      | Examples                                                  |
| :---------             | :---------------------------------------------------------|
| By file category       | Raw data grouped together; processed data grouped together; <br>protocols grouped together; data dictionaries grouped together|
| By experimental subject| All raw data files from a particular cell (across all protocols grouped <br>together, etc.) |
| By type of experiment  | All current clamp experiment files grouped together; all voltage <br> clamp experiment files grouped together |
| By experiment          | All raw data files mkdocsfrom a particular protocol, across all cells to which <br> the protocol applies, grouped together |
| By file type           | All CorelDraw figure files grouped together |
| By expected use        | All files you expect a primary or secondary user of the data/metadata <br> would want to use and/or cite together (as a package) - for example, <br> grouping files that you expect you will want to provide different levels <br> of access to/access restrictions for and/or that you want to provide <br>access to with different timing. See below for more information on <br>access level and timing.

## Consistently name your files and folders
### Universal conventions

* File and folder names should generally be informative/descriptive
    * Wherever possible name your files and folders in a way that will let a human user reasonably infer quite a lot about what the file holds without any further information
* It is very helpful if file and folder names are all lower case
* Don't use spaces or special characters
* Preferred separator is a dash ('-'), e.g., my-data-file-1

### Special conventions

* If you have **multiple files or folders of the same type**, choose a naming convention that's descriptive, and not unmanageably long, and be consistent. For example:
    * One file per day, per cell, per protocol:
        * Potential convention: "day"-YYYY-MM-DD-"cell"-[0-9]-"protocol"-{short-protocol-description}
            <br>Example filename: day-2023-03-17-cell-3-protocol-200ms-pulse.asc
    * One folder per experimental objective:
        *   Potential convention: {cell-type}-{short-experimental-approach-description}-{short-experimental-objective-description}
            <br>Example foldrer name: drg-current-clamp-effect-of-K1395R-on-drg-neuronal-excitability; drg-voltage-clamp-biophysical-properties-of-K1395R
* If you have **files that are related**, choose a naming convention that's descriptive, and not unmanageably long, and be consistent. For example:
    * A tabular/csv data file that has a data dictionary
        * Potential convention: The data dictionary for a data file has the same filename as the data file, with a "dd-" prefix
        * Example file name(s):
            * <u><i>Data file name</i></u>: my-data-1.csv
            * <u><i>Corresponding data dictionary file name</i></u>: dd-my-data-1.csv
    * Several experiments that each have an experimental protocol
        * Potential convention: The protocol of the experiment has the id of that experiment (from the experiment tracker) in the filename, with a "protocol-" prefix
        * Example file name(s):
            * <u><i>Experiment id (from experiment tracker)</i></u>: exp-1
            * <u><i>Corresponding protocol file name</i></u>: protocol-exp-1.txt
