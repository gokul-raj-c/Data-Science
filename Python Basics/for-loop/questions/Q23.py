#Count uppercase, lowercase, digits, and special characters in a string

s=input("enter string: ")
upper_count=0
lower_count=0
digit_count=0
special_character_count=0
for i in s:
    if i.islower():
        lower_count=lower_count+1
    elif i.isupper():
        upper_count=upper_count+1
    elif i.isdigit():
        digit_count=digit_count+1
    else:
        special_character_count=special_character_count+1
print(s)
print("count of upper case:",upper_count)
print("count of lower case:",lower_count)
print("count of digits:",digit_count)
print("count of special characters:",special_character_count)