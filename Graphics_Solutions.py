from transformers import pipeline
import gradio as gr
import Graphics
import WorldMap



gr.close_all()

demo = gr.TabbedInterface([Graphics.app_gdp, WorldMap.app_worldmap], ["Graphics Gdp Change", "WorldMap"])


demo.launch(share=True) # (share=True for public link)

