import math

def suma(a, b):
    pr = a[0] + b[0]
    pi = a[1] + b[1]
    return (pr, pi)

def producto(a, b):
    pr = a[0] * b[0] - (a[1] * b[1])
    pi = (a[0] * b[1] + a[1] * b[0])
    return (pr, pi)

def resta(a, b):
    pr = a[0] - b[0]
    pi = a[1] - b[1]
    return (pr, pi)


def division(a, b):
    pr = (a[0] * b[0] + a[1] * b[1]) / ((b[0]) ** 2 + (b[1]) ** 2)
    pi = (a[1] * b[0] - a[0] * b[1]) / ((b[0] ** 2) + (b[1] ** 2))
    return (pr, pi)


def modulo(a):
    pr = (a[0] ** 2 + a[1] ** 2) ** (1 / 2)
    return (pr)


def conjugado(a):
    pr = a[0]
    pi = -a[1]
    return (pr, pi)


def polar_cartesiano(a):
    pr = a[0] * math.cos(a[1])
    pi = a[0] * math.sin(a[1])
    return (pr, pi)


def cartesiano_polar(a):
    pr = modulo(a) * math.cos(fase(a))
    pi = modulo(a) * math.sin(fase(a))
    return (pr, pi)


def fase(a):
    fase = math.atan(a[1] / a[0])
    return (fase)


if __name__ == "__main__":
    c1 = (0, 1)
    c2 = (0, 1)