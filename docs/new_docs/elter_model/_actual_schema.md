[Back to model](_base.md)

# Actual eLTER Metadata model schema

```json
{
    "type": "object",
    "properties": {
        "$schema": {
            "type": "string"
        },
        "created": {
            "type": "string",
            "format": "date-time"
        },
        "externalWorkflow": {
            "type": "object",
            "properties": {
                "defaultWorkflowTemplateId": {
                    "type": "string"
                },
                "history": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "date": {
                                "type": "string",
                                "format": "date-time"
                            },
                            "status": {
                                "type": "string"
                            },
                            "workflowHandle": {
                                "type": "string"
                            },
                            "workflowTemplateId": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "id": {
            "type": "string"
        },
        "metadata": {
            "type": "object",
            "properties": {
                "SOReference": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "url": {
                            "type": "string"
                        }
                    }
                },
                "additionalMetadata": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "value": {
                                "type": "string"
                            }
                        }
                    }
                },
                "assetType": {
                    "type": "string"
                },
                "authors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "email": {
                                "type": "string"
                            },
                            "familyName": {
                                "type": "string"
                            },
                            "fullName": {
                                "type": "string"
                            },
                            "givenName": {
                                "type": "string"
                            },
                            "ids": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "string"
                                        },
                                        "schema": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "contributors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "email": {
                                "type": "string"
                            },
                            "familyName": {
                                "type": "string"
                            },
                            "fullName": {
                                "type": "string"
                            },
                            "givenName": {
                                "type": "string"
                            },
                            "ids": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "string"
                                        },
                                        "schema": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "type": {
                                "type": "string"
                            }
                        }
                    }
                },
                "dataLevel": {
                    "type": "integer"
                },
                "datasetIds": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "identifier": {
                                "type": "string"
                            },
                            "sourceName": {
                                "type": "string"
                            },
                            "type": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        }
                    }
                },
                "descriptions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "description": {
                                "type": "string"
                            },
                            "language": {
                                "type": "string"
                            },
                            "type": {
                                "type": "string"
                            }
                        }
                    }
                },
                "ecosystem": {
                    "type": "object",
                    "properties": {
                        "PID": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                },
                "files": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "format": {
                                "type": "string"
                            },
                            "md5": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "size": {
                                "type": "string"
                            },
                            "sourceUrl": {
                                "type": "string"
                            }
                        }
                    }
                },
                "geoLocations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "EX_BoundingPolygon": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "inPolygonPoint": {
                                            "type": "object",
                                            "properties": {
                                                "latitude": {
                                                    "type": "number"
                                                },
                                                "longitude": {
                                                    "type": "number"
                                                }
                                            }
                                        },
                                        "points": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "latitude": {
                                                        "type": "number"
                                                    },
                                                    "longitude": {
                                                        "type": "number"
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
                                        "type": "number"
                                    },
                                    "northBoundLatitude": {
                                        "type": "number"
                                    },
                                    "southBoundLatitude": {
                                        "type": "number"
                                    },
                                    "westBoundLongitude": {
                                        "type": "number"
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
                                        "type": "number"
                                    },
                                    "longitude": {
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    }
                },
                "geoServerInfo": {
                    "type": "object",
                    "properties": {
                        "mapData": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "bytetype": {
                                        "type": "boolean"
                                    },
                                    "epsgCode": {
                                        "type": "integer"
                                    },
                                    "features": {
                                        "type": "object",
                                        "properties": {
                                            "label": {
                                                "type": "string"
                                            },
                                            "name": {
                                                "type": "string"
                                            },
                                            "style": {
                                                "type": "object",
                                                "properties": {
                                                    "colour": {
                                                        "type": "string"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "path": {
                                        "type": "string"
                                    },
                                    "type": {
                                        "type": "string"
                                    }
                                }
                            }
                        },
                        "serviceType": {
                            "type": "string"
                        }
                    }
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        }
                    }
                },
                "language": {
                    "type": "string"
                },
                "licenses": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        }
                    }
                },
                "methods": {
                    "type": "object",
                    "properties": {
                        "PID": {
                            "type": "string"
                        },
                        "instrumentationDescription": {
                            "type": "string"
                        },
                        "qualityControlDescription": {
                            "type": "string"
                        },
                        "sampling": {
                            "type": "object",
                            "properties": {
                                "samplingDescription": {
                                    "type": "string"
                                },
                                "studyDescription": {
                                    "type": "string"
                                }
                            }
                        },
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "description": {
                                        "type": "string"
                                    },
                                    "title": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "project": {
                    "type": "object",
                    "properties": {
                        "DOI": {
                            "type": "string"
                        },
                        "PID": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                },
                "propertyRights": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        }
                    }
                },
                "publicationDate": {
                    "type": "string",
                    "format": "date"
                },
                "shortNames": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "language": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            }
                        }
                    }
                },
                "siteReference": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "PID": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            }
                        }
                    }
                },
                "taxonomicCoverages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "classification": {
                                "type": "object",
                                "properties": {
                                    "commonName": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "rankName": {
                                        "type": "string"
                                    },
                                    "rankValue": {
                                        "type": "string"
                                    }
                                }
                            },
                            "description": {
                                "type": "string"
                            }
                        }
                    }
                },
                "temporalCoverages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "endDate": {
                                "type": "string",
                                "format": "date"
                            },
                            "startDate": {
                                "type": "string",
                                "format": "date"
                            }
                        }
                    }
                },
                "temporalResolution": {
                    "type": "integer"
                },
                "titles": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "language": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            }
                        }
                    }
                },
                "version": {
                    "type": "string"
                }
            }
        },
        "pid": {
            "type": "object",
            "properties": {
                "obj_type": {
                    "type": "string"
                },
                "pid_type": {
                    "type": "string"
                },
                "pk": {
                    "type": "integer"
                },
                "status": {
                    "type": "string"
                }
            }
        },
        "state": {
            "type": "string"
        },
        "substring_search_field": {
            "type": "string"
        },
        "updated": {
            "type": "string",
            "format": "date-time"
        }
    }
}
```

[Back to model](_base.md)