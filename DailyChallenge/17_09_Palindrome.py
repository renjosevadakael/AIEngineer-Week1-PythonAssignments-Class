def isPalindrome(text):
    if text == text[::-1]:
        print(f"{text} is palindrome")
    else:
        print(f"{text} is not palindrome")

isPalindrome('madam')
isPalindrome('hello')
isPalindrome('a')


