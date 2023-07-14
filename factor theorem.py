def get_expression(highest_degree : int):
    coeff = []
    for i in range(highest_degree, -1, -1):
        if i == 0:
            msg = "Enter the constant: "
        elif i == 1:
            msg = "Enter coefficient of x: "
        else:
            msg = f"Enter coefficient of x^{i}: "
        coeff.append(int(input(msg)))
    return coeff

# Get main expression (test if factor of this)
print("****Enter details of the expression****")
highest_degree_exp = int(input("Enter the degree of the highest power: "))
coeff_exp = get_expression(highest_degree_exp)

# Get factor to test and find solution to factor = 0
print("****Enter details of the factor****")
highest_degree_fac = 1
coeff_fac = get_expression(highest_degree_fac)
solution = (coeff_fac[1] / coeff_fac[0]) * -1
print(solution)

# Test this solution in the expression
total = 0
for i in range(len(coeff_exp)):
    coeff = coeff_exp[i]
    power = highest_degree_exp - i
    total += coeff * (solution**power)
print(total)

