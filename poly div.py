import re

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

def extract_terms(expr_str):
    # Divide expression into terms
    patterns = ["[-]?[\d]{0,}x\\^[\d]{1,}", "[-]?[\d]{0,}x", "[-]?[\d]{1,}"]
    terms = re.findall("|".join(patterns), expr_str)
    return terms

def parse_terms(terms):
    parsed_terms = []
    for term in terms:
        if "x" in term:
            if "^" in term:
                # Power of x
                split = "x^"
            else:
                # Without a power
                split = "x"
            coeff, power = term.split(split)
            if coeff == "-":
                # Negative - no digit present
                coeff = -1
            elif len(coeff) > 0:
                # Digit(s) present
                coeff = int(coeff)
            else:
                # Positive - no digit present
                coeff = 1
            #coeff = int(coeff) if len(coeff) > 0 else 1
            power = int(power) if len(power) > 0 else 1
            parsed_terms.append((coeff, power))
        else:
            # Term is just a constant
            parsed_terms.append((int(term), 0))
    return parsed_terms


def get_expr():
    valid = False
    while not valid:
        expr_str = input("Enter expression (in form ax^n except for x and constant):\n").replace(" ", "")
        terms = extract_terms(expr_str)
        # Validate input
        length = 0
        for term in terms:
            length += len(term)
        #print(terms)
        #print(length, len(expr_str))
        expr_str = expr_str.replace("+", "")
        if length == len(expr_str):
            valid = True
        else:
            print("Please enter valid input of the form ax^n except for x^1 and constant")
    parsed_terms = parse_terms(terms)
    return parsed_terms

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

def get_order(terms):
    # Find highest power in expression given as list of tuples (coeff, power)
    powers = []
    for term in terms:
        powers.append(term[1])
    return max(powers)

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
    print(dividend)
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


def nicer_answer(answer):
    nice_answer = ""
    for term in answer:
        coeff, power = term
        if coeff.is_integer():
            coeff = int(coeff)
        if coeff == 0:
            # No term of the current order - placeholder so don't output
            continue
        elif coeff < 0:
            # Deal with negatives
            coeffstr = f" - {-coeff if coeff < -1 else ''}"
        else:
            # Deal with positives
            coeffstr = f" + {coeff if coeff > 1 else ''}"
        if power == 0:
            # Term is just a constant
            x = ""
        elif power == 1:
            # Just x
            x = "x"
        else:
            # A power of x
            x = f"x^{power}"
        nice_answer += f"{coeffstr}{x}"
    if nice_answer[0:3] == " + ":
        # Remove leading +, not needed
        nice_answer = nice_answer[3:]
    if nice_answer == "":
        # Placeholder
        nice_answer = "0"
    return nice_answer

print("answer:", nicer_answer(answer))
print("remainder:", nicer_answer(remainder))