import plotly.graph_objects as go
# from async_pull import date_to_today_list
from mapbox_token import mapbox_token

import colorama
from data.request_map_api import request_map_data
import requests
import pandas as pd

print(colorama.Fore.CYAN + 'Checking Moonlight')
df = request_map_data()


def request_map_style_moonlight(df, lat=0, long=0):
    token = mapbox_token

    maps = []

    map_confirmed = go.Scattermapbox(
        name='Active',
        lon=df['lon'],
        lat=df['lat'],
        text=df['name'],
        customdata=df.loc[:, ['name']],
        hovertemplate=
        "<b>%{text}</b><br><br>" +
        "Location: %{customdata[0]}<br>" +
        "<extra></extra>",
        mode='markers',
        fillcolor='rgb(242, 177, 172)',

        ids=df['pk'],
        marker=go.scattermapbox.Marker(
            size=5,
            color='red',
            opacity=0.5
        ),
        opacity=0.5,
    )



    layout = go.Layout(
            height=700,
            autosize=True,
            mapbox_accesstoken=token,
            mapbox_style="mapbox://styles/cryptopotluck/clbd5fc7d001414kcj49x1yof",
            mapbox_center={"lat": 27.952323793542178, "lon": -97.10239291191102},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=0, b=0, l=0, r=0),

            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            ),
            mapbox = dict(
                center=dict(
                    lat=27.952323793542178,
                    lon=-97.10239291191102
                ),
                pitch=0,
                zoom=3,
            )
        )

    fig = go.Figure(data=map_confirmed, layout=layout)

    return fig


if __name__ == '__main__':
    map = request_map_style_moonlight(df)
    map.show()
    print(map)