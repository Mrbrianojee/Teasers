import operator

dict = {'a':'tom', 'f': 'dick', 'c': 'harry', 'd': 'jane'}

sorted_in_descending = sorted(dict.items(), key=operator.itemgetter(0), reverse=True)

sorted_in_acsending = sorted(dict.items(), key=operator.itemgetter(0))

print "Ascending:  " + str(sorted_in_acsending)

print "Descending: " + str(sorted_in_descending)
