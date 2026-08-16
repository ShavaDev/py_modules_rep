from __future__ import annotations

import manim as mn
from manim import Create


# создаем анимацию окружности
class CreateCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle() # показываем какую фигуру хотим рендерить
        circle.set_fill(mn.PINK, opacity=0.5) # задаем цвет и прозрачность
        self.play(Create(circle)) # рендерит фигуру


class SquareToCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle()
        circle.set_fill(mn.PINK, opacity=0.5)

        square = mn.Square()
        square.set_fill(mn.BLUE, opacity=0.5)
        square.rotate(mn.PI / 4)

        # Рисуем квадрат за 1.5 секунды
        self.play(mn.Create(square), run_time=1.5)
        self.wait(0.5)  # Пауза полсекунды

        # Превращаем в круг
        self.play(mn.Transform(square, circle))
        self.wait(0.5)

        # Растворяем
        self.play(mn.FadeOut(square)) # (затухание / растворение) — это анимация исчезновения объекта.
        self.wait(0.5)


class SquareAndCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle()
        circle.set_fill(mn.GREEN, opacity=0.5)

        square = mn.Square()
        square.set_fill(mn.GRAY_BROWN, opacity=0.5)

        square.next_to(circle, mn.RIGHT, buff=0.5) # создаем позицию квадрата относительно круга
        self.play(Create(circle), Create(square), run_time=1.5)
        self.play(mn.FadeOut(circle), mn.FadeOut(square))
        self.wait(0.5)


class AnimatedSquareToCircle(mn.Scene):
    """
    Метод animate это простой и удобный способ анимировать абсолютно любой обычный метод вашего объекта (Mobject).
    Вместо того чтобы искать или писать специальные классы анимаций, вы просто вызываете нужный метод через .animate,
    и Manim сам превращает его из мгновенного изменения в плавный процесс.
    Правило: Вызов .animate помещается между самим объектом и методом, который вы хотите анимировать,
    и весь этот вызов обязательно передается внутрь self.play(...).
    """
    def construct(self):
        circle = mn.Circle()
        square = mn.Square()

        self.play(Create(square), run_time=1.5)
        self.play(square.animate.rotate(mn.PI / 4))
        self.play(mn.Transform(square, circle))
        self.play(circle.animate.set_fill(mn.PINK, opacity=0.5))
        # self.play(mn.FadeOut(circle))
        self.wait(0.5)


class WorkWithText(mn.Scene):
    """
        1. .shift(*vectors) — Сдвиг (Перемещение)
        Перемещает объект на заданный вектор относительно его текущего положения.
        Зачем нужен: Подвинуть объект в любую сторону на фиксированное расстояние.
        Направления: В Manim есть готовые константы направлений: UP, DOWN, LEFT, RIGHT, OUT, IN (каждый равен вектору длиной 1 unit).
        # Подвинуть по диагонали (вверх и влево)
        square.shift(UP + LEFT)
        2. .flip(axis) — Отражение (Зеркало)
        Отражает объект относительно указанной оси.
        Зачем нужен: Перевернуть текст, стрелку или неравностороннюю фигуру зеркально.
        Параметры: По умолчанию отражает относительно горизонтальной оси RIGHT (вверх ногами). Можно передать UP (слева направо).
        # Отразить вверх ногами (по умолчанию)
        text.flip()
        # Отразить слева направо (зеркально)
        text.flip(axis=UP)
        3. .scale(factor) — Масштабирование (Размер)
        Изменяет размер объекта в factor раз.
        Зачем нужен: Увеличить или уменьшить объект.
        Параметры: Число > 1 увеличивает, от 0 до 1 — уменьшает.
        4. .rotate(angle) — ВращениеПоворачивает объект на заданный угол.Зачем нужен: Повернуть фигуру или текст.Параметры:
        Угол задается в радианах. Для удобства используют константу PI ($180^\circ$) или функцию deg_to_rad.
    """
    def construct(self):
        raw_text = (
            "Методы вроде shift, flip, scale, rotate в Manim "
            "называются методами трансформации позиционирования и формы. "
            "Они нужны для того, чтобы перемещать, поворачивать, отражать и изменять размеры объектов на сцене. "
            "Любой объект в Manim (текст, геометрическая фигура, график) на самом деле является "
            "набором математических точек (векторов). Эти методы просто пересчитывают координаты этих точек."
        )

        # Класс Text отлично поддерживает русский язык
        text = mn.Text(raw_text, font_size=24)

        # Ограничиваем ширину текста, чтобы он помещался на экране и переносился
        text.width = 12

        self.play(mn.Create(text))
        self.wait(2)


class DifferentRotations(mn.Scene):
    def construct(self):
        # left_square = mn.Square(color=mn.BLUE, fill_opacity=0.7).shift(2 * mn.LEFT)
        # right_square = mn.Square(color=mn.GREEN, fill_opacity=0.7).shift(2 * mn.RIGHT)

        left_square = mn.Square(color=mn.BLUE, fill_opacity=0.7)
        right_square = mn.Square(color=mn.GREEN, fill_opacity=0.7)

        self.play(left_square.animate.shift(2 * mn.LEFT), right_square.animate.shift(2 * mn.RIGHT))

        self.play(left_square.animate.rotate(mn.PI / 2), right_square.animate.rotate(mn.PI / 4), run_time=2)
        self.wait(2)


class TwoTransforms(mn.Scene):
    """
    Transform vs ReplacementTransform
    В Manim оба эти класса нужны для превращения одного объекта в другой, но между ними есть принципиальная разница в том,
    какой объект физически остается в памяти сцены после завершения анимации.
    1. Transform(A, B)
    Что делает? Перерисовывает точки объекта A, придавая ему форму и свойства объекта B.
    Кто остается на сцене? Объект A (принявший вид B).
    Дальнейшая анимируемость: Вы продолжаете управлять объектом A.
    2. ReplacementTransform(A, B)
    Что делает? Заменяет объект A на объект B и удаляет A из сцены.
    Кто остается на сцене? Объект B.
    Дальнейшая анимируемость: Вы продолжаете управлять объектом B.

    Что использовать и когда?Используйте ReplacementTransform почти всегда, когда вы логически переходите от одной
    переменной к другой в длинном сценарии (например: Шаг 1: Формула А $\rightarrow$ Шаг 2: Формула Б $\rightarrow$
    Шаг 3: Формула В). Это защитит вас от путаницы в именах переменных.Используйте Transform,
    если вам нужно временно изменить один и тот же объект и вы планируете продолжать работать
    с его первично объявленным именем в коде.
    """
    def transform(self):
        a = mn.Circle(color=mn.PINK, fill_opacity=0.7)
        b = mn.Square(color=mn.BLUE, fill_opacity=0.7)
        c = mn.Triangle(color=mn.GREEN, fill_opacity=0.7)

        self.play(Create(a), run_time=2)
        self.play(mn.Transform(a, b), run_time=2)
        self.play(mn.Transform(a, c), run_time=2)
        self.play(mn.FadeOut(a))

    def replacement_transform(self):
        a = mn.Circle()
        b = mn.Square()
        c = mn.Triangle()
        self.play(mn.ReplacementTransform(a, b))
        self.play(mn.ReplacementTransform(b, c))
        self.play(mn.FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(2)
        self.replacement_transform()