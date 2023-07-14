from funcs import get_expr, get_order, substitute

# Get main expression (test if factor of this)
print("****Expression****")
expression = get_expr()

# Get factor to test and find solution to factor = 0. Factor must be linear.
valid = False
while not valid:
    print("****Factor****")
    factor = get_expr()
    if get_order(factor) == 1:
        valid = True
    else:
        print("Factor must be linear")
solution = -(factor[1][0] / factor[0][0])
#print(solution)

# Test this solution in the expression
rem = substitute(expression, solution)

if rem == 0:
    print("It is a factor")
else:
    print("Not a factor. Remainder:", rem)

