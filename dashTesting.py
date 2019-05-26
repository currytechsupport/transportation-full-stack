import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H1(children='Transportation Safety Calculator '),


    dcc.Slider(
            id = 'age-slider',
            min=13,
            max=19,
            step=1,
            value=13,
            ),

    html.Div(id='age-slider-output-container'),

    dcc.Dropdown(
        id='gender-dropdown',
        options=[
            {'label': 'Male', 'value': 'male'},
            {'label': 'Female', 'value': 'female'}

        ],
        value='male'
    ),
    html.Div(id='gender-output-container'),

    dcc.Slider(
            id = 'people-slider',
            min=1,
            max=10,
            step=1,
            value=-3,
            ),
    html.Div(id='people-slider-output-container'),

    dcc.RadioItems(
    options=[
        {'label': 'New Driver (< 6 months)', 'value': 'true'},
        {'label': 'Experienced Driver', 'value': 'wrong'}
    ],
    value='true'
    ),
    html.Div(id='gender-output-container')


])






@app.callback(
    dash.dependencies.Output('age-slider-output-container', 'children'),
    [dash.dependencies.Input('age-slider', 'value')])

def update_output_slider(value):
    return 'Output: "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('gender-output-container', 'children'),
    [dash.dependencies.Input('gender-dropdown', 'value')])

def update_output_slider(value):
    return format(value)

@app.callback(
    dash.dependencies.Output('people-slider-output-container', 'children'),
    [dash.dependencies.Input('people-slider', 'value')])

def update_age_slider(value):
    return format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
