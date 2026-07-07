class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_word = ""
        palindrome_check = ""
        for i in s:
            if i.isalnum() == True:
                new_word += i
        for i in s[::-1]:
            if i.isalnum() == True:
                palindrome_check += i
        return new_word.lower() == palindrome_check.lower()
                    