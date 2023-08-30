# HEAL Experiment Tracker

*HEAL DSC Core Metadata piece to track and provide basic information about experiment(s) you will perform as part of your HEAL study. Clinical studies will often have only one experiment to report, while basic science studies often have several experiments that are grouped together under a single study.*

## Properties

- **`experiment.id`** *(string)*: id assigned to each experiment relevant to the data package; prefix is 'exp-' followed by a number starting with 1 for the first experiment, and iterating by 1 for each successive experiment (i.e. exp-1, exp-2, etc.).
- **`experiment.type`** *(string)*: discovery|materials and methods development. Must be one of: `["discovery", "materials and methods development"]`.
- **`experiment.description`** *(string)*: provide a brief description of the experiment; this is NOT a protocol.
- **`experiment.question`** *(array)*: what question(s) does the experimentalist hope to address with this experiment? be as specific as possible.
  - **Items** *(string)*
- **`experiment.hypothesis`** *(array)*: for each question the experimentalist hopes to address with this experiment, what does the experimentalist hypothesize will be the result(s) of the experiment? Be as specific as possible.
  - **Items** *(string)*

