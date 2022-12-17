import dash
from dash import html, Dash, dcc

app = Dash(__name__,
           # Showcase how to add external CSS and JS
           external_stylesheets=[
               'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
           ],
           # Use pages to organize your app
           use_pages=True,
           # Use assets_url_path to serve your assets (Folder name has to be assets)
           assets_url_path='assets',
           )


# Create a app layout
app.layout = html.Div([
        html.Div(
            [
                dash.page_container
            ],
        ),
])


if __name__ == '__main__':
    # add host = 'Ip.Address.number' to test on mobile
    # type in phone browser: Ip.Address.number:8001
    app.run_server(
        debug=True, port='8001', threaded=True
    )