# SEP Name
Hypothesis Object

## SEP Identifier
x-oasis-cti-tc-hypothesis

## SEP Version
1

## SEP Description
A Hypothesis Object would be a way to structure the process of hypothesis-testing. Currently, ACH (Analysis of Competing Hypotheses)
is conducted by analysts, producers, and consumers of intelligence to score and weigh evidence about a given threat. There is no way to structure
these findings as STIX entities; nor is there a way to show which hypothesis scored the strongest out of the set of hyptheses that were tested. 

## SEP Use Cases
* Structuring the proecss of ACH (Analysis of Competing Hypotheses)
* Have an entity that could represent analyst tradecraft
* Increase collaboration between providers/consumers of CTI who have varying hypotheses around a threat/relationship
* Have a machine readable way to identify patterns in hypotheses over time

## SEP Extension Context
* TBD

## SEP Sponsors
Org | Primary Contact
--- | ---------------
EclecticIQ | Caitlin Huey
EclecticIQ | Sergey Polzunov
EclecticIQ | Jörg Abraham

## POC Implementations
Org | GitHub Repository
--- | -----------------
TBD

## SEP Definition
A Hypothesis object would be a way to structure the process of hypothesis-testing. 

## Properties
| Property Name              | Type      | Description                            |
| -------------              | ----      | -----------                            |
| **type** (required) | `string` | [The value of this property MUST be hypothesis]|
| **explanation** (optional) | `string` | [An explanation of why the producer came to this Hypothesis. For example, if a Hypothesis was tested against several other Hypotheses, an explanation can contain why the Hypothesis producer supports this Hypothesis over the other hypotheses tested.]
| **author** (optional) | `list of type string` | [The name of the author(s) of this Hypothesis]|
| **relevancy** (required) | `enum` | [Relevance of the evidence to the question being analyzed, not to each individual hypothesis]|
| **credibility** (required) | `enum` | [Credibility of the evidence provided]
| **hypothesis_description** (optional) | `string` | [A description of the hypothesis that is being tested]|
| **evidence** (required) | `string` | [Evidence that is being used to test a Hypothesis]|
| **eviednce_type** (optional) | `string` | [Type of evidence (e.g. Media, Seconodary Source)]|
| **object_refs** (required) | `list of type identifier ` | [The STIX Objects (SDOs and SROs) that the Hypothesis is being applied to]|

