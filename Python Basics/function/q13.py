#Write a function check_even_odd(number) that prints whether the number is even or odd. Handle 0 correctly.

def check_even_odd(number):
    if number%2==0:
        print("even number")
    else:
        print("odd number")

num=int(input("enter number: "))
check_even_odd(num)