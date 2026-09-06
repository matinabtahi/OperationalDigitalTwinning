# Resistance–Capacitance Ontology (RCOnt)

**RCOnt** is a lightweight OWL ontology for representing reduced-order resistance–capacitance (RC) thermal models used in operational building digital twins, model-based control, calibration and energy-flexibility applications.

The ontology provides a machine-readable description of an RC model's **structure, parameters, states, inputs, disturbances, provenance, validity and performance metadata** while remaining interoperable with established Semantic Web vocabularies.

> **Current ontology version:** RCOnt v2.0.0

## Why RCOnt?

Reduced-order RC models are widely used for building simulation, system identification and model predictive control, but their structure and parameters are often exchanged through implementation-specific files or code. RCOnt provides a portable semantic layer so that an RC model can be discovered, inspected and exchanged independently of the software that generated or consumes it.

RCOnt is intentionally focused: it does **not** replace building ontologies such as Brick or SAREF. Instead, it represents the reduced-order thermal model and links it to building-system semantics, units and provenance.

## Scope

RCOnt v2.0 represents:

- RC-model structure and thermal nodes
- thermal resistances, capacitances and effective solar aperture
- measurable states and exogenous/control inputs
- actuators and disturbances
- parameter-estimation and simulation activities
- parameter provenance and data sources
- model versions and temporal validity
- uncertainty and performance metrics
- links to Brick, QUDT, PROV-O, OWL-Time and SAREF

The canonical RCOnt namespace remains:

```text
https://matinabtahi.github.io/OperationalDigitalTwinning/RCOnt#
```

The namespace is intentionally retained for backward compatibility even if the GitHub repository name changes.

## Repository contents

| File | Purpose |
|---|---|
| `RCOnt_V2.0.ttl` | Current RCOnt ontology (v2.0.0) |
| `RCOnt.ttl` | Original RCOnt v1 ontology retained for provenance/backward reference |
| `ZoneOnt.ttl` | Auxiliary zone-archetype vocabulary used by the example |
| `EXAMPLE_Description.ttl` | Example 1R1C1α building-zone knowledge graph using RCOnt v2 |
| `EXAMPLE_RDF.py` | Small RDF visualisation utility |
| `EXAMPLE_RDF.html` | Existing rendered example visualisation |
| `CITATION.cff` | Machine-readable citation metadata |
| `.zenodo.json` | Zenodo deposition metadata |
| `requirements.txt` | Python dependencies for the visualisation utility |
| `LICENSE.txt` | MIT licence |

## Quick start

Clone the repository and install the two optional Python dependencies:

```bash
pip install -r requirements.txt
python EXAMPLE_RDF.py
```

The script parses `EXAMPLE_Description.ttl` and writes an interactive graph to `EXAMPLE_RDF.html`.

To inspect the ontology directly with RDFLib:

```python
from rdflib import Graph

g = Graph()
g.parse("RCOnt_V2.0.ttl", format="turtle")
print(f"{len(g)} RDF triples loaded")
```

## Minimal modelling pattern

An RC model links to its thermal nodes and parameters:

```turtle
ex:Model a rcont:RCModel ;
    rcont:hasNode ex:IndoorNode, ex:OutdoorNode ;
    rcont:hasResistance ex:R1 ;
    rcont:hasCapacitance ex:C1 .

ex:R1 a rcont:RValue ;
    rcont:connectsFrom ex:IndoorNode ;
    rcont:connectsTo ex:OutdoorNode ;
    rcont:numericValue "0.0075"^^xsd:decimal ;
    rcont:unit unit:K-PER-W .
```

`RValue` and `CValue` are retained as backward-compatible RCOnt class names and are formally aligned with `ThermalResistance` and `ThermalCapacitance` in v2.0.

## Interoperability

RCOnt complements, rather than duplicates:

- **Brick** — building assets, zones, sensors, commands and control points
- **QUDT** — quantities and engineering units
- **PROV-O** — provenance of calibration, simulation and parameter generation
- **OWL-Time** — model validity intervals
- **SAREF** — broader smart-building and device interoperability

## Versioning

- **v1** — original core RC-model vocabulary (`RCOnt.ttl`)
- **v2.0.0** — current ontology with operational-control semantics, provenance, temporal validity, uncertainty, performance metadata and backward-compatible aliases (`RCOnt_V2.0.ttl`)

Stable ontology identifiers are preserved across repository revisions wherever possible.

## Citation

If you use RCOnt in research, software or publications, please cite the archived release. GitHub will expose the citation metadata from `CITATION.cff`; after the release is deposited through Zenodo, the version-specific DOI should be preferred.

## Licence

RCOnt and the accompanying examples are released under the **MIT License**.

## Author

**Matin Abtahi**  
Concordia University, Montréal, Canada  
ORCID: 0000-0003-3941-9485
