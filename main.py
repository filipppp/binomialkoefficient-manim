from manimlib.imports import *
import sys
sys.path.append("E:\\3b1b\\")
from customs import MarkingMobject, ZoomInAndOut

class PermutationScene(Scene):
    def construct(self):
        # All SVGs from students
        svg_m = SVGMobject("student")
        svg_r = svg_m.copy()
        svg_r.next_to(svg_m, 2*RIGHT)
        svg_rr = svg_r.copy()
        svg_rr.next_to(svg_r, 2*RIGHT)

        svg_l = SVGMobject("student")
        svg_l.next_to(svg_m, 2*LEFT)
        svg_ll = svg_l.copy()
        svg_ll.next_to(svg_l, 2*LEFT)
        svgs = [svg_ll, svg_l, svg_m, svg_r, svg_rr]

        # Animate Rectangles including moving to the bottom and changing colors
        self.play(DrawBorderThenFill(svg_m, rate_func=linear))
        self.wait(2)
        self.play(ReplacementTransform(svg_m.copy(), svg_r), ReplacementTransform(svg_m.copy(), svg_l), ReplacementTransform(svg_m.copy(), svg_rr), ReplacementTransform(svg_m.copy(), svg_ll))
        self.play(ApplyMethod(svg_m.set_color, GREEN), ApplyMethod(svg_rr.set_color, YELLOW), ApplyMethod(svg_r.set_color, RED), ApplyMethod(svg_l.set_color, BLUE), ApplyMethod(svg_ll.set_color, PURPLE))

        def ZoomInAndMove(mob):
            mob.shift(0.35*BOTTOM)
            mob.scale(0.5)
            return mob
        self.play(ApplyFunction(ZoomInAndMove, VGroup(*svgs)), run_time=1)
        self.wait(2)

        # Create Titles for student svgs and align + write them
        text_m = TextMobject("Eve")
        text_r = TextMobject("Alice")
        text_rr = TextMobject("Bob")
        text_l = TextMobject("Daniel")
        text_ll = TextMobject("Ted")
        texts = [text_ll, text_l, text_m, text_r, text_rr]
        for i, text in enumerate(texts):
            text.next_to(svgs[i], 0.1*TOP)
            text.scale(0.5)
        self.play(*[Write(text) for text in texts])
        self.wait(5)
        # Create squares to show different permutations
        square_l = Square().shift(1.2*LEFT).shift(0.35*TOP)
        square_r = Square().shift(1.2*RIGHT).shift(0.35*TOP)

        self.play(FadeInFromDown(square_l), FadeInFromDown(square_r))
        self.wait(3)
        # Algorithm for permutations
        for i in range(len(svgs)):
            main_group = Group(svgs[i], texts[i])
            main_pos = main_group.get_center()
            self.play(main_group.move_to, square_l)
            for j in range(len(svgs)):
                if i != j:
                    second_group = Group(svgs[j], texts[j])
                    second_pos = second_group.get_center()
                    self.play(second_group.move_to, square_r, run_time=0.3)
                    self.play(second_group.move_to, second_pos, run_time=0.3)
            self.play(main_group.move_to, main_pos, run_time=1)

        left_side_wo_symbol = Group(*svgs, *texts, square_l, square_r)
        sum_symbol = TexMobject("\sum").scale(2.2).next_to(left_side_wo_symbol, 1.7*LEFT).set_y(0)
        left_side = Group(left_side_wo_symbol, sum_symbol)

        equal = TexMobject("=").scale(3).shift(0.7*RIGHT)
        result = TexMobject("5", "\cdot", "4").scale(3).next_to(equal, 5*RIGHT)

        # Show Result
        self.wait(2)
        self.play(left_side_wo_symbol.scale, 0.7, run_time=1)
        self.play(Write(sum_symbol))
        self.play(left_side.to_edge, LEFT, run_time= 1)
        self.play(Write(equal), Write(result))
        self.wait(2)

        # Explain Result
        def start_indication(mob):
            mob.scale_in_place(1.2)
            mob.set_color(YELLOW)
            return mob
        def end_indication(mob):
            mob.scale_in_place(1/1.2)
            mob.set_color(WHITE)
            return mob
        self.play(ApplyFunction(start_indication, square_l))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(Group(*svgs, *texts)), ShowCreationThenDestructionAround(result[0]), run_time=3)
        self.wait(2)
        self.play(ApplyFunction(end_indication, square_l))
        self.wait(3)

        # Explain Second Part of the result
        temp_group = Group(svgs[0], texts[0])
        temp_pos = temp_group.get_center()
        self.play(ApplyMethod(temp_group.move_to, square_l))
        self.wait(2)
        self.play(ApplyFunction(start_indication, square_r))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(Group(*svgs[1:], *texts[1:])), ShowCreationThenDestructionAround(result[2]), run_time=3)
        self.wait(2)
        self.play(ApplyFunction(end_indication, square_r))
        self.play(ApplyMethod(temp_group.move_to, temp_pos))
        self.wait(3)

        # add braces
        n_brace = Brace(Group(*svgs)).set_color(BLUE)
        n_brace_text = n_brace.get_tex("n"," = 5").set_color(BLUE)
        self.play(GrowFromCenter(n_brace), FadeIn(n_brace_text))
        self.wait(11)

        k_brace = Brace(Group(square_l, square_r), UP).set_color(GREEN)
        k_brace_text = k_brace.get_tex("k"," = 2").set_color(GREEN)
        self.play(GrowFromCenter(k_brace), FadeIn(k_brace_text))
        self.wait(11)

        main_brace = Brace(result).set_color(RED)
        main_text = main_brace.get_tex("{n", "! ", "\over", "(", "n","-","k",")!}", " = ", "{ ", "5 \cdot 4 ", "\cdot", "3 \cdot 2 \cdot 1", "\over", "3 \cdot 2 \cdot 1}").scale(1.3)

        # n
        main_text[0].set_color(BLUE)
        main_text[4].set_color(BLUE)
        # k
        main_text[6].set_color(GREEN)


        original_left_pos = main_text[:8].get_center()
        main_text[:8].move_to(main_text.get_center())
        self.play(GrowFromCenter(main_brace), FadeIn(Group(main_text[1:4], main_text[5], main_text[7])), ReplacementTransform(n_brace_text[0].copy(), main_text[0]), ReplacementTransform(n_brace_text[0].copy(), main_text[4]), ReplacementTransform(k_brace_text[0].copy(), main_text[6]))
        self.wait(8)
        self.play(ReplacementTransform(result.copy(), main_text[10]), FadeIn(main_text[8:10]), FadeIn(main_text[11:]), ApplyMethod(main_text[:8].move_to, original_left_pos))
        self.wait(4)

        # Kürzen
        cross1 = Line(main_text[-1].get_left(), main_text[-1].get_right()).set_color(RED)
        cross2 = Line(main_text[-3].get_left(), main_text[-3].get_right()).set_color(RED)

        self.play(GrowFromEdge(cross1, LEFT), GrowFromEdge(cross2, LEFT))
        self.play(FadeOut(cross1), FadeOut(cross2), FadeOut(main_text[9]), FadeOut(main_text[11:]))
        self.play(ApplyMethod(main_text[10].next_to, Group(main_text[9:]).get_left()))
        self.play(Indicate(main_text[10]))
        self.wait(0.2)
        self.play(Indicate(result))
        self.wait(4)

        # Show similarity
        def scale_up_and_move(mob):
            mob.scale_in_place(2)
            mob.move_to(ORIGIN)
            return mob
        # GRÖ?TEN PART FERTIG
        self.play(FadeOut(left_side), FadeOut(Group(main_brace, k_brace, n_brace, n_brace_text, k_brace_text, main_text[8:11], result, equal)), ApplyFunction(scale_up_and_move, main_text[:8]))
        self.wait(2)
        self.play(ApplyMethod(main_text[:8].scale_in_place, 0.6))
        self.wait(2)

class CompareGeneralizationScene(Scene):
    def construct(self):
        general = MarkingMobject(r"{n! \over (n - k)!} ", r"\XYEQ {n! \over ", "k!", "\cdot (n-k)!}",).scale(1.56)
        left_eq = general[:7]
        original_pos = left_eq.get_center()
        left_eq.move_to(ORIGIN)
        k_factorial = general[10:12]

        self.play(ApplyMethod(left_eq.move_to, original_pos), FadeIn(general[7:]))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(general[10:12]), run_time=6)
        self.wait(2)
        self.play(ApplyMethod(k_factorial.move_to, ORIGIN), FadeOut(general[:10]), FadeOut(general[12:]))
        self.wait(2)

class WhatIsKFactorialScene(Scene):
    def construct(self):
        equation = MarkingMobject("k!", "=", r"\platzhalter ???").scale(1.56)
        definition = TextMobject("How often can you rearrange a", "certain combination")
        definition_p2 = TextMobject(" so it's still the ", "same", "one?").next_to(definition, 0.5*BOTTOM)

        k_factorial = equation[:2]
        original_k_pos = k_factorial.get_center()
        k_factorial.move_to(ORIGIN)

        self.play(ApplyMethod(k_factorial.move_to, original_k_pos), FadeIn(equation[2]))
        self.wait(1)
        self.play(Write(equation[3:]))
        self.wait(1)
        self.play(ApplyMethod(k_factorial.move_to, ORIGIN+0.35*TOP), FadeOut(equation[2:]))
        self.wait(1)
        self.play(Write(definition))
        self.play(Write(definition_p2))
        self.wait(3)
        self.play(Indicate(definition[1]))
        self.wait(1.5)
        self.play(Indicate(definition_p2[1]))
        self.wait(9)

class ComparisonScene(Scene):
    def construct(self):
        square_l = Square().shift(1.2 * LEFT)
        square_r = Square().shift(1.2 * RIGHT)
        main_svg = SVGMobject("student").move_to(square_l).set_color(RED).scale(0.5)
        second_svg = SVGMobject("student").move_to(square_r).set_color(BLUE).scale(0.5)
        group1 = Group(square_l, square_r, main_svg, second_svg).shift(4*LEFT).scale(0.5)

        plus_symbol = TexMobject("+").next_to(group1, 3*RIGHT).scale(2)

        square_l2 = Square().shift(1.2 * LEFT)
        square_r2 = Square().shift(1.2 * RIGHT)
        main_svg2 = SVGMobject("student").move_to(square_l2).set_color(BLUE).scale(0.5)
        second_svg2 = SVGMobject("student").move_to(square_r2).set_color(RED).scale(0.5)
        group2 = Group(square_l2, square_r2, main_svg2, second_svg2).scale(0.5)
        equals = TexMobject("=").shift(2.5*RIGHT).scale(2)
        two = TexMobject("2").next_to(equals, 2.5*RIGHT).scale(2)
        one = TexMobject("1").next_to(equals, 2.5 * RIGHT).scale(2)

        cross = SVGMobject("cross").move_to(one).set_color(RED).scale(0.5)

        self.play(FadeInFromDown(group1), FadeInFromDown(group2), FadeInFromDown(plus_symbol), run_time=1)
        self.wait(2)
        self.play(FadeInFromDown(equals), FadeInFromDown(two))
        self.wait(6)
        self.play(Write(cross))
        self.wait(1)
        self.play(FadeOut(cross))
        self.wait(3)
        self.play(ReplacementTransform(two, one))
        self.wait(1)
        self.play(ApplyMethod(equals.move_to, ORIGIN), ApplyMethod(group2.move_to, ORIGIN+2*RIGHT), ApplyMethod(group1.move_to, ORIGIN+2*LEFT), FadeOut(one), FadeOut(plus_symbol))
        self.wait(1)
        self.play(Indicate(group1), Indicate(group2))
        self.wait(0.5)
        self.play(Indicate(equals))
        self.wait(4)

class FormulaScene(Scene):
    def construct(self):
        binom = MarkingMobject("{n \choose k}", "= {n! \over k! \cdot (n - k)!}").scale_in_place(2)
        definition = TextMobject('"On how many ways can you arrange ', "$n$",  "Students on ", "$k$", 'chairs?"').shift(0.3*BOTTOM)
        definition[1].set_color(BLUE)
        definition[3].set_color(GREEN)

        binom[:5].set_color(WHITE)
        binom[2][0].set_color(BLUE)
        binom[2][1].set_color(GREEN)

        original_pos = binom[:5].get_center()
        binom[:5].set_x(0).set_y(0).shift(0.5*RIGHT)

        self.play(FadeIn(binom[:5]))
        self.wait(27)
        self.play(ApplyMethod(binom[:5].shift, 0.3*TOP))
        self.wait(1)
        self.play(Write(definition))
        self.play(ZoomInAndOut(definition[1]), ZoomInAndOut(binom[2][0]))
        self.play(ZoomInAndOut(definition[3]), ZoomInAndOut(binom[2][1]))
        self.wait(2)
        self.play(FadeOutAndShiftDown(definition))
        self.wait(2)
        self.play(ApplyMethod(binom[:5].move_to, original_pos))
        self.wait(0.5)
        self.play(Write(binom[5:]))
        self.wait(10)

class ExplainKFactorialScene(Scene):
    def construct(self):
        square_l = Square()
        square_m = Square()
        square_r = Square()

        person_l = SVGMobject("student").set_color(RED)
        person_m = SVGMobject("student").set_color(GREEN)
        person_r = SVGMobject("student").set_color(BLUE)

        squares = VGroup(square_l, square_m, square_r).arrange_submobjects(RIGHT)

        text_m = TextMobject("Eve")
        text_r = TextMobject("Alice")
        text_l = TextMobject("Daniel")
        texts = [text_l, text_m, text_r]
        persons_arr = [person_l, person_m, person_r]
        for i, text in enumerate(texts):
            text.next_to(persons_arr[i], 0.3*TOP)
            text.scale(1)

        persons = VGroup(VGroup(person_l, text_l), VGroup(person_m, text_m), VGroup(person_r, text_r)).scale(0.6)
        persons[0].move_to(square_l)
        persons[2].move_to(square_r)
        persons[1].move_to(square_m)
        # Explain Result
        def start_indication(mob):
            mob.scale_in_place(1.1)
            mob.set_color(YELLOW)
            return mob
        def end_indication(mob):
            mob.scale_in_place(1/1.1)
            mob.set_color(WHITE)
            return mob

        equation = TexMobject("=", "3", "\cdot 2", "\cdot 1", "k", "!").scale(2)
        equation[4].set_color(GREEN)
        equation.set_opacity(0)
        self.play(FadeIn(squares), FadeIn(persons))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(VGroup(squares, persons)), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(VGroup(squares, persons).arrange_submobjects, BOTTOM))
        self.play(ApplyMethod(persons[0].shift, RIGHT), ApplyMethod(persons[2].shift, LEFT))
        self.wait(2)
        self.play(ApplyMethod(VGroup(VGroup(squares, persons), equation).arrange_submobjects, RIGHT))
        self.wait(2)
        equation.shift(RIGHT)
        self.play(ApplyMethod(equation[0].set_opacity, 1))

        self.play(ApplyFunction(start_indication, square_l))
        self.wait(1)
        self.play(ShowCreationThenDestructionAround(persons), run_time=3)
        self.play(ReplacementTransform(persons.copy(), equation[1]), ApplyMethod(equation[1].set_opacity, 1))
        self.wait(0.5)
        self.play(ApplyFunction(end_indication, square_l))

        self.play(persons[0].move_to, square_l)
        self.wait(1)
        self.play(ApplyFunction(start_indication, square_m))
        self.wait(1)
        self.play(ShowCreationThenDestructionAround(persons[1:]), run_time=2)
        self.play(ReplacementTransform(persons[1:].copy(), equation[2]), ApplyMethod(equation[2].set_opacity, 1))
        self.wait(0.5)
        self.play(ApplyFunction(end_indication, square_m))

        self.play(persons[1].move_to, square_m)
        self.wait(1)
        self.play(ApplyFunction(start_indication, square_r))
        self.wait(1)
        self.play(ShowCreationThenDestructionAround(persons[2:]), run_time=1)
        self.play(ReplacementTransform(persons[2:].copy(), equation[3]), ApplyMethod(equation[3].set_opacity, 1))
        self.wait(0.5)
        self.play(ApplyFunction(end_indication, square_r))
        self.wait(2)

        self.play(persons[2].move_to, square_r)
        self.play(VGroup(persons, squares).set_y, 0)
        self.wait(1)

        # show brace
        k_brace = Brace(Group(square_l, square_m, square_r), UP).set_color(GREEN)
        k_brace_text = k_brace.get_tex("k"," = 3").set_color(GREEN)
        self.play(GrowFromCenter(k_brace), FadeIn(k_brace_text))

        self.wait(1)
        left_pos_eq = equation[1:4].get_left()
        equation[4:].move_to(left_pos_eq).shift(RIGHT)

        self.play(ReplacementTransform(equation[1:4], equation[4:]), ApplyMethod(equation[4:].set_opacity, 1))
        self.wait(5)

class ContinuedPermutationScene(Scene):
    def construct(self):
        # All SVGs from students
        svg_m = SVGMobject("student")
        svg_r = svg_m.copy()
        svg_r.next_to(svg_m, 2*RIGHT)
        svg_rr = svg_r.copy()
        svg_rr.next_to(svg_r, 2*RIGHT)

        svg_l = SVGMobject("student")
        svg_l.next_to(svg_m, 2*LEFT)
        svg_ll = svg_l.copy()
        svg_ll.next_to(svg_l, 2*LEFT)
        svgs = [svg_ll, svg_l, svg_m, svg_r, svg_rr]

        # Animate Rectangles including moving to the bottom and changing colors
        self.play(DrawBorderThenFill(svg_m, rate_func=linear))
        self.wait(2)
        self.play(ReplacementTransform(svg_m.copy(), svg_r), ReplacementTransform(svg_m.copy(), svg_l), ReplacementTransform(svg_m.copy(), svg_rr), ReplacementTransform(svg_m.copy(), svg_ll))
        self.play(ApplyMethod(svg_m.set_color, GREEN), ApplyMethod(svg_rr.set_color, YELLOW), ApplyMethod(svg_r.set_color, RED), ApplyMethod(svg_l.set_color, BLUE), ApplyMethod(svg_ll.set_color, PURPLE))

        def ZoomInAndMove(mob):
            mob.shift(0.35*BOTTOM)
            mob.scale(0.5)
            return mob
        self.play(ApplyFunction(ZoomInAndMove, VGroup(*svgs)), run_time=1)
        self.wait(2)

        # Create Titles for student svgs and align + write them
        text_m = TextMobject("Eve")
        text_r = TextMobject("Alice")
        text_rr = TextMobject("Bob")
        text_l = TextMobject("Daniel")
        text_ll = TextMobject("Ted")
        texts = [text_ll, text_l, text_m, text_r, text_rr]
        for i, text in enumerate(texts):
            text.next_to(svgs[i], 0.1*TOP)
            text.scale(0.5)
        self.play(*[Write(text) for text in texts])
        self.wait(3)
        # Create squares to show different permutations
        square_l = Square().shift(1.2*LEFT).shift(0.35*TOP)
        square_r = Square().shift(1.2*RIGHT).shift(0.35*TOP)

        self.play(FadeInFromDown(square_l), FadeInFromDown(square_r))
        # Algorithm for permutations
        for i in range(len(svgs)):
            break
            main_group = Group(svgs[i], texts[i])
            main_pos = main_group.get_center()
            self.play(main_group.move_to, square_l)
            for j in range(len(svgs)):
                if i != j:
                    second_group = Group(svgs[j], texts[j])
                    second_pos = second_group.get_center()
                    self.play(second_group.move_to, square_r, run_time=0.3)
                    self.play(second_group.move_to, second_pos, run_time=0.3)
            self.play(main_group.move_to, main_pos, run_time=1)

        left_side_wo_symbol = Group(*svgs, *texts, square_l, square_r)
        sum_symbol = TexMobject("\sum").scale(2.2).next_to(left_side_wo_symbol, 1.7*LEFT).set_y(0)
        left_side = Group(left_side_wo_symbol, sum_symbol)

        equal = TexMobject("=").scale(3).shift(0.7*RIGHT)
        result = TexMobject("5", "\cdot", "4").scale(3).next_to(equal, 5*RIGHT)
        real_result = TexMobject("5 \cdot 4", "\over 2 \cdot 1").scale_in_place(2).move_to(result).shift(0.5*UP)
        calculated_result = TexMobject("10").scale_in_place(3).move_to(result)

        # Show Result
        self.wait(2)
        self.play(left_side_wo_symbol.scale, 0.7, run_time=1)
        self.play(Write(sum_symbol))
        self.play(left_side.to_edge, LEFT, run_time= 1)
        self.play(Write(equal), Write(result))
        self.wait(2)

        # Explain Result
        def start_indication(mob):
            mob.scale_in_place(1.2)
            mob.set_color(YELLOW)
            return mob
        def end_indication(mob):
            mob.scale_in_place(1/1.2)
            mob.set_color(WHITE)
            return mob
        self.play(ApplyFunction(start_indication, square_l))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(Group(*svgs, *texts)), ShowCreationThenDestructionAround(result[0]), run_time=3)
        self.wait(2)
        self.play(ApplyFunction(end_indication, square_l))
        self.wait(3)

        # Explain Second Part of the result
        temp_group = Group(svgs[0], texts[0])
        temp_pos = temp_group.get_center()
        self.play(ApplyMethod(temp_group.move_to, square_l))
        self.wait(2)
        self.play(ApplyFunction(start_indication, square_r))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(Group(*svgs[1:], *texts[1:])), ShowCreationThenDestructionAround(result[2]), run_time=3)
        self.wait(2)
        self.play(ApplyFunction(end_indication, square_r))
        self.play(ApplyMethod(temp_group.move_to, temp_pos))
        self.wait(3)

        # add braces
        k_brace = Brace(Group(square_l, square_r), UP).set_color(GREEN)
        k_brace_text = k_brace.get_tex("k"," = 2").set_color(GREEN)
        self.play(GrowFromCenter(k_brace), FadeIn(k_brace_text))
        self.wait(2)

        n_brace = Brace(Group(*svgs)).set_color(BLUE)
        n_brace_text = n_brace.get_tex("n"," = 5").set_color(BLUE)
        self.play(GrowFromCenter(n_brace), FadeIn(n_brace_text))
        self.wait(2)

        main_brace = Brace(result).set_color(RED)
        main_text = main_brace.get_tex("{n", "! ", "\over", "k", "!\cdot", "(", "n","-","k",")!}", "\over ", "k", "!").scale(1.3)
        main_text_real_formula = main_brace.get_tex("{n", "! ", "\over", "k", "!\cdot", "(", "n","-","k",")!}")

        # n
        main_text[0].set_color(BLUE)
        main_text[6].set_color(BLUE)
        main_text_real_formula[0].set_color(BLUE)
        main_text_real_formula[6].set_color(BLUE)
        # k
        main_text[3].set_color(GREEN)
        main_text[8].set_color(GREEN)
        main_text[11].set_color(GREEN)
        main_text_real_formula[3].set_color(GREEN)
        main_text_real_formula[8].set_color(GREEN)

        main_text_real_formula2 = main_text_real_formula.copy()

        before_x = main_text[5:10].get_x()
        main_text[5:10].set_x(main_text.get_center()[0])
        original_y = main_text.get_y()

        main_text_real_formula[5:10].set_x(main_text.get_x())

        self.play(GrowFromCenter(main_brace), FadeIn(main_text_real_formula[:3]), FadeIn(main_text_real_formula[5:]))
        self.wait(7)
        self.play(Indicate(result))
        self.wait(13)
        self.play(ReplacementTransform(main_text_real_formula[:3], main_text[:3]),
                  ReplacementTransform(main_text_real_formula[5:], main_text[5:10]),
                  FadeIn(main_text[10:]))
        main_text_real_formula[5:10].set_x(before_x)

        self.wait(6)
        def scale_and_set(mob):
            mob.scale_in_place(1.3)
            mob.set_y(original_y)
            return mob

        self.play(ReplacementTransform(main_text[11:13], main_text_real_formula2[3:5]),
                  FadeOut(main_text[10]),
                  ReplacementTransform(main_text[:3], main_text_real_formula2[:3]),
                  ReplacementTransform(main_text[5:10], main_text_real_formula2[5:]),
                  FadeOut(main_text[10]))
        self.play(ApplyFunction(scale_and_set, main_text_real_formula2))
        self.wait(3)
        self.play(ReplacementTransform(result, real_result[0]), FadeIn(real_result[1]))
        self.wait(2)
        self.play(ReplacementTransform(real_result, calculated_result))
        self.wait(2)
        self.play(Indicate(calculated_result))
        self.wait(4)
        self.play(Indicate(main_text_real_formula2))
        self.wait(1)

        def move_and_scale(mob):
            mob.scale_in_place(2)
            mob.move_to(ORIGIN)
            return mob

        self.play(ApplyFunction(move_and_scale, main_text_real_formula2), FadeOut(left_side), FadeOut(equal), FadeOut(calculated_result), FadeOut(Group(k_brace_text, k_brace, n_brace_text, n_brace, main_brace)))
        self.wait(7)
