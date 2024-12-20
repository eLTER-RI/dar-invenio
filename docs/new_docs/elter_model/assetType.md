[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{  "assetType": {
    "type": "enum",
    "label": "Standard observation",
    "tooltip": "Please provide the corresponding eLTER standard observation for the dataset.",
    "required": true,
    "enum": [
      "Soil inventory (SOGEO_001)",
      "Soil chemical and physical properties (SOGEO_003)",
      "Soil water chemistry (SOGEO_167)",
      "Soil infiltration (SOGEO_048)",
      "Sediment (aquatic/marine) (SOGEO_155)",
      "Standing water - Profiles chemical/physical waters properties (SOHYD_004)",
      "Running water - chemical/physical properties (SOHYD_005)",
      "Groundwater - chemical/physical properties (SOHYD_006)",
      "Running water - nutrients (SOHYD_169)",
      "Standing water - Profiles nutrients (SOHYD_170)",
      "Surface water - Major ion concentrations (SOHYD_171)",
      "Running water level (SOHYD_010)",
      "Standing water - Ice cover/thickness (SOHYD_011)",
      "Snow (SOHYD_012)",
      "Soil water content/temperature (SOHYD_168)",
      "Surface water - Stable isotopes (SOHYD_058)",
      "Groundwater - Stable Isotopes (SOHYD_059)",
      "Groundwater - Major ion concentrations (SOHYD_062)",
      "Groundwater - Nutrients (SOHYD_064)",
      "Running water - micropollutants (SOHYD_067)",
      "Glacier - front variation (SOHYD_164)",
      "Glacier - mass balance (SOHYD_165)",
      "Glacier - area (SOHYD_166)",
      "Secchi-depth (SOHYD_174)",
      "Flying - insects (SOBIO_014)",
      "Vegetation - composition (SOBIO_017)",
      "Acoustic recording (SOBIO_018)",
      "Pollen and spores (SOBIO_019)",
      "eDNA Water (SOBIO_021)",
      "eDNA soil (SOBIO_022)",
      "Surface water - clorophyll (SOBIO_096)",
      "Running water - P/N (SOHYD_172)",
      "Standing water - Profiles P/N (SOHYD_173)",
      "Meteorological data (SOATM_027)",
      "Radiation (SOATM_028)",
      "Ground heat flux (SOATM_098)",
      "Atmospheric deposition in precipitation (SOATM_103)",
      "Dry deposition of N-components (SOATM_108)",
      "Eddy covariance (SOATM_176)",
      "Forest - Aboveground biomass (SOBIO_023)",
      "Tree growth (SOBIO_177)",
      "Non-forest - Aboveground biomass (SOBIO_024)",
      "Gross primary production (SOBIO_090)",
      "Transpiration (SOBIO_091)",
      "Forests - Litterfall (SOBIO_092)",
      "Belowground biomass (SOBIO_093)",
      "Phenological traits (Remote Sensing) (SOBIO_015)",
      "Phenological traits (on-site) (SOBIO_016)",
      "Forest - LAI (SOBIO_025)",
      "Non-forest - LAI (SOBIO_026)",
      "Leaf - Elements (SOBIO_095)",
      "Vegetation - LiDAR (SOBIO_140)",
      "Yield (SOSOC_031)",
      "Land-based income (SOSOC_030)",
      "Livestock (SOSOC_114)",
      "Governance (SOSOC_032)",
      "Land cover and use (CORINE) (SOSOC_036)",
      "Land cover and use (Statistics) (SOSOC_037)",
      "Ecosystem services (SOSOC_040)",
      "Economics - GDP (SOSOC_042)",
      "Demography (SOSOC_043)",
      "Employment (SOSOC_044)",
      "Consumption statistics (SOSOC_045)",
      "Resource use (SOSOC_183)",
      "Subsidies (SOSOC_184)"
    ],
    "comment": "see https://vocabs.lter-europe.net/so/en/ - as they are currently not integrated in the vocabs ('comming soon') I derived them from https://docs.google.com/spreadsheets/d/1F6mZNpdW0r6tQ8l69PU8Z_7XLljRlXEY/edit?gid=43892927#gid=43892927"
  }
}
```
## Description
### Definition
Type of asset.
### Multiplicity
### Required
### RDF Property
### EML URL

## JSON Example
## ISO Mapping


[Back to model](_base.md)
