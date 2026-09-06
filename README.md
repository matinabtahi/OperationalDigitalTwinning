# Resistance–Capacitance Ontology (RCOnt)

[![Validation](https://github.com/matinabtahi/Resistance-CapacitanceOntology/actions/workflows/validate.yml/badge.svg)](https://github.com/matinabtahi/Resistance-CapacitanceOntology/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Ontology version](https://img.shields.io/badge/ontology-v2.0.0-blue.svg)](RCOnt.ttl)

**RCOnt** is a lightweight OWL ontology for representing reduced-order resistance–capacitance (RC) thermal models used in building energy modelling, operational digital twins, calibration, model-based control and energy-flexibility applications.

RCOnt describes an RC model's **structure, parameters, states, inputs, disturbances, provenance, validity and performance metadata** in a portable RDF/OWL representation.

> **Current version:** RCOnt v2.0.0

## Why RCOnt?

RC models are widely used in building simulation, system identification and model predictive control, but model structure and parameters are often exchanged through implementation-specific files or code. RCOnt provides a machine-readable semantic layer so an RC model can be discovered, inspected and exchanged independently of the software that created it.

RCOnt is intentionally focused. It does **not** replace building ontologies such as Brick or SAREF; instead, it represents the reduced-order thermal model and links that model to building-system semantics, units and provenance.

## What RCOnt represents

- RC-model structure and thermal nodes
- thermal resistances, capacitances and effective solar aperture
- measurable states and exogenous/control inputs
- actuators and disturbances
- parameter-estimation and simulation activities
- parameter provenance and data sources
- model versions and temporal validity
- uncertainty and performance metrics
- links to Brick, QUDT, PROV-O, OWL-Time and SAREF

## Repository layout

```text
.
├── RCOnt.ttl                    # Current ontology (v2.0.0)
├── archive/
│   └── RCOnt-v1.0.ttl          # Original v1 ontology
├── extensions/
│   └── ZoneOnt.ttl              # Auxiliary zone-archetype vocabulary
├── examples/
│   ├── README.md
│   └── rc-zone.ttl              # Minimal 1R1C1α example
├── scripts/
│   └── visualize_example.py     # Optional RDF graph visualizer
├── .github/workflows/
│   └── validate.yml             # Automated syntax/smoke validation
├── CITATION.cff
├── .zenodo.json
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── requirements.txt
```

## Quick start

Clone the repository:

```bash
git clone https://github.com/matinabtahi/Resistance-CapacitanceOntology.git
cd Resistance-CapacitanceOntology
```

Parse the ontology with RDFLib:

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from rdflib import Graph

g = Graph()
g.parse("RCOnt.ttl", format="turtle")
print(f"Loaded {len(g)} RDF triples")
PY
```

Visualize the example graph:

```bash
python scripts/visualize_example.py
```

The script reads `examples/rc-zone.ttl` and writes `examples/rcont-graph.html`. The generated HTML is intentionally not tracked in Git.

## Minimal modelling pattern

```turtle
ex:Model a rcont:RCModel ;
    rcont:hasNode ex:IndoorNode, ex:OutdoorNode ;
    rcont:hasResistance ex:R1 ;
    rcont:hasCapacitance ex:C1 .

ex:R1 a rcont:ThermalResistance ;
    rcont:connectsFrom ex:IndoorNode ;
    rcont:connectsTo ex:OutdoorNode ;
    rcont:numericValue "0.0075"^^xsd:decimal ;
    rcont:unit unit:K-PER-W .
```

For backward compatibility, `rcont:RValue` and `rcont:CValue` remain equivalent to `rcont:ThermalResistance` and `rcont:ThermalCapacitance`.

## Namespace

The established RCOnt namespace is intentionally preserved:

```text
https://matinabtahi.github.io/OperationalDigitalTwinning/RCOnt#
```

This namespace is a **semantic identifier**, not the current GitHub repository URL. It is retained so existing RCOnt data does not become invalid after the repository rename.

The current source repository is:

```text
https://github.com/matinabtahi/Resistance-CapacitanceOntology
```

## Interoperability

RCOnt complements:

- **Brick** — building assets, zones, sensors, commands and control points
- **QUDT** — quantities, units and numerical values
- **PROV-O** — provenance of calibration, simulation and parameter generation
- **OWL-Time** — model-validity intervals
- **SAREF** — broader smart-building/device semantics

RCOnt v2 uses Brick's version-independent namespace (`https://brickschema.org/schema/Brick#`), following current Brick ontology guidance.

## Versioning

- **v1.0** — original RC-model vocabulary, retained in `archive/RCOnt-v1.0.ttl`
- **v2.0.0** — current ontology with directional RC connectivity, operational-control semantics, provenance, temporal validity, uncertainty and performance metadata

Future releases follow semantic versioning. The ontology namespace remains stable; release versions are recorded with `owl:versionInfo` and `owl:versionIRI`.

## Validation

Every push and pull request runs automated checks that:

1. parse every Turtle file with RDFLib; and
2. smoke-test the example visualization script.

Run the same checks locally:

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from pathlib import Path
from rdflib import Graph

for path in sorted(Path(".").rglob("*.ttl")):
    Graph().parse(path, format="turtle")
    print(f"OK  {path}")
PY
```

## Citation

GitHub reads citation metadata from [`CITATION.cff`](CITATION.cff). Zenodo-specific release metadata is stored in [`.zenodo.json`](.zenodo.json).

Once a tagged release is archived in Zenodo, cite the version-specific DOI for reproducible scholarly use.

## Contributing

Small, focused issues and pull requests are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for conventions on namespaces, ontology changes and validation.

## License

RCOnt, ZoneOnt, examples and supporting scripts are released under the [MIT License](LICENSE).

## Author

**Matin Abtahi**  
Concordia University, Montréal, Canada  
ORCID: [0000-0003-3941-9485](https://orcid.org/0000-0003-3941-9485)
