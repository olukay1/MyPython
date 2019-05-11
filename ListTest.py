li = [[1,3,4],
      [2,5,0],
      [8,7,6]]
me = [row[2] for row in li  ]
m = [li[i][i-1]  for i in [0,1,2]  ]
print(me)

print(m)
