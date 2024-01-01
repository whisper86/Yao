# 作者：许垚
# 开发时间2022年10月13日
import csv
import matplotlib.pyplot as plt

filename = "工作簿1.csv"
ID_card_number = []
Year = []
Sex = []
with open(filename, mode="r+", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        id_card_number = row[19]
        ID_card_number.append(id_card_number)
    for id_card_number in ID_card_number:
        year = id_card_number[6:10]
        Year.append(int(year))
        month = id_card_number[10:12]
        day = id_card_number[12:14]
        old = 2022 - eval(year)  # 根据具体年份来算年龄
        sex = id_card_number[16:17]
        s = sex
        if int(s) % 2 != 0:
            sex1 = "男"
        else:
            sex1 = "女"
        print(f"身份证号为：{id_card_number}")
        print("输出:", "你出生于", year, "年", month, "月", day, "日")
        print("你今年", old, "岁")
        Sex.append(sex1)
        print("你的性别为", sex1)
Male = Sex.count("男")
Female = Sex.count("女")
y_2002 = Year.count(2002)
y_2003 = Year.count(2003)
y_2004 = Year.count(2004)
y_2005 = Year.count(2005)
y_2006 = Year.count(2006)
y_2007 = Year.count(2007)
Y_year = [y_2002, y_2003, y_2004, y_2005, y_2006, y_2007]
X_sex = [Male, Female]
print(Y_year)
print(X_sex)
Percent1 = []
Percent2 = []
for y in Y_year:
    x = y / len(Year) * 100
    Percent1.append(x)
for z in X_sex:
    w = z / len(Sex) * 100
    Percent2.append(w)
print(Percent1)
print(Percent2)
labels1 = ['2002', '2003', '2004', '2005', '2006', '2007']
labels2 = ['Male', 'Female']
sizes1 = Percent1
sizes2 = Percent2
explode1 = (0.3, 0.1, 0.1, 0.1, 0.1, 0.1)
explode2 = (0, 0.1)

fig1, (ax1, ax2) = plt.subplots(2)
ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode1)
ax1.axis('equal')

ax2.pie(sizes2, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode2,
        pctdistance=1.12)
ax2.axis('equal')
ax2.legend(labels=labels2, loc='upper right')
ax2.set_title("Ratio of men and women")
ax1.set_title("Date of birth ratio")
plt.show()

# 源文件位于selenium-csv-matplotlib中的Sco Quary system文件夹中
