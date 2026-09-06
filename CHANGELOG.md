# Changelog

All notable changes to RCOnt are documented here.

The project follows [Semantic Versioning](https://semver.org/).

## [2.0.0] - Unreleased

### Added
- Operational-control concepts for actuators and disturbances.
- Provenance concepts for parameter estimation, simulation and data sources.
- Model-version and temporal-validity concepts.
- Performance metrics and parameter-uncertainty metadata.
- Directional `connectsFrom` / `connectsTo` resistance endpoints.
- Automated RDF syntax validation and example smoke testing.

### Changed
- `RCOnt.ttl` is now the canonical current ontology file.
- Brick references use the version-independent Brick namespace.
- Repository documentation, citation metadata and archival metadata were normalized.
- Example and utility files were organized into `examples/` and `scripts/`.

### Deprecated
- `rcont:connects` is retained for compatibility; new data should use `rcont:connectsFrom` and `rcont:connectsTo`.

### Preserved
- The established RCOnt namespace remains unchanged for backward compatibility.
- The original v1 ontology is preserved in `archive/RCOnt-v1.0.ttl`.

## [1.0.0] - 2025

### Added
- Initial RC-model classes, nodes, resistance/capacitance parameters, solar aperture and basic Brick/QUDT alignment.
