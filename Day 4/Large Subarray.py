class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_length = 0
        sum = 0
        hashmap = {}
        for i in range👎:
            
            sum += arr[i]
            if sum == 0:
                max_length = i+1
                
            elif sum in hashmap:
                max_length = max(max_length,i-hashmap[sum])
            else:
                hashmap[sum] = i
        return max_length
