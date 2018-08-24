# cti-sep-repository

* **NOTE:** This is an [OASIS TC Open Repository](https://www.oasis-open.org/resources/open-repositories/). See the [Governance](#governance) section for more information.

## Purpose
The CTI SEP Repository is intended to host STIX Enhancement Proposals (SEPs) as well as the central registry for SEPs contributed to the CTI TC via this repository.

SEPs are intended to establish a mechanism for folks to submit their ideas in a common structure, recruit others to help, and iterate on bleeding-edge stuff in an interoperable manner without degrading the ecosystem of production tools that only expect CS/CSD level inputs. It's not just enough having a great idea. For that idea to translate into reality, you have to educate potential supporters, recruit co-sponsors to help with the work, and gradually build consensus. STIX Enhancement Proposals are intended to make that easier, with the ultimate goal being a streamlined means of getting new capabilities added to the official STIX standard.

## Definitions
* **SEP Repository:** A collection of STIX Enhancement Proposals, each of which consisting minimally of Markdown (using the canonical SEP template) describing the use cases and semantics of the SEP, as well as a valid JSON Schema describing the data structure of the SEP.
* **SEP Registry:** A table enumerating SEPs by name, type, status, and version.
* **SDO:** A STIX Domain Object, used to characterize CTI as nodes in the STIX graph model.
* **SRO:** A STIX Relationship Object, used to provide context by connecting SDOs as edges in the STIX graph model
* **SCO:** A STIX Cyber Observable, used to characterize observations within a STIX Observed Data SDO.
* **STIX Object Extension:** A STIX Object Extension defines a coherent set of named properties which add additional capabilities to SDOs or SCOs. These may be logically constrained to certain SDO or SCO types where semantically it would be nonsensical outside a limited context. For example, using the SCO HTTP Request Extension makes sense in the context of a Network Traffic SCO, but would not in the case of a File SCO.

## Scope
Currently, the CTI TC have agreed to limit the scope of SEPs to contributions which are intended to be incorporated into a future revision of the STIX specification. This is limited to:
  * New SDOs
  * New SROs
  * New SCOs
  * New STIX Object Extensions
  
The following types of SEPs are presently out of scope:
  * Redefining the semantics of properties of existing SDOs, SROs, and/or SCOs already defined in CTI TC Committee Specification Drafts and/or Committee Specifications.
  * Adding to or redefining the semantics of STIX Patterning (including, but not limited to adding new elements, expressions, operators, or language elements). 

## Background
Things can move pretty slowly in a consensus-based standards body and good ideas can get bogged-down in committee. Part of the resistance to new ideas in STIX2 is that the technical committee's risk appetite has shifted towards demanding a higher level of vetting before changes get pulled into the formal work process. Meanwhile there are folks trying to tackle real-world problems who can't wait on changes to the formal specifications to be finalized. STIX2 has support for custom objects and properties, but while these are sufficient to address the needs of vendor-specific implementations they are only interoperable given out-of-band discussions between vendors.

SEPs, on the other hand, provide a mechanism for individuals and organizations to collaboratively develop enhancements to STIX and to use these in an interoperable manner, regardless of whether or not the CTI TC decides to incorporate them into the official standard.

# The SEP Registry
If you receive an SDO or SCO with its `type` property prefixed with `x-oasis-cti-tc-*`, an SRO with its `relationship_type` property prefixed with `x-oasis-cti-tc-*`, or a STIX Object Extension with its name prefixed with `x-oasis-cti-tc-*`, then look in [`manifest.md`](manifest.md). This will allow you to determine where to find details (Markdown and JSON Schema) in the SEP Repository, as well as the status and current version of the SEP. 
  * Note that SEP versions in the Registry are based on the corresponding git commit SHA1 hash.

# SEP statuses
* `draft`: for SEPs which are in active development and/or production use
* `deprecated`: for SEPs which have been EOL'ed or withdrawn
* `integrated`: for SEPs which have been EOL'ed due to having been published in a CSD

## Howto
* [Process for defining new STIX SDOs as SEPs](#seps-for-new-sdos)
* [Process for defining new STIX Cyber Observables (SCOs) as SEPs](#seps-for-new-scos)
* [Process for defining new STIX Extensions as SEPs](#seps-for-new-stix-extensions-sdo-or-sco)

### A note for non-CTI TC members
The majority of the CTI TC's work is conducted via a Slack instance and mailing lists which are only available to CTI TC members. In lieu of this, you can email the [SEP Open Repository maintainers](#current-maintainers-of-this-tc-open-repository) or by emailing the [cti-users mailing list](http://lists.oasis-open.org/archives/cti-users/). (Subscribe by sending an blank email to [cti-users-subscribe@lists.oasis-open.org](mailto:cti-users-subscribe@lists.oasis-open.org).)

### SEPs for new SDOs
1. Fork this repository.
2. Give your SEP a name and create a corresponding directory within [`seps/draft/sdos/`](seps/draft/sdos/).
3. Copy [`templates/sdo_sep_template/template.md`](templates/sdo_sep_template/template.md) and [`templates/sdo_sep_template/template.json`](templates/sdo_sep_template/template.json) into the directory you just created (s/template/your SEP name).
4. Start by filling out as much as you can of \<your SEP name\>.md.
5. Define your SEP's data model in JSON Schema in \<your SEP name\>.json.
6. Do a pull request against this git repo.
7. ...profit!

#### An example
If you look under [`seps/draft/sdos/x-oasis-cti-tc-grouping/`](seps/draft/sdos/x-oasis-cti-tc-grouping/) you'll see the Grouping proposal (taken from the [STIX 2.1-Working Concepts Google Doc](https://docs.google.com/document/d/15qD9KBQcVcY4FlG9n_VGhqacaeiLlNcQ7zVEjc8I3b4/edit#heading=h.t56pn7elv6u7) defined as a SEP. There's Markdown (for the humans) and JSON Schema (for the machines.)

### SEPs for new SCOs
1. Fork this repository.
2. Give your SEP a name and create a corresponding directory within [`seps/draft/scos/`](seps/draft/scos/).
3. Copy [`templates/sco_sep_template/template.md`](templates/sco_sep_template/template.md) and [`templates/sco_sep_template/template.json`](templates/sco_sep_template/template.json) into the directory you just created (s/template/your SEP name).
4. Start by filling out as much as you can of \<your SEP name\>.md.
5. Define your SEP's data model in JSON Schema in \<your SEP name\>.json.
6. Do a pull request against this git repo.
7. ...profit!

#### An example
If you look under [`seps/draft/scos/x-oasis-cti-tc-webpage/`](seps/draft/scos/x-oasis-cti-tc-webpage/) you'll see the Webpage proposal (based on [Terry MacDonald's proposal to the TC mailing list](https://lists.oasis-open.org/archives/cti-stix/201712/msg00003.html)) defined as a SEP. There's Markdown (for the humans) and JSON Schema (for the machines.)

### SEPs for new STIX Extensions (SDO or SCO)
1. Fork this repository.
2. Give your SEP a name and create a corresponding directory within [`seps/draft/extensions/`](seps/draft/extensions/).
3. Copy [`templates/extension_sep_template/template.md`](templates/extension_sep_template/template.md) and [`templates/extension_sep_template/template.json`](templates/extension_sep_template/template.json) into the directory you just created (s/template/your SEP name).
4. Start by filling out as much as you can of \<your SEP name\>.md.
5. Define your SEP's data model in JSON Schema in \<your SEP name\>.json.
6. Do a pull request against this git repo.
7. ...profit!

#### Examples
* If you look under [`seps/draft/extensions/x-oasis-cti-tc-http-response-ext/`](seps/draft/extensions/x-oasis-cti-tc-http-response-ext/) you'll see the HTTP Response (SCO) Extension (based on [Terry MacDonald's proposal to the TC mailing list](https://lists.oasis-open.org/archives/cti-stix/201712/msg00003.html)) defined as a SEP. There's Markdown (for the humans) and there will be JSON Schema (for the machines) just as soon as I get a few minutes.

* If you look under [`seps/draft/extensions/x-oasis-cti-tc-assertion-ext/`](seps/draft/extensions/x-oasis-cti-tc-assertion-ext/) you'll see the STIX Assertion Proposal reimagined as an SDO Extension (based on [Jason Kierstead's proposal in STIX 2.1-Working Concepts](https://docs.google.com/document/d/15qD9KBQcVcY4FlG9n_VGhqacaeiLlNcQ7zVEjc8I3b4/edit#heading=h.qxvz3vox3ksj)) and defined as a SEP. There's Markdown (for the humans) and there will be JSON Schema (for the machines) just as soon as I get a few minutes.

## Governance
This GitHub public repository (**[https://github.com/oasis-open/cti-sep-repository](https://github.com/oasis-open/cti-sep-repository)**) was created at the request of the [OASIS Cyber Threat Intelligence (CTI) TC](https://www.oasis-open.org/committees/cti/) as an [OASIS TC Open Repository](https://www.oasis-open.org/resources/open-repositories/) to support development of open source resources related to Technical Committee work.

While this TC Open Repository remains associated with the sponsor TC, its development priorities, leadership, intellectual property terms, participation rules, and other matters of governance are [separate and distinct](https://github.com/oasis-open/cti-sep-repository/blob/master/CONTRIBUTING.md#governance-distinct-from-oasis-tc-process) from the OASIS TC Process and related policies.

All contributions made to this TC Open Repository are subject to open source license terms expressed in the [BSD-3-Clause License](https://github.com/oasis-open/cti-sep-repository/blob/master/LICENSE.md). That license was selected as the declared ["Applicable License"](https://www.oasis-open.org/resources/open-repositories/licenses) when the TC Open Repository was created.

As documented in ["Public Participation Invited"](https://github.com/oasis-open/cti-sep-repository/blob/master/CONTRIBUTING.md#public-participation-invited), contributions to this OASIS TC Open Repository are invited from all parties, whether affiliated with OASIS or not. Participants must have a GitHub account, but no fees or OASIS membership obligations are required. Participation is expected to be consistent with the [OASIS TC Open Repository Guidelines and Procedures](https://www.oasis-open.org/policies-guidelines/open-repositories), the open source [LICENSE](https://github.com/oasis-open/cti-sep-repository/blob/master/LICENSE) designated for this particular repository, and the requirement for an [Individual Contributor License Agreement](https://www.oasis-open.org/resources/open-repositories/cla/individual-cla) that governs intellectual property.

## Statement of Purpose
Statement of Purpose for this OASIS TC Open Repository (cti-sep-repository) as [proposed](https://www.oasis-open.org/apps/org/workgroup/cti/email/archives/201807/msg00051.html) and [approved](https://www.oasis-open.org/apps/org/workgroup/cti/email/archives/201807/msg00055.html) by the TC:

The cti-sep-repository is set up to host the Registry and the Repository for STIX Enhancement Proposals (SEPs).

## Additions to Statement of Purpose
Repository Maintainers may include here any clarifications &mdash; any additional sections, subsections, and paragraphs that the Maintainer(s) wish to add as descriptive text, reflecting (sub-) project status, milestones, releases, modifications to statement of purpose, etc.  The project Maintainers will create and maintain this content on behalf of the participants.

## Maintainers
TC Open Repository [Maintainers](https://www.oasis-open.org/resources/open-repositories/maintainers-guide) are responsible for oversight of this project's community development activities, including evaluation of GitHub [pull requests](https://github.com/oasis-open/cti-sep-repository/blob/master/CONTRIBUTING.md#fork-and-pull-collaboration-model) and [preserving](https://www.oasis-open.org/policies-guidelines/open-repositories#repositoryManagement) open source principles of openness and fairness. Maintainers are recognized and trusted experts who serve to implement community goals and consensus design preferences.

Initially, the associated TC members have designated one or more persons to serve as Maintainer(s); subsequently, participating community members may select additional or substitute Maintainers, per [consensus agreements](https://www.oasis-open.org/resources/open-repositories/maintainers-guide#additionalMaintainers).

### Current Maintainers of this TC Open Repository
| name          | email                                             | GitHub user                          | member company                             |
|---------------|---------------------------------------------------|--------------------------------------|--------------------------------------------|
| Trey Darley   | [trey@newcontext.com](mailto:trey@newcontext.com) | [treyka](https://github.com/treyka/) | [New Context](https://www.newcontext.com/) |
| Ivan Kirillov | [ikirillov@mitre.org](mailto:ikirillov@mitre.org) | [ikiril01](https://github.com/ikiril01/)                             | [MITRE](https://www.mitre.org/)                                      |

## About OASIS TC Open Repositories
* [TC Open Repositories: Overview and Resources](https://www.oasis-open.org/resources/open-repositories/)
* [Frequently Asked Questions](https://www.oasis-open.org/resources/open-repositories/faq)
* [Open Source Licenses](https://www.oasis-open.org/resources/open-repositories/licenses)
* [Contributor License Agreements (CLAs)](https://www.oasis-open.org/resources/open-repositories/cla)
* [Maintainers' Guidelines and Agreement](https://www.oasis-open.org/resources/open-repositories/maintainers-guide)

## Feedback
Questions or comments about this TC Open Repository's activities should be composed as GitHub issues or comments. If use of an issue/comment is not possible or appropriate, questions may be directed by email to the Maintainer(s) [listed above](#current-maintainers-of-this-tc-open-repository). Please send general questions about TC Open Repository participation to OASIS Staff at [repository-admin@oasis-open.org](mailto:repository-admin@oasis-open.org) and any specific CLA-related questions to [repository-cla@oasis-open.org](mailto:repository-cla@oasis-open.org).

## TODO
- [ ] Add workflow diagram
- [ ] Add template and example for SRO SEPs.
- [ ] Discuss how to address SEPs from TC members who want to have their SEPs added to the SEP Registry without submitting their IPR to the CTI TC.
- [ ] Discuss how to address SEPs from TC members who are only willing to submit their SEP to the CTI TC provided it is incorporated into the official specification without modification.
- [ ] Discuss how to address SEPs from non-TC members who want to have their SEPs added to the SEP Registry without submitting their IPR to the CTI TC.
- [ ] Discuss how to address SEPs from non-TC members who want to submit their IPR to the CTI TC.
