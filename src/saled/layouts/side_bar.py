""" Side Bar Layout
  This file contains layout components for the local waveform, spectrogram,
  and vertical timestamps.
"""

from dash import dcc
import dash_mantine_components as dmc

layout = dmc.Grid(
    children=[
        dmc.GridCol(
            [
                dcc.Graph(
                    id="local-waveform",
                    style={"height": "100%"},
                    config={"displaylogo": False},
                ),
            ],
            span=6,
            h="82vh",
        ),
        dmc.GridCol(
            [
                dcc.Graph(
                    id="spectrogram",
                    style={"height": "100%"},
                    config={"displaylogo": False},
                ),
            ],
            span=4,
            h="82vh",
        ),
        dmc.GridCol(
            [
                dmc.SimpleGrid(
                    [
                        dmc.Text(
                            "Beginning",
                            id="beginning",
                            ta="right",
                            c="dimmed",
                            style={"transform": "rotate(-90deg) translateX(-5.4vh)"},
                        ),
                        dmc.Text(
                            "End",
                            id="end",
                            ta="left",
                            c="dimmed",
                            style={"transform": "rotate(-90deg) translateX(-2.2vh)"},
                        ),
                    ],
                    cols=1,
                    verticalSpacing="70vh",
                    ml="-1vw",
                )
            ],
            span=2,
        ),
    ],
    gutter=0,
)
