# 作者：许垚
# 开发时间2022年10月4日
import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline
filename = "chengji.csv"
Chinese = []
Math = []
English = []
Physics = []
Chemistry = []
Biology = []
Name = []
All_score = []
Academic_Performance = []
All_Score_Performances = []
with open(filename, mode="r+", encoding="utf-8") as f:
    reader = csv.reader(f)
    object = next(reader)
    o = object
    for O in reader:
        name = str(O[1])
        Name.append(name)
        chinese = float(O[4])
        Chinese.append(chinese)
        math = float(O[5])
        Math.append(math)
        english = float(O[6])
        English.append(english)
        physics = float(O[7])
        Physics.append(physics)
        chemistry = float(O[8])
        Chemistry.append(chemistry)
        biology = float(O[9])
        Biology.append(biology)
        all_score = float(O[11])
        All_score.append(all_score)
        academic_performance = [chinese, math, english, physics, chemistry, biology, all_score]
        Academic_Performance.append(academic_performance)
        All_Score_Performance = {
            '语文': chinese,
            '数学': math,
            '英语': english,
            '物理': physics,
            '化学': chemistry,
            '生物': biology,
            '总分': all_score
        }
        All_Score_Performances.append(All_Score_Performance)
Object = []
for i in range(2, 12):
    Object.append(o[i])
Object.remove("性别")
Object.remove("考号")
Object.remove("理综")
# print(Object)
# print(Name)
# for academic_performance, name in zip(Academic_Performance, Name):
#     x_values = Object
#     data = [Bar(x=x_values, y=academic_performance)]
#
#     x_config = {'title': "OBJECT"}
#     y_config = {'title': "SCORE"}
#
#     my_layout = Layout(title=f"{name}'s score", xaxis=x_config, yaxis=y_config)
#     offline.plot({'data': data, 'layout': my_layout}, filename=f"{name}'s academic performance.html")
