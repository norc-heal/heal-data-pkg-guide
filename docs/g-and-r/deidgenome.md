---
hide:
  - toc
full-width: true
---

# Deidentification Guidance for Genomic Data

When considering how to deidentify or anonymize data before it is submitted to a repository, genomic data is a special case. Genomic data is complex and highly identifying, especially in combination with other information (e.g., other genomic data types, phenotypic information, etc.), which makes it very difficult to adequately anonymize. 

There is not currently consensus on best practice for deidentification of genomic data, although some methods have shown promise.  Deidentification methods for this type of data will also likely continue to rapidly advance and shift over time as the field of genomic research expands and the number of researchers interested in sharing this type of data increases.

There are a number of different strategies that researchers have utilized to attempt to adequately anonymize this type of data, with varying success. Strategies and recommendations range from only sharing summary data to sharing individual level data with phenotype-only de-identification with strong access controls, to using complex statistical methods, such as differential privacy to additionally de-identify the genotype data directly (still with strong access controls). 

Given the difficulty of anonymizing this data adequately, the best practice at this time is to **apply current best practices in deidentification of this type of data, in consultation with a statistician or other individual familiar with genomic privacy considerations, supplemented by privacy and governance protections**. Privacy and governance protections can include applying access controls, data use agreements, and physical and electronic security protocols.

!!! tip "Note about NIH-funded Genomic Research"

    If your study is funded by NIH and will generate genomic or sequencing data, **you must adhere to the [NIH Genomic Data Sharing Policy](https://sharing.nih.gov/genomic-data-sharing-policy/about-genomic-data-sharing/gds-policy-overview){:target="_blank"}**.

    The genomic data sharing policy provides a framework for genomic data sharing, but some individual NIH Institutes and Centers (IC) may have additional requirements for genomic data sharing. You should review [your specific funding IC requirements](https://sharing.nih.gov/genomic-data-sharing-policy/about-genomic-data-sharing/gds-policy-expectations-by-nih-institute-and-center){:target="_blank"} to help determine what you are required to submit, requirements for submission timing in relation to data collection, and which of the below deidentification methods you should pursue.

Although there is not consensus on best practices for deidentifying this type of data, investigators can generally choose from a few different options when considering how to share their genomic data:

* **Option 1**: Share summary data only
  * If you would like to use this approach and your study is funded by NIH, review the [NIH Genomic Data Sharing Policy](https://sharing.nih.gov/genomic-data-sharing-policy/about-genomic-data-sharing/gds-policy-overview){:target="_blank"} guidelines and those of your specific funding IC to ensure that there are no restrictions on sharing in this way. 
  * If you are able to share summary data only in a public repository, you will still be required to register your study on dbGaP to comply with the NIH Genomic Data Sharing Policy.

* **Option 2**: Share individual-level data
  * This approach requires **sharing with strict access controls**, which can include:
    * Requiring data use agreements (DUA) with IRB approval
    * Requiring researchers work with data in a secure environment such as a data enclave
  * Additionally, **some amount of deidentification will be required for this option**
    * **Best practice**: Work with an expert of deidentification
    * There are two options for deidentifying when sharing individual-level data with strict access controls:
      * **Option A**: Phenotype-only deidentification
        * This involves deidentifying only the clinical/phenotype data that accompanies genotype data but *not* deidentifying the genotype data
        * *Note*: This is the approach dbGaP suggests for data submitted to their repository; dbGaP additionally implements very strong access controls to protect the data
      * **Option B**: Phenotype *and* genotype deidentification
        * This approach involves the use of complex statistical methods that have been used with some success in deidentification of genomic data such as differential privacy tools/algorithms
        * Although with this approach, the resulting dataset with have deidentified phenotypic and genotypic data, this data will likely still require strict access controls due to its sensitivity. Consult with a deidentification expert for guidance on appropriate access controls for your specific dataset.

**References**

* [NIH Genomic Data Sharing Policy](https://sharing.nih.gov/genomic-data-sharing-policy){:target="_blank"}
* [dbGaP Study Submission Guide](https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/){:target="_blank"}: Submission guide for the database of Genotypes and Phenotypes (dbGaP), the repository where all large-scale human genomic studies funded by NIH must register. This guide also provides information on [subject de-identification](https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/#4-what-is-a-dbgap-subject){:target="_blank"} for submission to the repository.
* [A practical path toward genetic privacy (2020)](https://fpf.org/wp-content/uploads/2020/04/APracticalPathTowardGeneticPrivacy_April2020.pdf){:target="_blank"}: Reviews the deidentification landscape as it relates to genomic data, including reviewing regulatory requirements, the challenge of deidentifying this type of data, and some technical solutions. Brings together findings from multiple leading organizations to recommend that deidentification methods be combined with privacy and governance protections.
* [Methods for de-identification of electronic health records for genomic data (2011)](https://genomemedicine.biomedcentral.com/articles/10.1186/gm239){:target="_blank"}: Discusses issues related to deidentification and some good practices for managing reidentification risk related to genomic data. 
* [Privacy considerations for sharing genomic data (2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8326502/){:target="_blank"}: Reviews multiple different genomic data types (sequence, transcriptomic, epigenetic) and their risk of reidentification and reviews some established data sharing techniques
* [Membership privacy in microRNA-based studies (2016)](https://dl.acm.org/doi/10.1145/2976749.2978355){:target="_blank"}: Discusses the threat of reidentification related to microRNA data and discusses potential solutions for sharing this type of data

