from rdflib import Graph
from pyvis.network import Network

# Load the RDF data from the TTL file
ttl_path = "https://raw.githubusercontent.com/matinabtahi/operational_digital_twinning/main/EXAMPLE.ttl"
g = Graph()
g.parse(ttl_path, format="ttl")

# Create an interactive network graph
net = Network(height="800px", width="100%", directed=True, notebook=False)
net.force_atlas_2based()

# Add nodes and edges
for s, p, o in g:
    s_label = s.split("#")[-1] if "#" in s else s.split("/")[-1]
    p_label = p.split("#")[-1] if "#" in p else p.split("/")[-1]
    o_label = o.split("#")[-1] if "#" in o else o.split("/")[-1]

    net.add_node(s_label, label=s_label, title=str(s))
    net.add_node(o_label, label=o_label, title=str(o))
    net.add_edge(s_label, o_label, label=p_label)
