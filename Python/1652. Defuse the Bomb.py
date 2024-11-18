class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        code_dev = code[:]
        for i in range(len(code)):
            if k == 0:
                code_dev[i] = 0
            elif k > 0:
                kode = k
                a = 0
                while kode > 0:
                    a = a + code[(i + kode) % len(code)]  # Uso de % para manejar índices circulares
                    kode -= 1
                code_dev[i] = a

            elif k < 0:
                kode = -k
                a = 0
                while kode > 0:
                    a = a + code[(i - kode) % len(code)]  # Uso de % para manejar índices circulares
                    kode -= 1
                code_dev[i] = a

        return code_dev
