import dash
from dash import html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import pydeck as pdk
import pandas
import dash_trich_components as dtc
from templates.map_style.map_style_moonlight import request_map_style_moonlight
from data.request_map_api import request_map_data
from dash_iconify import DashIconify

dash.register_page(__name__, path='/')

# data fetching
df = request_map_data()


dropdown = dbc.DropdownMenu(
children=[

    dbc.DropdownMenuItem(html.Img(src=dash.get_asset_url('imgs/branding/inventory.png'), style={'height': "100%",
                                                                                             'display': "flex",
                                                                                             'alignItems': "center",
                                                                                             'justifyContent': "center"}),
                         href='https://pipinstallpython.pythonanywhere.com/catalogue/'),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Django Map", href="https://pipinstallpython.pythonanywhere.com/map/everything/"),
    dbc.DropdownMenuItem("Ukraine🇺🇦MapWar", href="https://pipinstallpython.pythonanywhere.com/Ukraine/"),
    dbc.DropdownMenuItem("Github Account", href='https://github.com/Pip-Install-Python'),
    dbc.DropdownMenuItem("Discord Server",
                         href='https://www.youtube.com/channel/UC-pBvv8mzLpj0k-RIbc2Nog?sub_confirmation=1'),
    dbc.DropdownMenuItem("Youtube Channel",
                         href='https://www.youtube.com/channel/UC-pBvv8mzLpj0k-RIbc2Nog?sub_confirmation=1'),

    ],
    nav=True,
    in_navbar=True,
    label="Important Links",

)

# Navbar Layout
navbar = dbc.Navbar(
        [

            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(width=3),
                    dbc.Col(html.Img(src=dash.get_asset_url('imgs/branding/pip_logo.jpeg'), height="40px",
                                     width="50px"), align='left', width=3),
                    dbc.Col([dbc.NavbarBrand("Pip Install Python", style={'align': 'left','position':'absolute', "z-index": -1}), html.Br(), dropdown], width=4),

                ],
                align='center',
            ),
dbc.Nav(
            dmc.Group(
                        position='right',
                        children=[
                            dmc.ListItem(
                                dcc.Link('Home', href='/'),
                                icon=[
                                    DashIconify(icon="flat-color-icons:home", width=32)],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('archive', href='/archive'),
                                icon=[
                                    DashIconify(icon="openmoji:openstreetmap", width=32)],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('analytics', href='/analytics'),
                                icon=[
                                    DashIconify(icon="vscode-icons:file-type-graphviz", width=30, rotate=1, flip="horizontal", style={})],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('Github', href='/analytics'),
                                icon=[
                                    DashIconify(icon="ion:logo-github", width=30, rotate=1, flip="horizontal")],
                                class_name='nav-list-items'),


                        ]), className="ml-auto", navbar=True),

            dbc.Nav(
                [dtc.ThemeToggle(
                    bg_color_dark='#232323',
                    icon_color_dark='#EDC575',
                    bg_color_light='#07484E',
                    icon_color_light='#C8DBDC',
                    tooltip_text='Toggle light/dark theme',
                    id='light_dark'
                ),
                ], className="ml-auto", navbar=True
            ),

        ]
    ,
    # color="dark",
    # dark=True,
    className='navbar',
)


# Videos
videos = html.Div([
    dcc.Dropdown(
        id='video-dropdown',
        options=[
            {'label': 'Project Intro', 'value': 'Available Videos'},
            # {'label': 'Video 2', 'value': 'video2'},
            # {'label': 'Video 3', 'value': 'video3'},
        ],
        value='Available Videos'
    ),
    html.Div(id='video-target'),
], style={'height': '30vh'})

# Timeline
project_timeline = dmc.Paper(dmc.Container([
    dbc.Row([dbc.Col(dmc.Title('Project Goals'), width=12)]),
    dmc.Divider(variant="solid"),
    dmc.Col(videos, span=12),
    dmc.Space(h=15),
    dmc.Timeline(
        active=1,
        bulletSize=15,
        lineWidth=2,
        children=[
            dmc.TimelineItem(
                title="Launched Django HQ",
                bullet=[
                    dmc.Avatar(
                        src=dash.get_asset_url('imgs/static/question_something.gif'),
                        radius="xl",
                        size=30,
                    )
                ],
                children=[
                    dmc.Text(
                        [
                            "We've established a full feature Django Application. ",
                            dmc.Anchor("PiratesBargain", href="http://piratesbargain.com", size="sm"),
                            " hosting e-commerce, teaching, admin portal, apis & satellite mapping.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
                color='green',
            ),
            dmc.TimelineItem(
                title="Launching Flask HQ",
                children=[
                    dmc.Text(
                        [
                            "We are currently building a full featured Flask Application ",
                            dmc.Anchor("pipinstallpython.com", href="http://www.pipinstallpython.com", size="sm"),
                            " The aim is to build something rich & dynamic that's interactive and mobile friendly."
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
            ),
            dmc.TimelineItem(
                title="Seamless Relationship",
                lineVariant="dashed",
                children=[
                    dmc.Text(
                        [
                            "We have stated a GitHub Organization and are actively releasing code and cheat codes to "
                            "the public. Check out: ",
                            dmc.Anchor(
                                "Pip-Install-Pirate",
                                href="https://github.com/Pip-Install-Pirate",
                                size="sm",
                            ),
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
            ),
            dmc.TimelineItem(
                [
                    dmc.Text(
                        [
                            "The Django and Flask applications although separate are going to need to be closely "
                            "compatible. With a solid API development we aim to connect both frameworks together "
                            "while keeping them separate in design each has skills & attributes that a stand alone"
                            "version wouldn't be able to provide. However together they correct each others "
                            "individual weaknesses and become a much stronger foundation.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
                title="Launch a Public Internet Network",
            ),
            dmc.TimelineItem(
                title="Sustainable number of Daily Users",
                children=[
                    dmc.Text(
                        [
                            "We would like to see an active user base of 35,000 for the Aransas area. Hopefully "
                            "more users in regards to the war logistics software we are actively developing. "
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
            ),
            dmc.TimelineItem(
                title="100k Subs on Youtube",
                children=[
                    dmc.Text(
                        [
                            "One of our main goals is to achieve 100k subs on Youtube as its a way to grow the "
                            "network, teach and expand underlying projects and goals. "
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
            ),

            dmc.TimelineItem(
                [
                    dmc.Text(
                        [
                            dmc.Anchor(
                                "Pip",
                                href="https://austinkiese.com",
                                size="sm",
                            ),
                            " Will hopefully have created something self sustaining to retire off and go offline.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
                title="Going Off the Grid",
            ),

        ],
    ), dmc.Space(h=10)]),
    shadow='xl',
    withBorder=True,
    style={'height': '80vh', 'overflow-y': 'auto', }
)


layout = html.Div([navbar,dmc.BackgroundImage(src=dash.get_asset_url('imgs/gif/cyberpunk_map_background.gif'),
                             children=dbc.Container(
                                 children=[
                                 dmc.Tabs(
                                     color="red",
                                     orientation="horizontal",
                                     style={'background-color': '#232020'},
                                     children=[
                                         dmc.Tab(label="Home", children=[
                                             dmc.Grid([
                                                 dmc.Col([
                                                     html.Img(
                                                         src=dash.get_asset_url('imgs/gif/ships_shooting_cannons.gif'), style={'width':'100%'}
                                                     ),
                                                     html.Hr(),
                                                    dmc.MantineProvider(
                                                         theme={"colorScheme": "dark"},
                                                         children=[
                                                         dmc.Paper(dmc.Container(children=[
                                                                dmc.Title(f"Welcome aboard,", order=1),
                                                                dmc.Text(f"The internet is a vast ocean of "
                                                                         f"information and data. Traveling admits"
                                                                         f" the currents some individuals barely keep "
                                                                         f"their heads above water while others sail "
                                                                         f"massive ships. Filled with tools, crews, "
                                                                         f"weapons and loot. The goal of this project "
                                                                         f"is to setup the proper foundation to sail "
                                                                         f"these waters. A ship that's able to navigate "
                                                                         f"the data, return fire if needed but mostly "
                                                                         f"explore and better understand the digital"
                                                                         f" world around us. Gaining new cheat codes"
                                                                         f" and abilities along the way, extracting new"
                                                                         f" opportunities, making new alies and"
                                                                         f" expanding what is a personal network to"
                                                                         f" the equivalent of the colonial era. "
                                                                         f" establishing satellite bases, concurring "
                                                                         f" new lands at the start of the 1600's."
                                                                         f" This is my 21st century digital equivalent."),
                                                            dmc.Group([
                                                                html.A(href='https://shorturl.at/FIRT3', children=[DashIconify(icon="flat-color-icons:money-transfer", width=32)]),
                                                                html.A(href='https://www.youtube.com/channel/UC-pBvv8mzLpj0k-RIbc2Nog?sub_confirmation=1', children=[DashIconify(icon="logos:youtube-icon", width=32)]),
                                                                html.A(href='https://discord.gg/VXW7cpsnJk', children=[DashIconify(icon="logos:discord-icon", width=32)]),
                                                                html.A(href='https://www.reddit.com/r/PipInstallPython/', children=[DashIconify(icon="line-md:reddit-loop", width=32)]),
                                                                html.A(href='https://github.com/Pip-Install-Pirate', children=[DashIconify(icon="typcn:social-github-circular", width=32)]),
                                                                html.A(href='https://www.snapchat.com/add/thegatsbypirate?share_id=6ZAGSwu2Kts&locale=en-US', children=[DashIconify(icon="fa-brands:snapchat-square", width=32)]),
                                                                html.A(href='https://pipinstallpython.pythonanywhere.com/home/direct_message/', children=[DashIconify(icon="openmoji:mobile-message", width=32)]),
                                                            ], spacing='md', position='center'),
                                                         ]))]),

                                                 ], sm=12, md=6, lg=4),
                                                 dmc.Col(html.Div([dcc.Graph(figure=request_map_style_moonlight(df)), dmc.Space(h=35)],  style={'margin-left': '0', 'margin-right': '0', 'margin-top': '0', 'margin-bottom': '0', 'height': '80vh'}), sm=12, md=6, lg=4),
                                                 dmc.Col(dmc.MantineProvider(
                                                     theme={"colorScheme": "dark"},
                                                     children=[project_timeline]), sm=12, md=12, lg=4),

                                             ]
                                             )
                                         ]),
                                         dmc.Tab(label="Hide Content", children=[

                                         ]),
                                     ]
                                 ),

                             ], style={'height': '90vh', 'overflow-y': 'scroll'})
                             )])


@dash.callback(Output('video-target', 'children'), [Input('video-dropdown', 'value')])
def embed_iframe(value):
    videos = {
        'Available Videos': 'pip-install-python-flask-intro',
        # 'video2': '5BAthiN0htc',
        # 'video3': 'e4ti2fCpXMI',
    }
    return dmc.LoadingOverlay(html.Iframe(src=f"https://archive.org/embed/{videos[value]}",
                                          style={'width': '100%', 'height': '25vh', 'webkitallowfullscreen': 'true',
                                                 'mozallowfullscreen': 'true'}))
