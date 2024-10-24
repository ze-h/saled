<!--
Note info:

-   Creator: jhl
-   Created on: 9/17/2022
-   Last modified on: 2/29/2024

-->

<!-- bgn cli -->

# Command-line instructions

```sh
pandoc -N -V fontsize=11pt "plotly-dash--cheatsheet.md" -o "../salai/cec595/plotly-dash--cheatsheet.pdf" --data-dir=../../a5ar/pandoc -L select-blocks.lua -M blocks2select="nil" -L output2verbatim.lua --template=eagle.tex -V linestretch=1.1 -V verbatim-in-note -V codefontsize=9.5 -M geometry="top=2.7cm, bottom=2.8cm, left=2.5cm, right=2.4cm, headsep=0.3cm, footskip=0.9cm" --listings --filter pandoc-crossref -M listings -M titleblock --toc -M title="Cheatsheet of Plotly Dash" -M author="Jianhua Liu" -M date="Spring 2024"
```

```sh
pandoc -N -V fontsize=11pt "plotly-dash--cheatsheet.md" -o "../salai/cec595/plotly-dash--cheatsheet.tex" --data-dir=../../a5ar/pandoc -L select-blocks.lua -M blocks2select="nil" -L output2verbatim.lua --template=eagle.tex -V linestretch=1.1 -V verbatim-in-note -V codefontsize=9.5 -M geometry="top=2.7cm, bottom=2.8cm, left=2.5cm, right=2.4cm, headsep=0.3cm, footskip=0.9cm" --listings --filter pandoc-crossref -M listings -M titleblock --toc -M title="Cheatsheet of Plotly Dash" -M author="Jianhua Liu" -M date="Spring 2024"
```

<!-- end cli -->

<!-- bgn tags -->

Tags: #playGround, #PlotlyDash

<!-- end tags -->

<!-- bgn hidden -->

```toc
style: number
min_depth: 1
max_depth: 6
```

<!-- end hidden -->

<!-- bgn ch-title -->

# A MiniGuide to Plotly Dash

<!-- end ch-title -->

## Introduction

### What is Plotly Dash

Dash is a low-code framework for rapidly building interactive data visualization apps in Python and several other languages. Written on top of Plotly.js and React.js, Dash is ideal for building and deploying data apps with customized user interfaces. It's particularly suited for anyone who works with data.

Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build a full-stack web app with interactive data visualization.

Dash is simple enough that you can bind a user interface to your code quickly.

Dash apps are rendered in the web browser. You can deploy your apps to VMs or Kubernetes clusters and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.

There is a lot behind the framework. To learn more about how it is built and what motivated Dash, read:

-   [Introducing Dash. Create Reactive Web Apps in pure Python](https://medium.com/plotly/introducing-dash-5ecf7191b503) or
-   [Dash is React for Python, R, and Julia](https://medium.com/plotly/dash-is-react-for-python-r-and-julia-c75822d1cc24).

Dash is an *open source* library released under the permissive MIT license. Plotly develops Dash and also offers a platform for writing and deploying Dash apps in an enterprise environment.

### References

-   This is a simplified introduction to Plotly Dash based on [Introduction | Dash for Python Documentation | Plotly](https://dash.plotly.com/introduction), where we can find the index of all the document of Dash.
-   Here is a link for the Real Python tutorial on Dash: https://realpython.com/python-dash/
-   Here is the link for the Dash cheatsheet: [Dash Club Cheat Sheet - Google Docs](https://docs.google.com/document/d/15P9TIIxKHujkesBnYL_4nLU3Pr9AEKw12Ov-X1Bca7s/edit)

## Installation of Dash

Official instruction for installing Dash is given at [Installation | Dash for Python Documentation | Plotly](https://dash.plotly.com/installation). 

For us, we use virtual envs created by conda which has Poetry installed. Hence, we can use the following to install all the packages we use:
```sh
poetry add jupyterlab jupytext ipywidgets
poetry add pandas
poetry add dash dash-bootstrap-components dash-mantine-components flask-caching redis jupyter-dash 
```

Note that Jupyter-dash is deprecated, and we don't need to install it in the future.

To run the code below, we need to use the `salcls11` or `salai11` env.

To check the version of Dash, run the following code:
```python
import dash
print(dash.__version__)
```

## Running a Dash app

There are two approaches to run a Dash-based app:

-   Running it as a normal Python script.
-   Running it in Jupyter Lab.

The difference is that for the former, we normally invoke the app via 
```python
if __name__ == '__main__':
   app.run_server(debug=True)
```
and for the latter, we invoke it using
```python
if __name__ == '__main__':
   app.run_server(mode='inline')
```

There are a number of options in `app.run_server()`:

-   `app.run_server(mode='jupyterlab')`: display the result in a new tab. Due to compatibility issues, this does not always work. See https://github.com/plotly/jupyter-dash/issues/43.
-   `app.run_server(mode='inline')`: display the result inline.
-   `app.run_server(mode='external')`: display the result externally by hitting the given link below the code cell.

Note that:

-   We prefer to use the `external` mode for larger apps. Yet, with this mode, hot-reloading does not seem to work.
-   To stop the server, we need to click Kernel >> Restart Kernel ....

To stop the server, just press Ctrl + C.

## Getting started with Dash and Plotly

The following Dash apps are adapted from [Dash in 20 Minutes Tutorial | Dash for Python Documentation | Plotly](https://dash.plotly.com/tutorial)

### Hello world

```python
from dash import Dash, html

app = Dash()

app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(mode='inline')
```

Note that:

-   The above `app.layout` is created as a list, although it only has one item, the `html.Div` component.
-   The `html.Div` component has a few properties, and property `childern` is used to add text content to the page.

### Connecting to data

There are many ways to add data to an app, including using APIs, external databases, local `.txt` files, JSON files, and more. Below, we will highlight one of the most common ways of incorporating data from a CSV sheet.

```python
# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15)
]

# Run the app
if __name__ == '__main__':
    app.run(mode='inline')
```

### Visualizing data

The Plotly graphing library has more than [50 chart types](https://plotly.com/python/) to choose from. In this example, we will make use of the histogram chart.

```python
# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15),
    dcc.Graph(figure=px.histogram(
        df, 
        x='continent', 
        y='lifeExp', 
        histfunc='avg'
    ))
]

# Run the app
if __name__ == '__main__':
    app.run(mode='inline')
```

Note:

-   The `dcc` module contains Dash Core Components, which include the `Graph` component. `dcc.Graph` is used to render interactive graphs.
-   The figure is generated by using the `plotly.express` library.

### Controls and callbacks

In this example we will add radio buttons to the app layout. Then, we will build the callback to create the interaction between the radio buttons and the histogram chart.

```python
# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], 
                   value='lifeExp', 
                   id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
]

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', 
           component_property='figure'),
    Input(component_id='controls-and-radio-item', 
          component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(mode='inline')
```

Notes:

-   Both the `RadioItems` and the `Graph` components were given `id` names: these will be used by the **callback** to identify the components.
-   **The inputs and outputs of our app are the properties of a particular component**. In this example, our input is the `value` property of the component that has the ID `"controls-and-radio-item"`. If you look back at the layout, you will see that this is currently `lifeExp`. Our output is the `figure` property of the component with the ID `"controls-and-graph"`, which is currently an empty dictionary (empty graph).
-   There are three pieces of the callback function:
    -   The callback function's argument `col_chosen` refers to the component property of the input `lifeExp`. 
    -   We build the histogram chart inside the callback function, assigning the chosen radio item to the y-axis attribute of the histogram. This means that every time the user selects a new radio item, the figure is rebuilt and the y-axis of the figure is updated.
    -   We return the histogram at the end of the function. This assigns the histogram to the `figure` property of the `dcc.Graph`, thus displaying the figure in the app.

### Another Dash app with callback

The app below is adapted from the one shown at [A Minimal Dash App | Dash for Python Documentation | Plotly](https://dash.plotly.com/minimal-app). 

```python
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder_unfiltered.csv')

app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(figure={}, id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(mode='inline')
```

Note that we have omitted the names of the ID and Property parameters in the Output and Inputs of the callback function. 

## Styling the apps

The examples in the previous section used Dash HTML Components to build a simple app layout, but you can style your app to look more professional. This section will give a brief overview of the multiple tools that you can use to enhance the layout style of a Dash app:

-   HTML and CSS
-   Dash Design Kit (DDK)
-   Dash Bootstrap Components
-   Dash Mantine Components

Below, we will illustrate how to use HTML and CSS as well as Dash Bootstrap Components. We will not run the following two here:

-   Dash Design Kit requires a Dash Enterprise license. So we cannot run it freely. 
-   Dash Mantine Components has changed the API and the provided demo does not run with the newest version of the package. We will use a separate section later for this package.

### HTML and CSS

HTML and CSS are the lowest level of interface for rendering content on the web. The HTML is a set of components, and CSS is a set of styles applied to those components. CSS styles can be applied within components via the `style` property, or they can be defined as a separate CSS file in reference with the `className` property, as in the example below.

```python
# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

# App layout
app.layout = [
    html.Div(
        className='row', 
        children='My First App with Data, Graph, and Controls',
        style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}
    ),

    html.Div(
        className='row', 
        children=[dcc.RadioItems(
            options=['pop', 'lifeExp', 'gdpPercap'],
            value='lifeExp',
            inline=True,
            id='my-radio-buttons-final'
        )]
    ),

    html.Div(
        className='row', 
        children=[
            html.Div(
                className='six columns', 
                children=[
                    dash_table.DataTable(
                        data=df.to_dict('records'), 
                        page_size=11, 
                        style_table={'overflowX': 'auto'}
                    )
                ]
            ),
            html.Div(
                className='six columns', 
                children=[dcc.Graph(figure={}, id='histo-chart-final')]
            )
        ]
    )
]

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', 
           component_property='figure'),
    Input(component_id='my-radio-buttons-final', 
          component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(mode='inline')
```

### Dash Bootstrap Components

Dash Bootstrap is a community-maintained library built off of the bootstrap component system. Although it is not officially maintained or supported by Plotly, Dash Bootstrap is a powerful way of building elegant app layouts. Notice that we first define a row and then the width of columns inside the row, using the `dbc.Row` and `dbc.Col` components.

For the app below to run successfully, make sure to install the Dash Bootstrap Components library: `pip install dash-bootstrap-components`

Read more about the Dash Bootstrap Components in the [third-party documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/).

```python
# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Incorporate data
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container([
    dbc.Row([
        html.Div(
            'My First App with Data, Graph, and Controls', 
            className="text-primary text-center fs-3"
        )
    ]),

    dbc.Row([
        dbc.RadioItems(
            options=[{"label": x, "value": x} for x in \
                     ['pop', 'lifeExp', 'gdpPercap']],
            value='lifeExp',
            inline=True,
            id='radio-buttons-final'
        )
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                data=df.to_dict('records'), 
                page_size=12, 
                style_table={'overflowX': 'auto'}
            )
        ], width=6),

        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final')
        ], width=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='my-first-graph-final', 
           component_property='figure'),
    Input(component_id='radio-buttons-final', 
          component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(mode='inline')
```

## Dash Mantine Components

This section will be detailed later.

### Modified Dash Mantine Components example 

Dash Mantine is a community-maintained library built off of the Mantine component system. Although it is not officially maintained or supported by the Plotly team, Dash Mantine is another powerful way of customizing app layouts. The Dash Mantine Components uses the Grid module to structure the layout. Instead of defining a row, we define a `dmc.Grid`, within which we insert `dmc.Col`s and define their width by assigning a number to the `span` property.

For the app below to run successfully, make sure to install the Dash Mantine Components library: `pip install dash-mantine-components==0.12.1`

Read more about the Dash Mantine Components in the [third-party documentation](https://www.dash-mantine-components.com/).

```python
from dash import Dash, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master'
df = pd.read_csv(data_url + '/gapminder2007.csv')

app = Dash()

app.layout = dmc.Container([
    dmc.Title(
        'My First App with Data, Graph, and Controls', 
        #color="blue", 
        size="h3"
    ),
    dmc.RadioGroup(
        [dmc.Radio(i, value=i) for i in  \
                 ['pop', 'lifeExp', 'gdpPercap']],
        id='my-dmc-radio-item',
        value='lifeExp',
        size="sm"
    ),
    dmc.Grid([
        dmc.GridCol([
            dash_table.DataTable(
                data=df.to_dict('records'), 
                page_size=12, 
                style_table={'overflowX': 'auto'}
            )
        ], span=6),
        dmc.GridCol([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

@callback(
    Output(component_id='graph-placeholder', 
           component_property='figure'),
    Input(component_id='my-dmc-radio-item', 
          component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(mode='inline')
```


---


## Dash Layout

This is a simplified version of the online tutorial for Dash layout: [Layout | Dash for Python Documentation | Plotly](https://dash.plotly.com/layout). 

Dash apps are composed of two parts. The first part is the **layout** of the app, which describes what the application looks like. The *layout* of a Dash app describes what the app looks like. The layout is a hierarchical tree of components. Dash HTML Components (`dash.html`) provides classes for all of the HTML tags and the keyword arguments describe the HTML attributes like style, class, and id. Dash Core Components (`dash.dcc`) generates higher-level components like controls and graphs.

The second part describes the **interactivity** of the application and will be covered in the **callback** section below

### A simple layout app

```python
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

app.run_server(mode='inline')
```

Note:

-   The *layout* is composed of a tree of *components*, including `html.Div` and `dcc.Graph`.
-   The Dash HTML Components module (`dash.html`) has a component for every HTML tag. The `html.H1(children='Hello Dash')` component generates a `<h1>Hello Dash</h1>` HTML element in the application.
-   Not all components are pure HTML. The Dash Core Components module, `dash.dcc`, contains higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library.
-   Each component is described entirely through keyword attributes. Dash is declarative: we will primarily describe our application through these attributes.
-   The `children` property is special. By convention, it's always the first attribute: `html.H1(children='Hello Dash')` is the same as `html.H1('Hello Dash')`. It can contain a string, a number, a single component, or a list of components.
-   The fonts in the application will look a little bit different than what is displayed here. This application is using a custom CSS stylesheet and Dash Enterprise Design Kit to modify the default styles of the elements.

### More about HTML components

As mentioned before, Dash HTML Components (`dash.html`) contains a component class for every HTML tag. It also contains keyword arguments for all of the HTML arguments.

```python
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            children='Dash: A web application framework for your data.',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        dcc.Graph(
            id='example-graph-2',
            figure=fig
        )
    ]
)

app.run_server(mode='inline')
```

In this example, we modified the inline styles of the `html.Div` and `html.H1` components with the `style` property.

```
html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'})
```

The above code is rendered in the Dash application as `<h1 style="text-align: center; color: #7FDBFF">Hello Dash</h1>`.

There are a few important differences between the `dash.html` and the HTML attributes:

-   The `style` property in HTML is a semicolon-separated string. In Dash, we can just supply a dictionary.
-   The keys in the `style` dictionary are *camelCased*. So, instead of `text-align`, it is `textAlign`.
-   The HTML `class` attribute is `className` in Dash. 
-   The children of the HTML tag is specified through the `children` keyword argument. By convention, this is always the `first` argument and so it is often omitted.

Besides that, all of the available HTML attributes and tags are available to us in the Python context.

### Reusable components

By writing our markup in Python, we can create complex reusable components like tables without switching contexts or languages.

```python
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in \
                        dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

app.run_server(mode='inline')
```

### More about visualization

The Dash Core Components module (`dash.dcc`) includes a component called `Graph`.

Graph renders interactive data visualizations using the open source plotly.js JavaScript graphing library. Plotly.js supports over 35 chart types and renders charts in both vector-quality SVG and high-performance WebGL.

The figure argument in theGraph component is the same figure argument that is used by plotly.py, Plotly's open source Python graphing library. Check out the plotly.py documentation and gallery to learn more.

Here's an example that creates a scatter plot from a Pandas dataframe. Create a file named app.py with the following code:

```python
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

app.run_server(mode='inline')
```

These graphs are interactive and responsive. Hover over points to see their values, click on legend items to toggle traces, click and drag to zoom, hold down shift, and click and drag to pan.

### Markdown

While Dash exposes HTML through Dash HTML Components (`dash.html`), it can be tedious to write text in HTML. *For writing blocks of text*, we can use the `Markdown` component in Dash Core Components (`dash.dcc`).

```python
from dash import Dash, html, dcc

app = Dash(__name__)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

app.run_server(mode='external')
```

### Dash Core Components

Dash Core Components (`dash.dcc`) includes a set of higher-level components like dropdowns, graphs, markdown blocks, and more.

Like all Dash components, they are described entirely declaratively. Every option that is configurable is available as a keyword argument of the component.

We can view all of the available components in the [Dash Core Components Gallery](https://dash.plotly.com/dash-core-components).

Here are a few of the available components.

```python
from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'],
                     ['Montreal', 'San Francisco'],
                     multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montreal', 'San Francisco'],
                      ['Montreal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

app.run_server(mode='external')
```

### Getting help with layout

Dash components are declarative: every configurable aspect of these components is set during instantiation as a keyword argument.

There are two easy approaches to get help:

-   In a Python console, call help on any of the components. `help(dcc.Dropdown)`
-   In a Jupyter Lab cell, type `dcc.Dropdown??`

## Dash callbacks

This is a simplified version of the online tutorial for Dash callback: https://dash.plotly.com/basic-callbacks. 

Earlier, we have discussed the layout of a Dash app. 

Here, we discuss how to make our Dash apps interactive by using *callback functions*, which are Python functions automatically called by Dash whenever an *input* component's property changes. This will update some property of the *output* component(s).

Let's get started with a simple example of an interactive Dash app.

### A simple interactive Dash app

```python
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

app.run_server(mode='inline')
```

Let's break down this example:

-   The "inputs" and "outputs" of our application's interface are described declaratively as the arguments of the `@app.callback` decorator. Here are some details of this decorator and the decorated function, the callback function.
    -   By using this decorator, we're telling Dash to call the callback function for us whenever the value of the *input* component (the text box) changes. This way, we can update the children of the *output* component on the page (the `html.Div` field).
    -   We can use any name for the callback function. The convention is to use a name that well *describes* the callback output(s).
    -   We can use any name for the callback function's arguments, but we must use the same names inside the callback function as we do in its definition, just like in a regular Python function. The arguments are positional by default: first the `Input` items and then any `State` items are given in the same order as in the decorator. However, we can also use named keyword arguments, as shown in https://dash.plotly.com/flexible-callback-signatures.
    -   We must use the same `id` we gave a Dash component in the `app.layout` code when referring to it as either an input or output of the `@app.callback` decorator.
    -   The `@app.callback` decorator needs to be directly above the callback function declaration. If there is a blank line between the decorator and the callback function definition, the callback registration will not be successful.
-   In Dash, the inputs and outputs of our callback function are simply **the properties of a particular component**. In this example, our input is the `value` property of the component that has the ID `my-input`. Our output is the `children` property of the component with the ID `my-output`.
-   Whenever an input property changes, the call function will get called automatically. Dash provides the function with the new value of the input property as an input argument and updates the property of the output component with whatever was returned by the function.
-   The `component_id` and `component_property` keywords are optional (there are only two arguments for each of those objects). They are included in this example for clarity but will be omitted in the rest of the documentation for the sake of brevity and readability.
-   Don't confuse the `dash.Input` object with the `dash_core_components.Input` object. The former is just used in these callbacks and the latter is an actual component.
-   Notice how we don't set a value for the `children` property of the `my-output` component in the `layout`. When the Dash app starts, it automatically calls all of the callbacks with the initial values of the input components in order to populate the initial state of the output components. In this example, if we specified something like `html.Div(id='my-output', children='Hello world')`, it would get overwritten when the app starts.

This type of programing is like programming with Microsoft Excel: whenever an input cell changes, all of the cells that depend on that cell will get updated automatically. This is called "Reactive Programming".

Recall that every component is described entirely through its set of keyword arguments. Those properties are important now. With Dash interactivity, we can dynamically update any of those properties through a callback function. Frequently we'll update

-   the `children` of a component to display new text,
-   the `figure` of a `dcc.Graph` component to display new data in figure,
-   the `style` of a component, or even
-   the available `options` of a `dcc.Dropdown` component.

Let's take a look at another example where a `dcc.Slider` updates a `dcc.Graph`.

### A Dash app layout with figure and slider

```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),

    dcc.Slider(
        min=df['year'].min(),
        max=df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider',
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(
        filtered_df, x="gdpPercap", y="lifeExp",
        size="pop", color="continent", hover_name="country",
        log_x=True, size_max=55
    )

    fig.update_layout(transition_duration=500)

    return fig

app.run_server(mode='inline')
```

In this example, the `value` property of the `Slider` is the input to the callback function, and the output is the `figure` property of the `Graph`. Whenever the `value` of the `Slider` changes, Dash calls the callback function `update_figure` with the new value. The function filters the DataFrame object with this new value, constructs a `figure` object, and returns it to the Dash application.

There are a few patterns in this example:

-   We're using the [Pandas](http://pandas.pydata.org/) library for importing and filtering datasets in memory. We load our dataframe with `df = pd.read_csv('...')`. This dataframe `df` is in the global state of the app and can be read inside the callback functions.
-   Loading data into memory can be expensive. By loading querying data at the start of the app instead of inside the callback functions, we ensure that this operation is only done when the app server starts. When a user visits the app or interacts with the app, that data (`df` ) is already in memory. If possible, expensive initialization (like downloading or querying data) should be done in the global scope of the app instead of within the callback functions.
-   The callback function does not modify the original data, it just creates copies of the dataframe by filtering through pandas filters.
    -   As a rule of thumb, *the callbacks should not mutate variables outside of their scope*. (If the callbacks modify global state, then one user's session might affect the next user's session and when the app is deployed on multiple processes or threads, those modifications will not be shared across sessions.)
    -   **In some cases, we need to change the value of a global variable to simplify the flow of the program. In this case, we need to clearly indicate so in the name of the callback function**.
-   We are turning on transitions with `layout.transition` to give an idea of how the dataset evolves with time: transitions allow the chart to update from one state to the next smoothly, as if it were animated.

### A Dash app with multiple inputs

In Dash, any `Output` can have multiple `Input` components. Here's a simple example that binds five Inputs (the `value` property of 2 `Dropdown` components, 2 `RadioItems` components, and 1 `Slider` component) to 1 Output component (the `figure` property of the `Graph` component). Notice how the `app.callback` lists all five `Input` inside a list in the second argument.

```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                options=df['Indicator Name'].unique(),
                value='Fertility rate, total (births per woman)',
                id='xaxis-column',
            ),
            dcc.RadioItems(
                options=['Linear', 'Log'],
                value='Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                options=df['Indicator Name'].unique(),
                value='Life expectancy at birth, total (years)',
                id='yaxis-column',
            ),
            dcc.RadioItems(
                options=['Linear', 'Log'],
                value='Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        min=df['Year'].min(),
        max=df['Year'].max(),
        step=None,
        id='year--slider',
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
    )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type, year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(
        x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
        y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
        hover_name=dff[dff['Indicator Name'] == yaxis_column_name]\
                ['Country Name']
    )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                      hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


app.run_server(mode='inline')
```

In this example, the `update_graph` function gets called whenever the `value` property of the `Dropdown`, `Slider`, or `RadioItems` components change.

The input arguments of the `update_graph` function are the new or current value of each of the `Input` properties, in the order that they were specified.

Even though only a single `Input` changes at a time (a user can only change the value of a single Dropdown in a given moment), Dash collects the current state of all of the specified `Input` properties and passes them into the callback function. The callback functions are always guaranteed to be passed the representative state of the app.

Let's extend our example to include multiple outputs.

### A Dash app with multiple outputs

So far all the callbacks we've written only update a single `Output` property. We can also update several at once: list all the properties we want to update in `app.callback` and return that many items from the callback. This is particularly useful if two outputs depend on the same computationally intense intermediate result, such as a slow database query.

```python
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])

@app.callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value'))
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x

app.run_server(mode='inline')
```

A word of caution: it's not always a good idea to combine Outputs, even if we can:

-   If the Outputs depend on some but not all of the same Inputs, keeping them separate can avoid unnecessary updates.
-   If they have the same Inputs but do independent computations with these inputs, keeping the callbacks separate can allow them to run in parallel.

### A Dash app with chained callbacks

We can also chain outputs and inputs together: the output of one callback function could be the input of another callback function.

This pattern can be used to create dynamic UIs where one input component updates the available options of the next input component. Here's a simple example.

```python
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montreal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(
        options=list(all_options.keys()),
        value='America',
        id='countries-radio',
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': city, 'value': city}
            for city in all_options[selected_country]]

@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )


app.run_server(mode='inline')
```

The first callback updates the available options in the second `RadioItems` component based on the selected value in the first `RadioItems` component.

The second callback sets an initial value when the `options` property changes: it sets it to the first value in that `options` array.

The final callback displays the selected `value` of each component. If we change the `value` of the countries `RadioItems` component, Dash will wait until the `value` of the cities component is updated before calling the final callback. This prevents the callbacks from being called with inconsistent state like with`"America"`and`"Montreal"`.

### A Dash app with state

In some cases, you might have a "form"-type pattern in your application. In such a situation, you might want to read the value of the input component, but only when the user is finished entering all their information in the form.

Attaching a callback to the input values directly can look like this:

```python
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="Montreal"),
    dcc.Input(id="input-2", type="text", value="Canada"),
    html.Div(id="number-output"),
])


@app.callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value"),
)
def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)


app.run_server(mode='inline')
```

In this example, the callback function is fired whenever any of the attributes described by `Input` change.

`State`allows us to pass along extra values without firing the callbacks. Here's the same example as above but with the `dcc.Input` as `State` and a new button component as an `Input`.

```python
from dash import Dash, dcc, html, Input, Output, State
# import dash_design_kit as ddk

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value')
)
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


app.run_server(mode='inline')
```

In this example, changing text in the `dcc.Input` boxes won't fire the callback but clicking on the **Submit** button will. The current values of the `dcc.Input` values are still passed into the callback even though they don't trigger the callback function itself.

Note that we're triggering the callback by listening to the `n_clicks` property of the `html.Button` component. `n_clicks` is a property that gets incremented every time the component has been clicked on. It is available in every component in Dash HTML Components (`dash.html`), but most useful with buttons.

### Passing components into callbacks instead of IDs

When creating app layouts in earlier examples, we assigned IDs to components within the layout and later referenced these in callback inputs and outputs.

In the first example, there is a `dcc.Input` component with the id `my-input` and a `html.Div` with the `id` being `my-output`.

We can also provide components directly as inputs and outputs without adding or referencing an `id`. Dash autogenerates IDs for these components.

Here is the first example again. Prior to declaring the app layout, we create two components, assigning each one to a variable. We then reference these variables in the layout and pass them directly as inputs and outputs to the callback.

```python
from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

my_input = dcc.Input(value='initial value', type='text')
my_output = html.Div()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        my_input
    ]),

    html.Br(),
    my_output
])

@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


app.run_server(mode='inline')
```

In Python 3.8 and higher, you can use the walrus operator (https://realpython.com/python-walrus-operator/) to declare the component variables within the app layout:

```python
from jupyter_dash import JupyterDash
from dash import dcc, html, Input, Output, callback

app = JupyterDash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        my_input := dcc.Input(value='initial value', type='text')
    ]),

    html.Br(),
    my_output := html.Div(),
])

@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


app.run_server(mode='external')
```

Note: Auto component IDs won't work with dynamic callback content unless the component variables are defined out of the callback scope. Additionally, they are not compatible with Pattern-Matching Callbacks.

### Summary

We've covered the fundamentals of callbacks in Dash. Dash apps are built on a set of simple but powerful principles: UIs that are customizable through reactive callbacks. Every attribute/property of a component can be modified as the output of a callback, while a subset of the attributes (such as the `value` property of the `dcc.Dropdown` component) are editable by the user through interacting with the page.

## Interactive graphing and crossfiltering

See https://dash.plotly.com/interactive-graphing.

## Sharing data between callbacks

We have mentioned that **Dash Callbacks must never modify variables outside of their scope** (unless clearly labeled using the name of the callback to warning the developer). It is not safe to modify any global variables. This chapter explains why and provides some alternative patterns for sharing state between callbacks.

### Why sharing states?

In some apps, you may have multiple callbacks that depend on expensive data processing tasks like making database queries, running simulations, or downloading data.

Rather than having each callback run the same expensive task, you can have one callback run the task and then share the results with the other callbacks.

One way to achieve this is by having [multiple outputs](https://dash.plotly.com/basic-callbacks) for one callback: the expensive task can be done once and immediately used in all the outputs. For example, if some data needs to be queried from a database and then displayed in both a graph and a table, then you can have one callback that calculates the data and creates both the graph and the table outputs.

But sometimes having multiple outputs in one callback isn't a good solution. For example, suppose your **temperature handling** app allows a user to select a date and a unit (Fahrenheit or Celsius) of the temperature, and then displays the temperature for that day. You could have one callback that outputs the temperature by taking both the date and the temperature unit as inputs, but this means that if the user merely changes from Fahrenheit to Celsius, then the weather data would have to be re-downloaded, which can be time consuming. Instead, it can be more efficient to have two callbacks: one callback that fetches the weather data, and another callback that outputs the temperature based on the downloaded data. This way, when only the unit is changed, the data does not have to be downloaded again. This is an example of **sharing** a variable, or state, between callbacks.

### Dash is stateless

Dash was designed to be a **stateless** framework.

Stateless frameworks are more scalable and robust than stateful ones. Most websites that you visit are running on stateless servers.

They are more scalable because it's trivial to add more compute power to the application. In order to scale the application to serve more users or run more computations, run more "copies" of the app in separate processes.

In production, this can be done either with `gunicorn`'s worker command:
```
gunicorn app:server --workers 8
```
or by running the app in multiple Docker containers or servers and load balancing between them.

Stateless frameworks are more robust because even if one process fails, other processes can continue serving requests. In Dash Enterprise Kubernetes, these containers can run on separate servers or even separate regions, providing resiliency against server failure.

With a stateless framework, user sessions are not mapped 1-1 with server processes. Each callback request can be executed on _any_ of the available processes. `gunicorn` will check which process isn't busy running a callback and send the new callback request to that process. This means that a few processes can balance the requests of 10s or 100s of concurrent users so long as those requests aren't happening at _the exact same time_ (they usually don't!).

### Why global variables will break your app

Dash is designed to work in multi-user environments where multiple people view the application at the same time and have **independent sessions**.

If your app uses and modifies a global variable, then one user's session could set the variable to some value which would affect the next user's session.

Dash is also designed to be able to run with **multiple workers** so that callbacks can be executed in parallel.

This is commonly done with `gunicorn` using syntax like

```shell
$ gunicorn --workers 4 app:server
```

(`app` refers to a file named `app.py` and `server` refers to a variable in that file named `server`: `server = app.server`).

When Dash apps run across multiple workers, their memory _is not shared_. This means that if you modify a global variable in one callback, that modification will not be applied to the other workers / processes.

Here is a sketch of an app that will _not work reliably_ because the callback modifies a global variable, which is outside of its scope.

```python
df = pd.DataFrame({
    'student_id' : range(1, 11),
    'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	global df
	df = df[df['score'] == value]
	return len(df)
```

The callback returns the correct output the very first time it is called, but once the global `df` variable is modified, any subsequent callback that uses that dataframe is not using the original data anymore.

To improve this app, reassign the filtered dataframe to a new variable inside the callback as shown below, or follow one of the strategies outlined in the next parts of this guide.

```python
df = pd.DataFrame({
    'student_id' : range(1, 11),
    'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
    dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	filtered_df = df[df['score'] == value]
	return len(filtered_df)
```

### Storing shared data

To share data safely across multiple processes or servers, we need to store the data somewhere that is accessible to each of the processes.

There are three places you can store this data:

-   In the user's browser session, using [dcc.Store](https://dash.plotly.com/dash-core-components/store).
-   On the disk (e.g. in a file or database).
-   In server-side memory (RAM) shared across processes and servers such as a Redis database. 
    -   Dash Enterprise includes [onboard, one-click Redis databases](https://dash.plotly.com/dash-enterprise/redis-database) for this purpose.

The following examples illustrate some of these approaches.

#### Example 1 - Storing data in the browser with `dcc.Store`

To save data in the user's browser's session:

-   The data has to be converted to a string like JSON or base64 encoded binary data for storage.
-   Data that is cached in this way will _only be available in the user's current session_.
-   If you open up a new browser window, the app's callbacks will always re-compute the data. The data is only cached between callbacks within the same session.
-   This method doesn't increase the memory footprint of the app.
-   There could be a cost in network traffic. If you're sharing 10MB of data between callbacks, then that data will be transported over the network between each callback.
-   If the network cost is too high, then compute the aggregations upfront and transport those. Your app likely won't be displaying 10MB of data, it will just be displaying a subset or an aggregation of it.

The example below shows one of the common ways you can leverage `dcc.Store`: if processing a dataset takes a long time and different outputs use this dataset, `dcc.Store` can be used to store the processed data as an _intermediate value_ that can then be used as an input in multiple callbacks to generate different outputs. This way, the expensive data processing step is only performed once in one callback instead of repeating the same expensive computation multiple times in each callback.

```python
app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),

    # dcc.Store stores the intermediate value
    dcc.Store(id='intermediate-value')
])

@callback(
    Output('intermediate-value', 'data'), 
    Input('dropdown', 'value')
)
def clean_data(value):
     # some expensive data processing step
     cleaned_df = slow_processing_step(value)

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return cleaned_df.to_json(date_format='iso', orient='split')

@callback(Output('graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data)
    dff = pd.read_json(jsonified_cleaned_data, orient='split')

    figure = create_figure(dff)
    return figure

@callback(
    Output('table', 'children'), 
    Input('intermediate-value', 'data')
)
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    table = create_table(dff)
    return table
```

Notice that the data needs to be serialized into a JSON string before being placed in storage. Also note how the processed data gets stored in `dcc.Store` by assigning the data as its output, and then the same data gets used by multiple callbacks by using the same `dcc.Store` as an input.

#### Example 2 - Computing aggregations upfront

Sending the computed data over the network can be expensive if the data is large. In some cases, serializing this data to JSON can also be expensive.

In many cases, your app will only display a subset or an aggregation of the processed data. In these cases, you could precompute the aggregations in your data processing callback and transport these aggregations to the remaining callbacks.

Here's a simple example of how you might transport filtered or aggregated data to multiple callbacks, again using the same `dcc.Store`.

```python
@callback(
    Output('intermediate-value', 'data'),
    Input('dropdown', 'value')
)
def clean_data(value):
     cleaned_df = slow_processing_step(value)

     # a few filter steps that compute the data
     # as it's needed in the future callbacks
     df_1 = cleaned_df[cleaned_df['fruit'] == 'apples']
     df_2 = cleaned_df[cleaned_df['fruit'] == 'oranges']
     df_3 = cleaned_df[cleaned_df['fruit'] == 'figs']

     datasets = {
         'df_1': df_1.to_json(orient='split', date_format='iso'),
         'df_2': df_2.to_json(orient='split', date_format='iso'),
         'df_3': df_3.to_json(orient='split', date_format='iso'),
     }

     return json.dumps(datasets)

@callback(
    Output('graph1', 'figure'),
    Input('intermediate-value', 'data')
)
def update_graph_1(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_1'], orient='split')
    figure = create_figure_1(dff)
    return figure

@callback(
    Output('graph2', 'figure'),
    Input('intermediate-value', 'data')
)
def update_graph_2(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_2'], orient='split')
    figure = create_figure_2(dff)
    return figure

@callback(
    Output('graph3', 'figure'),
    Input('intermediate-value', 'data')
)
def update_graph_3(jsonified_cleaned_data):
    datasets = json.loads(jsonified_cleaned_data)
    dff = pd.read_json(datasets['df_3'], orient='split')
    figure = create_figure_3(dff)
    return figure
```

#### Example 3 - Caching and signaling

This example:

-   Uses Redis via Flask-Cache for storing “global variables” on the server-side in a database. This data is accessed through a function `global_store()`, the output of which is cached and keyed by its input arguments.
-   Uses the `dcc.Store` solution to send a signal to the other callbacks when the expensive computation is complete.
-   Note that instead of Redis, you could also save this to the file system. See [https://flask-caching.readthedocs.io/en/latest/](https://flask-caching.readthedocs.io/en/latest/) for more details.
-   This “signaling” is performant because it allows the expensive computation to only take up one process and be performed once. Without this type of signaling, each callback could end up computing the expensive computation in parallel, locking four processes instead of one.

Another benefit of this approach is that future sessions can use the pre-computed value. This will work well for apps that have a small number of inputs.

Here's what this example looks like.

```python
import os
import copy
import time

from dash import Dash, dcc, html, Input, Output, callback

import numpy as np
import pandas as pd
from flask_caching import Cache

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

CACHE_CONFIG = {
    # try 'FileSystemCache' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

N = 100

df = pd.DataFrame({
    'category': (
        (['apples'] * 5 * N) +
        (['oranges'] * 10 * N) +
        (['figs'] * 20 * N) +
        (['pineapples'] * 15 * N)
    )
})
df['x'] = np.random.randn(len(df['category']))
df['y'] = np.random.randn(len(df['category']))

app.layout = html.Div([
    dcc.Dropdown(df['category'].unique(), 'apples', id='dropdown'),
    html.Div([
        html.Div(dcc.Graph(id='graph-1'), className="six columns"),
        html.Div(dcc.Graph(id='graph-2'), className="six columns"),
    ], className="row"),
    html.Div([
        html.Div(dcc.Graph(id='graph-3'), className="six columns"),
        html.Div(dcc.Graph(id='graph-4'), className="six columns"),
    ], className="row"),

    # signal value to trigger callbacks
    dcc.Store(id='signal')
])

# perform expensive computations in this "global store"
# these computations are cached in a globally available
# redis memory store which is available across processes
# and for all time.
@cache.memoize()
def global_store(value):
    # simulate expensive query
    print(f'Computing value with {value}')
    time.sleep(3)
    return df[df['category'] == value]


def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_dataframe = global_store(value)
    fig['data'][0]['x'] = filtered_dataframe['x']
    fig['data'][0]['y'] = filtered_dataframe['y']
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b': 20, 't': 10} }
    return fig


@callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_value(value):
    # compute value and send a signal when done
    global_store(value)
    return value


@callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })


@callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'lines',
            'line': {'shape': 'spline', 'width': 0.5},
        }]
    })


@callback(Output('graph-3', 'figure'), Input('signal', 'data'))
def update_graph_3(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2d',
        }]
    })


@callback(Output('graph-4', 'figure'), Input('signal', 'data'))
def update_graph_4(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2dcontour',
        }]
    })


if __name__ == '__main__':
    # app.run(debug=True, processes=6, threaded=False)
    app.run(mode='inline')
```

Some things to note:

-   We've simulated an expensive process by using a system sleep of 3 seconds.
-   When the app loads, it takes three seconds to render all four graphs.
-   The initial computation only blocks one process.
-   Once the computation is complete, the signal is sent and four callbacks are executed in parallel to render the graphs. Each of these callbacks retrieves the data from the "global server-side store": the Redis or filesystem cache.
-   We've set `processes=6` in `app.run` so that multiple callbacks can be executed in parallel. In production, this is done with something like `$ gunicorn --workers 6 app:server`. If you don't run with multiple processes, then you won't see the graphs update in parallel as callbacks will be updated serially.
-   As we are running the server with multiple processes, we set `threaded` to `False`. A Flask server can't be be both multi-process and multi-threaded.
-   Selecting a value in the dropdown will take less than three seconds if it has already been selected in the past. This is because the value is being pulled from the cache.
-   Similarly, reloading the page or opening the app in a new window is also fast because the initial state and the initial expensive computation has already been computed.

#### Example 4 - User-based session data on the server

The previous example cached computations in a way that was accessible for all users.

Sometimes you may want to keep the data isolated to user sessions: one user's derived data shouldn't update the next user's derived data. One way to do this is to save the data in a `dcc.Store`, as demonstrated in the first example.

Another way to do this is to save the data in a cache along with a session ID and then reference the data using that session ID. Because data is saved on the server instead of transported over the network, this method is generally faster than the `dcc.Store` method.

_This method was originally discussed in a [Dash Community Forum thread](https://community.plotly.com/t/capture-window-tab-closing-event/7375/2?u=chriddyp)._

This example:

-   Caches data using the `flask_caching` filesystem cache. You can also save to an in-memory cache or database such as Redis instead.
-   Serializes the data as JSON.
    -   If you are using Pandas, consider serializing with Apache Arrow for faster serialization or Plasma for smaller dataframe size. [Community thread](https://community.plotly.com/t/fast-way-to-share-data-between-callbacks/8024/2)
-   Saves session data up to the number of expected concurrent users. This prevents the cache from being overfilled with data.
-   Creates unique session IDs for each session and stores it as the data of `dcc.Store` on every page load. This means that every user session has unique data in the `dcc.Store` on their page.

Here's what this example looks like in code:

```python
from dash import Dash, dcc, html, Input, Output, callback

import datetime
from flask_caching import Cache
import pandas as pd
import time
import uuid

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',

    # the maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})


def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by 
        # generating data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(3)

        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Store(data=session_id, id='session-id'),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')
    ]) 

app.layout = serve_layout

@callback(
    Output('output-1', 'children'),
    Input('get-data-button', 'n_clicks'),
    Input('session-id', 'data')
)
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


@callback(
    Output('output-2', 'children'),
    Input('get-data-button', 'n_clicks'),
    Input('session-id', 'data')
)
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


if __name__ == '__main__':
    app.run(mode='inline')
```

There are three things to notice in this example:

-   The timestamps of the dataframe don't update when we retrieve the data. This data is cached as part of the user's session.
-   Retrieving the data initially takes three seconds but successive queries are instant, as the data has been cached.
-   The second session displays different data than the first session: the data that is shared between callbacks is isolated to individual user sessions.

Questions? Discuss these examples on the [Dash Community Forum](https://community.plotly.com/c/dash).

## Dash Context `dash.ctx`

`dash.ctx` is used to provide context information for Dash apps. It is available in Dash 2.4 and later. For earlier versions, `dash.callback_context` is used to provide similar functionality, as shown below:

```python
ctx = dash.callback_context
input_id = (ctx.triggered[0]['prop_id'].split('.')[0]
            if ctx.triggered else None)

if input_id == 'rcd_time':
    record_num = 0
elif input_id == 'rcd_npts':
    record_num = 0
```

In the sequel, we only discuss `dash.ctx`.

Currently, dash 2.17.1, we cannot find the documentation of `dash.ctx`. Yet, we can use `help(dash.ctx)` to see the help file.

### Determining which button is changed with `dash.ctx`

```python
from dash import Dash, html, Input, Output, ctx

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
    html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
    html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
    html.Div(id='container-button-timestamp')
])

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)
def displayClick(btn1, btn2, btn3):
    msg = "None of the buttons have been clicked yet"
    if "btn-nclicks-1" == ctx.triggered_id:
        msg = "Button 1 was most recently clicked"
    elif "btn-nclicks-2" == ctx.triggered_id:
        msg = "Button 2 was most recently clicked"
    elif "btn-nclicks-3" == ctx.triggered_id:
        msg = "Button 3 was most recently clicked"
    return html.Div(msg)


app.run_server(mode='inline')
```

### `dash.ctx` attributes

`dash.ctx` has many attributes. The following are most useful:

-   `triggered_id`: Returns the component ID (str or dict) of the *Input component* that triggered the callback. 
    -   For an example of returning a str, see [Determining which button is changed with dash ctx](y3lib-dash-fe--dash-context.md#Determining%20which%20button%20is%20changed%20with%20dash%20ctx).
    -   For an example of returning a dict, see https://dash.plotly.com/determining-which-callback-input-changed.
-   `triggered_prop_ids`: Returns a dictionary of all the Input props that changed and caused the callback to execute. Note that we need to use `triggered_prop_ids` if we need both the component ID and the properties that triggered the callback or if multiple Inputs triggered the callback. It is empty when the callback is called on initial load, unless an Input prop got its value from another initial callback. Callbacks triggered by user actions typically have one item in triggered, unless the same action changes two props at once or the callback has several Input props that are all modified by another callback based on a single user action.
    -   For an example, see https://dash.plotly.com/determining-which-callback-input-changed.
