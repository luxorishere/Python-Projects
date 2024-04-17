
def base_to_decimal(number, base):
    decimal = 0
    i = 0
    while number != 0:
        p = base**i
        decimal = (decimal) + ((number % 10) * p)
        i += 1
        number //= 10
    return decimal

def decimal_to_base(number, base):
    list = []
    while number >= base:
        temp = number % base
        list.append(int(temp))
        number /= base
        
    if number != 0:
        list.append(int(number))
    list = list[::-1]
    return list
def list_to_integer(list):
    string = ""
    for i in list:
        string += str(i)
    return int(string)
        

def compound():
    number1 = int(input("Enter the first number"))
    base1 = int(input("Enter the base 1"))
    base2 = int(input("Enter the base 2"))
    decimal = base_to_decimal(number1, base1)
    result = decimal_to_base(decimal, base2)
    result1 = list_to_integer(result)
    return result1

print(compound())

