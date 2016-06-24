word = 'aBba'


def palindrome_test(word):
    right = len(word) -1
    for left in range(len(word)-1):
        if word[left] != word[right]:
            print "Word is not a palindrome"
            return
        right -= 1
    print (word + " is indeed a palindrome")


palindrome_test(word.lower())
