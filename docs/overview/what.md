# What is a data package? 

A *data package* is a stand-alone collection of data and supporting files
intended for a specific purpose. A data package contains the following:

1. One or more data files or links to data files accessible or stored elsewhere
2. Non-data, supporting files such as protocols, data collection instruments,
   code for manipulating or analyzing the data, discipline-specific metadata
   files describing the data, and additional documentation
3. [Standard data package metadata files](../terms/index.md#standard-data-package-metadata-files)
   that are both human- and machine-readable

A *shareable data package* is a data package that meets the following three
requirements:

1. All of the files are intended for sharing, possibly under a
   *data use agreement* (DUA) or specific set of restrictions.
2. Sufficient information on the provenance and terms of use are included to
   make the data reusable.
3. Sufficient metadata and documentation are included so that the package may
   be used by a researcher unconnected to and without special knowledge of the
   original study.

Typically, a data package can be converted to a shareable data package simply
by redacting any items that cannot be shared, replacing them with an
appropriate substitute or placeholder whenever possible. For example, a
researcher may replace dates with shifted dates or topcode certain variables
to help maintain participant confidentiality. Such changes are ideally made
prior to analysis so that the original investigator is analyzing the exact
same data file(s) that will be shared to facilitate reproduciblity.

A common and important case is when none of the data can be shared, and thus
all of the data file(s) must be excluded from the data package. For example, a
research project may exclusively be analyzing secondary data that, while
broadly accessible, may not be redistributed (research data available from
public repositories often falls into this category). In such cases, the data
may be physically stored outside the data package and replaced with a link to
the data; the resulting data package may then be shared with and used by
researchers who independently obtain access to the data. In this way, one may
think of a data package as *supporting the use a particular dataset for a
specific purpose, whether are not the data themselves are contained in the
package*.


## Metadata files provide context and usability

Data sharing requirements by funders or journals are often stated in general
terms only (e.g., "You must share all data underlying published results").
This creates two problems: (1) a researcher may nominally comply by simply
sharing his or her existing files, which may or may not be useable by others;
and (2) it leads researchers to focus on the data only, to the exclusion of
metadata and other resources (e.g., code) that are needed to use the data
effectively and/or increase their scientific value.

Aside from the data themselves, it is important for investigators to provide
context and usability information, including: what questions was the study
group trying to answer in collecting the data, how did they design study
experiment(s)/activity(s) to answer those questions, how was data collected,
what data was collected, what is in each data file, how to use it, how it
relates to other data files, how it relates to published results, etc.

**In fact, supporting or metadata files that include this context and
usability information are arguably as or more important than the data
itself**. Without the context information, it is difficult for potential
secondary data users or collaborators to get even a high-level sense of
whether it may be productive to request access to study data or to reach out
regarding a collaboration with the originating study group. Without the
usability information, it is difficult for potential secondary data users or
collaborators to get a more granular view of whether the collected data may be
usable for their secondary data use purposes, and it may be difficult or
impossible to understand and actually use the data for their secondary data
use purpose.

Some research communities have clear standards for how to create and provide
at least some of the critical metadata required to ensure discoverability,
understanding, and usability of commonly collected data types (e.g.
neuroimaging, genomice, GIS) or datasets collected in the course of a commonly
conducted study type (e.g. clinical trial). These standards are incredibly
valuable and essential for detailed discovery and reuse of especially very
complex data and study types. Research communities should always be in charge
of forging the standards very specific to their own community as they are,
indeed, the only ones with the deep knowledge and experience to do so.


### Standard Data Package Metadata as a bridge across communities 

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

The HEAL Initiative has developed [Standard Data Package Metadata](../terms/index.md#standard-data-package-metadata-files) and best practices as to [when](./when.md) and [how](./how.md) to implement these metadata, to be leveraged by all studies across all research communities, as a way to bridge across research communities and other data and knowledge producer and consumer communities. 

Standard Data Package Metadata are a small set of standard metadata file types that, altogether, provide essential usability and context information about the study as a whole and about the data files your study has produced/collected. These metadata files should be included in all HEAL Initiative data packages. 

They produce a common language and universally understandable structure for all studies across the spectrum of research communities that are a part of the HEAL Initiative. 

These are not meant to replace or supercede research community specific standards. Rather, they are meant to fully accommodate, never conflict with, and lightly add value to research community specific metadata standards.
