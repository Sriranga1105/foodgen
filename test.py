import flet as ft

def main(page: ft.Page):
    page.window_width = 400;
    page.window_height = 600;
    page.add(ft.Text(value="Hello World!"))

ft.app(target=main)