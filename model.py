import json
import networkx as nx
from pyvis.network import Network

donors = {}

with open('donors.json') as json_file:
    donors = json.load(json_file)

G = nx.DiGraph()

for donor in donors.keys():             # First iteration to declare nodes in graph
    alive = None
    for recipient in donors[donor].keys():
        if recipient == 'alive':
            alive = donors[donor][recipient]
    
    if alive:
        G.add_node(donor, label='Alive')
    else:
        G.add_node(donor, label='Deceased')

for donor in donors.keys():             # Second iteration to declare edges in graph
    for recipient in donors[donor].keys():
        if recipient != 'alive':
            G.add_edge(donor, recipient, weight=donors[donor][recipient])

g = Network(height=800, width=800, notebook=True)
g.toggle_hide_edges_on_drag(False)
g.barnes_hut()
g.from_nx(G)
g.show("before.html")