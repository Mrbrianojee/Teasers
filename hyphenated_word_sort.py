the_info = raw_input("enter a hyphenated '-' list ")

#split_list =[]
split_list = the_info.split('-')
split_list.sort()
print '-'.join(split_list)
