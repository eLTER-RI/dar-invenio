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
  "comment": "Maybe we can consider to use SPDX licence identifier in the future: https://spdx.org/licenses/",
  "licenses": {
    "type": "array",
    "required": "once",
    "comment-on-required": "Required once but more than one occurence is allowed."
    "items": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "tooltip": "For example CC BY-SA 4.0"
        },
        "url": {
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
### Multiplicity
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
