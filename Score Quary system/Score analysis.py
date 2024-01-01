# 作者：许垚
# 开发时间2022年10月13日

import csv
import matplotlib.pyplot as plt

first = []
second = []
third = []
fourth = []
fifth = []
filename = "工作簿1.csv"
with open(filename, mode="r+", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        all_score = row[16]
        if int(all_score) >= 600:
            first.append(all_score)
        elif 500 <= int(all_score) < 600:
            second.append(all_score)
        elif 400 <= int(all_score) < 500:
            third.append(all_score)
        elif 300 <= int(all_score) < 400:
            fourth.append(all_score)
        else:
            fifth.append(all_score)
S1 = len(first)
S2 = len(second)
S3 = len(third)
S4 = len(fourth)
S5 = len(fifth)
S = [S1, S2, S3, S4, S5]
Percent = []
for s in S:
    percent = (s / 2312) * 100
    Percent.append(percent)
labels = ['Above 600(including 600)', '500--599', '400--499', '300--399', 'Below 299(including 299)']
sizes = Percent
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title("Score analysis")

plt.show()

# 源文件位于selenium-csv-matplotlib中的Sco Quary system文件夹中
