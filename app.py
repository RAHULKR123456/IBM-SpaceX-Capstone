"""SpaceX launch records dashboard (IBM Data Science Capstone).

Components
- Dropdown to choose a launch site (or all sites)
- Pie chart: successful launches by site, or success vs failure for one site
- Range slider for payload mass (kg)
- Scatter plot: payload mass versus landing outcome, coloured by booster version category

Run:  python app.py   then open http://127.0.0.1:8050
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
            "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")

SITE, OUTCOME, PAYLOAD, BOOSTER = "Launch Site", "class", "Payload Mass (kg)", "Booster Version Category"


def success_counts(data, site):
    """Return the DataFrame used by the pie chart for the selected site."""
    if site == "ALL":
        counts = data[data[OUTCOME] == 1].groupby(SITE).size().reset_index(name="count")
        return counts.rename(columns={SITE: "label"})
    chosen = data[data[SITE] == site]
    counts = chosen[OUTCOME].map({1: "Success", 0: "Failure"}).value_counts().reset_index()
    counts.columns = ["label", "count"]
    return counts


def filter_launches(data, site, low, high):
    """Filter launches by site and payload range (kg) for the scatter plot."""
    subset = data[(data[PAYLOAD] >= low) & (data[PAYLOAD] <= high)]
    if site != "ALL":
        subset = subset[subset[SITE] == site]
    return subset


def build_app(data):
    app = Dash(__name__)
    sites = sorted(data[SITE].unique())
    app.layout = html.Div([
        html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center"}),
        dcc.Dropdown(
            id="site-dropdown",
            options=[{"label": "All Sites", "value": "ALL"}] + [{"label": s, "value": s} for s in sites],
            value="ALL", placeholder="Select a launch site", searchable=True),
        dcc.Graph(id="success-pie-chart"),
        html.P("Payload range (kg):"),
        dcc.RangeSlider(id="payload-slider", min=0, max=10000, step=1000, value=[0, 10000],
                        marks={i: str(i) for i in range(0, 10001, 2500)}),
        dcc.Graph(id="success-payload-scatter-chart"),
    ])

    @app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
    def update_pie(site):
        counts = success_counts(data, site)
        title = ("Total successful launches by site" if site == "ALL"
                 else f"Success vs failure for {site}")
        return px.pie(counts, values="count", names="label", title=title)

    @app.callback(Output("success-payload-scatter-chart", "figure"),
                  [Input("site-dropdown", "value"), Input("payload-slider", "value")])
    def update_scatter(site, payload_range):
        subset = filter_launches(data, site, payload_range[0], payload_range[1])
        return px.scatter(subset, x=PAYLOAD, y=OUTCOME, color=BOOSTER,
                          title="Payload mass versus landing outcome")

    return app


if __name__ == "__main__":
    launches = pd.read_csv(DATA_URL)
    application = build_app(launches)
    try:
        application.run(host="0.0.0.0", port=8050)      # Dash 2.9 and later
    except AttributeError:
        application.run_server(host="0.0.0.0", port=8050)  # older Dash versions
