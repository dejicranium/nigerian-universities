filepath = 'uni.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line_list = line.split(' ')
       name = line_list[0]
       print(name)
       line = fp.readline()
       cnt += 1
