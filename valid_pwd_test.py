import re
pwd = "Apple000006$" #raw_input("Enter a password")



if ((len(pwd)<6 or len(pwd)>16)
    or not re.search("[a-z]",pwd)
    or not re.search("[0-9]",pwd)
    or not re.search("[A-Z]",pwd)
    or not re.search("[$#@]",pwd)
    or re.search("\s",pwd)):

    print "Invalid Password"
else:
    print "Valid Password"

