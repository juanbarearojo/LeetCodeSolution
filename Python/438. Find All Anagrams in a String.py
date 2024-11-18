class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter

        # Crear el hash map (contador) de la segunda cadena
        p_map = Counter(p)
        p_len = len(p)
        s_map = Counter()
        result = []

        # Recorrer el primer string
        for i in range(len(s)):
            # Agregar el carácter actual al hash map
            s_map[s[i]] += 1

            # Si el tamaño de la ventana excede el tamaño de p, reducir el tamaño
            if i >= p_len:
                if s_map[s[i - p_len]] == 1:
                    del s_map[s[i - p_len]]
                else:
                    s_map[s[i - p_len]] -= 1

            # Comparar los mapas
            if s_map == p_map:
                result.append(i - p_len + 1)

        return result
