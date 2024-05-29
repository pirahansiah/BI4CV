# Farshid
import os
import pandas as pd
from datetime import datetime
import plotly.express as px
from dash import dcc, html, Dash
import logging
from image_score import *
from dash.dependencies import Input, Output

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from utils import (
    get_folder_path_from_file,
    gather_folder_info,
    gather_metadata
)

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, 'folder_path.txt')
    folder_path = get_folder_path_from_file(config_file_path)
    folder_info = gather_folder_info(folder_path)
    
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div([
        html.H1("Image/Video Metadata Dashboard"),
        html.Div([
            html.P(f"Folder Path: {folder_path}"),
            html.P(f"Total Folders: {len(next(os.walk(folder_path))[1])+1}"),
            html.P(f"Total Files: {sum(info['images'] + info['videos'] for info in folder_info.values())}")
        ]),
        html.Div([
            html.H2("Folder Info"),
            html.Table([
                html.Thead([
                    html.Tr([html.Th("Folder Path"), html.Th("Number of Images"), html.Th("Number of Videos")])
                ]),
                html.Tbody([
                    html.Tr([html.Td(key), html.Td(value['images']), html.Td(value['videos'])]) for key, value in folder_info.items()
                ])
            ])
        ]),
        dcc.Loading(
            id="loading",
            type="default",
            children=[
                html.Div(id="metadata-dashboard")
            ]
        )
    ])
    
    @app.callback(
        Output('metadata-dashboard', 'children'),
        Input('loading', 'children')
    )
    def update_dashboard(_):
        metadata_df = gather_metadata(folder_path)
        if metadata_df.empty:
            return html.P("No metadata found. Check the folder path or the file types.")
        else:
            metadata_df.to_csv(os.path.join(script_dir, 'metadata.csv'), index=False)
            return dcc.Tabs([
                dcc.Tab(label='File Count by Format', children=[
                    dcc.Graph(figure=px.bar(metadata_df, x='format', title='File Count by Format'))
                ]),
                dcc.Tab(label='File Size Distribution', children=[
                    dcc.Graph(figure=px.histogram(metadata_df, x='file_size', title='File Size Distribution'))
                ]),
                dcc.Tab(label='Resolution Distribution', children=[
                    dcc.Graph(figure=px.histogram(metadata_df[metadata_df['resolution'].notna()], x='resolution', title='Resolution Distribution'))
                ]),
                dcc.Tab(label='Creation Date Timeline', children=[
                    dcc.Graph(figure=px.line(metadata_df.sort_values(by='created_at'), x='created_at', y='file_size', title='File Size Over Time'))
                ]),
                dcc.Tab(label='Image Quality Details', children=[
                    html.Table([
                        html.Thead([
                            html.Tr([
                                html.Th("Filename"), html.Th("Thumbnail"), html.Th("MSCN Coefficients"), html.Th("NIQE Features"), html.Th("PIQE Index"), html.Th("JPEG Quality"), html.Th("BLIINDS Features"), html.Th("CORNIA Features"), html.Th("SSEQ"), html.Th("FQADI Features")
                            ])
                        ]),
                        html.Tbody([
                            html.Tr([
                                html.Td(img['filename']),
                                html.Td(html.Img(src=img['thumbnail'], style={'height': '50px', 'width': '50px'})),
                                html.Td(str(img['calculate_mscn_coefficients'])),
                                html.Td(str(img['compute_niqe_features'])),
                                html.Td(str(img['calculate_piqe_index'])),
                                html.Td(str(img['estimate_jpeg_quality'])),
                                html.Td(str(img['compute_bliinds_features'])),
                                html.Td(str(img['extract_cornia_features'])),
                                html.Td(str(img['calculate_sseq'])),
                                html.Td(str(img['calculate_fqadi_features']))
                            ]) for img in metadata_df.to_dict('records')
                        ])
                    ])
                ])
            ])
    
    app.run_server(debug=True)
