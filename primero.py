def obtener_FizzBuzz(n):
    if(n % 5 == 0 and n % 3 == 0):
        return "Fizzbuzz"
    if(n % 5 != 0 and n % 3 != 0):
        return n
    if (n%3 == 0):
       return "fizz"
    if(n % 5 == 0 and n % 3 != 0):
        return "Fizzbuzz"
print (obtener_FizzBuzz(15))