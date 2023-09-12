# HEAL Data Dictionary

*HEAL DSC Core Metadata piece to track and provide basic information about variables in a tabular data file (i.e. a data file with rows and columns) from your HEAL study. Objective is to list all variables and descriptive information about those variables. This will ensure that potential secondary data users know what data has been collected or calculated and how to use these data. Note that a given study can have multiple tabular data files; If the tabular data files contain different variables, you should create a data dictionary for each tabular data file. Thus, a study may have multiple data dictionaries*

*This is an abridged version of the schema and only describes the fields/information you should provide for each variable. For the full HEAL Data Dictionary document schema specification, see [here](https://github.com/HEAL/heal-metadata-schemas/blob/main/variable-level-metadata-schema/schemas/jsonschema/data-dictionary.json).*

## Properties



- **`module`** *(string)*: The section, form, survey instrument, set of measures  or other broad category used 
to group variables.


    Examples:
    ```json
    "Demographics"
    ```

    ```json
    "PROMIS"
    ```

    ```json
    "Substance use"
    ```

    ```json
    "Medical History"
    ```

    ```json
    "Sleep questions"
    ```

    ```json
    "Physical activity"
    ```

- **`name`** *(string, required)*: The name of a variable (i.e., field) as it appears in the data.    
- **`title`** *(string)*: The human-readable title or label of the variable.   

    Examples:
    ```json
    "My Variable (for name of my_variable)"
    ```

- **`description`** *(string, required)*: An extended description of the variable. This could be the definition of a variable or the question text (e.g., if a survey). 


    Examples:
    ```json
    "Definition"
    ```

    ```json
    "Question text (if a survey)"
    ```

- **`type`** *(string)*: A classification or category of a particular data element or property expected or allowed in the dataset. Must be one of: `["number", "integer", "string", "any", "boolean", "date", "datetime", "time", "year", "yearmonth", "duration", "geopoint"]`. For details and examples of each of these types see [here].
- **`format`**: A format taken from one of the [frictionless specification](https://specs.frictionlessdata.io/) schemas. Each format is dependent on the `type` specified. For example: If `type` is "string", then see the String formats. If `type` is one of the date-like formats, then see Date formats. For format type details and examples and technical details on how to populate this field see [here].

- **`constraints`** *(object)*
    - **`maxLength`** *(integer)*: Indicates the maximum length of an iterable (e.g., array, string, or
  object). For example, if 'Hello World' is the longest value of a
  categorical variable, this would be a maxLength of 11.
    - **`enum`** *(array)*: Constrains possible values to a set of values.
    - **`pattern`** *(string)*: A regular expression pattern the data MUST conform to.
    - **`maximum`** *(integer)*: Specifies the maximum value of a field (e.g., maximum -- or most
  recent -- date, maximum integer etc). Note, this is different then
  maxLength property.
    - **`minimum`** *(integer)*: Specifies the minimum value of a field.
- **`encodings`** *(object)*: Variable value encodings provide a way to further annotate any value within a any variable type, making values easier to understand. Many analytic software programs (e.g., SPSS,Stata, and SAS) use numerical encodings and some algorithms only support numerical values. Encodings (and mappings) allow categorical values to be stored as numerical values. Additionally, as another use case, this field provides a way to store categoricals that are stored as  "short" labels (such as abbreviations).


    Examples:
    ```json
    {
        "0": "No",
        "1": "Yes"
    }
    ```

    ```json
    {
        "HW": "Hello world",
        "GBW": "Good bye world",
        "HM": "Hi, Mike"
    }
    ```

- **`ordered`** *(boolean)*: Indicates whether a categorical variable is ordered. This variable  is
relevant for variables that have an ordered relationship but not
necessarily  a numerical relationship (e.g., Strongly disagree < Disagree
< Neutral < Agree).
- **`missingValues`** *(array)*: A list of missing values specific to a variable.
- **`trueValues`** *(array)*: For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing
readability of the field). It can include one or more values.
    - **Items** *(string)*

        Examples:
        ```json
        "Required"
        ```

        ```json
        "REQUIRED"
        ```

        ```json
        "required"
        ```

        ```json
        "Yes"
        ```

        ```json
        "Checked\""
        ```

- **`falseValues`** *(array)*: For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing
readability of the field) that is not a standard false value. It can include one or more values.

- **`repo_link`** *(string)*: A link to the variable as it exists on the home repository, if applicable
.
- **`standardsMappings`** *(array)*: A published set of standard variables such as the NIH Common Data Elements program.

    - **Items** *(object)*
        - **`type`** *(string)*: The **type** of mapping linked to a published set of standard variables such as the NIH Common Data Elements program.

            Examples:
            ```json
            "cde"
            ```

            ```json
            "ontology"
            ```

            ```json
            "reference_list"
            ```

        - **`label`** *(string)*: A free text **label** of a mapping indicating a mapping(s) to a published set of standard variables such as the NIH Common Data Elements program.

            Examples:
            ```json
            "substance use"
            ```

            ```json
            "chemical compound"
            ```

            ```json
            "promis"
            ```

        - **`url`** *(string)*: The url that links out to the published, standardized mapping.
    
            Examples:
            ```json
            "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
            ```

        - **`source`** *(string)*: The source of the standardized variable.


            Examples:
            ```json
            "TBD (will have controlled vocabulary)"
            ```

        - **`id`** *(string)*: The id locating the individual mapping within the given source.

- **`relatedConcepts`** *(array)*: Mappings to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc)

    - **Items** *(object)*
        - **`type`** *(string)*: The **type** of mapping to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc).
        - **`label`** *(string)*: A free text **label** of mapping to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc).
        - **`url`** *(string)*: The url that links out to the published, standardized concept.

            Examples:
            ```json
            "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
            ```

        - **`source`** *(string)*: The source of the related concept.
            Examples:
            ```json
            "TBD (will have controlled vocabulary)"
            ```

        - **`id`** *(string)*: The id locating the individual mapping within the given source.

- **`univarStats`** *(object)*: Univariate statistics inferred from the data about the given variable.
    - **`median`** *(number)*
    - **`mean`** *(number)*
    - **`std`** *(number)*
    - **`min`** *(number)*
    - **`max`** *(number)*
    - **`mode`** *(number)*
    - **`count`** *(integer)*: Minimum: `0`.
    - **`twentyFifthPercentile`** *(number)*
    - **`seventyFifthPercentile`** *(number)*
    - **`categoricalMarginals`** *(array)*
        - **Items** *(object)*
            - **`name`** *(string)*
            - **`count`** *(integer)*

