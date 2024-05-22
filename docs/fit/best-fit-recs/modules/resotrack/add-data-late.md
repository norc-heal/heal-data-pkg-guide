<!-- Late data standard, low; early data low-->

* First, add your finalized dataset-of-interest to your Resource Tracker.
  * If the finalized dataset-of-interest is a tabular data file, include the data dictionary as one of the dependencies of this resource.
* Next, add all associated files/dependencies for the finalized dataset-of-interest to the Resource Tracker. 
  * Remember that whenever you add a tabular data file to your Resource Tracker, you should first create a data dictionary. Then, add the tabular file to the Resource Tracker and list the data dictionary you have created as a dependency.
* Finally, any file that has been added as an associated files/dependency of a resource in the Resource Tracker should themselves be added as a resource.
  * Repeat this process with the dependencies of these files until you're listing files without any dependencies.

