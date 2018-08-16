# SEP Name
DNP3

## SEP Identifier
`x-oasis-cti-tc-dnp3`

## SEP Description
Add support for the SCADA protocol [DNP3](https://en.wikipedia.org/wiki/DNP3)

## SEP Use Cases
* Support common ICS/SCADA Protocol
* Allow utilities to describe and detect possible attacks.

## SEP Extension Context

This is an extension to the `network-traffic` SCO object.

### Properties


#### dnp3-ext object

| Property Name                 | Type                             | Description                                                                                                                                                                                                  |
| -------------                 | ----                             | -----------                                                                                                                                                                                                  |
| **func_code** (required)      | `integer`                        | The function code from the Application Layer.                                                                                                                                                                |
| **objects** (optional)        | `list` of type `dnp3object-type` | This defines the included objects in the Application Layer.                                                                                                                                                  |
| **iin** (optional)            | `integer`                        | The value of the IIN field.  They are also broken out in additional properties.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.        |
| **broadcast** (optional)      | `boolean`                        | This specifies the IIN1.0 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **class1** (optional)         | `boolean`                        | This specifies the IIN1.1 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **class2** (optional)         | `boolean`                        | This specifies the IIN1.2 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **class3** (optional)         | `boolean`                        | This specifies the IIN1.3 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **needtime** (optional)       | `boolean`                        | This specifies the IIN1.4 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **localcontrol** (optional)   | `boolean`                        | This specifies the IIN1.5 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **devicetrouble** (optional)  | `boolean`                        | This specifies the IIN1.6 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **devicerestart** (optional)  | `boolean`                        | This specifies the IIN1.7 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **nofunccodesup** (optional)  | `boolean`                        | This specifies the IIN2.0 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **objectunkn** (optional)     | `boolean`                        | This specifies the IIN2.1 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **paramerror** (optional)     | `boolean`                        | This specifies the IIN2.2 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **eventbufovrflw** (optional) | `boolean`                        | This specifies the IIN2.3 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **alrdyexec** (optional)      | `boolean`                        | This specifies the IIN2.4 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **confcorrupt** (optional)    | `boolean`                        | This specifies the IIN2.5 if it is present.  As IIN is only present on a response, the func_code MUST be greater than or equal to 129 when this field is present.                                            |
| **uns** (optional)            | `boolean`                        | The value of the UNS field (unsolicited response or confirmation of unsolicited response) in the Application control octet.  If the value is not provided, it is not determined if this bit is set or clear. |

#### dnp3object-type object

One and only one of the data values MUST be present.

| Property Name         | Type        | Description                                                                         |
| -------------         | ----        | -----------                                                                         |
| group (required)      | `integer`   | The function code from the Application Layer.                                       |
| variant (require)     | `integer`   | The defines the included objects in the Application Layer.                          |
| bitstr_hex (optional) | `hex`       | If the data is BSTR, the value is stored in this property.                          |
| number (optional)     | `integer`   | If the data is one of UINT, INT, FLT, or BCD, the value is stored in this property. |
| string (optional)     | `string`    | If the data is one of VSTR or UNCD, the value is stored in this property.           |
| binary_bin (optional) | `binary`    | If the data is OSTR, the value is stored in this property.                          |
| time (optional)       | `timestamp` | If the data is DNP3TIME, the value is stored in this property.                      |

Note: SET of n and VARIANT are not specified yet.

## SEP Slack Channel
TBD

## SEP Sponsors
Org | Primary Contact
--- | ---------------
New Context | John-Mark Gurney

## POC Implementations
Org | GitHub Repository
--- | -----------------

## SEP Definition
Draft normative text goes here
