import random
import decimal
from decimal import *
from random import uniform
import re
_=singular.lib('random.lib')
_=singular.lib('sing.lib')
possiblevars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
def automator(Num,variablecount,length):
    poly = ''
    successes = []
    for x in range(Num):
        poly = polynomial(variablecount,length)


def polynomial(variablecount,length):
    if(variablecount > 24):
        variablecount = 24
    vars = []
    final = []
    variables = '('
    s = 0
    for X in range(variablecount):
        s = randint(0,50)
        if s not in vars:
            vars.append(s)
            variables = variables + ',' + possiblevars[s]
    variables = variables[0]+variables[2:]+')'
    R = singular.ring(0,variables,'ds')
    poly = singular.sparsepoly(length);"";
    if singular.dim_slocus(poly) == 1:
        print(poly)

#find the milnor numbers when you test with a large exponent if milnor is below 200 or above 500
#find ones that have small changes in the milnor numbers when increased by 1

#  'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
