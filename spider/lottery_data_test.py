from shlex import join

Str = "2212803121824272901 1,889,014,542117,471,238210161,807420,999,8862022-11-08"
str_list = list(Str)
# print(str_list)
date = str_list[:5]
data1 = str_list[5:7]
print(join(date))
print(join(data1))
