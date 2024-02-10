from shiny.express import input, render, ui

ui.input_slider('val','slider',min=0,max=10, value=5)

@render.text
def slider_val():
    return f"Slider value: {input.val()}"