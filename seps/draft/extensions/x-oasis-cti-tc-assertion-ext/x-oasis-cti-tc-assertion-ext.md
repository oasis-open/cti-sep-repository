# SEP Name
Assertion Extensions

## SEP Identifier
`x-oasis-cti-tc-assertion-ext`

## SEP Description
The Assertion Extension is intented to convey an assertion about the
SDO it is included in, which currently is either an Observed Data or
an Indicator SDO. It allows a content creator to communicate
information such as threat level, categorization, etc. for a piece of
data without any pre-defined value judgements as to its maliciousness
within a specific client environment.

An assertion about a particular SDO can only be made by the SDO
Producer. (Any third-party assessments of the correctness of
information in an object - including assertions (or lack thereof) -
may be communicated using the Opinion SDO.)

## SEP Use Cases
* Communicating the threat level of a URL.

## SEP Extension Context
* Extends the Indicator and Observed Data SDOs.

## SEP Slack Channel
#assertion-extension-dev

## SEP Sponsors
Org | Primary Contact
--- | ---------------
IBM | Jason Kierstead
New Context | Trey Darley

## POC Implementations
Org | GitHub Repository
--- | -----------------
IBM | https://github.com/...
New Context | https://github.com/...

## SEP Definition

### Properties
| Property Name               | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------               | ----        | -----------                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **valid_from** (optional)   | `timestamp` | The first time at which this Assertion was considered valid. If the `valid_until` property is provided, then the value **MUST** be greater than or equal to the value in `valid_until`.<br /><br />If the `valid_from` property is omitted, then there is no constraint on the first time for which the Assertion should be considered valid.                                                                                           |
| **valid_from** (optional)   | `timestamp` | The time at which this Assertion should no longer be considered valid. If the `valid_from` property is provided, then the value **MUST** be less than or equal to the value in `valid_from`.<br /><br />If the `valid_until` property is omitted, then there is no constraint on the latest time for which the Assertion should be considered valid.                                                                                    |
| **source** (optional)       | `string`    | The source of this assertion.                                                                                                                                                                                                                                                                                                                                                                                                           |
| **threat_level** (optional) | `integer`   | The `threat_level` property identifies the threat level that the creator is asserting with respect to this data. It should be noted that this value **SHOULD NOT** assume anything about the recipient of the assertion; that is, the value should be receiver-agnostic and not take into account any specifics with regard to environment, industry, etc.<br /><br />If present, the value **MUST** be a number in the range of 0-100. |
| **description** (optional)  | `string`    | A description that provides the recipient with a human-readable description of this threat level.                                                                                                                                                                                                                                                                                                                                       |
| **categories** (reserved)   | `n/a`       | This property is reserved.                                                                                                                                                                                                                                                                                                                                                                                                              |

### Examples
```json
{
    "type": "indicator",
    "id": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "created_by_ref": "identity--f431f809-377b-45e0-aa1c-6a4751cae5ff",
    "created": "2016-04-06T20:03:48.000Z",
    "modified": "2016-04-06T20:03:48.000Z",
    "labels": ["phishing"],
    "name": "54.72.9.51",
    "pattern": "[network-traffic:dst_ref.type = 'ipv4-addr' AND network-traffic:dst_ref.value = '54.72.9.51/32']",
    "valid_from": "2016-01-01T00:00:00Z",
    "extensions": {
        "x-oasis-cti-tc-assertion-ext": [
			    {
                    "categories": ["anonymization"],
                    "threat_level": 80,
                    "source": "ACME Corp"
                },
                {
                    "categories": ["botnet_cnc"],
                    "threat_level": 20,
                    "source": "Foobar Inc."
                }
		]
	}
}
```
