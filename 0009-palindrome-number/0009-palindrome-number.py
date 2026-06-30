class Solution(object):
    def isPalindrome(self, x):
        rev=0
        temp=x

        while x>0:
            ld=x%10
            rev=rev*10+ld
            x=x//10
        if temp==rev:
            return True
        else:
            return False       

s= Solution()
print(s.isPalindrome(121))      