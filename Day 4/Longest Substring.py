class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		a,res,start=dict(),0,-1
		for i,ch in enumerate(s):
			if ch in a:
				start=max(start,a[ch])
			res,a[ch]=max(res,i-start),i
		return res
