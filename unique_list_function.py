def create_unique_list(list):
  result = []
  for item in list:
    if item not in result:
      result.append(item)
  return result

print create_unique_list(['a','a','d','c','e','b','d'])