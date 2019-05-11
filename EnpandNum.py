# Number in expanded form

def expand_me():
    num = int(input("Let me have your integer:  "))
    a = (num // 10) * 10
    b = num % 10
    c = float(a+b)
    return a, "+", b, "=  ", c

print(expand_me())