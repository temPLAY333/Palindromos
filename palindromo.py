def IsthisaPalindromo(a):
    if a != str(a):
        return "No No No No No No"
    orig = a.lower()
    b = orig[::-1]
    b = b.replace(" ","")
    orig = orig. replace(" ","")
    if orig == b:
        return "Yes Yes Yes Yes Yes"