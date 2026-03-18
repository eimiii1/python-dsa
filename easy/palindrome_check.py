# Problem 3: Palindrome Check

def is_palindrome(text):
    palindrome_text = text.replace(" ", "").lower()
    return palindrome_text == palindrome_text[::-1]
    

print(is_palindrome('racecar'))
print(is_palindrome('A man a plan a canal Panama'))
print(is_palindrome('hello'))