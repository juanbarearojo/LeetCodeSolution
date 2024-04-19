"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal  substringconsisting of non-space characters only."""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        longitud = len(s)
        indice = longitud - 1
        longitud_palabra = 0  # Usar una variable diferente para la longitud de la última palabra
        while indice >= 0:
            char = s[indice]
            if char == " ":
                if longitud_palabra > 0:
                    break
            else:
                longitud_palabra += 1
            indice -= 1
        return longitud_palabra