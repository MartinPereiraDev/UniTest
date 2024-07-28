# palindrome function

def is_palindrome(word):
    # convert to lowercase and remove spaces
    word = word.lower().replace(" ", "")
    # test word 
    verificar = word == word[::-1]
    return verificar

#print( "This word  ", word, "is palindrome ", verificar)
#is_palindrome("oso")