"""Dash-based image/video metadata dashboard with Plotly visualizations."""

from __future__ import annotations

import logging
from pathlib import Path

import plotly.express as px
from dash import dcc, html
from dash import Dash
from dash.dependencies import Input, Output

from .image_score import ImageQualityScorer
from .utils import gather_folder_info, gather_metadata, get_folder_path_from_file

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def create_dash_app() -> Dash:
    """Build and return the Dash metadata dashboard app."""
    script_dir = Path(__file__).resolve().parent
    config_file = script_dir / "folder_path.txt"
    folder_path = get_folder_path_from_file(config_file)
    folder_info = gather_folder_info(folder_path)
    scorer = ImageQualityScorer()

    total_images = sum(info.images for info in folder_info)
    total_videos = sum(info.videos for info in folder_info)

    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div([
        html.H1(
            "Image Metadata Dashboard",
            style={"textAlign": "center", "color": "#007BFF"},
        ),
        html.Div([
            html.P(f"Folder Path: {folder_path}", style={"fontWeight": "bold"}),
            html.P(f"Total Subfolders: {len(folder_info)}", style={"fontWeight": "bold"}),
            html.P(
                f"Total Files: {total_images + total_videos} "
                f"({total_images} images, {total_videos} videos)",
                style={"fontWeight": "bold"},
            ),
        ], style={"textAlign": "center"}),
        html.Div([
            html.H2("Folder Info", style={"textAlign": "center"}),
            html.Table([
                html.Thead(html.Tr([
                    html.Th("Folder Path"),
                    html.Th("Images"),
                    html.Th("Videos"),
                ])),
                html.Tbody([
                    html.Tr([
                        html.Td(info.path),
                        html.Td(info.images),
                        html.Td(info.videos),
                    ])
                    for info in folder_info
                ]),
            ], style={
                "width": "80%",
                "margin": "auto",
                "border": "1px solid #ddd",
                "borderCollapse": "collapse",
            }),
        ]),
        dcc.Loading(
            id="loading",
            type="default",
            children=[html.Div(id="metadata-dashboard")],
        ),
    ])

    @app.callback(
        Output("metadata-dashboard", "children"),
        Input("loading", "children"),
    )
    def update_dashboard(_):
        metadata_df = gather_metadata(folder_path, scorer)
        if metadata_df.empty:
            return html.P("No metadata found. Check the folder path or the file types.")

        csv_path = script_dir / "metadata.csv"
        metadata_df.to_csv(str(csv_path), index=False)

        return dcc.Tabs([
            dcc.Tab(label="File Count by Format", children=[
                dcc.Graph(figure=px.bar(
                    metadata_df, x="format",
                    title="File Count by Format",
                    labels={"x": "Format", "y": "Count"},
                    color="format",
                )),
            ]),
            dcc.Tab(label="File Size Distribution", children=[
                dcc.Graph(figure=px.histogram(
                    metadata_df, x="file_size",
                    title="File Size Distribution",
                    labels={"x": "File Size", "y": "Count"},
                    nbins=50,
                )),
            ]),
            dcc.Tab(label="Resolution Distribution", children=[
                dcc.Graph(figure=px.histogram(
                    metadata_df[metadata_df["resolution"].notna()],
                    x="resolution",
                    title="Resolution Distribution",
                    labels={"x": "Resolution", "y": "Count"},
                    nbins=50,
                )),
            ]),
            dcc.Tab(label="Creation Date Timeline", children=[
                dcc.Graph(figure=px.line(
                    metadata_df.sort_values(by="created_at"),
                    x="created_at", y="file_size",
                    title="File Size Over Time",
                    labels={"x": "Created At", "y": "File Size"},
                )),
            ]),
            dcc.Tab(label="Image Quality Details", children=[
                html.Table([
                    html.Thead(html.Tr([
                        html.Th("Filename"),
                        html.Th("MSCN"),
                        html.Th("NIQE"),
                        html.Th("PIQE"),
                        html.Th("JPEG Q"),
                        html.Th("BLIINDS"),
                        html.Th("CORNIA"),
                        html.Th("SSEQ"),
                        html.Th("FQADI"),
                    ])),
                    html.Tbody([
                        html.Tr([
                            html.Td(row.get("filename", "")),
                            html.Td(str(row.get("mscn", ""))),
                            html.Td(str(row.get("niqe", ""))),
                            html.Td(str(row.get("piqe", ""))),
                            html.Td(str(row.get("jpeg_quality", ""))),
                            html.Td(str(row.get("bliinds", ""))),
                            html.Td(str(row.get("cornia", ""))),
                            html.Td(str(row.get("sseq", ""))),
                            html.Td(str(row.get("fqadi", ""))),
                        ])
                        for row in metadata_df.to_dict("records")
                    ]),
                ], style={
                    "width": "100%",
                    "margin": "auto",
                    "border": "1px solid #ddd",
                    "borderCollapse": "collapse",
                }),
            ]),
        ], style={"marginTop": "20px"})

    return app


if __name__ == "__main__":
    app = create_dash_app()
    app.run_server(debug=True, port=5003)
