from dash import Output, Input, callback, State
from dash.exceptions import PreventUpdate
from dash import _dash_renderer

_dash_renderer._set_react_version("18.2.0")

import plotly.express as px
import pandas as pd
from librosa.feature import melspectrogram
from librosa import power_to_db
import numpy as np

import saled.utils.audio as atool
import saled.utils.fileIO as fio


def get_callbacks(app):
    """
    This function contains all the server-side callbacks for the main app.
    """

    @callback(Output("sampled-audio", "data"), Input("file-selector", "value"))
    def update_sampled_audio(FILE):
        """
        This function updates the audio stored on the client side when a new
        file is selected.

        Parameters:
        FILE (str): The file path selected in the menu.

        Returns:
        ndarray: A Numpy array containing sampled points from the original
                        waveform.
        """
        if FILE is None:
            raise PreventUpdate
        sample_audio = atool.envelope_sample(fio.load_audio(FILE))
        return sample_audio

    @callback(Output("global-waveform", "figure"), Input("sampled-audio", "data"))
    def plot_global_waveform(sampled):
        """
        This function plots the waveform of the entire selected audio file.

        Parameters:
        sampled (ndarray): A Numpy array containing sampled waveform values.

        Returns:
        Figure: A Ploty Figure object of the resulting waveform plot.
        """
        df = pd.DataFrame(sampled)
        graph = px.line(df, x=df.index, y=0, render_mode="webgl")
        graph.update_layout(
            showlegend=False,
            margin=dict(b=0, l=0, r=0, t=0),
            dragmode="select",
            selectdirection="h",
            activeselection={"opacity": 1},
            newselection=dict(
                line=dict(
                    color="Crimson",
                    width=3,
                    dash="solid",
                )
            ),
        )
        graph.update_xaxes(visible=False, fixedrange=True)
        graph.update_yaxes(visible=False, fixedrange=True)
        return graph

    @callback(
        Output("local-waveform", "figure"),
        Input("sampled-audio", "data"),
        Input("global-waveform", "selectedData"),
    )
    def plot_local_waveform(sampled, selection):
        """
        This function updates the local waveform.

        Parameters:
        sampled (ndarray): A Numpy array containing sampled waveform values.
        selection (dict): A dictionary containing Plotly selection information.

        Returns:
        Figure: A Plotly Figure object of the waveform plot.
        """
        df = pd.DataFrame(sampled)
        if selection is not None and "range" in selection.keys():
            left_bound = selection["range"]["x"][0]
            right_bound = selection["range"]["x"][1]
        else:
            left_bound = 0
            right_bound = len(sampled) / 10

        graph = px.line(df, x=0, y=df.index, render_mode="webgl")
        graph.update_xaxes(visible=False, fixedrange=True)
        graph.update_yaxes(
            autorange="reversed",
            visible=False,
            autorangeoptions=dict(clipmin=left_bound, clipmax=right_bound),
            fixedrange=True,
        )
        graph.update_layout(showlegend=False, margin=dict(b=0, l=0, r=0, t=0))

        return graph

    @callback(
        Output("spectrogram", "figure"),
        Input("sampled-audio", "data"),
        Input("global-waveform", "selectedData"),
        Input("file-selector", "value"),
        prevent_initial_call=True,
        running=[
            (
                Output("spectrogram", "loading_state"),
                {"is_loading": True},
                {"is_loading": False},
            )
        ],
    )
    def update_spectrogram(_, selection, FILE):
        """
        This function updates the spectrogram display independently of the
        local waveform. This function uses the raw file and not any sampled
        data.

        Parameters:
        _: Dumped ndarray (Required as an input to ensure plot updates when
                file changes).
        selection (dict): A dictionary containing Plotly selection information.
        FILE (str): The path of the raw audio file.

        Returns:
        Figure: A Plotly Figure object containing a heatmap of the spectrogram
                        image.
        """
        sample_audio = fio.load_audio(FILE)
        if selection is not None and "range" in selection.keys():
            left_bound = selection["range"]["x"][0] * 160
            right_bound = selection["range"]["x"][1] * 160
        else:
            left_bound = 0
            right_bound = sample_audio.size / 10

        spec = melspectrogram(
            y=sample_audio[int(left_bound) : int(right_bound)],
            sr=16000,
            n_mels=128,
            fmax=4000,
        )
        spec_dB = power_to_db(spec, ref=np.max)
        fig = px.imshow(
            np.flip(np.rot90(spec_dB), 0),
            aspect="auto",
            color_continuous_scale="Greys",
        )
        fig.update_coloraxes(showscale=False)
        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)
        fig.update_layout(
            showlegend=False,
            margin=dict(b=0, l=0, r=0, t=0),
        )
        return fig

    @callback(
        Output("beginning", "children"),
        Output("end", "children"),
        Input("global-waveform", "selectedData"),
        Input("file-selector", "value"),
        Input("sampled-audio", "data"),
    )
    def update_side_labels(selection, _, sample_audio):
        """
        This function updates timestamp labels alongside the local plots.

        Parameters:
        selection (dict): A dictionary containing Plotly selection information.
        _: Dumped file path. (Required to update timestamps when new file is
                selected.)
        sample_audio (ndarray): Stored sampled audio needed for measurement.

        Returns:
        str: The beginning timestamp as a formatted string.
        str: The end timestamp as a formatted string.
        """
        if selection is not None and "range" in selection.keys():
            left_bound = selection["range"]["x"][0] * 0.01
            right_bound = selection["range"]["x"][1] * 0.01
        else:
            left_bound = 0
            right_bound = len(sample_audio) / 10 * 0.01

        left_ms = int(left_bound % 1 * 1000)
        left_seconds = int(left_bound % 60)
        left_minutes = int((left_bound / 60) % 60)
        left_hours = int((left_bound / 3600) % 60)

        right_ms = int(right_bound % 1 * 1000)
        right_seconds = int(right_bound % 60)
        right_minutes = int((right_bound / 60) % 60)
        right_hours = int((right_bound / 3600) % 60)
        return (
            f"{left_hours:02d}:{left_minutes:02d}:{left_seconds:02d}.{left_ms:03d}",
            f"{right_hours:02d}:{right_minutes:02d}:{right_seconds:02d}.{right_ms:03d}",
        )
