some_code = 'print "hello bootcampers"'
other_code = """
def exp(x,y):
    return x**y

print '2 to the power of 4 is: ',exp(2,4)
"""
exec(some_code)
exec(other_code)