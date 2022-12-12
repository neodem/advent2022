from classes import CRT

c = CRT(40, 6)
c.draw()
print()
c.draw_pixel(0, '$')
c.draw_pixel(39, '$')
c.draw_pixel(40, '$')
c.draw()