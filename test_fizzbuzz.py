import fizzbuzz

def test_one():
    assert fizzbuzz.fizz_buzz(1) == 1, "Should be 1"

def test_three():
    assert fizzbuzz.fizz_buzz(3) == "Fizz", "Should be Fizz"

def test_five():
    assert fizzbuzz.fizz_buzz(5) == "Buzz", "Should be Buzz"

def test_seven():
    assert fizzbuzz.fizz_buzz(7) == 7, "Should be 7"

def test_nine():
    assert fizzbuzz.fizz_buzz(9) == "Fizz", "Should be Fizz"

def test_fifteen():
    assert fizzbuzz.fizz_buzz(15) == "FizzBuzz", "Should be FizzBuzz"
