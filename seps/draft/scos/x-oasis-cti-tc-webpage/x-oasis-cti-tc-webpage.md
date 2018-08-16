# SEP Name
Webpage SCO

## SEP Identifier
`x-oasis-cti-tc-webpage`

## SEP Description
The Webpage SCO allows the information from an (x)HTML webpage to be
captured. The design is flexible enough to allow only the important or
interesting bits of the webpage to be recorded if desired.

## SEP Use Cases
The Webpage SCO is designed to allow an intel provider to communicate
useful information, such as:

* Recording the javascript from an exploit redirection site
* Recording excerpts from a conversation held within a web forum
* Recording the redirect chain of multiple stages of exploit
  redirection to show how an attack was performed
* Recording a web defacement
* Recording changes to a webpage over time

## SEP Extension Context
* Often used in conjunction with the [`x-oasis-cti-tc-http-response-ext`](../../extensions/x-oasis-cti-tc-http-response-ext/) Extension.

## SEP Slack Channel
#webpage-dev

## SEP Sponsors
Org | Primary Contact
--- | ---------------
Cosive | Terry MacDonald
New Context | Trey Darley

## POC Implementations
Org | GitHub Repository
--- | -----------------
Mitre | https://github.com/...
New Context | https://github.com/...


## SEP Definition
The Webpage SCO represents an instance of a webpage, corresponding to
the [HTML W3C recommendations](https://www.w3.org/TR/#tr_HTML). The
webpage object represents the HTML content (and other content included
in the HTML such as Javascript) sent by the webserver to the web
client over HTTP or HTTPS. It does not include any server-side code
required to generate the HTML.

All HTML **MUST** be escaped so that it can be represented within JSON
(as per RFC7159.) All quotation marks, reverse solidus, and the
control characters (`U+0000` through `U+001F`) **MUST** be escaped by
preceding them with a reverse solidus (`\\`). For example, the HTML
string `&lt;link rel="stylesheet"&gt;` would be placed into the links
list as `"&lt;link rel=\\"stylesheet\\"&gt;"`.

Any characters in the encoded value which cannot be decoded into
Unicode **MUST** be replaced with the 'REPLACEMENT CHARACTER'
(`U+FFFD`). If it is necessary to capture the raw HTML as observed,
this can be achieved by referencing an Artifact SCO via the
`webpage_data_ref` property.

### Properties
* The Webpage SCO includes the STIX SCO Common Properties (`type` &
  `extensions`) but these are excluded from the table below for
  brevity.

| Property Name                         | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------                         | ----                        | -----------                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **url_ref** (optional)                | `object-ref`                | Specifies the location of the webpage using a URL object.<br /><br />The object referenced in this property **MUST** be of type `url`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **head** (optional)                   | `list` of type `string`     | Specifies a `list` of type `string` where each list item contains HTML excerpts from the *head* element of the HTML content (as defined in the latest [W3C HTML Recommendation](https://www.w3.org/TR/#tr_HTML)) of the webpage.<br /><br />Each list item **MUST** be an individual HTML element and **MUST** have come from the head element of the webpage.<br /><br />The list item string **MUST** begin with the HTML element start tag and end with the HTML element end tag, e.g. `<title>My Evil Site</title>`. All HTML **MUST** be escaped so that it can be represented within JSON as per [RFC7159](https://tools.ietf.org/html/rfc7159.html).<br /><br />List values **MUST** appear in the same order as present in the raw HTML of the webpage.                 |
| **body** (optional)                   | `list` of type `string`     | Specifies a `list` of type `string` where each list item contains HTML excerpts from the *body* element of the HTML content (as defined in the latest [W3C HTML Recommendation](https://www.w3.org/TR/#tr_HTML)) of the webpage.<br /><br />Each list item **MUST** be an individual HTML element and **MUST** have come from the body element of the webpage.<br /><br />The list item string **MUST** begin with the HTML element start tag and end with the HTML element end tag, e.g. `<a href="http://badsite.com">Click here</a>`. All HTML **MUST** be escaped so that it can be represented within JSON as per [RFC7159](https://tools.ietf.org/html/rfc7159.html).<br /><br />List values **MUST** appear in the same order as present in the raw HTML of the webpage. |
| **webpage_data_ref** (optional)       | `object-ref`                | Specifies the complete contents of the webpage, including both the headers and body, as a reference to an `artifact` SCO.<br /><br />The object referenced in this property **MUST** be of type `artifact`.<br /><br />**Note:** This property does NOT include the HTTP headers, which may be specified via the HTTP Response extension of a corresponding `network-traffic` SCO.                                                                                                                                                                                                                                                                                                                                                                                              |
| **redirects_to_ref** (optional)       | `object-ref`                | Specifies the next URL that this webpage redirects the client to, as a reference to as `url` SCO.<br /><br />The SCO referenced in this property **MUST** be of type `url`.<br /><br />This property **MAY** contain a URL extracted from anywhere on the webpage, or a URL generated dynamically from scripts included in the webpage running when viewed by the web client.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **loads_content_from_refs** (optional) | `list` of type `object-ref` | Specifies a list of URLs that this webpage instructs the web client to load content from, with each list entry as a reference to a different url object.<br /><br />The objects referenced in this property **MUST** all be of type `url`.<br /><br />This list **MAY** contain URLs extracted from anywhere on the webpage, or URLs generated dynamically from scripts included in the webpage running when viewed by the web client.                                                                                                                                                                                                                                                                                                                                           |

### Examples

#### Hacked Website redirecting to exploit site using Javascript
```json
{
	"0": {
		"type": "url",
		"value": "https://mymainnews.com/news/index.html"
	},
	"1": {
		"type": "x-oasis-cti-tc-webpage",
		"url_ref": "0",
		"body": [
			"&lt;script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.js\" type=\"text/javascript\"&gt;&lt;/script&gt;\"",
			"&lt;script src=\"https://myhackedsite.com/files/uploads/d.js\" type=\"text/javascript\"&gt;&lt;/script&gt;\""
		]
	}
}
```

#### Multiple chained exploit site redirects
```json
{
	"0": {
		"type": "url",
		"value": "https://wayneindustries.com/research/index.html"
	},
	"1": {
		"type": "x-oasis-cti-tc-webpage",
		"url_ref": "0",
		"body": [
			"&lt;iframe src=\"http://exssredaf.intsite.info/content/lfw?327xas\"&gt;"
		],
		"redirects_to_ref": "2"
	},
	"2": {
		"type": "url",
		"value": "http://exssredaf.intsite.info/content/lfw?327xas"
	},
	"3": {
		"type": "x-oasis-cti-tc-webpage",
		"url_ref": "2",
		"body": [
			"&lt;script src=\"http://389553.teaparty2.biz/uploads/j.jpg\"&gt;"
		],
		"loads_content_from_refs": ["4"]
	},
	"4": {
		"type": "url",
		"value": "http://389553.teaparty2.biz/uploads/j.jpg"
	},
	"5": {
		"type": "x-oasis-cti-tc-webpage",
		"url_ref": "2",
		"body": [
			"&lt;script&gt; eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 0=\"2 3!\";4(0);',5,5,'thing|var|Hello|World|alert'.split('|'),0,{})) &lt;/script&gt;"
		]
	}
}
```

#### Recording Forum Posts on Website (including the HTTP request)
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
		"type": "x-oasis-cti-tc-webpage",
		"url_ref": "3",
		"body": [
			"&lt;div class=\"highlight\"&gt;I hack3d the Internetz and no 1 will get me eva.&lt;/div&gt;",
			"&lt;div class=\"highlight\"&gt;I've managed to get into the CIA man!&lt;/div&gt;"
		]
	},
	"3": {
		"type": "url",
		"value": "https://wayneindustries.com/research/index.html"
	}
}
```

### STIX Patterning Examples
