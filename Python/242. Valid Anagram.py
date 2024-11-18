class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Crear mapas para contar las letras en ambas cadenas
        def build_map(string):
            char_map = {}
            for char in string:
                char_map[char] = char_map.get(char, 0) + 1
            return char_map

        # Construir mapas de caracteres para ambas cadenas
        s_map = build_map(s)
        t_map = build_map(t)

        # Comparar los mapas
        return s_map == t_map
