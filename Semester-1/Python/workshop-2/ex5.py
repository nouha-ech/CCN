def palindrome(text):
    n = len(text)
    for i in range(n):
        if text[i] != text[n - i - 1]:
            return False
    return True

mot = input("Entrez un mot : ")

if palindrome(mot):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
