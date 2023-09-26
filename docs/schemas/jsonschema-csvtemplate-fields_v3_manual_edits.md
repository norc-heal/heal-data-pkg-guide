# HEAL Data Dictionary

*HEAL DSC Core Metadata piece to track and provide basic information about variables in a tabular data file (i.e. a data file with rows and columns) from your HEAL study. Objective is to list all variables and descriptive information about those variables. This will ensure that potential secondary data users know what data has been collected or calculated and how to use these data. Note that a given study can have multiple tabular data files; You should create a data dictionary for each tabular data file. Thus, a study may have multiple data dictionaries*

*This is an abridged version of the schema and only describes the fields/information you should provide for each variable. For the full HEAL Data Dictionary document schema specification, see [here](https://github.com/HEAL/heal-metadata-schemas/blob/main/variable-level-metadata-schema/schemas/jsonschema/data-dictionary.json).*

<div markdown="1" style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: top; padding:10px 10px; margin-bottom: 10px;">

NOTE:

* Only `name` and `description` properties are required. 
* For categorical variables, `constraints.enum` and `encodings` (where applicable) properties are highly encouraged. 
* For studies using HEAL or other common data elements (CDEs), `standardsMappings` information is highly encouraged.
* `type` and `format` properties may be particularly useful for some variable types (e.g. date-like variables)  

</div>

## Properties


**`module`** _(string)_: The section, form, survey instrument, set of measures  or other broad category used 
to group variables.

Examples:

```
    Demographics

```

```
    PROMIS

```

```
    Medical History

```


**`name`** _(string,required)_: The name of a variable (i.e., field) as it appears in the data. 

Examples:

```
    gender_id

```


**`title`** _(string)_: The human-readable title or label of the variable. 


Examples:

```
    Gender identity

```

**`description`** _(string,required)_: An extended description of the variable. This could be the definition of a variable or the question text (e.g., if a survey). Include measurement units in the description where relevant (e.g. temperature in celsius, distance in millimeters). 

Examples:


```
    The participant's age at the time of study enrollment, in years

```

**`type`** _(string)_: A classification or category of a particular data element or property expected or allowed in the dataset. Must be one of: `["number", "integer", "string", "any", "boolean", "date", "datetime", "time", "year", "yearmonth", "duration", "geopoint"]`. For details and examples of each of these types see [here](#type-enum-definitions).



**`format`** _(of below)_: Indicates the format of the type specified in the `type` property. Each format is dependent on the `type` specified. For example: If `type` is "string", then see the [String formats](https://specs.frictionlessdata.io/table-schema/#string). If `type` is "date", "datetime", or "time", default format is ISO8601 formatting for those respective types (see details on ISO8601 format for [Date](https://specs.frictionlessdata.io/table-schema/#date), [Datetime](https://specs.frictionlessdata.io/table-schema/#datetime), or [Time](https://specs.frictionlessdata.io/table-schema/#time)) - If you want to specify a date-like variable using standard Python/C strptime syntax, see [here](#format-details-for-date-datetime-time-type-variables) for details. See [here](https://specs.frictionlessdata.io/table-schema/#types-and-formats) for more information about appropriate `format` values by variable `type`. 


**`constraints.maxLength`** _(integer)_: Indicates the maximum length of an iterable (e.g., array, string, or object). For example, if 'Hello World' is the longest value of a categorical variable, this would be a maxLength of 11.


**`constraints.enum`** _(string)_: Constrains possible values to a set of values. If a variable is contrained to a set of values, you may want to consider providing more information about what each value in the set mean using the `encodings` property for the same variable (e.g. If a variable has possible values of 1, 2, and 3 and these correspond to "yes", "no" and "maybe", you can indicate the constraint of this variable to values of 1, 2, and 3 using the `constraints.enum` property for that variable, and you can indicate that 1="yes", 2="no", and 3="maybe" using the `encodings` property for that variable).

Examples:


```
    1|2|3|4|5|6|7|8

```


```
    Treated|Control

```

**`constraints.pattern`** _(string)_: A regular expression pattern the data MUST conform to.


**`constraints.maximum`** _(integer)_: Specifies the maximum value of a field (e.g., maximum -- or most
recent -- date, maximum integer etc). Note, this is different than maxLength property.


**`constraints.minimum`** _(integer)_: Specifies the minimum value of a field.


**`encodings`** _(string)_: For variables constrained to a set of values, variable value encodings provide a way to further annotate each value in the constrained set of values the variable can take on, making values easier to understand. If a variable is contrained to a set of values, you may want to consider providing the set of values to which the variable is constrained using the `constraints.enum` property for that variable, and then providing more information about what each value in the set means using the `encodings` property for the same variable (e.g. If a variable has possible values of 1, 2, and 3 and these correspond to "yes", "no" and "maybe", you can indicate the constraint of this variable to values of 1, 2, and 3 using the `constraints.enum` property for that variable, and you can indicate that 1="yes", 2="no", and 3="maybe" using the `encodings` property for that variable).


Examples:


```
    0=No|1=Yes

```

```
    HW=Hello world|GBW=Good bye world|HM=Hi,Mike

```

**`ordered`** _(boolean)_: Indicates whether a categorical variable is ordered. This variable is relevant for variables that have an ordered relationship but not necessarily  a numerical relationship (e.g., Strongly disagree < Disagree < Neutral < Agree). If ordered is set as True, order will be set based on ordering of values provided in the `constraints.enum` property for this variable. 


**`missingValues`** _(string)_: A list of missing values specific to a variable.

Examples:


```
    Missing|Skipped|No preference

```

```
    Missing

```

**`trueValues`** _(string)_: For boolean (true) variable (as defined in type field), this field allows
a physical string representation to be cast as true (increasing readability of the field). It can include one or more values.

Examples:


```
    REQUIRED

```

```
    required|Yes|Y|Checked

```


**`falseValues`** _(string)_: For boolean (false) variable (as defined in type field), this field allows
a physical string representation to be cast as false (increasing readability of the field) that is not a standard false value. It can include one or more values.


**`standardsMappings.url`** _(string)_: A url that links out to a published, standardized mapping for the variable. For example, if a variable corresponds to the first question in a published, validated survey  instrument to measure depression (e.g. PHQ9), provide a link to the PHQ9 Questionnaire at the NIH Common Data Element Repository. This property is under development, and may be restricted in future to persistent identifier urls such as a [DOI](https://www.doi.org/).  



Examples:


```
    https://cde.nlm.nih.gov/formView?tinyId=myG8MkTbwg

```

**`standardsMappings.type`** _(string)_: The type of published, standardized mapping available for the variable (e.g. a variable may correspond to a Common Data Element, or CDE, within the NIH Common Data Elements program). This property is under development, and will have a controlled vocabulary. 


Examples:


```
    cde
```

```
    ontology
```

```
    reference_list
```

**`standardsMappings.label`** _(string)_: A free text label that may be used to provide any information available about a published, standardized mapping available for the variable in an unstructured manner (e.g. if a variable corresponds to the first question in the PHQ9 Questionnaire, which is a published, validated survey  instrument to measure depression, it may be useful to provide information about th standard that variable reflects using free text such as "depression, PHQ, PHQ9"). 


**`standardsMappings.source`** _(string)_: The source of the published, standardized mapping available for the variable (e.g. the [NIH CDE Repository](https://cde.nlm.nih.gov/home)). This property is under development, and will have a controlled vocabulary. 


**`standardsMappings.id`** _(string)_: The identifier (ID) of the published, standardized mapping available for the variable within the source provided in the `standardsMappings.source` property for this variable (e.g. the PHQ9 Questionnaire has been assigned ID "[myG8MkTbwg](https://cde.nlm.nih.gov/formView?tinyId=myG8MkTbwg#identifiers:~:text=NLM-,myG8MkTbwg,-2014Mar19)" at the NIH CDE Repository CDE source).


**`relatedConcepts.url`** _(string)_: The url that links out to the published, standardized concept.


Examples:


```
    https://meshb.nlm.nih.gov/record/ui?ui=D018410

```

**`relatedConcepts.type`** _(string)_: The type of mapping to a published set of concepts related to the given field such as ontological information (eg. NCI thesaurus, bioportal etc)


**`relatedConcepts.label`** _(string)_: A free text label of mapping to a published set of concepts related to the given field such as ontological information (eg., NCI thesaurus, bioportal etc)


**`relatedConcepts.source`** _(string)_: The source of the related concept. This property is under development, and will have a controlled vocabulary. 


**`relatedConcepts.id`** _(string)_: The id locating the individual mapping within the given source.


**`univarStats.median`** _(number)_
 

**`univarStats.mean`** _(number)_
 

**`univarStats.std`** _(number)_
 

**`univarStats.min`** _(number)_
 

**`univarStats.max`** _(number)_
 

**`univarStats.mode`** _(number)_
 

**`univarStats.count`** _(integer)_
 

**`univarStats.twentyFifthPercentile`** _(number)_
 

**`univarStats.seventyFifthPercentile`** _(number)_
 

**`univarStats.categoricalMarginals.name`** _(string)_
 

**`univarStats.categoricalMarginals.count`** _(integer)_

----------------------------

# End of schema - Extra infomation


## `type` enum definitions

-  `number` (A numeric value with optional decimal places. (e.g., 3.14))
-  `integer` (A whole number without decimal places. (e.g., 42))
-  `string` (A sequence of characters. (e.g., \"test\"))
-  `any` (Any type of data is allowed. (e.g., true))
-  `boolean` (A binary value representing true or false. (e.g., true))
-  `date` (A specific calendar date. (e.g., \"2023-05-25\"))
-  `datetime` (A specific date and time, including timezone information. (e.g., \"2023-05-25T10:30:00Z\"))
-  `time` (A specific time of day. (e.g., \"10:30:00\"))
-  `year` (A specific year. (e.g., 2023)
-  `yearmonth` (A specific year and month. (e.g., \"2023-05\"))
-  `duration` (A length of time. (e.g., \"PT1H\")
-  `geopoint` (A pair of latitude and longitude coordinates. (e.g., [51.5074, -0.1278]))

## `format` details for date, datetime, time `type` variables

__Date Formats__ _(string)_
     A format for a date variable (`date`,`time`,`datetime`). Highly recommended to be an ISO8601 format string   
        **default**: An ISO8601 format string.
        **any**: Any parsable representation of a date/time/datetime. The implementing library can attempt to parse the datetime via a range of strategies.

    **{PATTERN}**: The value can be parsed according to `{PATTERN}`,
     which `MUST` follow the date formatting syntax of 
     C / Python [strftime](http://strftime.org/) such as:

    - "`%Y-%m-%d` (for date, e.g., 2023-05-25)"
    - "`%Y%-%d` (for date, e.g., 20230525) for date without dashes"
    - "`%Y-%m-%dT%H:%M:%S` (for datetime, e.g., 2023-05-25T10:30:45)"
    - "`%Y-%m-%dT%H:%M:%SZ` (for datetime with UTC timezone, e.g., 2023-05-25T10:30:45Z)"
    - "`%Y-%m-%dT%H:%M:%S%z` (for datetime with timezone offset, e.g., 2023-05-25T10:30:45+0300)"
    - "`%Y-%m-%dT%H:%M` (for datetime without seconds, e.g., 2023-05-25T10:30)"
    - "`%Y-%m-%dT%H` (for datetime without minutes and seconds, e.g., 2023-05-25T10)"
    - "`%H:%M:%S` (for time, e.g., 10:30:45)"
    - "`%H:%M:%SZ` (for time with UTC timezone, e.g., 10:30:45Z)"
    - "`%H:%M:%S%z` (for time with timezone offset, e.g., 10:30:45+0300)" 
