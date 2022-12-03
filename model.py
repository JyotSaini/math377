import json
import networkx as nx
import numpy as np
from pyvis.network import Network

donors = {}
# donors_mat = []

with open('donors.json') as json_file:
    donors = json.load(json_file)

G = nx.Graph()

for donor in donors.keys():             # First iteration to declare nodes in graph
    alive = None

    for recipient in donors[donor].keys():
        if recipient == 'alive':
            alive = donors[donor][recipient]

    if alive:
        G.add_node(donor, label=donor)
    else:
        G.add_node(donor, label='Deceased')

for donor in donors.keys():             # Second iteration to declare edges in graph
    for recipient in donors[donor].keys():
        if recipient != 'alive':
            G.add_edge(donor, recipient, weight=(donors[donor][recipient]))      # We're scaling down the weight to make the graph look nicer

g = Network(height=500, width="100%", bgcolor="#222222", font_color="white", notebook=True)
# g = Network()
g.toggle_hide_edges_on_drag(False)
g.barnes_hut()
g.from_nx(G)
# g.show_buttons()
g.set_options("""
const options = {
  "edges": {
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.55
      }
    },
    "smooth": false
  },
  "physics": {
    "enabled": false,
    "barnesHut": {
      "gravitationalConstant": -80000,
      "springLength": 250,
      "springConstant": 0.001
    },
    "minVelocity": 0.75
  }
}
""")
g.show("before.html")

intermediate = nx.max_weight_matching(G)
newset = set()
toremove = set()
for edge in intermediate:
    if int(edge[0][1:]) > len(intermediate):
        newset.add(('Deceased' + str(int(edge[0][1:]) - len(intermediate)), edge[1]))
        toremove.add(edge)
for edge in newset:
    intermediate.add(edge)
for edge in toremove:
    intermediate.remove(edge)
H = nx.Graph(intermediate)

print(intermediate)
print(H)

h = Network(height=500, width="100%", bgcolor="#222222", font_color="white", notebook=True)
# g = Network()
h.toggle_hide_edges_on_drag(False)
h.barnes_hut()
h.from_nx(H)
# g.show_buttons()
h.set_options("""
const options = {
  "edges": {
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.55
      }
    },
    "smooth": false
  },
  "physics": {
    "enabled": false,
    "barnesHut": {
      "gravitationalConstant": -80000,
      "springLength": 250,
      "springConstant": 0.001
    },
    "minVelocity": 0.75
  }
}
""")
h.show("after.html")

# def row_operation(G):
# mat = np.array([np.array(x) for x in donors_mat])
# print(mat)