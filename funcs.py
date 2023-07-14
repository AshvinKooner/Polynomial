import re

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

def get_order(terms):
    # Find highest power in expression given as list of tuples (coeff, power)
    powers = []
    for term in terms:
        powers.append(term[1])
    return max(powers)

def normalise(terms):
    # Fill any missing terms with coeff 0 (for purpose of poly division)
    order = get_order(terms)
    mapping = {} #power:coefficient
    for term in terms:
        # Fill in the power-coeff pairings already present
        mapping[term[1]] = term[0]
    normalised = []
    for i in range(order, -1, -1):
        if i in mapping:
            normalised.append((mapping[i], i))
        else:
            # Add placeholder if the power of x isn't present
            normalised.append((0, i))
    return normalised
        
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
            if coeff > 0:
                # Positive constant
                coeffstr = f" + {coeff}"
            else:
                # Negative constant
                coeffstr = f" - {-coeff}"
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
