#Binary Search template
'''
def bynary_search(array):
    def condition(value):
        pass
    left, right = min(search_space), max(search_space) #could it be [0,n], [1,n] etc. depend on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid +1

    return left 
'''

'''
You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which will return whether version is bad.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
First, we initialize left = 1 and right = n to include all possible values. Then we notice that we don't even need to design the condition function. It's already given by the isBadVersion API. Finding the first bad version is equivalent to finding the minimal k satisfying isBadVersion(k) is True. Our template can fit in very nicely:
'''

class Solution:
    def first isBadVersion(self, n):
        left, right = 1, n 
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left          

'''
69. Sqrt(x) [Easy]
Implement int sqrt(int x). Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example:

Input: 4
Output: 2
Input: 8
Output: 2
Easy one. First we need to search for minimal k satisfying condition k^2 > x, then k - 1 is the answer to the question. We can easily come up with the solution. Notice that I set right = x + 1 instead of right = x to deal with special input cases like x = 0 and x = 1.
'''

def mySqrt(x):
    left, right = 0, x +1
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid
        else: 
            left = mid + 1
    return left - 1 # left is the minimun k value, 'k - 1' is the answer
