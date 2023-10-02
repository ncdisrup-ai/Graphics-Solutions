import plotly.express as px
import pandas as pd

import gradio as gr
import matplotlib
matplotlib.use('Agg')

def map_plot():
  #define a map element
    df = px.data.gapminder().query("year==2002")
    fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                        hover_name="country", size="lifeExp",
                        projection="natural earth")
    return fig
outputs = gr.Plot()

app_worldmap = gr.Interface(fn=map_plot, inputs=None, outputs=outputs)

#demo.launch(share=true)