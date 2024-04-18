#Validar si una palabra es palindromo

text = input ("Ingrese una palabra o frase: ")
def palindromo (text):
    reversed = str(text).lower()
    print (reversed, reversed [::-1])
    if reversed == reversed [::-1]:
        return True
    else:
        return False
    
print (palindromo (text))