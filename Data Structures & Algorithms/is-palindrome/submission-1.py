class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(ch.lower() for ch in s if ch.isalnum())
        return new[:] == new[::-1]