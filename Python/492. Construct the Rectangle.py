class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math  # Se debe importar el módulo math para usar sqrt
        a = int(math.sqrt(area))  # Usar math.sqrt correctamente
        while a > 0:
            if area % a == 0:
                w = a
                break  # Cambiar exit por break para salir del bucle
            else:
                a -= 1
        l = area // w  # Usar // para la división entera

        return [l, w]

        