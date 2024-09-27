# File Handling Modules
import glob
import os
from pathlib import Path

# Dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import _dash_renderer

# Custom modular component files
# import saled.layouts.side_bar
# import saled.layouts.top_bar
# import saled.layouts.transcript_region
from saled.layouts import side_bar, top_bar, transcript_region
from saled.callbacks import get_callbacks

# Required minimum react version to ensure all features load properly.
_dash_renderer._set_react_version("18.2.0")

# Ensure project is executing from project root directory.
#       This makes sure all paths work between systems.
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

# Path for audio files
# DATA_PATH_NAME = "..\\doc\\"

current_directory = Path.cwd()

# Checks path for all currently-supported audio formats.
# DIR_CONTENTS = glob.glob(DATA_PATH_NAME + "/*.mp3") + glob.glob(
#     DATA_PATH_NAME + "/*.wav"
# )

DIR_CONTENTS = glob.glob(str(current_directory) + "*/*.mp3")
# print(f'{DIR_CONTENTS = }')


if DIR_CONTENTS is None:
    raise ValueError("Empty Assets Directory.")

# Start App
app = Dash(__name__)
app.title = "Speech & Language Editor"

# Load all our callback functions.
get_callbacks(app)
# Send file contents to top bar layout, initialize layout.
top_bar.set_contents(DIR_CONTENTS)

# Layout skeleton, complex features are now in their own respective files.
app.layout = dmc.MantineProvider(
    [
        top_bar.layout,
        dmc.Grid(
            children=[
                dmc.GridCol(
                    [side_bar.layout],
                    span=2.5,
                ),
                dmc.GridCol(
                    [
                        dmc.Space(h="sm"),
                        transcript_region.layout,
                    ],
                    span=9.5,
                ),
            ],
            grow=True,
            gutter="md",
            h="82vh",
        ),
        dcc.Store(id="sampled-audio"),  # Client-side storage.
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
