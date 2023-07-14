from funcs import get_expr, normalise, substitute, nicer_answer, get_order
from math import sqrt

def diff_power(terms):
    # Diff by power rule
    new_terms = []
    for term in terms:
        coeff, power = term
        new_c = coeff * power
        new_p = power - 1
        new_terms.append((new_c, new_p))
    return new_terms

def solve_quad(terms):
    # Solve quadratic
    terms = normalise(terms)
    a = terms[0][0]
    b = terms[1][0]
    c = terms[2][0]
    #print(a,b,c)
    solutions = []
    try:
        x1 = ( -b + sqrt(b**2 - 4*a*c) ) / (2*a)
        y1 = substitute(terms, x1)
        solutions.append((x1, y1))
    except:
        pass
    try:
        x2 = ( -b - sqrt(b**2 - 4*a*c) ) / (2*a)
        if x1 != x2:
            # If repeated root, only give one root
            y2 = substitute(terms, x2)
            solutions.append((x2, y2))
    except:
        pass
    return solutions

valid = False
while not valid:
    print("*****Enter a cubic expression*****")
    cubic = get_expr()
    if get_order(cubic) == 3:
        valid = True
quad = diff_power(cubic)
sols = solve_quad(quad)
xvals = (sols[i][0] for i in range(len(sols)))
coords = []
for x in xvals:
    coords.append((x, substitute(cubic, x)))

for coord in coords:
    print(f"Turning point at ({coord[0]}, {coord[1]})")