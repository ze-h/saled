""" Top Bar Layout
  File for the top bar component objects. This includes the title, file select,
  action buttons, and placeholder global timestamps.
"""

from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

DIR_CONTENTS = None
layout = None


def set_contents(content):
    global DIR_CONTENTS
    global layout
    DIR_CONTENTS = content
    layout = html.Div(
        [
            dmc.Group(
                [
                    dmc.Title("SaLED", order=2, m="md"),
                    dmc.Select(
                        placeholder="Select File",
                        id="file-selector",
                        data=[
                            {"label": file, "value": file}
                            for file in sorted(DIR_CONTENTS, reverse=True)
                        ],
                        value=(
                            DIR_CONTENTS[0]
                            if DIR_CONTENTS
                            else "Warning: Empty Directory"
                        ),
                        m="md",
                        w="25%",
                    ),
                    dmc.Group(
                        [
                            dmc.Button(
                                DashIconify(icon="mingcute:play-fill"),
                                size="lg",
                                variant="outline",
                                id="play-button",
                            ),
                            dmc.Button(
                                DashIconify(icon="mingcute:pause-fill"),
                                size="lg",
                                variant="outline",
                                id="pause-button"
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="mingcute:skip-previous-fill"),
                                size="lg",
                                variant="outline",
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="mingcute:skip-forward-fill"),
                                size="lg",
                                variant="outline",
                            ),
                            dmc.Text("00:00:00.000/99:99:99.999", size="lg", p="md"),
                        ],
                        gap=0,
                    ),
                ],
                id="title-bar",
            ),
            dcc.Graph(
                id="global-waveform",
                style={"height": "10vh"},
                config={"displaylogo": False, "modeBarButtonsToAdd": ["select2d"]},
            ),
        ]
    )
