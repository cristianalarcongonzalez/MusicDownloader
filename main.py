import flet as ft 
from pytube import YouTube
import os

def main(page :ft.Page):
    url = ft.TextField(label="url",
                      autofocus=True)
    submit = ft.ElevatedButton("Descargar")

    

    def btn_click(e):
        current_folder =os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=current_folder)


    submit.on_click=btn_click

    page.add(
        url,
        submit, 
        ft.Dropdown(
            label="Escoja la calidad del video",
            hint_text="Escoja la calidad del video?",
            options=[
                ft.dropdown.Option("Alta Resolucion"),
                ft.dropdown.Option("Resolucion Media"),
                ft.dropdown.Option("Baja Resolucion"),
            ],
            autofocus=True,        
    )
)

ft.app(target=main)

