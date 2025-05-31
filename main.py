from generate import ask_nain
import gradio as gr

gr.ChatInterface(ask_nain, title="Le Nain de Naheulbeuk").launch()
