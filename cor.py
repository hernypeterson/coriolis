from manim import *


class Intro(Scene):
	def construct(self):
		title = Tex(
			r"The Coriolis Effect", font_size=100
		)
		subtitle = Tex(
			r"\textit{a mathematical introduction}", font_size=35
		)
		subtitle.shift(DOWN)
		self.play(Write(title))
		self.wait()
		self.play(Write(subtitle))
		self.wait()
		self.play(FadeOut(title), FadeOut(subtitle))


class NonInert(Scene):
	def construct(self):
		ax = Axes(x_range=[-2, 2], y_range=[-2, 2], x_length=4, y_length=4)
		e = VGroup(Vector([0, 1], color=GREEN), Vector([1, 0], color=GREEN))
		self.play(Write(ax))
		self.play(Write(e))
		self.wait()

		func_complex = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
		field_complex = StreamLines(func_complex, stroke_width=1, max_anchors_per_line=30)
		self.add(field_complex)
		field_complex.start_animation(warm_up=True, flow_speed=1)
		self.wait(4)

		i_basis_2d = MathTex(
			r"\hat{\imath}", r"\ \ ", r"\hat{\jmath}", color=GREEN
		)
		self.play(FadeOut(field_complex), FadeOut(ax), ReplacementTransform(e[0], i_basis_2d[0]),
		          ReplacementTransform(e[1], i_basis_2d[2]))
		self.wait()
		r_i_basis_2d = MathTex(
			r"\textbf{r}", r"_i", r"=",
			r"r" r"_{\!x}", r"\hat{\imath}",
			r"+", r"r" r"_{\!y}", r"\hat{\jmath}",
		)
		self.play(TransformMatchingTex(i_basis_2d, r_i_basis_2d))
		r_i_basis = MathTex(
			r"\textbf{r}", r"_i", r"=",
			r"r" r"_{\!x}", r"\hat{\imath}",
			r"+", r"r" r"_{\!y}", r"\hat{\jmath}",
			r"+", r"r" r"_{\!z}", r"\hat{k}"
		)
		self.play(TransformMatchingTex(r_i_basis_2d, r_i_basis))
		self.wait()
		v_i_basis = MathTex(
			r"\textbf{v}", r"_i", r"=",
			r"v", r"_{\!x}", r"\hat{\imath}",
			r"+", r"v", r"_{\!y}", r"\hat{\jmath}",
			r"+", r"v", r"_{\!z}", r"\hat{k}"
		)
		a_i_basis = MathTex(
			r"\textbf{a}", r"_i", r"=",
			r"a", r"_{\!x}", r"\hat{\imath}",
			r"+", r"a", r"_{\!y}", r"\hat{\jmath}",
			r"+", r"a", r"_{\!z}", r"\hat{k}"
		)
		a_i_basis.shift(DOWN)
		self.play(r_i_basis.animate.shift(UP), Write(v_i_basis), Write(a_i_basis))
		self.play(FadeOut(r_i_basis), FadeOut(v_i_basis), FadeOut(a_i_basis))

		self.play(Write(ax))
		e_rot = VGroup(Vector([0, 1], color=GREEN), Vector([1, 0], color=GREEN))
		self.play(Write(e_rot))
		self.wait()
		func_rot = lambda pos: (pos[0] / 3 * UP + pos[1] / 3 * LEFT)
		field_rot = StreamLines(func_rot, stroke_width=1, max_anchors_per_line=30, max_color_scheme_value=4)
		self.add(field_rot)
		field_rot.start_animation(warm_up=True, flow_speed=1)
		self.wait(3)
		self.play(Rotating(ax), Rotating(e_rot), radians=TAU, run_time=2 * TAU * PI / 3,
		          about_point=ax.coords_to_point(0, 0))

		e_basis_2d = MathTex(
			r"\textbf{e}_1", r"\ \ ", r"\textbf{e}_2", color=GREEN
		)
		self.play(FadeOut(field_rot), FadeOut(ax), ReplacementTransform(e_rot[0], e_basis_2d[0]),
		          ReplacementTransform(e_rot[1], e_basis_2d[2]))

		self.wait()
		e_basis_2d_split = MathTex(
			r"\textbf{e}",
			r"_1", r"\ \ ", r"\textbf{e}",
			r"_2", color=GREEN
		)
		self.remove(e_basis_2d[0], e_basis_2d[2])
		r_basis_2d = MathTex(
			r"\textbf{r}", r"=",
			r"r", r"_1", r"\textbf{e}",
			r"_1",
			r"+", r"r", r"_2", r"\textbf{e}",
			r"_2",
		)
		self.play(TransformMatchingTex(e_basis_2d_split, r_basis_2d))
		r_basis = MathTex(
			r"\textbf{r}", r"=",
			r"r", r"_1", r"\textbf{e}",
			r"_1",
			r"+", r"r", r"_2", r"\textbf{e}",
			r"_2",
			r"+", r"r", r"_3", r"\textbf{e}",
			r"_3"
		)
		self.play(TransformMatchingTex(r_basis_2d, r_basis))
		self.wait()
		r_dot_e = MathTex(
			r"\textbf{r}", r"=",
			r"r", r"\cdot", r"\textbf{e}"
		)
		self.play(TransformMatchingTex(r_basis, r_dot_e))
		self.wait()
		v_dot_e = MathTex(
			r"\textbf{v}", r"=",
			r"v", r"\cdot", r"\textbf{e}"
		)
		a_dot_e = MathTex(
			r"\textbf{a}", r"=",
			r"a", r"\cdot", r"\textbf{e}"
		)
		a_dot_e.shift(DOWN)
		self.play(r_dot_e.animate.shift(UP), Write(v_dot_e), Write(a_dot_e))
		self.wait()
		self.play(FadeOut(r_dot_e), FadeOut(v_dot_e), FadeOut(a_dot_e))

		translation_1 = MathTex(
			r"\textbf{r}", r"=", r"f(", r"\textbf{r}_i", r")"
		)
		translation_2 = MathTex(
			r"\textbf{r}_i", r"=", r"f(", r"\textbf{r}", r")"
		)
		self.play(Write(translation_1))
		self.wait()
		self.play(TransformMatchingTex(translation_1, translation_2))
		self.wait()
		self.play(FadeOut(translation_2))


class AppForce(Scene):
	def construct(self):
		apparent_forces = Tex(
			r"Apparent Forces"
		)
		self.play(Write(apparent_forces))
		self.wait()
		self.play(FadeOut(apparent_forces))

		inert_ax = Axes(x_range=[-1, 1], y_range=[-1, 1], x_length=2, y_length=2)
		inert_ax.shift(4 * LEFT + DOWN)
		rot_ax = Axes(x_range=[-2, 2], y_range=[-2, 2], x_length=4, y_length=4)
		rot_dot = Dot(rot_ax.coords_to_point(-1.5, 1))

		x = DashedLine(inert_ax.c2p(0, 0), rot_ax.c2p(0, 0), color=BLUE).add_tip()
		r = rot_ax.get_lines_to_point(rot_ax.c2p(-1.5, 1), color=RED)
		e = VGroup(Vector([0, 1], color=GREEN), Vector([1, 0], color=GREEN))

		self.add(inert_ax, rot_ax, rot_dot, x, r, e)
		self.play(Rotating(rot_ax),
		          Rotating(rot_dot, about_point=rot_ax.coords_to_point(0, 0)),
		          Rotating(r, about_point=rot_ax.coords_to_point(0, 0)),
		          Rotating(e, about_point=rot_ax.coords_to_point(0, 0)))

		x_r_e = MathTex(
			r"\textbf{x}", r"\ \ ", r"r", r"\ \ ", r"\textbf{e}"
		)
		x_r_e.set_color_by_tex(r"\textbf{x}", BLUE)
		x_r_e.set_color_by_tex(r"r", RED)
		x_r_e.set_color_by_tex(r"\textbf{e}", GREEN)
		self.play(FadeOut(inert_ax, rot_ax, rot_dot))
		self.play(ReplacementTransform(x, x_r_e[0]),
		          ReplacementTransform(r, x_r_e[2]),
		          ReplacementTransform(e, x_r_e[4]))
		self.wait()

		x_plus_r_dot_e = MathTex(
			r"\textbf{r}_i", r"=",
			r"\textbf{x}",
			r"+", r"r", r"\cdot", r"\textbf{e}"
		)
		self.play(TransformMatchingTex(x_r_e, x_plus_r_dot_e))
		self.wait()
		x_plus_r_dot_e_ft = MathTex(
			r"\textbf{r}_i", r"(t)", r"=",
			r"\textbf{x}", r"(t)",
			r"+", r"r", r"(t)",
			r"\cdot", r"\textbf{e}", r"(t)"
		)
		self.play(TransformMatchingTex(x_plus_r_dot_e, x_plus_r_dot_e_ft))
		self.wait()
		self.play(TransformMatchingTex(x_plus_r_dot_e_ft, x_plus_r_dot_e))
		dr_i_dt_setup = MathTex(
			r"\frac{d\textbf{r}_i}{dt}="
			r"\frac{d\textbf{x}}{dt}",
			r"+", r"\frac{d}{dt}",
			r"\left(", r"r\cdot\textbf{e}", r"\right)"
		)
		self.play(TransformMatchingShapes(x_plus_r_dot_e, dr_i_dt_setup))
		self.wait()
		dr_i_dt_product_rule = MathTex(
			r"\frac{d\textbf{r}_i}{dt}="
			r"\frac{d\textbf{x}}{dt}",
			r"+", r"\left(",
			r"\frac{dr}{dt}\cdot\textbf{e}"
			r"+r\cdot\frac{d\textbf{e}}{dt}",
			r"\right)"
		)
		self.play(TransformMatchingTex(dr_i_dt_setup, dr_i_dt_product_rule))
		self.wait()
		v_i = MathTex(
			r"\textbf{v}_i="
			r"\dot{\textbf{x}}"
			r"+v\cdot\textbf{e}"
			r"+r\cdot\dot{\textbf{e}}"
		)
		self.play(TransformMatchingShapes(dr_i_dt_product_rule, v_i))
		self.wait()
		dv_i_dt_setup = MathTex(
			r"\frac{d\textbf{v}_i}{dt}", r"=",
			r"\frac{d\dot{\textbf{x}}}{dt}",
			r"+", r"\frac{d}{dt}",
			r"\left(", r"v\cdot\textbf{e}", r"\right)",
			r"+", r"\frac{d}{dt}",
			r"\left(", r"r\cdot\dot{\textbf{e}}", r"\right)"
		)
		self.play(TransformMatchingShapes(v_i, dv_i_dt_setup))
		self.wait()
		dv_i_dt_product_rule = MathTex(
			r"\frac{d\textbf{v}_i}{dt}", r"=",
			r"\frac{d\dot{\textbf{x}}}{dt}",
			r"+", r"\left(",
			r"\frac{dv}{dt}", r"\cdot", r"\textbf{e}",
			r"+", r"v", r"\cdot", r"\frac{d\textbf{e}}{dt}",
			r"\right)", r"+", r"\left(",
			r"\frac{dr}{dt}", r"\cdot", r"\dot{\textbf{e}}",
			r"+", r"r", r"\cdot", r"\frac{d\dot{\textbf{e}}}{dt}",
			r"\right)"
		)
		self.play(TransformMatchingTex(dv_i_dt_setup, dv_i_dt_product_rule))
		self.wait()
		a_i_expand = MathTex(
			r"\textbf{a}_i", r"=",
			r"\ddot{\textbf{x}}",
			r"+", r"\left(",
			r"a", r"\cdot", r"\textbf{e}",
			r"+", r"v", r"\cdot", r"\dot{\textbf{e}}",
			r"\right)", r"+", r"\left(",
			r"v", r"\cdot", r"\dot{\textbf{e}}",
			r"+", r"r", r"\cdot", r"\ddot{\textbf{e}}",
			r"\right)"
		)
		self.play(TransformMatchingTex(dv_i_dt_product_rule, a_i_expand))
		self.wait()
		a_i = MathTex(
			r"\textbf{a}_i="
			r"\ddot{\textbf{x}}"
			r"+\textbf{a}"
			r"+2v\cdot\dot{\textbf{e}}"
			r"+r\cdot\ddot{\textbf{e}}"
		)
		self.play(TransformMatchingShapes(a_i_expand, a_i))
		self.wait()
		a = MathTex(
			r"\textbf{a}", r"=",
			r"\textbf{a}_i", r"-\ddot{\textbf{x}}",
			r"-2", r"v", r"\cdot", r"\dot{\textbf{e}}",
			r"-", r"r", r"\cdot", r"\ddot{\textbf{e}}"
		)
		self.play(TransformMatchingShapes(a_i, a))
		self.wait()
		a_app_general = MathTex(
			r"\textbf{a}_\text{app.}", r"=",
			r"-\ddot{\textbf{x}}", r"-2", r"v", r"\cdot", r"\dot{\textbf{e}}",
			r"-", r"r", r"\cdot", r"\ddot{\textbf{e}}"
		)
		self.play(TransformMatchingTex(a, a_app_general))
		self.wait()
		self.play(FadeOut(a_app_general))

		stat_rot = Tex(
			r"Stationary Rotation"
		)
		self.play(Write(stat_rot))
		self.wait()
		stat_rot_conditions = Tex(
			r"\begin{enumerate}"
			r" \item Non-accelerating origin"
			r" \item \textbf{e}: Constant magnitude"
			r" \item \textbf{e}: Constant relative angle"
			r"\end{enumerate}"
		)
		self.play(ReplacementTransform(stat_rot, stat_rot_conditions))
		self.play(FadeOut(stat_rot_conditions))
		ang_vel = MathTex(
			r"|", r"\Omega", r"|", r"=",
			r"\frac{2\pi}{T}"
		)
		self.play(Write(ang_vel))
		self.wait()
		u_dot_rotation = MathTex(
			r"\dot{\textbf{u}}",
			r"=",
			r"\Omega",
			r"\times",
			r"\textbf{u}"
		)
		self.play(TransformMatchingTex(ang_vel, u_dot_rotation))
		self.wait()
		e_dot_rotation = MathTex(
			r"\dot{\textbf{e}}",
			r"=",
			r"\Omega",
			r"\times",
			r"\textbf{e}"
		)
		self.play(ReplacementTransform(u_dot_rotation, e_dot_rotation))
		self.wait()
		self.play(e_dot_rotation.animate.shift(UP))
		e_ddot_rotation_with_e_dot = MathTex(
			r"\ddot{\textbf{e}}",
			r"=",
			r"\dot{\Omega}",
			r"\times",
			r"\textbf{e}",
			r"+",
			r"\Omega",
			r"\times",
			r"\dot{\textbf{e}}"
		)
		self.play(Write(e_ddot_rotation_with_e_dot))
		self.wait()
		e_ddot_rotation_expand = MathTex(
			r"\ddot{\textbf{e}}", r"=", 
			r"\dot{\Omega}", r"\times", r"\textbf{e}", 
			r"+", r"\Omega", r"\times", 
			r"(", r"\Omega", r"\times", r"\textbf{e}", r")"
		)
		self.play(TransformMatchingTex(e_ddot_rotation_with_e_dot, e_ddot_rotation_expand))
		self.wait()
		e_ddot_rotation = MathTex(
			r"\ddot{\textbf{e}}",
			r"=", r"\dot{\Omega}", r"\times", r"\textbf{e}",
			r"-",
			r"|", r"\Omega", r"|^2", r"\textbf{e}"
		)
		self.play(TransformMatchingTex(e_ddot_rotation_expand, e_ddot_rotation))
		self.wait()
		self.play(e_dot_rotation.animate.shift(UP), e_ddot_rotation.animate.shift(UP))
		self.play(Write(a_app_general))
		a_app_stat = MathTex(
			r"\textbf{a}_\text{app.}",
			r"=", r"-2", r"v",
			r"\cdot", r"\dot{\textbf{e}}",
			r"-", r"r", r"\cdot", r"\ddot{\textbf{e}}"
		)
		self.play(TransformMatchingTex(a_app_general, a_app_stat))
		self.wait()
		a_app_rotation_with_e = MathTex(
			r"\textbf{a}_\text{app.}", r"=", 
			r"-2", r"v", r"\cdot", r"\Omega", 
			r"\times", r"\textbf{e}", r"-", r"r", 
			r"\cdot", r"(", r"\dot{\Omega}", r"\times", r"\textbf{e}", 
			r"-", r"|", r"\Omega", r"|", r"^2", r"\textbf{e}", r")",
		)
		self.play(TransformMatchingTex(a_app_stat, a_app_rotation_with_e))
		self.wait()
		self.play(FadeOut(e_dot_rotation), FadeOut(e_ddot_rotation))
		a_app_rotation_with_e_dist = MathTex(
			r"\textbf{a}_\text{app.}", r"=", r"-2", r"\Omega",
			r"\times", r"(", r"v", r"\cdot", r"\textbf{e}", r")", 
			r"-", r"\dot{\Omega}", r"\times", r"(", r"r", r"\cdot", r"\textbf{e}", r")",
			r"+", r"|", r"\Omega", r"|", r"^2", r"(", r"r", r"\cdot", r"\textbf{e}", r")"
		)
		self.play(TransformMatchingShapes(a_app_rotation_with_e, a_app_rotation_with_e_dist))
		self.wait()
		a_app_rotation_expand = MathTex(
			r"\textbf{a}_\text{app.}="
			r"-2\Omega\times\textbf{v}"
			r"-\dot{\Omega}\times\textbf{r}"
			r"+|\Omega|^2\textbf{r}"
		)
		self.play(TransformMatchingShapes(a_app_rotation_with_e_dist, a_app_rotation_expand))
		self.wait()
		a_app_rotation = MathTex(
			r"\textbf{a}", r"_\text{app.}",
			r"=",
			r"-2", r"\Omega\times\textbf{v}",
			r"-", r"\dot{\Omega}\times\textbf{r}",
			r"+", r"|\Omega|^2\textbf{r}"
		)
		self.play(TransformMatchingShapes(a_app_rotation_expand, a_app_rotation))
		self.wait()
		f_app_rotation_labeled = MathTex(
			r"\textbf{F}", r"_\text{app.}",
			r"=", r"-2", r"m", r"\Omega\times\textbf{v}",
			r"-", r"m", r"\dot{\Omega}\times\textbf{r}",
			r"+", r"m", r"|\Omega|^2\textbf{r}"
		)

		self.play(TransformMatchingTex(a_app_rotation, f_app_rotation_labeled))
		self.wait()

		coriolis_slice = slice(3, 6)
		euler_slice = slice(6, 9)
		centrifugal_slice = slice(10, 12)
		coriolis_frame = SurroundingRectangle(f_app_rotation_labeled[coriolis_slice], buff=.1, color=GREEN)
		euler_frame = SurroundingRectangle(f_app_rotation_labeled[euler_slice], buff=.1, color=RED)
		centrifugal_frame = SurroundingRectangle(f_app_rotation_labeled[centrifugal_slice], buff=.1, color=BLUE)
		self.play(Create(coriolis_frame))
		self.wait()
		self.play(ReplacementTransform(coriolis_frame, euler_frame))
		self.wait()
		self.play(ReplacementTransform(euler_frame, centrifugal_frame))
		self.wait()
		self.play(Uncreate(centrifugal_frame))
		self.wait()
		c_f = MathTex(
			r"\textbf{C}",
			r"=", r"-2", r"m",
			r"\Omega\times\textbf{v}"
		)
		self.play(TransformMatchingTex(f_app_rotation_labeled, c_f))
		self.wait()
		self.play(FadeOut(c_f))


class CorEarth(Scene):
	def construct(self):
		coriolis_earth = Tex(
			r"The Coriolis Effect on Earth"
		)
		self.play(Write(coriolis_earth))
		self.play(FadeOut(coriolis_earth))

		h_plane = MathTex(
			r"\Pi_h", r"\perp", r"\textbf{n}"
		)
		self.play(Write(h_plane))
		self.play(h_plane.animate.shift(UP))
		c_a = MathTex(
			r"\textbf{C}_a", r"=",
			r"-2",
			r"\Omega",
			r"\times",
			r"\textbf{v}"
		)
		self.play(Write(c_a))
		c_ah_proj = MathTex(
			r"\textbf{C}_{a(h)}", r"=",
			r"\text{proj}_{\Pi_h}",
			r"(", r"-2\Omega", r"\times", r"\textbf{v}", r")",
			r";\ ", r"\textbf{v}", r"\in", r"\Pi_h"
		)
		self.play(TransformMatchingShapes(c_a, c_ah_proj))
		self.wait()
		self.play(TransformMatchingShapes(c_ah_proj, c_a), FadeOut(h_plane))

		c_a_decompose_mag = MathTex(
			r"|", r"\textbf{C}_a", r"|", r"=",
			r"-2", r"|", r"\Omega", r"|",
			r"\cdot", r"|", r"\textbf{v}", r"|",
			r"\cdot", r"\sin", r"\theta"
		)
		c_a_decompose_dir = MathTex(
			r"\textbf{C}_a",
			r"\perp", r"\Omega", r";\ ",
			r"\textbf{C}_a",
			r"\perp", r"\textbf{v}"
		)
		c_a_decompose_dir.shift(.5 * DOWN)
		self.play(TransformMatchingTex(c_a, c_a_decompose_mag))
		self.play(c_a_decompose_mag.animate.shift(.5 * UP), Write(c_a_decompose_dir))
		self.wait()
		c_ah_decompose_dir = MathTex(
			r"\textbf{C}_{a(h)}",
			r"\perp", r"\textbf{n}", r";\ ",
			r"\textbf{C}_{a(h)}",
			r"\perp", r"\textbf{v}"
		)
		c_ah_decompose_dir.shift(.5 * DOWN)
		self.play(TransformMatchingShapes(c_a_decompose_dir, c_ah_decompose_dir))
		self.wait()
		self.play(FadeOut(c_ah_decompose_dir), c_a_decompose_mag.animate.shift(.5 * DOWN))


class HorizontalProjection(ThreeDScene):
	def construct(self):
		ax = ThreeDAxes()
		earth = Sphere(radius=3)

		self.add(ax, earth)


class Curvature(Scene):
	def construct(self):
		curvature = Tex(
			r"Curvature"
		)
		self.play(Write(curvature))
		self.play(FadeOut(curvature))

		p1 = np.array([-1, 1, 0])
		p2 = np.array([2, 1, 0])
		p3 = np.array([-2, -1, 0])
		p4 = np.array([3, -1, 0])
		arbitrary_path = CubicBezier(p1, p2, p3, p4)
		self.play(Write(arbitrary_path))


class Outro(Scene):
	def construct(self):
		banner = ManimBanner().scale(0.2)
		created = Tex(
			r"\textit{created by Henry Peterson with}", font_size=35
		)
		VGroup(created, banner).arrange(DOWN)
		self.play(Write(created))
		self.play(Write(banner))
		self.play(banner.expand())
		self.wait()
		self.play(FadeOut(banner, created))
