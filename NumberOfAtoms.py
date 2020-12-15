class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def helper():
            count = {}
            while self.i < len(formula) and formula[self.i] != ')':
                if formula[self.i] == '(':
                    self.i += 1
                    res = helper()
                    for k in res.keys():
                        count[k] = count[k] + res[k] if k in count else res[k]
                    
                else:
                    start = self.i
                    self.i += 1
                    while self.i < len(formula) and formula[self.i].islower():
                        self.i += 1
                    name = formula[start: self.i]
                    start = self.i
                    while self.i < len(formula) and formula[self.i].isdigit():
                        self.i += 1
                    num = int(formula[start:self.i]) if self.i > start else 1
                    count[name] = num if name not in count else num + count[name]
            self.i += 1
            start = self.i
            while self.i < len(formula) and formula[self.i].isdigit():
                self.i += 1
            if start < self.i:
                multiplier = int(formula[start:self.i])
                print(multiplier)
                for k in count.keys():
                    count[k] = count[k] * multiplier
            
            return count
        
        self.i = 0
        res = helper()
        sorted_key = sorted(res.keys())
        final = ''
        for k in sorted_key:
            final += k
            final += str(res[k]) if res[k] > 1 else ''
        return final
            