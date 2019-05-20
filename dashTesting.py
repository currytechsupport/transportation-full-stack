import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H1(children='Hello '),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    ),
    html.Div(id='output-container'),

    dcc.Slider(
            id = 'my-slider',
            min=0,
            max=10,
            step=0.5,
            value=-3,
            ),
    html.Div(id='slider-output-container')

])






@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])

def update_output_slider(value):
    return 'Output: "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])

def update_output_slider(value):
    if value == 'NYC':
        return 'gey'
    elif value == 'MTL':
        return 'feg'
    else:
        return 'Output: {}'.format(value)




if __name__ == '__main__':
    app.run_server(debug=True)
