class Solution:
    def frequencySort(self, s: str) -> str:
        store = Counter(s)
        
        ordered = sorted(store, key = lambda val: store[val], reverse = True)
        result = []

        for el in ordered:
            
            while store[el] > 0:

                result.append(el)
                store[el] -= 1

        return "".join(result)