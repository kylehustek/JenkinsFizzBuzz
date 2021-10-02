'''A Simple Python FizzBuzz Script'''

def fizz_buzz(i):
    '''Prints fizzbuzz of i'''
    fizzbuzz = ""
    if i % 3 == 0:
        fizzbuzz = fizzbuzz + "Fizz"
    if i % 5 == 0:
        fizzbuzz = fizzbuzz + "Buzz"
    print(fizzbuzz or i)

def main():
    '''Runs fizz_buzz FIZZ_CAP times'''
    fizz_cap = 15
    for i in range(1,fizz_cap+1):
        fizz_buzz(i)

if __name__ == "__main__":
    main()
