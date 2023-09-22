# What is a data package? 

[TL;DR](#a-data-package-includes) to skip to a clear list of what's in a data package!

### Context and usability are important

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Data sharing requirement often only mention sharing data (e.g. "You must share all data underlying published results"). Aside from the data itself, it is important for investigators to provide context and usability information, including: what questions was the study group trying to answer in collecting the data, how did they design study experiment(s)/activity(s) to answer those questions, how was data collected, what data was collected, what is in each data file, how to use it, how it relates to other data files, how it relates to published results, etc. 

</div>

### Metadata files provide context and usability

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

**In fact, supporting or metadata files that include this context and usability information are arguably as or more important than the data itself**. Without the context information, it is difficult for potential secondary data users or collaborators to get even a high-level sense of whether it may be productive to request access to study data or to reach out regarding a collaboration with the originating study group. Without the usability information, it is difficult for potential secondary data users or collaborators to get a more granular view of whether the collected data may be usable for their secondary data use purposes, and it may be difficult or impossible to understand and actually use the data for their secondary data use purpose.

</div>

### Existing metadata standards are valuable

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

Some research communities have clear standards for how to create and provide at least some of the critical metadata required to ensure discoverability, understanding, and usability of commonly collected data types (e.g. neuroimaging, genomice, GIS) or datasets collected in the course of a commonly conducted study type (e.g. clinical trial). These standards are incredibly valuable and essential for detailed discovery and reuse of especially very complex data and study types. Research communities should always be in charge of forging the standards very specific to their own community as they are, indeed, the only ones with the deep knowledge and experience to do so. 

</div>

### Existing metadata standards are not sufficient

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

However, especially in the context of an effort like the NIH HEAL Initiative, which spans many research communities (e.g. pain, opioids, basic science, pre-clinical, clinical, wet-lab, computational, materials and methods development, community-based, surveys, observational, qualitative, pharma, business development), and seeks to promote discoverability, interpretability, and usability of all funded research across these communities, and by both researchers and a broader audience (e.g. community-members, community-based organizations, journalists), research community specific standards alone may fall short of enabling full discoverability, interpretability, and usability across this wide spectrum of data and knowledge producers and consumers, due to: 

#### Within specific research community standards

* Inconsistent or missing content or format recommendations impacting data types, datasets, and data collections collected within the context of the specific research community
* E.g. A standard specifies the need for a data dictionary, but does not provide further specification, so that some people provide it as a PDF, others as a Word document, and still others as an Excel document with a header row containing explanatory notes

#### Across specific research community standards

* No one specific research community standard can be adopted by all communities 

    * It would miss standards needed by other communities
    * It would require or recommend standards not needed or even nonsensical for other communities

* If each community adopted their own community specific standard **and did nothing else**, there would be a lack of discoverability and usability **across** communities

    * Some communities lack clear standards, and so would implement no or inconsistent/ad hoc standards
    * Inward-facing research community specific standards may assume knowledge and understanding that cannot be taken for granted outside of that community both with respect to organization of data and metadata, and with respect to terminology used to describe it
    * Inconsistent content or format recommendations across research communities - E.g. Many community standards require a description of the overall study in some format, however the content and format varies - some specify to provide this is a readme.txt document, others as entered into structured forms such as when registering a clinical trial on [clinicaltrials.gov](https://clinicaltrials.gov/) or a genomic study on [dbGaP](https://www.ncbi.nlm.nih.gov/gap/), and still others do not specify a format; content varies across all of these examples  

</div>

### Standard Data Package Metadata as a bridge across communities 

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

The HEAL Initiative has developed [Standard Data Package Metadata](../terms/index.md#standard-data-package-metadata-files) and best practices as to how to implement these metadata, to be leveraged by all studies across all research communities, as a way to bridge across research communities and other data and knowledge producer and consumer communities. 

Standard Data Package Metadata are a small set of standard metadata file types that, altogether, provide essential usability and context information about the study as a whole and about the data files your study has produced/collected. These metadata files should be included in all HEAL Initiative data packages. 

They produce a common language and universally understandable structure for all studies across the spectrum of research communities that are a part of the HEAL Initiative. 

These are not meant to replace or supercede research community specific standards. Rather, they are meant to fully accommodate, never conflict with, and lightly add value to research community specific metadata standards.

</div>

### A Data Package includes:

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

1. Data files produced/collected by or for the study 
2. Non-data supporting files produced/collected by or for the study 
    * including research community specific standards-based metadata files
3. [Standard Data Package Metadata Files](../terms/index.md#standard-data-package-metadata-files) 

</div>