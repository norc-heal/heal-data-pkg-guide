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
