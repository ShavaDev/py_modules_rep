"""
Вы можете отключить автоматическое обновление для более точного контроля над тем, когда обновления отправляются клиенту.
Используйте ft.context.disable_auto_update()и ft.context.enable_auto_update()для переключения этого поведения.
При вызове вне обработчиков событий (например, на уровне модуля) он управляет глобальным значением по умолчанию для всего приложения:

import flet as ft

# disable auto-update globally
ft.context.disable_auto_update()

def main(page: ft.Page):
    def button_click(e):
        page.controls.append(ft.Text("Clicked!"))
        page.update()  # must call explicitly since auto-update is off

    page.controls.append(ft.Button("Click me", on_click=button_click))
    page.update()

ft.run(main)
"""
import flet as ft

def main(page: ft.Page) -> None:
    def button_click(e: ft.ControlEvent) -> None:
        page.controls.append(ft.Text(value="Clicked!"))
        # no need to code: page.update()

    page.controls.append(ft.Button(content="Click me!", on_click=button_click))
    # again no need to code: page.update()

# def main(page: ft.Page):
#     def add_many_items(e):
#         ft.context.disable_auto_update()
#         for i in range(100):
#             page.controls.append(ft.Text(f"Item {i}"))
#         page.update()  # single update for all 100 items
#
#     page.controls.append(ft.Button("Add items", on_click=add_many_items))

if __name__ == '__main__':
    ft.app(target=main)
