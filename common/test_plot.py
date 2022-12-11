from common import Plot

p = Plot(10, 10, 5, 5)
p.set_point(1, 0, "A")
p.set_point(0, 1, "B")
p.set_point(-1, 0, "C")
p.set_point(0, -1, "D")

p.print_plot(1)
