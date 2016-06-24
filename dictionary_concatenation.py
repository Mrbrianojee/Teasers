d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50, 6:60}

result = {}
for dict in (d1, d2, d3):
    result.update(dict)
print(result)