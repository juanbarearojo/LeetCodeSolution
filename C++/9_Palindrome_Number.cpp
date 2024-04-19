//Given an integer x, return true if x is a  palindrome, and false otherwise.
class Solution {
public:
    bool isPalindrome(int x) {
        string valor = to_string(x);
        string palindromo = valor;
        reverse(palindromo.begin(),palindromo.end());
        if(valor == palindromo){
            return true;
        }
        else{
            return false;
        }
    }
};