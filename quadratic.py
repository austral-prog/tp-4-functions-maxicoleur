# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante=b**2-(4*a*c)
    if discriminante<0:
        return "( )"
    r1 = (-b + (b ** 2 - 4 * a * c) ** (1/2))/2*a
    r2 = (-b - (b ** 2 - 4 * a * c) ** (1/2))/2*a
    if r1==r2:
        return f"({r1})"
    return f"({r1}, {r2})"


def value_y(a, b, c, x):
    valor_y=a*x**2+b*x+c
    return valor_y


def to_string(a, b, c):
    if a==0:
     if b==0:
      return f"f(x) = {c}"
     elif b!=0:
        return f"f(x) = {b} * X + {c}"
    if a!=0:
        if b==0:
            return f"f(x) = {a} * X^2 + {c}"
        elif b!=0:
            return f"f(x) = {a} * X^2 + {b} * X + {c}"



def derivation(a, b, c):
    if a ==0:
        if b ==0:
            return "f'(x) = 0"
        return f"f'(x) = {b}"
    if a>0:
        if b==0:
            return f"f'(x) = {2*a} * X"
        return f"f'(x) = {2*a} * X + {b}"



