""" Transcript Region Layout
  This is a separate file for managing the layout of the transcript cards.
  This will later be actively generated based on the current transcript file.
"""

import dash_mantine_components as dmc

# Layout as a dash object.
layout = dmc.ScrollArea(
    h="82vh",
    w="95%",
    type="hover",
    id="card-area",
    children=[
        dmc.Paper(
            "Text box for different tiers of annotations.",
            shadow="sm",
            radius="sm",
            p="md",
            style={"font-style": "italic"},
        ),
        dmc.Space(h="md"),
        dmc.Paper(
            [
                dmc.Group(
                    [
                        dmc.Text("Text:", c="blue"),
                        dmc.Text(
                            "DELTA 2387 to BRAVO 2 via Echo, cross runway 26L, sorry hold short of runway 26L, then into ramp 2."
                        ),
                    ]
                ),
                dmc.Group(
                    [
                        dmc.Text("NLP:", c="purple"),
                        dmc.Text(
                            "DELTA 2387 to BRAVO 2 via Echo, hold short of runway 26L, then into ramp 2."
                        ),
                    ]
                ),
                dmc.Group(
                    [
                        dmc.Text("Callsign:", c="red"),
                        dmc.Text("DELTA 2387"),
                    ]
                ),
                dmc.Group(
                    [
                        dmc.Text("Runway", c="green"),
                        dmc.Text("Runway 26L"),
                    ]
                ),
                dmc.Group(
                    [
                        dmc.Text("Taxiway:", c="blue"),
                        dmc.Text("BRAVO 2; Echo"),
                    ]
                ),
            ],
            shadow="sm",
            radius="sm",
            p="md",
        ),
        dmc.Space(h="md"),
        dmc.Paper(
            [
                dmc.Text("Text box for different tiers of annotations."),
                dmc.Text(
                    "Note: The above text is the verbatim transciption. It includes non-verbal vocalizations like 'uh', 'um', and laughter. We can alo consider the orthographic transcription, where the non-verbal vocalizations are omitted. In any case, we need to label separately 2-4, which is pronounced as two four, and 24, which is pronounced as twenty-four."
                ),
            ],
            shadow="sm",
            radius="sm",
            p="md",
            style={"font-style": "italic"},
        ),
    ],
)
