class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Si mid es mayor que high, el mínimo está en la derecha
            if nums[mid] > nums[high]:
                low = mid + 1
            # Si mid es menor que high, el mínimo está en la izquierda o es mid
            elif nums[mid] < nums[high]:
                high = mid
            # Si nums[mid] == nums[high], no podemos determinar; reducir el rango
            else:
                high -= 1

        return nums[low]
