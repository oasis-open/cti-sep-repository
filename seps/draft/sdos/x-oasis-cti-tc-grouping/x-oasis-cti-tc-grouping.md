# SEP Name
Grouping

## SEP Identifier
`x-oasis-cti-tc-grouping`

## SEP Description
A Grouping is a set of references to STIX context that the object
creator wishes to treat as a distinct entity with shared context. For
example, Grouping should be used to characterize a security event or
incident. Grouping can also be used to share references to STIX
content related to an ongoing analysis process, such as in the case of
a threat analyst wishing to collaborate with other in their trust
community to examine a series of Campaigns and Indicators. The
Grouping SDO contains a list of references to SDOs and SROs along with
an explicit statement of the context shared by the content, a textual
description and the name of the grouping.


## SEP Use Cases
* Sharing related content which isn't appropriate for publication in a
  STIX Report.

## SEP Slack Channel
#grouping-dev

## SEP Sponsors
Org | Primary Contact
--- | ---------------
CIRCL | Alexandre Dulaunoy
New Context | Trey Darley

## POC Implementations
Org | GitHub Repository
--- | -----------------
CIRCL | https://github.com/...
New Context | https://github.com/...

## SEP Definition

### Properties
* The Grouping SDO includes the STIX SDO Common Properties (`type`,
  `id`, etc) but these are excluded from the table below for brevity.

| Property Name              | Type                        | Description                                                                                                                                                                                                                                     |
| -------------              | ----                        | -----------                                                                                                                                                                                                                                     |
| **name** (required)        | `string`                    | A name used to identify the Grouping.                                                                                                                                                                                                           |
| **description** (optional) | `string`                    | A description that provides more details and context about the Grouping, potentially including its purpose and its key characteristics.                                                                                                         |
| **context** (required)     | `open-vocab`                | A description that provides more details and context about the Grouping, potentially including its purpose and its key characteristics. <br /> This is an open vocabulary and values **SHOULD** come from the `grouping-context-ov` vocabulary. |
| **object_refs** (optional) | `list` of type `identifier` | Specifies the STIX Objects that are referred to by this Grouping.                                                                                                                                                                               |

### Relationships
There are no Grouping-specific SROs defined. The usual embedded
references defined in SDO Common Properties (`created_by_ref`, etc)
apply to Grouping. The Grouping object's `object_refs` property allows embedding references to the STIX Objects related to a Grouping instance.

### Vocabularies

#### Grouping Context
**Vocabulary Name:** `grouping-context-ov`

While the majority of this vocabulary is undefined (producers may use
custom vocabulary entries), it has been added specifically to capture
the suspicious-activity-event value. That value indicates that the
information contained in the Grouping relates to a suspicious event.

| Vocabulary Value      | Description                                                                                                                             |
| -------------------   | -----------                                                                                                                             |
| `suspicious-activity` | A set of STIX content related to a particular suspicious activity event.                                                                |
| `malware-analysis`    | A set of STIX content related to a particular malware instance or family.                                                               |
| `unspecified`         | A set of STIX content contextually related but without any precise characterization of the contextual relationship between the objects. |
|                       |                                                                                                                                         |

#### Grouping Label
**Vocabulary Name:** `grouping-label-ov`

While the majority of this vocabulary is undefined (producers may use
custom vocabulary entries), it has been added specifically to capture
the pending-verification value. That value indicates that the
information contained in the Grouping is still pending verification
and consumers should treat it as such.

| Vocabulary Value       | Description                                                                                                                                                                             |
| -------------------    | -----------                                                                                                                                                                             |
| `pending-verification` | The Report contains an initial analysis. Information should be considered preliminary and is subject to change as additional data collection, investigation, and analysis is performed. |

### Examples

#### A standalone Grouping - the consumer may or may not already have access to the referenced STIX Objects.

```json
{
    "type": "x-oasis-cti-tc-grouping",
    "id": "x-oasis-cti-tc-grouping--84e4d88f-44ea-4bcd-bbf3-b2c1c320bcb3",
    "created_by_ref": "identity--a463ffb3-1bd9-4d94-b02d-74e4f1658283",
    "created": "2015-12-21T19:59:11.000Z",
    "modified": "2015-12-21T19:59:11.000Z",
    "name": "The Black Vine Cyberespionage Group",
    "description": "A simple collection with an indicator and campaign",
    "context": "Black Vine Cyberespionage Group attributed intel",
    "labels": ["campaign", "pending-verification"],
    "object_refs": [
        "indicator--26ffb872-1dd9-446e-b6f5-d58527e5b5d2",
        "campaign--83422c77-904c-4dc1-aff5-5c38f3a2c55c",
        "relationship--f82356ae-fe6c-437c-9c24-6b64314ae68a"
    ]
}
```
