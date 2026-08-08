"""
Во Flet сейчас логика выравнивания разделена очень четко:
За выравнивание элементов внутри контейнеров (Row, Column) отвечает ft.MainAxisAlignment и ft.CrossAxisAlignment.
За выравнивание самого текста внутри текстовых блоков (Text, TextField) отвечает ft.TextAlign.
"""
import flet as ft

def main(page: ft.Page) -> None:
    page.title = 'Flet counter example'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_field = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100) #MainTextAlignment -> TextAlign

    def minus_click(e: ft.ControlEvent) -> None:
        input_field.value = str(int(input_field.value) - 1)
        # не обязательно вызывать обновление, он сам оказывается обновляется
        input_field.update()

    def plus_click(e: ft.ControlEvent) -> None:
        input_field.value = str(int(input_field.value) + 1)
        input_field.update()

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                input_field,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click)
            ]
        )
    )

# ft.run(main) old method

if __name__ == "__main__":
    ft.app(target=main)