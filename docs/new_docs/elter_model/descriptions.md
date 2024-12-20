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
  "descriptions": {
    "type": "array",
    "required": "once",
    "comment-on-required": "required once but more then one occurence is allowed",
    "items": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "required": true,
          "min-length": 200,
          "max-length": 4000,
          "comment-on-length": "number of characters",
          "tooltip": "Please describe the dataset with an abstract of at least 200 characters. Please consider giving the description more structure by adding additional description fields.",
        },
        "type": {
          "type": "enum",
          "required": true,
          "enumValues": [
            "Abstract",
            "AdditionalInfo",
            "Methods",
            "SeriesInformation",
            "TableOfContents",
            "TechnicalInfo",
            "Other"
          ]
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
