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
The value of the definition_type property **MUST** be `x-isa-acs-3-0` when using this marking type.

Information sharing across a Federal Cybersecurity Information Sharing Community requires a capability 
to protect and allow access to information in accordance with applicable information sharing agreements, 
policies, and laws. This marking definition is the result of collaboration among this community.

Please refer to "Information Sharing Architecture (ISA) Access Control Specification (ACS) Version 3.0"  
[ref] for more information on creating ACS data marking definitions.

## SEP Use Cases
* When content is shared with the DHS NCCIC, it should use these markings.

## SEP Extension Context
* This extension will be used to mark all STIX content consumed and distributed by DHS NCCIC.
* The markings specified in this SEP incorporate data markings related to the CAPCO classification scheme and can be useful
outside the DHS NCCIC.

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

`x-isa-acs-3-0` is the top-level type object of the ACS marking definition type.  

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **sep_version** (required) | `integer` | This required property indicated the specification version of the serialization being used.  <br/> <br/>The value of this property **MUST** be 1 for ACS data marking objects defined according to this specification. | 
| **identifier** (required)  | `string`  | This required property holds a single unique identifier associated with the resource. This value can be used for tracking data provenance, executing data retraction, and enforcing auditing requirements. The Resource Identifier will use a format that includes a prefix and an RFC4122 suffix. The prefix used will include the ISA common prefix (GUIDE prefix). The ISA has been assigned a GUIDE7 (Globally Unique Identifier for Everything) prefix of 19001 for production and 999191 for test use. It is recommended that RFC 4122 Version 4 UUIDs be used for the suffix; however, other versions are permitted. |
| **name** (optional)        |  `string` | This property provides a "handle" to identify and describe this marking definition.  <br/> <br/>Note that the **name** property in no way defines the data marking. It is simply provided as a convenience for users. |                           
| **create_date_time** (required) | `timestamp` | This required property provides the creation date and time of the associated resource as identified by the Identifier. This value supports a number of functions including enforcing data retention policies and auditing requirements. |
| **responsible_entity_custodian** (required) | `string` | This required property represents the data producer that is responsible for providing the associated resource to be shared. It is represented as an organization token. This value is necessary for auditing and enforcing data retention and provenance policies. <br/> <br/> Allowable values listed in Appendix A: List of Organizations of [ref] **MUST** be used. <br/> <br/>The set of allowable values can be thought of as an open vocabulary, but it is not explicitly defined in this specification.|
| **responsible_entity_originator** (optional) | `string` | This optional property represents the originating organization for the associated resource. If not present then the origin of the information is unspecified. It is represented as an organization token. The organizations in Appendix A **SHOULD** be used. However, additional tokens may be created to specify the originator. <br/> <br/>The set of allowable values can be thought of as an open vocabulary, but it is not explicitly defined in this specification.<br/> <br/>Certain Originators may require anonymity to protect their identity. This is common when dealing with a cybersecurity threat or incident where the originator is an entity in the Private Sector. Cover terms (e.g., USENERGY01) assigned to an entity should be carried through anytime the resource is shared. |
| **authority_reference** (optional) | `string` | This property captures the legal authority under which the content was created, not the limitation on sharing the content. This property is used for auditing and records management, not for access control decisions. In some cases, the Authority Reference is needed by ESSA Participants to be included in the Control Policy Group as well as the Resource Accounting Group.  <br/> <br/>It **MUST** be of the be of the format urn(:\w+)+. |
| **policy_reference** (required) | `string` | This property provides the means of indicating a particular policy related to the sharing of the resource. <br/> <br/>Multiple URNs can be included, separated by a space, but one of the following **MUST** be included: <ul><li>urn:isa:policy:acs:ns:v3.0?privdefault=permit&amp;sharedefault=permit</ul></li> <ul><li>urn:isa:policy:acs:ns:v3.0?privdefault=permit&amp;sharedefault=deny</ul></li><ul><li>urn:isa:policy:acs:ns:v3.0?privdefault=deny&amp;sharedefault=permit</ul></li> <ul><li>	urn:isa:policy:acs:ns:v3.0?privdefault=deny&amp;sharedefault=deny</ul></li> Each value MUST be of the format urn(:\w+)+. |
| **original_classification** (optional) | `x-isa-acs-original-classification-type` | This property provides details for generating a classification authority block for presentation of a classified resource to an operator. <br/> <br/>Either the **original_classification** or **derivative_classification** property **MUST** be provided for classified resources, as appropriate. <br/> <br/>Details regarding the basic encoding specification detail for Original Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **derivative_classification** (optional) | `x-isa-acs-derivative-classification-type` | This property provides details for generating a classification authority block for presentation of a classified resource to an operator. <br/> <br/>Either the **original_classification** or **derivative_classification** property **MUST** be provided for classified resources, as appropriate. <br/> <br/>Details regarding the basic encoding specification detail for Original Classification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **declassification** (optional) | `x-isa-acs-declassification-type` | This property provides the declassification instructions associated with an original or derived classification for generating a classification authority block for presentation of a classified resource to an operator. <br/> <br/>Details regarding the basic encoding specification detail for Declassification are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **resource_disposition** (optional) | `x-isa-acs-resource_disposition-type` | This property can be used to provide a fixed date and time at which an action is to be taken on the associated resource, such as destruction. Retention can be enforced through the use of this property or through the use of policies. <br/> <br/>This property allows for specifying ad hoc (i.e., not policy based) retention limitation requests from information creators such as private industry. <br/> <br/>Details regarding the basic encoding specification detail for Resource Disposition are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **public_release** (required) | `x-isa-acs-public-release-type` | This property will be used to provide the release authority and date for resources that have been through a formal public release determination process, or note that the resource has not been publicly released. <br/> <br/>Details regarding the basic encoding specification detail for Public Release are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community [ref]. |
| **access_privilege** (optional) | `list` of type `x-isa-acs-access-privilege-type` | This property provides a means of limiting or permitting specific actions once access control decisions have been made. |
| **further_sharing** (optional) | `list` of type `x-isa-acs-access-privilege-type` |  This property provides a means of limiting or permitting further sharing once original access control decisions have been made. |
| **control_set** (required) | `x-isa-acs-control-set-type` | The **control_set** property is the group of data tags that are used to inform automated access control decisions. |

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

### x-isa-acs-resource-disposition-type

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **disposition_date** (required) | `timestamp` | This property contains the date upon which the declared disposition process is to be initiated. |
| **disposition_process** (required) | `string` | This property contains the allowed disposition process to be performed (e.g., destruction). |


### x-isa-acs-public-release-type

This type will be used to provide the release authority and date for resources that have been through a formal public release determination process. Resources will further be marked with a formal determination marking (FD=PUBREL) (See Section 2.2.3.4). Details regarding the basic encoding specification detail for Public Release are included in the Smart Data – Enterprise Data Header (EDH) Implementation Profile for the Cyber Community (Reference 15).

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **released_by** (optional) | `string` | This property contains the authority that authorized the public release.|
| **released_on**  (optional)  | `timestamp` | This property contains the date of public release |

### x-isa-acs-access-privilege-type

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **privilege_action** (required) | `open-vocab` | This property indicates the action that may be taken when the access privilege is allowed. <br/> <br/>This is an open vocabulary and values **SHOULD** come from `x-isa-privilege-action-ov` vocabulary.|
| **privilege_scope** (required) | `x-isa-acs-privilege-scope-type` | This property indicates the scope of the access privilege. |
| **rule_effect** (required) | `x-isa-acs-rule-effect-enum` | This property indicates if actions are permitted or denied. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-rule-effect-enum` enumeration. |

### x-isa-acs-privilege-scope-type 

| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **permitted_nationalities** (optional) | `list` of type `string` | The **permitted_nationalities** (CTRY) property identifies the limitation on the distribution of the resource based on nationality. <br/> <br/>Allowable values are listed in Geopolitical Entities, Names, and Codes (GENC) Standard Edition 1  **MUST** be used. |
| **permitted_organizations** (optional) | `list` of type `open vocab` | The **permitted_organizations** (ORG) property identifies the limitation on the distribution of the resource based on organization. <br/> <br/>Allowable values listed in Appendix A: List of Organizations of [ref] or the literal ALL **MUST** be used. <br/> <br/>The set of possible values can be thought of as an open vocabulary, but it is not explicitly defined in this specification. |
| **shareabiity** (optional) |  `list` of type `x-isa-acs-shar-enum` | The **shareability** (SHAR) property is used to identify the shareability of a resource that may be released based on the determination of an originator in accordance with established disclosure procedures. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-shar-enum` enumeration.|
| **entity** (optional) | `list` of type `x-isa-acs-entity-enum` | The **entity** (ENTITY) property is used to identify the entities to which information may be released based on the determination of an originator. <br/> <br/>The values of this property MUST come from the `x-isa-acs-entity-enum` enumeration.|

### x-isa-acs-further-sharing-type

| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **sharing_scope** (required) | `list` of type `open-vocab` | This property indicates the scope of the further sharing. The organizations in Appendix A: List of Organizations of [ref] **SHOULD** be used. The values, FOREIGNGOV or SECTOR **MAY** also be used. <br/> <br/> The set of possible values can be thought of as an open vocabulary, but it is not explicitly defined in this specification.
| **rule_effect** (required) | `x-isa-rule-effect-enum` | This property indicates if further sharing is permitted or denied. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-rule-effect-enum` enumeration.  |

### x-isa-acs-control-set-type

#### Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **classification** (required) | `x-isa-acs-classification-enum` | This property contains information specifying the classification level. <br/> <br/>The Classification value contains the classification of the data based on the Executive Order 13526, Classified National Security Information [ref] and the Information Security Manual (ISM) [ref] marking system. Unclassified information will include a classification marking. <br/> <br/>The value of this property **MUST** come from the `x-isa-acs-classification-enum` enumeration. |
| **sci_controls** (optional) | `list` of type `open-vocab` | The appropriate values for the sensitive compartmented information (SCI) property are listed in MDM SCI Control List [ref]. <br/> <br/>The set of possible values can be thought of as an open vocabulary, but it is not explicitly defined in this specification. |
| **logical_authority_category** (optional) | `list` of type `open-vocab` | The **logical_authority_category** (LAC) property represent classes of authority upon which data can be generated or acquired and that can be used to apply mandatory special access control and handling policies. <br/> <br/>The allowable values are listed in the NSA’s Master Data Registry [ref].  <br/> <br/>The set of possible values can be thought of as an open vocabulary, but it is not explicitly defined in this specification. |
| **formal_determination** (optional) | `list` of type `x-isa-acs-fd-enum` | The **formal_determination** (FD) property is used to Indicate other formal determinations beyond classification that have been applied to a resource. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-fd-enum` enumeration. |
| **caveat** (optional) | `list` of type `x-isa-acs-cvt-enum` | The **caveat** (CVT) property is used to indicate a specific control. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-cvt-enum` enumeration. |
| **sensitivity** (optional) | `list` of type `x-isa-acs-sens-enum` |The **sensitivity** (SENS) property is used to specify an inherent sensitivity about the data that requires specific restrictions in access or handling. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-sens-enum` enumeration.
| **shareabiity** (optional) |  `list` of type `x-isa-acs-shar-enum` | The **shareability** (SHAR) property is used to identify the shareability of a resource that may be released based on the determination of an originator in accordance with established disclosure procedures. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-shar-enum` enumeration.|
| **entity** (optional) | `list` of type `x-isa-acs-entity-enum` | The entity (ENTITY) property is used to identify the entities to which information may be released based on the determination of an originator. <br/> <br/>The values of this property **MUST** come from the `x-isa-acs-entity-enum` enumeration. |
| **permitted_nationalities** (optional) | `list` of type `string` |The **permitted_nationalities** (CTRY) property identifies the limitation on the distribution of the resource based on nationality. <br/> <br/>Allowable values are listed in Geopolitical Entities, Names, and Codes (GENC) Standard Edition (https://api.nsgreg.nga.mil/geo-political/ISO3166-1/3/VI-12) **MUST** be used.|
| **permitted_organization** (optional) | `list` of type `string` | The **permitted_organizations** (ORG) property identifies the limitation on the distribution of the resource based on organization. <br/> <br/>Allowable values listed in Appendix A: List of Organizations of [ref] **MUST** be used. <br/> <br/>The set of possible values can be thought of as an open vocabulary, but it is not explicitly defined in this specification.|

## Enumerations

### x-isa-privilege-action-ov

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
| DSPLY |	The action of displaying, either in a hard copy document or a visual presentation of the resource. DSPLY should be used to permit display when there is generally a global deny for all actions. |
| IDSRC | . The action of identifying the source of the resource further than the entity receiving the resource. When set to deny, attributes or elements in the resource that identify the source and custodian must be removed or replaced prior to additional actions being taken. This restriction applies not only to the elements in the header of the resource but may also apply to elements within the body of the document being shared. The use of IDSRC does not authorize any changes to markings on the resource. For example, the removal of the source information will not change the classification of the resource. |
| TENOT |	The action of notifying a targeted entity of a cybersecurity incident based on the resource. |
| NETDEF |	The action of taking network defense actions including detection and mitigation, remediation, and local analysis and signature development, based on the resource.|
| LEGAL|	The action of using the resource in legal proceedings.|
|INTEL|	The action of conducting additional intelligence analysis based on the resource.|
|TEARLINE|	The action of removing and taking further action on components of a resource based on their component markings. To be tear-lineable indicates that marked components of a document may be removed and treated as individually marked components. When set to deny, even though there may be components with fewer restrictions than the overall document, they may not be removed.|
|OPACTION	|The action of conducting cyber-based operations applied to adversary capabilities based on the resource.|
|REQUEST|	The action of requesting a waiver to an access privilege restriction. When set to deny, the originator will not consider specific requests to take actions based on the resource.|
|ANONYMOUSACCESS|	The action of allowing anonymous access to the resource. This action is included to support the restrictions placed on the indicators shared with the US government from the DHS Automated Indicator Sharing (AIS) program.|
|CISAUSES|	The cybersecurity purposes allowed in the Cybersecurity Information Sharing Act of 2015 [ref]|

### x-isa-acs-rule-effect-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|permit|	The specified action, privilege, etc is permitted|
|deny	|The specified action, privilege, etc is denied|

### x-isa-acs-classification-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|U|	Unclassified|
|C|	Confidential|
|S|	Secret|
|TS|	Top Secret|

### x-isa-acs-fd-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|  AIS| The resource is appropriate for AIS. |
| FOUO | The resource is appropriate For Official Use Only. |
| NF | Indicates that the resource is releasable to U.S. citizens and not releasable to foreign nationals without the permission of the originator.|
| PII-NECESSARY-TO-UNDERSTAND-THREAT | Personally identifiable information (PII) necessary to understand the context of the resource is present. |
| PII-NOT-PRESENT |Personally identifiable  (PII) is _not_ present.|
|PUBREL |Approved for Public Release |

### x-isa-acs-cvt-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|FISA |	The FISA caveat marking denotes the presence of Foreign Intelligence Surveillance Act (FISA) (Reference 18) or FISA-derived information in the document. This is an informational marking only to highlight such information. Recipients of resources with the FISA control marking are responsible for ensuring that the resource is protected in conformance with the legal requirements of the FISA for limitations on use and warning displays. |
| POSSIBLEPII	| The POSSIBLEPII caveat marking indicates to the recipient that the resource may contain Personally Identifiable Information (PII). Recipients are responsible for ensuring that the resource is protected according to their agencies policies related to PII.|
|CISAPROPRIETARY	|The CISAPROPRIETARY caveat marking indicates that the resource must observe appropriate restrictions as requested by the originator in accordance with the Cybersecurity Information Sharing Act of 2015 [ref] |

### x-isa-acs-sens-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|NTOC_DHS_ECYBER_SVC_SHARE.NSA.NSA 	|Enhanced Cybersecurity Services|
|PCII |	Protected Critical Infrastructure Information|
|LES	|Law Enforcement Sensitive Information|
|INT |	Intelligence Information|
|PII|	Personally Identifiable Information|
|PR	|Cybersecurity Targeted Entity Information|
|TEI|	Commercial Proprietary Information|

### x-isa-acs-shar-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
| NCC	| National Cyber Centers|
|EM|	Emergency Management|
|LE|	Law Enforcement|
|IC|	Intelligence Community|

### x-isa-acs-entity-enum

| Vocabulary Value      | Description  |                                                                                    
| -------------------   | -----------        |
|MII|	Military service member|
|GOV|	U.S. federal government civilian employee|
|CTR|	Contractor|
|SVR|	Server|
|SVC|	Service, Widget, Application, Software, etc|
|DEV	|End-point device|
|NET|	Network device|


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
          "sep_version": "1",
          "identifier": "isa:guide.19001.ACS3-bc9034f8-c732-5328-b9df-d9d72aae480b",
	   "name": "banner_marking",
          "create_date_time": "2016-06-27T14:10:26.723Z",
          "responsible_entity_custodian": "USA.NSA",
          "responsible_entity_originator": "USA.NSA",
          "authority_reference": "urn:isa:authority:CFR2013_32_2_236", 
          "policy_reference": "urn:isa:policy:acs:ns:v3.0?privdefault=deny&amp;sharedefault=deny",
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
          "access_privilege": [
		{
		    "privilege_action": "CISAUSES",
		    "rule_effect": "permit"
		},
		{
		    "privilege_action": "ANONYMOUSACCESS",
		    "rule_effect": "deny"
		}
          ],
          "public_release": {
               "releasable_to_public ": "false"
          },
          "control_set": {
                "classification": "TS",
		  "sci_controls": ["SI"],
		  "logical_authority_category": ["LAC12345"],
		  "formal_determination": ["AIS"],
		  "sensitivity": ["NTOC_DHS_ECYBER_SVC_SHARE.NSA.NSA"],
                "permitted_nationalities": ["USA", "AUS", "CAN", "GBR", "NZL"],
                "permitted_organizations": ["USA.NSA", "USA.DHS"]
          }
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
          "sep_version": "1",
          "identifier": "isa:guide.19001.ACS3-bc9034f8-c732-5328-b9df-d9d72aae4ccc",
          "name": "some_unclassified_marking", 
          "create_date_time": "2016-06-27T14:10:26.723Z",
          "responsible_entity_custodian": "USA.NSA",
          "responsible_entity_originator": "USA.NSA",  
          "authority_reference": "urn:isa:authority:CFR2013_32_2_236",
          "policy_reference": "urn:isa:policy:acs:ns:v3.0?privdefault=denyt&amp;sharedefault=deny", 
          "access_privilege": [
               {
		    "privilege_action": "CISAUSES",
		    "rule_effect": "permit"
               },
               {
		    "privilege_action": "ANONYMOUSACCESS",
		    "rule_effect": "permit"
		}
          ],
          "control_set": {
                "classification": "U",
   		  "formal_determination": ["FOUO", "AIS"],
      		  "permitted_organizations": ["USA.NSA", "USA.DHS"]
           },
    }
}

```


