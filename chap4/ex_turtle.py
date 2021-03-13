
import turtle

bob = turtle.Turtle()
print(bob)
bob.speed(0)

n = 360

for i in range(n):
    bob.fd(1)
    bob.lt(360.0/n)


turtle.mainloop()