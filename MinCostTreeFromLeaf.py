class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        sum_of_non_leaf = {'sum': 0}
        def find(arr, start, end):
            max_leaf_index = -1
            max_leaf = 0
            if start>end:
                return 0
            if start == end:
                return arr[start]
            for i in range(start, end + 1):
                if arr[i] > max_leaf:
                    max_leaf_index = i
                    max_leaf = arr[i]
            a = find(arr, start, max_leaf_index - 1)
            b = find(arr, max_leaf_index + 1, end)
            sum_of_non_leaf['sum'] = sum_of_non_leaf['sum'] + max_leaf * a + max_leaf * b
            print(sum_of_non_leaf['sum'])
            return max_leaf
        
        find(arr, 0, len(arr) - 1)
        return sum_of_non_leaf['sum']
            
            
        