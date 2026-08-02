## Author

**Dr. Seyed Matin Abtahi**  
Postdoctoral Fellow  
Centre for Zero Energy Building Studies (CZEBS)  
Department of Building, Civil and Environmental Engineering  
Concordia University, Montréal, Canada

📧 Email: matinabtahi@gmail.com

Research interests include operational digital twins, building energy systems, semantic interoperability, demand flexibility and B2G services.


## Version

**Current release:** **RCOnt v2.0**

Version 2.0 extends the original ontology with:

- Operational control semantics
- Actuator and disturbance modeling
- Simulation and calibration workflows
- Model provenance using PROV-O
- Temporal validity using OWL-Time
- Performance metrics
- Model versioning
- Parameter uncertainty representation
- Improved thermal network connection semantics

- ## Repository Structure

```
.
├── RCOnt.ttl                  # Original ontology
├── RCOnt_V2.0.ttl             # Latest ontology
├── ZoneOnt.ttl                # Operational zone ontology
├── EXAMPLE_Description.ttl    # Example knowledge graph
├── EXAMPLE_RDF.py             # RDF generation example
├── EXAMPLE_RDF.html           # RDF visualization
├── README.md
└── LICENSE.txt
```

## Related Standards

RCOnt complements existing Semantic Web standards rather than replacing them.

- **Brick** – Building assets, equipment, sensors, and HVAC systems
- **PROV-O** – Provenance and model lifecycle
- **OWL-Time** – Temporal validity and versioning
- **QUDT** – Physical quantities and engineering units
- **SAREF** – Smart appliance and building interoperability

  ## Contributing

Contributions are welcome.

If you find a bug, identify an inconsistency, or have suggestions for improving the ontology, please feel free to:

- Open an Issue
- Submit a Pull Request
- Share feedback or implementation experiences

Constructive discussions and collaborations are always appreciated.
