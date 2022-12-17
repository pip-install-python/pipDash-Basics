import dash
from dash import html, dcc
import dash_mantine_components as dmc

dash.register_page(__name__)


timeline= dmc.Timeline(
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        dmc.TimelineItem(
            title="New Branch",
            children=[
                dmc.Text(
                    [
                        "You've created new branch ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                        " from master",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Commits",
            children=[
                dmc.Text(
                    [
                        "You've pushed 23 commits to ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Pull Request",
            lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "You've submitted a pull request ",
                        dmc.Anchor(
                            "Fix incorrect notification message (#178)",
                            href="#",
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
                        dmc.Anchor(
                            "Ann Marie Ward",
                            href="https://github.com/AnnMarieW",
                            size="sm",
                        ),
                        " left a comment on your pull request",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
            title="Code Review",
        ),
    ],
)

layout = html.Div(children=[
    html.H1(children='This is our Archive page'),

    html.Div([
        timeline,
        timeline,
        timeline,
        timeline,
    ]),


])