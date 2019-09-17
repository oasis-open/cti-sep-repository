# SEP Name
Access Control Specitifcation (ACS) Marking Object Type

## SEP Identifier
`x-isa-acs-3-0`

## SEP Version
1

## SEP Description
This SEP models ACS markings used by DHS NCCIC.

The Access Control Specification (ACS)  marking type defines the object types required to implement 
automated access control systems based on the relevant policies governing sharing between participants. 
The value of the definition_type property MUST be x-isa-acs-3-0 when using this marking type.

Information sharing across a Federal Cybersecurity Information Sharing Community requires a capability 
to protect and allow access to information in accordance with applicable information sharing agreements, 
policies, and laws. This marking definition is the result of collaboration among this community.

Please refer to "Information Sharing Architecture (ISA) Access Control Specification (ACS) Version 3.0"  
[ref] for more information on creating ACS data marking definitions.

## SEP Use Cases
* When content is shared with the DHS NCCIC, it should use these markings.

## SEP Sponsors
Org | Primary Contact
--- | ---------------
Mitre | Rich Piazza
DHS | Marlon Taylor

## POC Implementations
Org | GitHub Repository
--- | -----------------
Mitre | TBD 

## SEP Definition

### x-isa-acs-3-0

x-isa-acs-3-0 is the top-level type object of the ACS marking definition type.  

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **sep_version** (required) | `integer` | This required property indicated the specification version of the serialization being used.  The value of this property MUST be 1 for ACS data marking objects defined according to this specification. |                | **identifier** (required)  | `string`  | This required property holds a single unique identifier associated with the resource. This value can be used for tracking data provenance, executing data retraction, and enforcing auditing requirements. The Resource Identifier will use a format that includes a prefix and an RFC4122 suffix. The prefix used will include the ISA common prefix (GUIDE prefix). The ISA has been assigned a GUIDE7 (Globally Unique Identifier for Everything) prefix of 19001 for production and 999191 for test use. It is recommended that RFC 4122 Version 4 UUIDs be used for the suffix; however, other versions are permitted. |
| **name** (optional)        |  `string` | This property provides a "handle" to identify and describe this marking definition.  Note that the name property in no way defines the data marking. It is simply provided as a convenience for users. |                | **create_date_time** (required) | `timestamp` | This required property provides the creation date and time of the associated resource as identified by the Identifier. This value supports a number of functions including enforcing data retention policies and auditing requirements. |
| **responsible_entity_custodian** (required) | `string` | This required property represents the data producer that is responsible for providing the associated resource to be shared. It is represented as an organization token. This value is necessary for auditing and enforcing data retention and provenance policies. Allowable values listed in Appendix A: List of Organizations of [ref] **MUST** be used. |
| **responsible_entity_originator** (optional) | `string` | This optional property represents the originating organization for the associated resource. If not present then the origin of the information is unspecified. It is represented as an organization token. The organizations in Appendix A **SHOULD** be used. However, additional tokens may be created to specify the originator. Certain Originators may require anonymity to protect their identity. This is common when dealing with a cybersecurity threat or incident where the originator is an entity in the Private Sector. Cover terms (e.g., USENERGY01) assigned to an entity should be carried through anytime the resource is shared. |
| **authority_reference** (optional) | `string` | This property captures the legal authority under which the content was created, not the limitation on sharing the content. This property is used for auditing and records management, not for access control decisions. In some cases, the Authority Reference is needed by ESSA Participants to be included in the Control Policy Group as well as the Resource Accounting Group.  It **MUST** be of the be of the format urn(:\w+)+. |
| **original_classification** (optional) | `x-isa-acs-original-classification-type` | This property provides details for generating a classification authority block for presentation of a classified resource to an operator. Either the Original Classification or the Derivative Classification is required for classified resources, as appropriate. Details regarding the basic encoding specification detail for Original Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **derivative_classification** (optional) | `x-isa-acs-derivative-classification-type` | This property provides details for generating a classification authority block for presentation of a classified resource to an operator. Either the Original Classification or the Derivative Classification is required for classified resources, as appropriate. Details regarding the basic encoding specification detail for Original Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **declassification** (optional) | `x-isa-acs-declassification-type` | This property provides the declassification instructions associated with an original or derived classification for generating a classification authority block for presentation of a classified resource to an operator. Details regarding the basic encoding specification detail for Declassification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **public_release** (required) | `x-isa-acs-public-release-type` | This property will be used to provide the release authority and date for resources that have been through a formal public release determination process, or note that the resource has not been publicly released. Details regarding the basic encoding specification detail for Public Release are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **control_set** (required) | `x-isa-acs-control-set-type` | The Control Set property is the group of data tags that are used to inform automated access control decisions. |
| **other_determination** (optional) | `list` of type `x-isa-acs-other-determination-enum` | The property holds additional information about the access control. |
| **terms_of_use** (optional) | `list` of type `string` | This property holds caveats and/or other textual statements of usage limits. |

### x-isa-acs-original-classification-type

This type provides details for generating a classification authority block for presentation of a classified resource to an operator. Either the Original Classification or the Derivative Classification is required for classified resources, as appropriate. Details regarding the basic encoding specification detail for Original Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community (Reference 15).

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **classified_by** (required) | `string` | This property contains the name of person with the original classification authority who made a classification determination |
| **classified_on** (optional)  | `timestring` | This property contains the date an original classification determination was made. |
| **classification_reason** (optional)  | `string` | This property contains the rationale for an original classification determination. |
| **compilation_reason** (optional)  | `string` | This property contains the rationale for assigning a higher classification level than a simple roll-up of its portions would indicate. |

### x-isa-acs-derivative-classification-type

This type provides details for generating a classification authority block for presentation of a classified resource to an operator. Either the Original Classification or the Derivative Classification is required for classified resources, as appropriate. Details regarding the basic encoding specification detail for Derivative Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community (Reference 15).

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **classified_by** (required)  | `string` | This property contains the name of person with the derivative classification authority who made a classification determination |
| **classified_on** (optional)  | `timestring` | This property contains the date an original classification determination was made. |
| **derived_from** (required) | `string` | This property contains the citation of the original classification guidance used for a derivative classification. |

### x-isa-acs-declassification-type

This type provides the declassification instructions associated with an original or derived classification for generating a classification authority block for presentation of a classified resource to an operator. Details regarding the basic encoding specification detail for Declassification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community (Reference 15).

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **declass_exemption** (optional)  | `string` | This property contains the basis for a resource not being subject to standard automatic declassification processes. |
| **declass_period** (optional)  | `integer` | This property contains the duration of time in years for calculating from a create date or classification date when a resource will be automatically declassified if not exempt. |
| **declass_date**  (optional)  | `timestamp` | This property contains the date upon which a resource will be automatically declassified if not exempt.|
| **declass_event**  (optional)  | `string` | This property contains the future occurrence upon which a resource will be automatically declassified if not exempt.|

### x-isa-acs-public-release-type

This typr will be used to provide the release authority and date for resources that have been through a formal public release determination process. Resources will further be marked with a formal determination marking (FD=PUBREL) (See Section 2.2.3.4). Details regarding the basic encoding specification detail for Public Release are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community (Reference 15).

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **releasable_to_public**  (required) | `boolean` | This property indicates if this resource can be publicly released. Note, for certain values of the capco_classification property in x-isa-acs-control-set-type the value of this property MUST be false.|
| **released_by** (optional) | `string` | This property contains the authority that authorized the public release.|
| **released_on**  (optional)  | `timestamp` | This property contains the date of public release |

### x-isa-acs-control-set-type

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **capco_classification** (required) | `string` | This property contains information specifying the classification level, SCI controls and dissemination markings as a string adhering to "Intelligence Community Authorized Classification and Control Markings, Register and Manual (Version 5.1)" [ref] |
| **logical_authority_category** (optional) | `list` of type `string` | This property represents classes of authority upon which data can be generated or acquired and that can be used to apply mandatory special access control and handling policies. |
| **community_of_interest** (optional) | `list` of type `string` | This property identifies the limitation on the distribution of the resource based on membership in a closed, secure community of interest (COI). COI membership is managed by the owners of the COI, possibly as a list of authorized users and/or servers.|
| **organization** (optional) | `list` of type `string` | This property identifies the limitation on the distribution of the resource based on organization. Allowable values listed in Appendix A: List of Organizations of [ref] **MUST** be used. |

## Enumerations

### x-isa-acs-other-determination-enum


| Vocabulary Value      | Description        |
| -------------------   | -----------        |
|  AIS| The resource is appropriate for AIS. |
| INFORMATION-DIRECTLY-RELATED-TO-CYBERSECURITY-THREAT |  |
| PII-NECESSARY-TO-UNDERSTAND-THREAT | Personally identifiable information (PII) necessary to understand the context of the resource is present. |
| PII-NOT-PRESENT |Personally identifiable  (PII) is _not_ present.|
| PII |Personally identifiable  (PII) is present.
| PCII |Protected Critical Infrastructure Information (PCII) is present. |

## Examples

Notice these examples of the ACS marking definitions appear as part of a marking-definition STIX object type.

### Example 1

```json
{
      "type": "marking-definition",
      "id": "marking-definition--f4d1771b-d6a6-4eb1-9768-9686efeeb89a",
      "created": "2018-10-01T00:00:00Z",
      "definition_type": "x-isa-acs-3-0", 
      "definition": {
          "identifier": "isa:guide.19001.ACS3-bc9034f8-c732-5328-b9df-d9d72aae480b", 
          "name": "banner-marking",
          "create_date_time": "2016-06-27T14:10:26.723Z",
          "responsible_entity_custodian": "USA.NSA",
          "responsible_entity_originator": "USA.NSA",
          "auth_ref": "urn:isa:authority:CFR2013_32_2_236", 
           "original_classification": {
               "classified_by": "Available-On-Request",
               "classified_on": "2017-01-10T00:00:00Z",
               "classification_reason ": "Example",
               "compilation_reason": "Orig-Doc"
           },
           "derivative_classification": {
               "classified_by": "Available-On-Request",
               "classified_on": "2018-02-20T00:00:00Z",
               "derived_from": "Orig-Doc"
           },
           "declassification": {
               "declass_period": "32",
               "declass_date": "2020-02-20T00:00:00Z",
               "declass_event": "Per Exec Order blah-blah-blah"
           },
           "public_release": {
               "releasable_to_public": "false"
           },
           "control_set": {
                "capco_classification": "TS//SI//REL TO USA, FVEY",
                "logical_authority_category": ["LAC12345"],
                "community_of_interest": ["NTOC_DHS_ECYBER_SVC_SHARE.NSA.NSA"],
                "organization": ["USA.NSA", "USA.DHS"]
           },
           "other_determination": ["AIS"], 
           "terms_of_use": ["May be used for network defense for CISA uses. Anonymous access is not allowed. May be further shared with…."]
      }
}

```
### Example 2

```json

{
    "type": "marking-definition",
    "id": "marking-definition--11b6042f-7b98-4b97-a168-bec4c025dda9",
    "created": "2018-10-01T00:00:00Z",
    "definition_type": "x-isa-acs-3-0", 
    "definition": {
          "identifier": "isa:guide.19001.ACS3-bc9034f8-c732-5328-b9df-d9d72aae4ccc", 
          "name": "some_unclassified_marking",
          "create_date_time": "2016-06-27T14:10:26.723Z",
          "responsible_entity_custodian": "USA.NSA",
          "responsible_entity_originator": "USA.NSA",
          "auth_ref": "urn:isa:authority:CFR2013_32_2_236",
          "public_release": {
               "releasable_to_public": "true",
               "released_by": "DHS Public Relations Office",
               "released_on": "2018-07-20T00:00:00Z"
            },
          "control_set": {
                "capco_classification": "U//FOUO",
                "organization": ["USA.NSA", "USA.DHS"]
           },
          "other_determination": ["AIS", "INFORMATION-DIRECTLY-RELATED-TO-CYBERSECURITY-THREAT"],
          "terms_of_use": ["May be used for network defense for CISA uses. Anonymous access is not allowed. May be further shared with…."]
    }
}
```


