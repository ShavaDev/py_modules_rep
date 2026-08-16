from manim import *
# from moviepy.editor import *

# для того, чтобы изменить задний фон надо прописать следующее:
# config.background_color = BLUE

class Theory(Scene):
    """
    Тут я поясню разницу между self.add() self.play(Create())
    Золотое правило Manim:
    Всё, что является контекстом/фоном — добавляйте через self.add().
    Всё, что является главной темой кадра в данный момент — заводите на экран через self.play(...).

    1. Используйте self.add() (Мгновенное добавление):
    Для фоновых и начальных объектов: Когда сцена только начинается, и вам нужно сразу показать координатную сетку,
    оси (Axes), фоновые фигуры или базовый текст без лишней суеты.
    При подготовке композиции: Когда объект будет анимироваться позже. Например, вы хотите добавить круг
    на сцену незаметно для зрителя, чтобы потом плавно сдвинуть его с помощью self.play(circle.animate.shift(...)).
    Для статических элементов: Шапки, логотипы, нумерация страниц — всё, что не требует внимания зрителя при рождении.

    2. Используйте self.play(Create()) (Анимированное рисование):
    Для акцента внимания: Когда вы хотите, чтобы зритель посмотрел именно на этот объект в момент его появления.
    Для математических доказательств и схем: Плавная прорисовка линий, векторов и геометрических фигур помогает зрителю уследить за логикой построения.
    При создании текста и формул: Демонстрация того, как с нуля появляется важное уравнение.
    """
    def construct(self):
        # Оси координат должны быть на экране сразу, их не нужно «рисовать»
        axes = Axes()
        self.add(axes)

        # А вот график функции рисуем плавно
        graph = axes.plot(lambda x: x ** 2)
        self.play(Create(graph), run_time=3)
        # тут все анимировано
        # self.play(Create(axes), run_time=2)
        # self.play(Create(graph), run_time=2)


class Example1(Scene):
    def construct(self):
        square = Square(color=GREEN, fill_opacity=1)
        # square = Square().set_fill(RED, opacity=1)
        # self.play(FadeIn(square), run_time=3) # обратное действие FadeOut, то есть красиво появляется
        # self.play(Rotate(square, PI), run_time=2)
        # self.play(FadeOut(square), run_time=2)
        self.play(square.animate.set_fill(YELLOW))
        self.wait()
        self.play(square.animate.shift(UP).rotate(PI/3))
        self.wait()


class Equation(Scene):
    """
    SurroundingRectangle (окаймляющий прямоугольник) — это специальный класс, который высчитывает габариты
    (высоту, ширину и центр) переданного ему объекта и строит вокруг него прямоугольную рамку.
    Первый аргумент (equation[0]) — объект, вокруг которого рисуется рамка.
    """
    def construct(self):
        equation = MathTex(r"\int_{-\infty}^\infty e^{-x^2}", "=", r"\sqrt{\pi}")

        self.play(Write(equation), run_time=2)

        framebox1 = SurroundingRectangle(equation[0], buff=.1) # Запись .1 — это просто стандартное сокращение в Python для числа 0.1 (ноль перед точкой можно опускать).
        framebox2 = SurroundingRectangle(equation[2], buff=.1)

        self.play(Create(framebox1))
        self.wait()

        self.play(ReplacementTransform(framebox1, framebox2))

        self.wait()


class MovingCamera(MovingCameraScene):
    """
    Класс MovingCameraScene добавляет на сцену специальный управляемый объект — self.camera.frame (рамка/объектив камеры).
    Всё, что попадает внутрь этой рамки, рендерится на весь экран.
    self.camera.frame
    Это прямоугольник, который определяет, куда смотрит камера и насколько близко она подошла.
    С ним можно работать как с любым обычным объектом Manim: двигать (move_to), менять размер (set_width / scale), поворачивать (rotate) и анимировать через .animate.
    """
    def construct(self):
        equation = MathTex(r"\int_{-\infty}^\infty e^{-x^2}", "=", r"\sqrt{\pi}")

        self.play(Write(equation), run_time=2)

        # работаем с камерой
        self.play(self.camera.frame.animate.move_to(equation[0]).set(width=equation[0].width*2))
        self.wait()
        self.play(self.camera.frame.animate.move_to(equation[2]).set(width=equation[2].width*2))

        self.wait()


