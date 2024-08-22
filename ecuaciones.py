import math

def sumar(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def restar(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def multiplicar(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imaginario)

def dividir(c1, c2):
    denom = c2[0]**2 + c2[1]**2
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / denom
    imaginario = (c1[1] * c2[0] - c1[0] * c2[1]) / denom
    return (real, imaginario)

def modulo(c):
    return math.sqrt(c[0]**2 + c[1]**2)

def conjugado(c):
    return (c[0], -c[1])

def cartesiano_a_polar(c):
    modulo = math.sqrt(c[0]**2 + c[1]**2)
    fase = math.atan2(c[1], c[0])
    return (modulo, fase)

def polar_a_cartesiano(p):
    real = p[0] * math.cos(p[1])
    imaginario = p[0] * math.sin(p[1])
    return (real, imaginario)

def fase(c):
    return math.atan2(c[1], c[0])


