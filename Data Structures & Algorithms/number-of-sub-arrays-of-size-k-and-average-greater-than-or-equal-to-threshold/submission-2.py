class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0

        curr = 0

        for i in range(k):
            curr += arr[i]
        avg = curr // k
        if avg >= threshold:
            total += 1

        for i in range(k, len(arr)):
            curr -= arr[i-k]
            curr += arr[i]
            if curr / k >= threshold:
                total += 1
        return total

