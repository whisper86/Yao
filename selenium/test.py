import re
from shlex import join

# 这是一个re测试py文件
text = "GotoUrl('/BoxOffice/MovieStock/movieShow.html?id=709649',1)"
r = "'(/BoxOffice/.*?)'"
result = re.findall(r, text)  # 使用正则之后的结果：['/BoxOffice/MovieStock/movieShow.html?id=709649']
# print(result)
urllib = join(result)   # 直接将单个元素的列表result转变为str 结果：'/BoxOffice/MovieStock/movieShow.html?id=709649'
# print(urllib)
urllib1 = eval(urllib)  # 通过eval函数去掉str两边的引号
urllib2 = "https://www.endata.com.cn"+urllib1   # 将两个元素拼接成一个网址
print(urllib2)
for i in result:
    # print(i)
    url = "https://www.endata.com.cn"+i
    print(url)


# dataList = ['1', '2', '3', '4']
# str1 = join(dataList)
# print(str1)
