class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # If there is no odd number,
        # all numbers must already be even.
        if min_odd == float('inf'):
            return True

        # We can make everything odd only if
        # every even number has a smaller odd number.
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True