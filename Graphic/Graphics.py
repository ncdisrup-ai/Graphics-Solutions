import gradio as gr
from math import log
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gdp_change(r, year, country, smoothen):
    years = ['1850', '1900', '1950', '2000', '2050']
    m = years.index(year)
    start_day = 10* m
    final_day = 10* (m + 1)
    x = np.arange(start_day, final_day + 1)
    pop_count = {"USA": 350, "Canada": 40, "Mexico": 300, "UK": 120}
    if smoothen:
        r = log(r)
    df = pd.DataFrame({'day': x})
    df[country] = ( x ** (r) * (pop_count[country] + 1))
    fig = plt.figure()
    plt.plot(df['day'], df[country].to_numpy(), label = country)
    plt.title("GDP in " + year)
    plt.ylabel("GDP (Millions)")
    plt.xlabel("Population Change since 1800")
    plt.grid()
    return fig

inputs = [
        gr.Slider(1, 4, 3.1, label="R"),
        gr.Dropdown(['1850', '1900', '1950', '2000', '2050'], label="Year"),
        gr.Radio(["USA", "Canada", "Mexico", "UK"], label="Countries", ),
        gr.Checkbox(label="Log of GDP Growth Rate?"),
    ]
outputs = gr.Plot()

app_gdp = gr.Interface(fn=gdp_change, inputs=inputs, outputs=outputs, allow_flagging="manual", flagging_options=["No plot shown", "Wrong axis", "Other"])

#demo.launch(share=True)


