# SEP Name
HTTP Response Extension

## SEP Identifier
`x-oasis-cti-tc-http-response-ext`

## SEP Description
Allows for characterizing HTTP responses to capture things like HTTP
redirects and to link HTTP requests with the webpage content that gets
returned.

## SEP Use Cases
* Characterizing HTTP responses in Network Traffic.

## SEP Extension Context
* Extends the Network Traffic SCO. Mainly intended to be used in
  conjunction with the [`x-oasis-cti-tc-webpage`](../../scos/x-oasis-cti-tc-webpage) SCO.

## SEP Slack Channel
#http-response-extension-dev

## SEP Sponsors
Org | Primary Contact
--- | ---------------
Cosive | Terry MacDonald
New Context | Trey Darley

## POC Implementations
Org | GitHub Repository
--- | -----------------
Cosive | https://github.com/...
New Context | https://github.com/...

## SEP Definition

## Properties
| Property Name                        | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------                        | ----         | -----------                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **response_url_ref** (optional)      | `object-ref` | Specifies the URL object that specifies the network location that the HTTP Response was received from.<br /><br />The object referenced in this property **MUST** be of type `url`.                                                                                                                                                                                                                                                             |
| **response_status** (optional)       | `integer`    | Specifies the HTTP status code for the HTTP response, as an integer.                                                                                                                                                                                                                                                                                                                                                                            |
| **response_version** (optional)      | `string`     | Specifies the HTTP version portion of the HTTP response line, as a lowercase string.                                                                                                                                                                                                                                                                                                                                                            |
| **response_content_type** (required) | `string`     | Specifies the HTTP content_type header portion of the HTTP response line, as a lowercase string.                                                                                                                                                                                                                                                                                                                                                |
| **response_header** (optional)       | `dictionary` | Specifies all of the HTTP header fields that may be found in the HTTP server response, as a dictionary. All HTTP header fields must be specified in the order they are shown in the HTTP response if the `response_header` property is used.<br /><br />Each key in the dictionary **MUST** be the name of the header field and SHOULD preserve case, e.g., `User-Agent`. The corresponding value for each dictionary key **MUST** be a string. |
| **response_request_ref** (optional)  | `object-ref` | Specifies the HTTP Request object that resulted in this HTTP Response being generated.<br /><br />The object referenced in this property **MUST** be of type `network-traffic` with a `http-request-ext` extension.                                                                                                                                                                                                                             |
| **message_body_length** (optional)   | `integer`    | Specifies the length of the HTTP message body, if included, in bytes.                                                                                                                                                                                                                                                                                                                                                                           |
| **message_body_data_ref** (required) | `object-ref` | Specifies the data contained in the HTTP message body.<br /><br />The object referenced in this property **MUST** be of type `artifact` or of type `x-oasis-cti-tc-webpage`.                                                                                                                                                                                                                                                                                   |
| **redirects_to_ref** (optional)      | `object-ref` | Specifies the URL object that specifies the network location that this HTTP Response is redirecting us to. This property is used to relate the URL that the HTTP client will be redirected to if it receives a HTTP 3xx Redirection Status code.<br /><br />The object referenced in this property **MUST** be of type `url`.                                                                                                                   |
## Examples

### HTTP Request using Webpage object and URL object
```json
{
    "0": {
        "type": "ipv4-addr",
        "value": "198.51.100.53"
    },
    "1": {
        "type": "network-traffic",
        "src_ref": "0",
        "protocols": [
            "tcp",
            "http"
        ],
        "extensions": {
            "x-oasis-cti-tc-http-response-ext": {
                "response_url_ref": "3",
                "response_status": 200,
                "response_version": "http/1.1",
                "response_content_type": "text/html",
                "response_header": {
                    "Date": "Mon, 27 Jul 2017 12:28:53 GMT",
                    "Server": "Apache/2.2.14 (Win32)",
                    "Last-Modified": "Wed, 22 Jul 2009 19:15:56 GMT",
                    "Content-Length": "88",
                    "Content-Type": "text/html",
                    "Connection": "Closed"
                },
                "message_body_length": 88,
                "message_body_data_ref": "2"
            }
        }
    },
    "2": {
        "type": "x-oasis-cti-tc-webpage",
        "url_ref": "3",
        "body": [
            "&lt;div class=\"highlight\"&gt;I hack3d the Internetz and no 1 will get me eva.&lt;/div&gt;",
            "&lt;div class=\"highlight\"&gt;I've managed to get into the CIA man!&lt;/div&gt;"
        ]
    },
    "3": {
        "type":"url",
        "value":"http://www.happydaze1988.com"
    }
}
```

### HTTP Request, and HTTP Response using Webpage object and URL object
```json
{
    "0": {
        "type": "domain-name",
        "value": "wayneindustries.com"
    },
    "1": {
        "type": "network-traffic",
        "dst_ref": "0",
        "protocols": [
            "tcp",
            "http"
        ],
        "extensions": {
            "http-request-ext": {
                "request_method": "get",
                "request_value": "/research/index.html",
                "request_version": "http/1.1",
                "request_header": {
                    "Accept-Encoding": "gzip,deflate",
                    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113",
                    "Host": "wayneindustries.com"
                },
                "message_webpage_ref": "2"
            }
        }
    },
    "2": {
        "type": "network-traffic",
        "src_ref": "0",
        "protocols": [
            "tcp",
            "http"
        ],
        "extensions": {
            "x-oasis-cti-tc-http-response-ext": {
                "response_url_ref": "4",
                "response_status": 200,
                "response_version": "http/1.1",
                "response_content_type": "text/html",
                "response_header": {
                    "Date": "Mon, 27 Dec 2017 12:28:53 GMT",
                    "Server": "Apache/2.2.14 (Win32)",
                    "Last-Modified": "Wed, 12 Jan 2017 19:15:56 GMT",
                    "Content-Length": "3558",
                    "Content-Type": "text/html",
                    "Connection": "Closed"
                },
                "response_request_ref": "2",
                "message_body_length": 88,
                "message_body_data_ref": "3"
                }
        }
    },
    "3": {
        "type": "x-oasis-cti-tc-webpage",
        "url_ref": "4",
        "body": [
            "&lt;div class=\"highlight\"&gt;I hack3d the Internetz and no 1 will get me eva.&lt;/div&gt;",
            "&lt;div class=\"highlight\"&gt;I've managed to get into the CIA man!&lt;/div&gt;"
        ]
    },
    "4": {
        "type": "url",
        "value": "http://wayneindustries.com/research/index.html"
    }
}
```

### HTTP Request redirecting to new URL (HTTP 302 Redirection)
```json
{
    "0": {
        "type": "ipv4-addr",
        "value": "198.51.100.53"
    },
    "1": {
        "type": "network-traffic",
        "src_ref": "0",
        "protocols": [
            "tcp",
            "http"
        ],
        "extensions": {
            "x-oasis-cti-tc-http-response-ext": {
                "response_url_ref": "3",
                "response_status": 302,
                "response_version": "http/1.1"
            }
        }
    },
    "2": {
        "type":"url",
        "value":"http://www.happydaze1988.com"
    },
    "3": {
        "type":"url",
        "value":"http://www.happydaze1988.nl"
    }
}
```
