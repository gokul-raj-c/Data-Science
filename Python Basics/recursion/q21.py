# Check whether a string is a palindrome.

def check_pallindrome(text,i=0,j=None):
    if j==None:
        j=len(text)-1
    if i >= j:
        return True
    if text[i] != text[j]:
        return False
    return check_pallindrome(text,i+1,j-1)

print(check_pallindrome("malayalam"))