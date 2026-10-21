class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = -1, n - k
        while left + 1 < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid
        return arr[right: right + k]