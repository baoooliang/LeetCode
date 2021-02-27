class TrieNode:
    zero = None
    one = None
    value = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bit_range = range(31, -1, -1)
        root = TrieNode()
        
        for num in nums:
            node = root
            for i in bit_range:
                bits = 1 << i
                bit_num = bits & num
                if bit_num is 0:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
                else:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
            node.value = num
            node = root
        
        max_ = float('-inf')
        for num in nums:
            node = root
            for i in bit_range:
                bits = 1 << i
                bit_num = bits & num
                if bit_num is 0:
                    if node.one:
                        node = node.one
                    else:
                        node = node.zero
                else:
                    if node.zero:
                        node = node.zero
                    else:
                        node = node.one
            xor_value = num ^ (node.value)
            max_ = max(max_, xor_value)
        return max_
            
        
        