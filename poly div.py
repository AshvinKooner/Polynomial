from funcs import get_expr, normalise, nicer_answer

# def get_expression(highest_degree : int):
#     expr = []
#     for i in range(highest_degree, -1, -1):
#         if i == 0:
#             msg = "Enter the constant: "
#         elif i == 1:
#             msg = "Enter coefficient of x: "
#         else:
#             msg = f"Enter coefficient of x^{i}: "
#         expr.append((int(input(msg)), i))
#     return expr


def divide_terms(dividend, divisor):
    coeff1, power1 = dividend
    coeff2, power2 = divisor
    new_coeff = coeff1 / coeff2
    new_power = power1 - power2
    return (new_coeff, new_power)

def mult_terms(term1, term2):
    coeff1, power1 = term1
    coeff2, power2 = term2
    new_coeff = coeff1 * coeff2
    new_power = power1 + power2
    return (new_coeff, new_power)

# h_order_dividend = int(input("Enter the highest order for the dividend: "))
# coeff_dividend = get_expression(h_order_dividend)
# valid = False
# while not valid:
#     h_order_divisor = int(input("Enter the highest order for the divisor (must be lower than dividend): "))
#     if h_order_divisor < h_order_dividend:
#         valid = True
# coeff_divisor = get_expression(h_order_divisor)

# coeff_answer = []
# for i in range(len(coeff_dividend) - 1, -1, -1):
#     term1 = (coeff_dividend[i], h_order_dividend-i)
#     term2 = (coeff_divisor[0], h_order_divisor)
#     result = divide_terms(term1, term2)
#     coeff_answer.append(result)

def sub_terms(term1, term2):
    # term1 - term2 (must have same power)
    coeff1, power1 = term1
    coeff2, power2 = term2
    new_coeff = coeff1 - coeff2
    return (new_coeff, power1)

def sub_expr(expr1, expr2):
    # Given 2 lists of (coeff, power) will do expr1 - expr2. Both must be same size and powers lined up.
    answer = []
    for i in range(len(expr1)):
        answer.append(sub_terms(expr1[i], expr2[i]))
    return answer

def mult_expr(expr, term):
    # Multiply all terms in expr (given as list of coeff, power pairs) by the term given
    answer = []
    for i in range(len(expr)):
        answer.append(mult_terms(expr[i], term))
    return answer

def poly_divide(dividend, divisor):
    #print(dividend)
    dividend = normalise(dividend)
    divisor = normalise(divisor)
    answer = []
    answer.append(divide_terms(dividend[0], divisor[0]))
    # Highest power of divisor
    #order_div = get_order(divisor)
    len_divisor = len(divisor)
    mult =  mult_expr(divisor[1:len_divisor], answer[-1])
    if len(dividend) > len_divisor:
        # Still need to recursively divide
        new_dividend = sub_expr(dividend[1:len_divisor], mult)
        new_dividend.extend(dividend[len_divisor:])
        #print(new_dividend)
        result, remainder = poly_divide(new_dividend, divisor)
        answer.extend(result)
    else:
        remainder = sub_expr(dividend[1:len_divisor], mult)
    return (answer, remainder)

print("*****DIVIDEND*****")
dividend = get_expr()
#print(dividend)
print("*****DIVISOR*****")
divisor = get_expr()
#print(divisor)
#print(poly_divide(dividend, divisor))
answer, remainder = poly_divide(dividend, divisor)
#print(answer)

print("answer:", nicer_answer(answer))
print("remainder:", nicer_answer(remainder))