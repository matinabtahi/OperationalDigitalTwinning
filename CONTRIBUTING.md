# Contributing to RCOnt

Contributions that improve correctness, interoperability, examples or documentation are welcome.

## Before opening a pull request

1. Keep the established RCOnt namespace unchanged:
   `https://matinabtahi.github.io/OperationalDigitalTwinning/RCOnt#`
2. Prefer backward-compatible additions over renaming or removing published terms.
3. Add an English `rdfs:label` and a concise `rdfs:comment` for new public terms.
4. Use established vocabularies such as Brick, QUDT, PROV-O, OWL-Time or SAREF when they already express the required concept.
5. Update examples and `CHANGELOG.md` when a public term or modelling pattern changes.
6. Run the validation checks before submitting.

## Local validation

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from pathlib import Path
from rdflib import Graph

for path in sorted(Path(".").rglob("*.ttl")):
    Graph().parse(path, format="turtle")
    print(f"OK  {path}")
PY

python scripts/visualize_example.py --output /tmp/rcont-example.html
```

## Versioning

RCOnt follows semantic versioning:

- **PATCH** — documentation/metadata corrections that do not change ontology semantics
- **MINOR** — backward-compatible ontology additions
- **MAJOR** — incompatible semantic changes

Published ontology identifiers should not be changed merely to match repository or directory names.
