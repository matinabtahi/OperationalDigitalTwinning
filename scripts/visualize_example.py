#!/usr/bin/env python3
"""Create an interactive HTML visualization of an RCOnt Turtle graph."""
from __future__ import annotations
import argparse
from pathlib import Path
from pyvis.network import Network
from rdflib import BNode, Graph, Literal, URIRef
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = REPO_ROOT / "examples" / "rc-zone.ttl"
DEFAULT_OUTPUT = REPO_ROOT / "examples" / "rcont-graph.html"
def compact_label(term: URIRef | BNode | Literal) -> str:
    if isinstance(term, Literal):
        text = str(term); return text if len(text) <= 60 else f"{text[:57]}..."
    text = str(term); return text.rsplit("#", 1)[-1] if "#" in text else text.rstrip("/").rsplit("/", 1)[-1]
def build_network(graph: Graph) -> Network:
    net = Network(height="800px", width="100%", directed=True, notebook=False, cdn_resources="remote"); net.force_atlas_2based(gravity=-50); added: set[str] = set()
    for subject, predicate, obj in sorted(graph, key=lambda triple: tuple(map(str, triple))):
        subject_id, object_id = subject.n3(), obj.n3()
        if subject_id not in added: net.add_node(subject_id, label=compact_label(subject), title=str(subject), shape="dot"); added.add(subject_id)
        if object_id not in added: net.add_node(object_id, label=compact_label(obj), title=str(obj), shape="dot"); added.add(object_id)
        net.add_edge(subject_id, object_id, label=compact_label(predicate), title=str(predicate))
    return net
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--input", type=Path, default=DEFAULT_INPUT); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT); return parser.parse_args()
def main() -> None:
    args = parse_args(); graph = Graph(); graph.parse(args.input, format="turtle"); args.output.parent.mkdir(parents=True, exist_ok=True); build_network(graph).write_html(str(args.output), open_browser=False, notebook=False); print(f"Wrote {args.output} from {len(graph)} RDF triples.")
if __name__ == "__main__": main()
