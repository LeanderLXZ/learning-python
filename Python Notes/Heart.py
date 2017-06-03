import sys
import math


def frange(start, end, step=1.0):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError('range() step must not be zero')


def f(x, y, z):
    a = x*x + 9.0/4*y*y + z*z - 1
    return a*a*a - x*x*z*z*z - 9.0/80*y*y*z*z*z


def h(x, z):
    for y in frange(1.0, 0.0, -0.001):
        if f(x, y, z) <= 0:
            return y
    return 0.0

if __name__ == '__main__':
    for z in frange(1.5, -1.5, -0.1):
        for x in frange(-1.5, 1.5, 0.05):
            v = f(x, 0, z)
            if v <= 0:
                y0 = h(x, z)
                ny = 0.01
                nx = h(x + ny, z) - y0
                nz = h(x, z + ny) - y0
                nd = 1.0/math.sqrt(nx*nx+ny*ny+nz*nz)
                d = (nx + ny - nz)*nd*0.5 + 0.5
                sys.stdout.write('.:-=+*#%@'[int(d*5)])
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')