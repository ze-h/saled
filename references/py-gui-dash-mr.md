<!--

-   2024-07-14: Note created by copying from:
-   2024-07-14: Summary of changes:

-->

<!-- bgn tags -->

Tags: #template

<!-- end tags -->

<!-- bgn hidden -->

```toc
style: number
min_depth: 1
max_depth: 6
```

<!-- end hidden -->

<!-- bgn ch-title -->

# A MiniRef for Plotly Dash

<!-- end ch-title -->

## Dash Bootstrap Components

### `dbc.ButtonGroup`

We can put two `html.Button`s side-by-side using `dbc.ButtonGroup`, as seen below.

```python
dbc.ButtonGroup([
    html.Button(id='plt_time', children='Plot power vs time',
                disabled=True),
    html.Button(id='plt_npts', children='Plot n-point power',
                disabled=True),
]),
```

Note that this code is from `srt_companion.py`, saved in the `./py-gui/` folder.


## Dash Core Components

Dash provides a large collection of core components in `dash.dcc`. (dcc stands for dash core component.).

Below is a list of all `dash.dcc` components:

-   Checklist
-   Clipboard
-   ConfirmDialog
-   ConfirmDialogProvider
-   DatePickerRange
-   DatePickerSingle
-   Download
-   Dropdown v
-   Graph v
-   Input v
-   Interval v
-   Link
-   Loading
-   Location
-   LogoutButton
-   Markdown v
-   RadioItems v
-   RangeSlider
-   Slider v
-   Store v
-   Tab
-   Tabs
-   Textarea
-   Tooltip
-   Upload

To check the original document of each of them, we can use the left column of the following link: https://dash.plotly.com/dash-core-components.

Below, we take brief notes about the important components, in the alphabetical order of the components.

### `dcc.Dropdown`

### `dcc.Graph`

#### `plotly.graph_objects`

We can use `plotly.graph_objects` to display various graphs and have overlays using lines and rectangles to control other components in the system. 

Below is an example, which can do the following:

-   Display the bar graph, illustrating the amplitude of audio amplitudes.
-   Display a vertical line, simulating the audio-play position indicator. This can be dragged so that the audio play location can be changed. Note that the drag of this line is only effective in the x direction.
-   Display two rectangles, simulating the display of two intervals. The separation line of the intervals can be dragged. Note that we can add callback functions to fix the two other ends of the rectangles.

Note that the `shapes` in `layout` is a list of dict, and we can add or remove rectangles by operating on `shapes`. 

```python
import json
import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

styles = {'pre': {'border': 'thin lightgrey solid', 'overflowX': 'scroll'}}

A = np.mod(np.arange(256), 100)
X = np.arange(256)

trace1 = go.Bar(
    x=X,
    y=A,
    name='Positive Values',
    marker_color='blue'
)

    # Add negative bars
trace2 = go.Bar(
    x=X,
    y=-A,
    name='Negative Values',
    marker_color='blue'
)

# Define the layout with the line shape
layout = go.Layout(
    barmode='overlay', # Set barmode to 'overlay' to make bars overlap
    yaxis=dict(range=[-250, 250]), # Set y-axis range from -10 to 10
    shapes=[
    {
        'type': 'line',
        'x0': 0.5,
        'x1': 0.5,
        'xref': 'paper',
        'y0': 0,
        'y1': 1,
        'yref': 'paper',
        'line': {
            'width': 1,
            'color': 'rgb(90, 30, 30)'
        },
    },
    {
        'type': 'rect',
        'x0': 0.55,
        'x1': 0.75,
        'xref': 'paper',
        'y0': 0,
        'y1': 1,
        'yref': 'paper',
        'fillcolor': 'rgba(0, 120, 0, 0.3)',
        'line': {
            'width': 0
        }
    },
    {
        'type': 'rect',
        'x0': 0.75,
        'x1': 1,
        'xref': 'paper',
        'y0': 0,
        'y1': 1,
        'yref': 'paper',
        'fillcolor': 'rgba(0, 0, 120, 0.3)',
        'line': {
            'width': 0
        }
    }]
)

# Create the figure
figure = go.Figure(data=[trace1, trace2], layout=layout)


app.layout = html.Div(className='row', children=[
    dcc.Graph(
        id='basic-interactions',
        className='six columns',
        figure=figure,
        config={
            'editable': True,
            'edits': {
                'shapePosition': True
            }
        }
    ),
    html.Div(
        className='six columns',
        children=[
            html.Div(
                [
                    html.Pre(id='relayout-data', style=styles['pre']),
                ]
            )
        ]
    )
])


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_selected_data(relayoutData):
    return json.dumps(relayoutData, indent=2)

@app.callback(
    Output('basic-interactions', 'figure'),
    [Input('basic-interactions', 'relayoutData')],
    [Input('basic-interactions', 'figure')]
)
def update_figure(relayoutData, figure):
    if relayoutData and 'shapes[0].x0' in relayoutData and 'shapes[0].x1' in relayoutData:
        new_x0 = relayoutData['shapes[0].x0']
        new_x1 = relayoutData['shapes[0].x1']

        # Update the shape in the figure with new y0 and y1 values
        figure['layout']['shapes'][0]['x0'] = new_x0
        figure['layout']['shapes'][0]['x1'] = new_x1
        figure['layout']['shapes'][0]['y0'] = 0
        figure['layout']['shapes'][0]['y1'] = 1

    # Update vertical line position based on rectangle's left edge if dragged
    if relayoutData and 'shapes[1].x1' in relayoutData:
        new_x = relayoutData['shapes[1].x1']
        figure['layout']['shapes'][1]['x1'] = new_x
        figure['layout']['shapes'][2]['x0'] = new_x

    if relayoutData and 'shapes[2].x0' in relayoutData:
        new_x = relayoutData['shapes[2].x0']
        figure['layout']['shapes'][1]['x1'] = new_x
        figure['layout']['shapes'][2]['x0'] = new_x

    return figure


if __name__ == '__main__':
    app.run_server(mode='inline', port=8052)
```



### `dcc.Interval`

https://dash.plotly.com/live-updates

### `dcc.Markdown`

### `dcc.Slider`

```python
dcc.Slider(
    min=undefined,
    max=undefined,
    step=undefined,
    marks=undefined,
    value=undefined,
    drag_value=undefined,
    disabled=undefined,
    dots=undefined,
    included=undefined,
    tooltip=undefined,
    updatemode=undefined,
    vertical=undefined,
    verticalHeight=undefined,
    className=undefined,
    id=undefined,
    loading_state=undefined,
    persistence=undefined,
    persisted_props=undefined,
    persistence_type=undefined,
    **kwargs,
)
```

### `dcc.Store`

Sources: https://dash.plotly.com/dash-core-components/store

To access the documentation of this component, we can run ` >>> help(dash_core_components.Store)` in the Python terminal.

#### dcc.Store properties

This component only has a small number of properties:

*   **`id`** (*string*; required). This is the ID of this component, used to identify dash components in callbacks. The ID needs to be unique across all of the components in an app.
*   **`clear_data`** (*boolean*; default`False`). This prob is used to control of removal of the data in the store. We can set it to True in a callback to remove the data contained in`data` property.
*   **`data`** (can be *dict | list | number | string | boolean*; optional). This is the field of the stored data of the store component. Note that we need to use the `id` and the `data` properties together to access the data in a callback.
    *   Note that we can not store a NumPy array or a Pandas dataframe. If we want to store these data type, we need to use catch.
*   **`modified_timestamp`** (*number*; default `-1`). This indicates the last time the storage was modified.
*   **`storage_type`** (one of the following strings: *'local'*, *'session'*, and *'memory'*; default `'memory'`). This is the type of the web storage. The persistence level of these three types is in the decreasing order as listed below.
    *   `'local'` stands for local persistence. The stored data will take the initial data value only the first time the page is loaded and will be kept even after the browser / tab is closed. Of course, its value will be the same when we open another browser / tab with the same web address.
    *   `'session'`, means session persistence. The stored data will take the initial data value when a new session (page) is opened.  Its value will be lost when the browser / tab is closed.
    *   `'memory'`, implies memory persistence. Its value will be reinitialized with a page refresh.

Note that sometimes, the **`local`** persistence can be too strong. For most applications, the default **`memory`** persistence is appropriate.

#### `dcc.Store`'s `data` properties

In Plotly Dash, the `dcc.Store` component is used to store data that can be shared between callbacks or sessions. It can hold any JSON-serializable data type. This includes:

-   Basic data types:
    -   **Numbers**: integers and floating-point numbers.
    -   **Strings**: text data.
    -   **Booleans**: `True` and `False`.
    -   **Null**: represented as `None` in Python.

-  **Complex Data Types**:
    -   **Lists**: arrays of values, which can include any combination of JSON-serializable data types.
    -   **Dictionaries**: key-value pairs, where the keys are strings and the values can be any JSON-serializable data type.
    -   **Nested structures**: combinations of lists and dictionaries containing other lists and dictionaries.

#### Application notes

*   We need to pay attention to the storage limitations. The maximum browser storage space is mainly determined by the application platform: mobile, laptop, or desktop. It is generally safe to store up to 2MB in most environments and up to 5~10MB in most desktop-only applications.
*   The `modified_timestamp` property is read only---cannot be the output of a callback.

#### A simple example to store clicks

```python
from dash import Dash, html, dcc, Output, Input, State, callback
from dash.exceptions import PreventUpdate

# This stylesheet makes the buttons and table pretty.
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # The memory store reverts to the default on every page refresh
    dcc.Store(id='memory'),

    # The local store will take the initial data
    # only the first time the page is loaded
    # and keep it until it is cleared.
    dcc.Store(id='local', storage_type='local'),

    # The session store is the same as the local store but will lose
    # the data when the browser/tab closes.
    dcc.Store(id='session', storage_type='session'),

    html.Table([
        html.Thead([
            html.Tr(html.Th('Click to store in:', colSpan="3")),
            html.Tr([
                html.Th(html.Button('memory', id='memory-btn')),
                html.Th(html.Button('localStorage', id='local-btn')),
                html.Th(html.Button('sessionStorage', id='session-btn'))
            ]),
            html.Tr([
                html.Th('Memory clicks'),
                html.Th('Local clicks'),
                html.Th('Session clicks')
            ])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(0, id='memory-clicks'),
                html.Td(0, id='local-clicks'),
                html.Td(0, id='session-clicks')
            ])
        ])
    ])
])

# Create two callback for every store.
for store in ('memory', 'local', 'session'):
    # add a click to the appropriate store.
    @callback(
        Output(store, 'data'),
        Input('{}-btn'.format(store), 'n_clicks'),
        State(store, 'data')
    )
    def on_click(n_clicks, data):
        if n_clicks is None:
            # prevent the None callbacks is important with the store
            # component. we don't want to update the store for nothing.
            raise PreventUpdate

        # Give a default data dict with 0 clicks if there's no data.
        data = data or {'clicks': 0}
        data['clicks'] = data['clicks'] + 1
        return data

    # output the stored clicks in the table cell.
    @callback(
        Output('{}-clicks'.format(store), 'children'),
        # Since we use the data prop in an output,
        # we cannot get the initial data on load with the data prop.
        # To counter this, you can use the modified_timestamp
        # as Input and the data as State.
        # This limitation is due to the initial None callbacks
        # https://github.com/plotly/dash-renderer/pull/81
        Input(store, 'modified_timestamp'),
        State(store, 'data')
    )
    def on_data(ts, data):
        if ts is None:
            raise PreventUpdate

        data = data or {}
        return data.get('clicks', 0)


if __name__ == '__main__':
    app.run(mode='inline', port=8077)
```

Note that there are some tricks / observations for the callbacks:
*   Several callbacks can have the same function name. This is a type of overload which can be resolved using the callback decorator.
*   Callbacks can be defined in a loop---as long as the loop is run.
*   We can use the output data as the state input to update the output data. This is illustrated in the first callback.

Note also that the `data` property of the `dcc.Store` is used as a state in the second callback. This is designed to show that we can use the `modified_timestamp` property to handle the update. This can have some advantages for some situations, as shown in https://github.com/plotly/dash-renderer/pull/81.  If we want to use the `data` property, we can use the following definition of the callback:
```python
    @app.callback(
        Output('{}-clicks'.format(store), 'children'),
        Input(store, 'data')
    )
    def on_data(data):
        data = data or {}
        return data.get('clicks', 0)
```


## Dash HTML Components

Dash provides HTML components in `dash.html`. A list of all `dash.html` components is given here: https://dash.plotly.com/dash-html-components.

The following are most important.

### `html.Audio`

Documentation can be found at [https://dash.plotly.com/dash-html-components/audio](https://dash.plotly.com/dash-html-components/audio).

#### Example using a local file

Below is an example used to play the audio in `/py-gui/FOIA_LC2_12Z-14Z_7-24-23-short.mp3`.

```python
from dash import Dash, html
from flask import Flask, send_from_directory
import os

server = Flask(__name__)
app = Dash(__name__, server=server)


# Path to your MP3 file
mp3_file_directory = os.path.join(os.getcwd(), 'py-gui')
mp3_file_name = 'FOIA_LC2_12Z-14Z_7-24-23-short.mp3'

# Serve the MP3 file using Flask
@server.route('/py-gui/<filename>')
def serve_mp3(filename):
    return send_from_directory(mp3_file_directory, filename)

app.layout = html.Div([
    html.H1("MP3 Player in Dash"),
    html.Audio(
        controls=True,
        src=f'/py-gui/{mp3_file_name}'
    )
])

if __name__ == '__main__':
    app.run_server(mode='inline', port=8052)
```

This works, but lack the detailed control we need.

#### Example using the in-memory file

```python
import dash
from dash import html
import numpy as np
import io
from scipy.io.wavfile import write
from flask import send_file

# Function to generate a sine wave and return it as a WAV file in memory
def generate_sine_wave():
    sample_rate = 44100  # Samples per second
    duration = 2  # Duration in seconds
    frequency = 440  # Frequency of the sine wave (A4)

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit PCM format

    # Create a BytesIO object to save the WAV file in memory
    byte_io = io.BytesIO()
    write(byte_io, sample_rate, audio_data)  # Write the WAV file to the BytesIO object
    byte_io.seek(0)  # Seek to the start of the BytesIO object

    return byte_io

# Generate the sine wave
wav_io = generate_sine_wave()

# Create the Dash app
app = dash.Dash(__name__)

# Define a route to serve the in-memory WAV file
@app.server.route("/audio/wav")
def serve_wav():
    return send_file(wav_io, mimetype="audio/wav")

app.layout = html.Div(
    [
        html.H1("In-Memory WAV Audio Playback"),
        html.Audio(
            controls=True,
            src="/audio/wav",  # Route to serve the WAV file
            style={"width": "100%"}
        )
    ]
)

if __name__ == "__main__":
    app.run_server(mode='inline', port=8053)
```

#### Controllable properties of `html.Audio`

`html.Audio` has many properties we can use. Below are the ones we are mostly interested in during the application.

-   `src`: Specifies the URL of the audio file.
    -   Example: `audioElement.src = 'audio.mp3';`
-   `currentTime`: Represents the current playback time in seconds. We can use this reading to display a cursor to indicate the current play position.
-   `paused`: Indicates whether the audio is paused (read-only).
    -   Example: `let isPaused = audioElement.paused;`
-   `loop`: Indicates whether the audio should loop after it ends.
    -   Example: `audioElement.loop = true;`
-   `autoplay`: Indicates whether the audio should start playing as soon as it is loaded.
    -   Example: `audioElement.autoplay = true;`
-   `controls`: Indicates whether the browser's default audio controls should be displayed.
    -   Example: `audioElement.controls = true;`
-   `playbackRate`: Controls the speed at which the audio is played, where 1.0 is normal speed.
    -   Example: `audioElement.playbackRate = 1.5;`

### `html.Button`

Documentation can be found at https://dash.plotly.com/dash-html-components/button

#### Basic application

```python
html.Button(children='Submit', id='submit-button-state', n_clicks=0),
```

Note that:

-   `children` is the text to be displayed on the button. This is the first named keyword and the name can be ignored.
-   `id` is a unique string which is used as the name of the button.
-   `n_clicks` will be incremented at each click of the button. It is the value we pass to a callback function when we use this button as an input.

Below is a simple of simple callback function:

```python
@app.callback(Output('output-state', 'children'),
              Input('submit-button', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)
```

Note that sometimes, we can change the parameter `n_clicks` to `no_use` if we don't plan to use this parameter.

#### Determining which button has changed with `dash.ctx`

See [Dash Context `dash.ctx`](py-gui-dash-mg.md#Dash%20Context%20`dash.ctx`).

#### `html.Button`'s properties

The following properties are provided. They are used in order, if possible:

-   **`children`** (*list of or a singular dash component, string or number*; optional): The children of this component.
-   **`id`** (*string*; optional): The ID of this component, used to identify dash components in callbacks. The ID needs to be unique across all of the components in an app.
-   **`n_clicks`** (*number*; default `0`): An integer that represents the number of times that this element has been clicked on.
-   **`n_clicks_timestamp`** (*number*; default `-1`): An integer that represents the time (in ms since 1970) at which `n_clicks` changed. This can be used to tell which button was changed most recently.
-   **`key`** (*string*; optional): A unique identifier for the component, used to improve performance by React.js while rendering components See [https://reactjs.org/docs/lists-and-keys.html](https://reactjs.org/docs/lists-and-keys.html) for more info.
-   **`autoFocus`** (*a value equal to: 'autoFocus', 'autofocus' or 'AUTOFOCUS' | boolean*; optional): The element should be automatically focused after the page loaded.
-   **`disabled`** (*a value equal to: 'disabled' or 'DISABLED' | boolean*; optional): Indicates whether the user can interact with the element.
-   **`form`** (*string*; optional): Indicates the *form* that is the owner of the element.
-   **`formAction`** (*string*; optional): Indicates the action of the element, overriding the action defined in the `form`.
-   **`formEncType`** (*string*; optional): If the button / input is a submit button (type="submit"), this attribute sets the encoding type to use during form submission. If this attribute is specified, it overrides the enctype attribute of the button's form owner.
-   **`formMethod`** (*string*; optional): If the button / input is a submit button (type="submit"), this attribute sets the submission method to use during form submission (GET, POST, etc.). If this attribute is specified, it overrides the method attribute of the button's form owner.
-   **`formNoValidate`** (*a value equal to: 'formNoValidate', 'formnovalidate' or 'FORMNOVALIDATE' | boolean*; optional): If the button / input is a submit button (type="submit"), this boolean attribute specifies that the form is not to be validated when it is submitted. If this attribute is specified, it overrides the novalidate attribute of the button's form owner.
-   **`formTarget`** (*string*; optional): If the button / input is a submit button (type="submit"), this attribute specifies the browsing context (for example, tab, window, or inline frame) in which to display the response that is received after submitting the form. If this attribute is specified, it overrides the target attribute of the button's form owner.
-   **`name`** (*string*; optional): Name of the element. For example used by the server to identify the fields in form submits.
-   **`type`** (*string*; optional): Defines the type of the element.
-   **`value`** (*string*; optional): Defines a default value which will be displayed in the element on page load.
-   **`accessKey`** (*string*; optional): Keyboard shortcut to activate or add focus to the element.
-   **`className`** (*string*; optional): Often used with CSS to style elements with common properties.
-   **`contentEditable`** (*string*; optional): Indicates whether the element's content is editable.
-   **`contextMenu`** (*string*; optional): Defines the ID of a `menu` element which will serve as the element's context menu.
-   **`dir`** (*string*; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left).
-   **`draggable`** (*string*; optional): Defines whether the element can be dragged.
-   **`hidden`** (*a value equal to: 'hidden' or 'HIDDEN' | boolean*; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
-   **`lang`** (*string*; optional): Defines the language used in the element.
-   **`role`** (*string*; optional): Defines an explicit role for an element for use by assistive technologies.
-   **`spellCheck`** (*string*; optional): Indicates whether spell checking is allowed for the element.
-   **`style`** (*dict*; optional): Defines CSS styles which will override styles previously set.
-   **`tabIndex`** (*string*; optional): Overrides the browser's default tab order and follows the one specified instead.
-   **`title`** (*string*; optional): Text to be displayed in a tooltip when hovering over the element.
-   **`loading_state`** (*dict*; optional): Object that holds the loading state object coming from dash-renderer. `loading_state` is a dict with keys:
    -   **`component_name`** (*string*; optional): Holds the name of the component that is loading.
    -   **`is_loading`** (_boolean_; optional): Determines if the component is loading or not.
    -   **`prop_name`** (*string*; optional): Holds which property is loading.

### `html.Div`

Documentation can be found at https://dash.plotly.com/dash-html-components/div

#### Basic application

```python
app.layout = html.Div(children=[
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])
```

Note that the most important keyword argument is **`children`**, a *list of or a singular dash component, string or number*. Note that the keyword is often ignored.

## Dash Mantine Components

Dash Mantine Components (DMC) library is a set of UI components for building interactive web applications in Python using the Plotly Dash framework.

### `dmc.Group`

`dmc.Group` is a layout component that is used to group other components together and control their alignment and spacing.

Key features of `dmc.Group`:

-   **Horizontal Arrangement**: By default, `dmc.Group` arranges its children components horizontally in a row.
-   **Spacing**: You can control the spacing between the child components using the `spacing` prop.
-   **Alignment**: The `align` prop allows you to align the children components vertically within the group.
-   **Positioning**: You can control the horizontal positioning of the children using the `position` prop (e.g., left, center, right).

Main properties of `dmc` includes:

-   **children**: List of Dash components to be grouped.
-   **spacing**: Controls the space between the children. It can be a string (e.g., "xs", "sm", "md", "lg", "xl") or a specific size in pixels.
-   **align**: Vertical alignment of the children. Options include "start", "center", "end".
-   **position**: Horizontal positioning of the children. Options include "left", "center", "right", "apart" (space between).

Example code:
```python
from dash import Dash, html
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = html.Div(
    [
        dmc.Group(
            children=[
                dmc.Button("Button 1"),
                dmc.Button("Button 2"),
                dmc.Button("Button 3")
            ],
            spacing="lg",      # Larger spacing
            align="center",    # Center alignment
            position="center"  # Center positioning
        ),
        dmc.Group(
            children=[
                dmc.Button("Button 4"),
                dmc.Button("Button 5"),
                dmc.Button("Button 6")
            ],
            spacing="sm",     # Smaller spacing
            align="start",    # Start alignment
            position="right"  # Right positioning
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
```

### `dmc.Paper`

`dmc.Paper` is useful for grouping other components together in a visually appealing way, often used to display content in a card format.

Key features of `dmc.Paper`:

-   **Border and Shadow**: `dmc.Paper` comes with configurable border and shadow properties, allowing you to create elevated effects and distinguish sections.
-   **Padding and Radius**: You can set the padding and border radius to control the inner spacing and rounded corners.
-   **Styling**: Easily apply custom styles and themes to match your application’s design.

Properties:

-   **children**: List of Dash components or HTML elements to be placed inside the Paper component.
-   **padding**: Controls the padding inside the Paper. Can be a size value like "xs", "sm", "md", "lg", "xl", or a specific size in pixels.
-   **shadow**: Controls the shadow effect. Can be "xs", "sm", "md", "lg", "xl", or a custom shadow value.
-   **radius**: Controls the border radius (roundness of corners). Can be "xs", "sm", "md", "lg", "xl", or a specific size.
-   **withBorder**: Boolean value to enable or disable the border.
-   **style**: Dictionary for applying custom CSS styles.

### `dmc.ScrollArea`

`dmc.ScrollArea` is useful for creating areas in your Dash application where content can overflow and be scrolled, especially when dealing with large datasets or long lists of items.

Key features of `dmc.ScrollArea`:

-   **Customizable Scrollbars**: You can customize the appearance of the scrollbars to match your application's design.
-   **Horizontal and Vertical Scrolling**: Supports both horizontal and vertical scrolling.
-   **Auto Hide**: Option to auto-hide scrollbars when not in use.
-   **Smooth Scrolling**: Provides smooth scrolling experience for better user interaction.

Properties:

-   **children**: List of Dash components or HTML elements to be placed inside the ScrollArea.
-   **style**: Dictionary for applying custom CSS styles, like height and width.
-   **type**: Type of scrollbar, can be "hover", "scroll", or "always". Default is "hover".
-   **offsetScrollbars**: Boolean to enable or disable offset scrollbars. Default is `False`.
-   **scrollbarSize**: Size of the scrollbar in pixels.
-   **scrollHideDelay**: Delay in milliseconds before hiding the scrollbars when `type` is set to "hover".

### `dmc.Space`

`dmc.Space` is a simple yet useful component that provides an easy way to add vertical or horizontal space between elements in your Dash application. It's particularly helpful for controlling layout spacing without needing to write custom CSS.

## Other Topics

### Dash image annotations

We can use the tricks presented at https://dash.plotly.com/annotations to display and annotate images.

This can be used in the Image processing and computer vision class.

### Dash DataTable

We can use the tricks presented at https://dash.plotly.com/datatable to display data in tables.


### Using data-based audio play

#### Using `sounddevice` to play audio

```python
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt


# Function to convert MP3 to a NumPy array
def mp3_to_np_array(mp3_path):
    audio = AudioSegment.from_mp3(mp3_path)
    samples = np.array(audio.get_array_of_samples())
    sample_rate = audio.frame_rate
    # If stereo, convert to 2D array
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
    return sample_rate, samples

# Load the MP3 file and convert to NumPy array
mp3_file_path = './py-gui/gettysburg_address_16k.mp3'
sample_rate, audio_data = mp3_to_np_array(mp3_file_path)

print(f"{sample_rate = }, {len(audio_data) = }")
print(f"{audio_data.dtype = }")
print(f"{sd.query_devices() = }")

# Normalize audio data to float32 in range [-1, 1]
if audio_data.dtype == np.int16:
    audio_data = audio_data / 32768.0
elif audio_data.dtype == np.int32:
    audio_data = audio_data / 2147483648.0
elif audio_data.dtype == np.uint8:
    audio_data = (audio_data - 128) / 128.0

# # Plot the array
plt.figure(figsize=(10, 4))
# plt.plot(t, amplitude, label='Sine Wave')
plt.plot(audio_data, label='Sine Wave')
plt.show()

# Define playback control variables
start_sample = 0
is_playing = False
stream = None

# sd.play(audio_data, sample_rate)
```

Unfortunately, the return of `sd.query_devices()` is empty. It says, according to the answer at https://stackoverflow.com/questions/75942747/no-mic-get-detected-as-sound-query-devices-returns-empty-list, that installing PortAudio from source will be able to address this problem. Details can be found at https://medium.com/@niveditha.itengineer/learn-how-to-setup-portaudio-and-pyaudio-in-ubuntu-to-play-with-speech-recognition-8d2fff660e94. Need to ask Luke to take a close look.


#### Using PyAudio

```python
import pyaudio
import numpy as np

# Parameters
sample_rate = 44100  # Sample rate
duration = 5.0  # Duration in seconds
frequency = 440.0  # Frequency in Hz

# Generate a sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

# Ensure audio data is in the correct format (16-bit)
audio_data = (audio_data * 32767).astype(np.int16)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                output=True)

# Play the audio data
stream.write(audio_data.tobytes())

# Close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
```

Unfortunately, PyAudio does not install due to the missing of a header file. Need to figure this out.

Here are the steps used to install pyaudio:

-   `sudo apt install python3-pyaudio`
-   `sudo apt install portaudio19-dev`
-   `poetry add pyaudio`

Still cannot find the audio device.

<!-- bgn hidden -->

### Ideas for an app

Ideas for an app for class activity and attendance. The app can be named as classivity.

-   There will be three tabs
    -   Class activity
    -   Attendance
    -   Pop quiz (future; not sure how to connect to user yet)

-   Attendance tab can be used to take attendance quickly. Each student will be listed in name and a number. Date and time will be populated automatically. We will be able to save the attendance so that a table can be generated.
-   Class activity tab will have a check box so that we can choose multiple volunteers. There should be buttons to select or deselect all. Only selected students will be randomly picked up. There should be a group of radio buttons to select the points: A, B, and C. The probability of picking up a student is related to the number of participations. We should be able to see the number of participations in a file, which is posted online. Even better, we can share this file in google drive so that students can see it in real time.

Here are some of the ideas we need to play:

-   https://stackoverflow.com/questions/53917648/plotly-dash-create-multiple-callbacks-with-loop
-   https://community.plotly.com/t/for-loop-with-callback/64731/2
-   https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

<!-- end hidden -->
