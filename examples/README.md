# RCOnt examples

## `rc-zone.ttl`

A compact **1R1C1α** thermal-zone example showing:

- a Brick HVAC zone and points;
- indoor and outdoor RCOnt nodes;
- one thermal resistance;
- one thermal capacitance;
- one effective solar aperture; and
- QUDT units.

Parse it with RDFLib:

```bash
python - <<'PY'
from rdflib import Graph

g = Graph()
g.parse("examples/rc-zone.ttl", format="turtle")
print(f"Loaded {len(g)} triples")
PY
```

Generate an interactive graph:

```bash
python scripts/visualize_example.py
```

The generated `examples/rcont-graph.html` file is excluded from version control.
