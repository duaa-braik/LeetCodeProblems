class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        elements = dict()
        for i in range(len(s)):
            if elements.get(s[i]) is None:
                elements[s[i]] = 1
            else:
                elements[s[i]] = elements.get(s[i]) + 1

        for element in elements.items():
            if element[1] == 1:
                return s.index(element[0])
        return -1
