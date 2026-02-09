class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        store = {}
        for word in words:
            formation = ''
            for char in word:
                idx = ord(char) % 97
                formation += Morse_code[idx]
            
            if formation not in store:
                store[formation] = 1
            else:
                store[formation] += 1

        return len(store)
                

        