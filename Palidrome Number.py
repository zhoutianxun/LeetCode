def isPalindrome(x:int ) -> bool:
    s = str(x)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

print(isPalindrome(11112))
