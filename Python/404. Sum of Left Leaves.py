"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000


Función sumOfLeftLeaves: Esta función simplemente llama a find_val con la raíz del árbol y el flag 1. El flag no se utiliza específicamente para la raíz en find_val, es más relevante para las llamadas recursivas que determinan si un nodo es una hoja izquierda o no.
Función find_val:
Parámetro root: El nodo actual del árbol.
Parámetro flag: Un indicador que es 0 si el nodo actual es una hoja izquierda y 1 si no lo es.
Si root es None, la función retorna 0. Esto se usa para manejar casos en que el árbol esté vacío o se hayan alcanzado hojas (nodos sin hijos).
Si flag es 0 y el nodo actual (root) no tiene hijos (not root.right and not root.left), entonces se identifica como una hoja izquierda y se retorna el valor de ese nodo (root.val).
Para cualquier otro caso, la función se llama recursivamente para los subárboles izquierdo y derecho:
Se llama a find_val(root.left, 0) para seguir buscando hojas izquierdas en el subárbol izquierdo.
Se llama a find_val(root.right, 1) para el subárbol derecho, pero pasando 1 porque los nodos del subárbol derecho no pueden ser hojas izquierdas según la definición.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.find_val(root,1)

    def find_val(self,root:Optional[TreeNode], flag:int ) -> int:
        if not root:
            return 0
        if flag == 0 and not root.right and not root.left:
            return root.val
        return self.find_val(root.left,0) + self.find_val(root.right,1)