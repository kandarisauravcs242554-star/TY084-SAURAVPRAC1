import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# Roads with distances
roads = [
    ("Andheri","Surat",205),
    ("Surat","Timarwani",138),
    ("Timarwani","Muzaffarnagar",834),
    ("Muzaffarnagar","Haridwar",113),

    ("Andheri","Dahisar",14),
    ("Dahisar","Borivali",17),
    ("Borivali","New Delhi",930),
    ("New Delhi","Haridwar",220),

    ("Andheri","Jaipur",160),
    ("Jaipur","Delhi",280),
    ("Delhi","Roorkee",210),
    ("Roorkee","Haridwar",77)
]

for u, v, d in roads:
    G.add_edge(u, v, weight=d)

# Position of nodes
pos = {
    "Haridwar": (8,10),

    "Muzaffarnagar": (3,8),
    "New Delhi": (8,8),
    "Roorkee": (13,8),

    "Timarwani": (3,5),
    "Borivali": (8,5),
    "Delhi": (13,5),

    "Surat": (3,2),
    "Dahisar": (8,2),
    "Jaipur": (13,2),

    "Andheri": (8,0)
}

# Draw nodes
plt.figure(figsize=(12,8))

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=2200,
    node_color="skyblue",
    edgecolors="black"
)

# Draw labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=9,
    font_weight="bold"
)

# Draw all roads
nx.draw_networkx_edges(
    G,
    pos,
    width=2,
    edge_color="gray"
)

# Highlight Best Route
best_route = [
    ("Andheri","Surat"),
    ("Surat","Timarwani"),
    ("Timarwani","Muzaffarnagar"),
    ("Muzaffarnagar","Haridwar")
]

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=best_route,
    edge_color="orange",
    width=5
)

# Distance Labels
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=9
)

plt.title(
    "IDDFS Route Map: Andheri (Mumbai) → Haridwar (Uttarakhand)\n"
    "Orange = Best Route | Gray = Alternate Routes",
    fontsize=14,
    fontweight="bold"
)

plt.axis("off")
plt.show()