#User function Template for python3
class Solution:

	def countIncreasing(self,arr, n):
		# code here
		
		count = 0
		l = 1
		for i in range(1, n):
		    if arr[i] > arr[i-1]:
		        count += l
		        l += 1
		    else:
		        l = 1
	    return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countIncreasing(arr, n)
        print(ans)
        tc -= 1


# } Driver Code Ends