word = 'abba'

def palindrome_test(word):
    right = len(word) -1
    for left in range(len(word)-1):
        if word[left] != word[right]:
            return False
        right -= 1
    return True


result  = palindrome_test(word)

print "palindrome? :" + str(result)
