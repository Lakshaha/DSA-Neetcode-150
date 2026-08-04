class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        #just get the peak and do binary search both sides, compare the minmum

        def findPeak():
            low = 0
            high = n-1
            while low < high:
                mid = (low + high)//2
                if mountainArr.get(mid) < mountainArr.get(mid+1):
                    low = mid+1
                else:
                    high = mid
            
            return low
        
        def binarySearchLeft(peak):
            low = 0
            high = peak
            result = 0
            while low <= high:
                mid = (low+high)//2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    low = mid+1
                else:
                    high = mid-1
            
            return -1
        
        def binarySearchRight(peak):
            low = peak
            high = n-1
            while low <= high:
                mid = (low+high)//2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    low = mid+1
                else:
                    high = mid-1
            return -1
        
        peak = findPeak()
        val = binarySearchLeft(peak)
        if val != -1:
            return val
        return binarySearchRight(peak)
            
            


        


