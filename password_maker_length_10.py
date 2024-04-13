def random_string(string, size):
    original_string = ""
    for i in range(0 , size):
        original_string += string[random.randint(0, len(string) - 1)]
        
    return original_string

def lowercasestring(string):
    return string.lower()

def password_creator(string1, string2, string3):
    string = ""
    string += random_string(string1, 3)
    string += random_string(string2, 3)
    string += random_string(string3, 4)
    return string

capital_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
smaller_string = lowercasestring(capital_string)
symbols = "!@#$%^&**()|?/.';"

print(password_creator(capital_string, smaller_string, symbols))

   
