class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                element = stack.pop()
                dic[element] = num
            stack.append(num)
        
        while len(stack) > 0:
            element = stack.pop()
            dic[element] = -1
        
        result = []
        for num in nums1:
            result.append(dic[num])
        
        return result
            