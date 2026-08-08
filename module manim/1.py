from __future__ import annotations

import manim
from manim import MathTex


class SquareToStar(manim.Scene):
    def construct(self):
        tex = manim.MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        self.play(manim.Write(tex))
        self.wait()
        # square = manim.Square()
        # square.set_fill(manim.GREEN, opacity=0.5)
        # star = manim.Star(outer_radius=2, color=manim.BLUE)
        # self.play(manim.Create(square))
        # self.play(manim.Transform(square, star))
        # self.play(manim.FadeOut(square))

if __name__ == "__main__":
    s = SquareToStar()
    scene = SquareToStar()
    scene.render()

