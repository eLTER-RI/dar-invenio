[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{
  "licenses": {
    "type": "array",
    "label": "License",
    "tooltip": "The license under which this data set is available to the users (e.g. GPL, Apache v2 or Commercial). Please use the License Selector for help and additional information.",
    "required": true,
    "comment-on-required": "Required once but more than one occurence is allowed."
    "items": {
      "type": "object",
      "properties": {
        "licenseCode": {
          "type": "string",
          "tooltip": "For example CC BY-SA 4.0"
        },
        "licenseURI": {
          "type": "string",
          "tooltip": "For example https://creativecommons.org/licenses/by-sa/4.0/deed.en",
        }
      }
    }
  }
}
```
## Description
### Definition
A legal document under which the resource is made available.
### Required
mandatory
### Multiplicity
1
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
