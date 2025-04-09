
---

## Ontologies Used

| Ontology/Schema | Role |
|-----------------|------|
| [Brick Schema](https://brickschema.org) | Describes building components, zones, systems |
| [EFOnt](https://github.com/LBNL-ETA/EnergyFlexibilityOntology) | Tags devices with flexibility service capabilities |
| [Custom Thermal RC Model](https://matinabtahi.github.io/operational_digital_twinning/thermal-model.ttl) | Extends Brick with thermal resistance/capacitance semantics |
| SHACL | Used for validating RDF structure and modeling rules |

---

## Main Features

- **Semantic modeling** of buildings, HVAC zones, devices, sensors, and DERs
- **Energy flexibility tagging** (LoadShifting, PeakShaving, etc.) via EFOnt
- **RC grey-box models** integrated with semantic metadata
- **SHACL validation** of modeling logic (e.g., thermostats must have both sensor and command)
- **SPARQL queries** to retrieve, group, and classify buildings and services

---

## Public Ontologies

| File | Public Link |
|------|-------------|
| `ODTRC` | [View TTL](https://matinabtahi.github.io/operational_digital_twinning/thermal-model.ttl) |
| Brick | [https://brickschema.org/schema/1.1/Brick#](https://brickschema.org/schema/1.1/Brick#) |
| EFOnt | [https://purl.org/efont#](https://purl.org/efont#) |

---

## License

MIT License — see `LICENSE` file.

---

## Author

**Matin Abtahi**  
PhD Candidate @ Concordia University  
Center for Zero Energy Building Studies (CZEBS)  
Email: matinabtahi@gmail.com

---

## Feedback & Contributions

Feel free to fork, raise issues, or open pull requests!  
This repo is a work-in-progress and supports a growing research project on **operational digital twinning and semantic control** for smart energy systems.
