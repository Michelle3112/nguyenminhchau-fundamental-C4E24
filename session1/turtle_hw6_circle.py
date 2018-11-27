from turtle import *

shape("arrow")
speed(0)

# 1 vòng tròn (hình3)
color("green")
fillcolor("yellow")
begin_fill()

circle(100)


end_fill()
mainloop() 

# 6 vòng tròn (hình4.1)
color("green")
for s in range (6):
 circle(100)
 left(60)

mainloop()

# multi vòng tròn (hình4.2)
color("green")
for s in range (100):
        circle(100)
        left(10)


mainloop()