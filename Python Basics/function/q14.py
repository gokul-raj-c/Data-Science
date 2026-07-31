#5. Write a function fizzbuzz_range(start, end) that loops from start to end (inclusive) and, for each number, prints:
# FizzBuzz if it's divisible by both 3 and 5
# Fizz if divisible by 3 only
# Buzz if divisible by 5 only
# the number itself otherwise
# Then, after the loop, print how many Fizz, Buzz, and FizzBuzz lines it produced — in the format Fizz: 4, Buzz: 2, FizzBuzz: 1.
# the counts must be tracked inside it and printed

def fizzbuzz_range(start, end):
    FizzBuzz=0
    Fizz=0
    Buzz=0
    for i in range(start,end+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
            FizzBuzz=FizzBuzz+1
        elif i%3==0:
            print("Fizz")
            Fizz=Fizz+1
        elif i%5==0:
            print("Buzz")
            Buzz=Buzz+1
        else:
            print(i)
    print("FizzBuzz:",FizzBuzz,", Fizz:",Fizz,", Buzz:",Buzz)

fizzbuzz_range(1,20)
