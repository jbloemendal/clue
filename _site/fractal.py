import math
import turtle

def square():
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)

#turtle.begin_fill()
#square()
#turtle.color("yellow")
#turtle.end_fill()

m=6
n=16
r=math.ceil(n/2) # conditions (and / or) range(0,2^8), 0=and 1=or
xi=0

print(range(1, 2**r))
for m in range(-m, m):
    m=abs(m)
    q=m*(m+1)/2
    for x in range(math.ceil(-2**r/2), math.ceil(2**r/2)):
        x=abs(x)
        a=bin(x)[2:].count('0')
        o=bin(x)[2:].count('1')
        i=0
        xi=0
        for k in range(0, len(bin(x)[2:])):
            if bin(x)[2:][k]:
                i += (1+a)/(2*abs(r-k+1))
            else:
                i += (1+o)/(2*abs(r-k+1))
        xi += math.sqrt(q**2+i**2)
        print('m: %s, q:%s, i:%s, x:%s, xi:%s' % (m, q, i, bin(x)[2:], xi))

    # turtle.begin_fill()
    # square()
    # turtle.color("yellow")
    # turtle.end_fill()
    # d=((m*(m+1))/2)^2 + 

#turtle.mainloop()
