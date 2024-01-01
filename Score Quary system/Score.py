# 作者：许垚
# 开发时间2022年10月13日
import csv

while True:
    student = input('"请输入学生姓名(Enter "q" to exit)')
    Name = []
    ID_card_number = []
    filename = "工作簿1.csv"
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # print(header_row)
        # 从csv文件中拿数据
        for row in reader:
            Class = row[0]
            class_ranking = row[1]
            name = row[2]
            Name.append(name)
            sex = row[3]
            chinese = row[5]
            math = row[6]
            english = row[7]
            physics = row[8]
            chemistry = row[9]
            biology = row[10]
            comprehensive_physiotherapy = row[14]
            all_score = row[16]
            grade_ranking = row[17]
            id_card_no = row[19]
            ID_card_number.append(id_card_no)
            informations = {"班级": Class,
                            "班名": class_ranking,
                            "性别": sex,
                            "语文": chinese,
                            "数学": math,
                            "英语": english,
                            "物理": physics,
                            "化学": chemistry,
                            "生物": biology,
                            "理综": comprehensive_physiotherapy,
                            "总分": all_score,
                            "年级排名": grade_ranking,
                            "身份证号码": id_card_no}

            information = {name: informations}
            for param, value in information.items():
                if student == param:
                    print(f"{student}的基本信息为" + str(value))
                elif student == "q":
                    exit()
                else:
                    pass
        if student not in Name and student != "q":
            print(f"你所查找的{student}不在毛坦厂中学2020届中")

# 源文件位于selenium-csv-matplotlib中的Sco Quary system文件夹中
