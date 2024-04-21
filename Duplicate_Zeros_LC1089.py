class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr)-1:

            if arr[i] == 0:
                arr.insert(i+1,0)
                i +=1
                arr.pop()
            i+=1
        return arr
    def duplicateZeros1(self, arr: List[int]) -> None:
            zeroes = arr.count(0)
            n = len(arr)
            for i in range(n-1, -1, -1):
                if i + zeroes < n:
                    print(arr[i + zeroes],arr[i])
                    arr[i + zeroes] = arr[i]
                if arr[i] == 0: 
                    zeroes -= 1
                    if i + zeroes < n:
                        arr[i + zeroes] = 0
