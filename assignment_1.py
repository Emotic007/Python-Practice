def is_valid_number(num: str) -> bool:
    """
    Returns True if and only if num is represents a valid number.
    See the corresponding .pdf for a definition of what a valid number
    would be.

    >>> is_valid_number("10")
    True
    >>> is_valid_number("-124")
    True
    >>> is_valid_number("12.9")
    True
    >>> is_valid_number("12.9.0")
    False
    >>> is_valid_number("abc")
    False
    """
    if "-" in num:
        num=num.lstrip("-")
    if num.isnumeric():
            return True
    elif num[-1]==".":
        return True
    elif num.count(".")==1 and num[-1]!=".":
            if num[:num.index(".")].isnumeric() and num[num.index(".")+1:].isnumeric():
                return True
    return False


def is_valid_term(term: str) -> bool:
    """
    Returns True if and only if num is represents a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> is_valid_term("44.4x^6")
    True
    >>> is_valid_term("-7x")
    True
    >>> is_valid_term("9.9")
    True
    >>> is_valid_term("7y**8")
    False
    >>> is_valid_term("7x^8.8")
    False
    >>> is_valid_term("7*x^8.8")
    False
    >>> is_valid_term("7x^ 8.8")
    False
    """
    if is_valid_number(term):
        return True
    
    elif term[-1]=="x" and is_valid_number(term[:-1]):
        return True
     
    elif "^" in term: 
        if is_valid_number(term[:term.index("^")-1]) and is_valid_number(term[term.index("^")+1:]):
            return True
        
    return False
    
def approx_equal(x: float, y: float, tol: float) -> bool:
    """
    Returns True if and only if x and y are within tol of each other.

    >>> approx_equal(5, 4, 1)
    True
    >>> approx_equal(5, 3, 1)
    False
    >>> approx_equal(0.999, 1, 0.001)
    True
    >>> approx_equal(0.999, 1, 0.0001)
    False
    """
    i=x-tol
    j=x+tol
    if i <=y and j >=y:
        return True
    return False


def degree_of(term: str) -> int:
    """
    Returns the degree of term, it is assumed that term is a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> degree_of("55x^6")
    6
    >>> degree_of("-1.5x")
    1
    >>> degree_of("252.192")
    0
    """
    if is_valid_term(term):
        if is_valid_number(term):
            return 0
        elif term[-1]=="x":
            return 1
        else:
            pow=int(term[term.index("^")+1:])
            return pow
    return False


def get_coefficient(term: str) -> float:
    """
    Returns the coefficient of term, it is assumed that term is a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> get_coefficient("55x^6")
    55
    >>> get_coefficient("-1.5x")
    -1.5
    >>> get_coefficient("252.192")
    252.192
    """
    if is_valid_term(term):
        if is_valid_number(term):
            return float(term)
        else:
            return float(term[:term.index("x")])

    return False



#Do not worry about the code past this point. 
#********************************************

def derive(poly):
    derivative = []
    degree = 1
    for coefficient in poly[1:]:
        derivative.append(coefficient*degree)
        degree += 1
    return derivative

def get_coefficients(terms):
    poly = []
    degree = 0
    for term in terms:
        while degree != degree_of(term):
            poly.append(0)
            degree += 1
        poly.append(get_coefficient(term))
        degree +=1
    return poly

def evaluate(poly, x):
    value = 0
    degree = 0
    for coefficient in poly:
        degree += 1
        value += coefficient * x**degree
    return value
        

if __name__ == "__main__":
    poly_string = input("Please enter a polynomial: ")
    terms = poly_string.strip().split("+")

    valid_poly = True
    for term in terms:
        if not is_valid_term(term):
            valid_poly = False

    while not valid_poly:
        poly_string = input("Incorrect format. Please enter a polynomial: ")
        terms = poly_string.strip().split("+")

        valid_poly = True
        for term in terms:
            if not is_valid_term(term):
                valid_poly = False
            
    poly = get_coefficients(terms)
    derivative = derive(poly)
    current_value = float(input("Please enter a starting point: "))
    tol = float(input("Please enter a tolerance: "))
    
    next_value = current_value - (evaluate(poly, current_value)/evaluate(derivative, current_value))
    while not(approx_equal(current_value, next_value, tol)):
        current_value = next_value
        next_value = current_value - (evaluate(poly, current_value)/evaluate(derivative, current_value))
    print("The polynoimal has a 'zero' approximately at: " + str(next_value))
    
