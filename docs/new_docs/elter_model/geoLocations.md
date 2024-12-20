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
  "geoLocations": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "comment": "one of Polygon/Box/Point",
        "EX_BoundingPolygon": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "inPolygonPoint": {
                "type": "object",
                "properties": {
                  "latitude": {
                    "type": "number",
                    "maximum": 90,
                    "minimum": -90,
                    "tooltip": "Please use WGS 84 notation with a dot as decimal separator, i.e. 51.340199.",
                  },
                  "longitude": {
                    "type": "number",
                    "maximum": 180,
                    "minimum": -180,
                    "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
                  }
                }
              },
              "points": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "latitude": {
                      "type": "number",
                      "maximum": 90,
                      "minimum": -90,
                      "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199.",
                    },
                    "longitude": {
                      "type": "number",
                      "maximum": 180,
                      "minimum": -180,
                      "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
                    }
                  }
                }
              }
            }
          }
        },
        "EX_GeographicBoundingBox": {
          "type": "object",
          "properties": {
            "eastBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
            },
            "northBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199.",
            },
            "southBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199.",
            },
            "westBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
            }
          }
        },
        "EX_GeographicDescription": {
          "type": "string"
        },
        "Point": {
          "type": "object",
          "properties": {
            "latitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199.",
            },
            "longitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
            }
          }
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
