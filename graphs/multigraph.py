""" graphs.multigraph.py
Model class: Multigraph
"""
from datamodels.graph import Graph

import networkx as nx
from plotly.graph_objs import Layout, Scatter, layout
from plotly.graph_objects import Scattergl, Figure


class Multigraph(Graph):
    """Multigraph graph class"""

    def __init__(self):
        super().__init__(type="Multigraph")
        self._G = nx.MultiGraph()

    @property
    def G(self):
        return self._G

    def add_nodes(self, nodes_df):
        self._G.add_nodes_from(
            [
                (node["ID"], {"color": node["COLOR"]})
                for node in nodes_df.to_dict("records")
            ]
        )

    def add_edges(self, edges_df):
        for e in edges_df.to_dict("records"):
            for w in ["DURATION", "PACKETS", "BYTES", "SPEED"]:
                self._G.add_weighted_edges_from(
                    [(e["SRC"], e["DST"], e[w])],
                    color={0: "#299e50", 1: "#ff0000", 2: "#ff0000"}.get(
                        e["ATTACK_TYPE"], "#000000"
                    ),
                )

    def plot(self, width=1100, height=900):
        pos = nx.random_layout(self._G)
        number_of_nodes = self._G.number_of_nodes()
        color_by_nodes = {x[0]: x[1]["color"] for x in self._G.nodes.data()}
        nodes_colors = [color_by_nodes[x] for x in pos]
        _title = "Multigraph plot using Netflow data"
        _axis = dict(
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=_title,
        )
        _layout = Layout(
            font=dict(size=12),
            showlegend=False,
            autosize=False,
            width=width,
            height=height,
            xaxis=layout.XAxis(_axis),
            yaxis=layout.YAxis(_axis),
            margin=layout.Margin(
                l=40,
                r=40,
                b=85,
                t=100,
            ),
            hovermode="closest",
            annotations=[
                dict(
                    showarrow=False,
                    text=_title,
                    xref="paper",
                    yref="paper",
                    x=0,
                    y=-0.1,
                    xanchor="left",
                    yanchor="bottom",
                    font=dict(size=12),
                )
            ],
        )

        nodes_scatter = Scattergl(
            x=[pos[k][0] for k in range(number_of_nodes)],
            y=[pos[k][1] for k in range(number_of_nodes)],
            mode="markers",
            marker=dict(size=8, color=nodes_colors, line_width=1),
        )
        edges_scatters = [
            Scatter(
                x=[pos[e[0]][0], pos[e[1]][0]],
                y=[pos[e[0]][1], pos[e[1]][1]],
                mode="lines",
                line=dict(width=0.5, color=e[2]["color"]),
            )
            for k, e in enumerate(self._G.edges.data())
        ]
        edges_scatters.append(nodes_scatter)
        fig = Figure(data=edges_scatters, layout=_layout)
        fig.show()
