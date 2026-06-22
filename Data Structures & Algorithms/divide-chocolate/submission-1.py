class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def can_split(min_sweet, sweetness, k):
            total = 0
            count = 0
            for i in range(len(sweetness)):
                total += sweetness[i]
                if total >= min_sweet:
                    count += 1
                    total = 0
            return count >= k+1

        left = 1
        right = sum(sweetness) // (k+1)
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid, sweetness, k):
                left = mid + 1
            else:
                right = mid - 1
        return right
        