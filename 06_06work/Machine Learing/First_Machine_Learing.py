import csv

Survived_List = []
Pclass_List = []

Survived1, Survived2 , Survived3 = 0, 0, 0
with open("archive3/Titanic-Dataset.csv", "r", encoding="utf-8") as f:
    row = csv.reader(f)
    header = next(row)

    for data in row:
        Survived = data[1]
        Pclass = data[2]
        name = data[3]

        Survived_List.append(Survived)
        Pclass_List.append(Pclass)
print(Pclass_List.count("1"), Pclass_List.count("2"), Pclass_List.count("3"))

for Survived, Pclass in zip(Survived_List, Pclass_List):
    if int(Survived) == 1 and int(Pclass) == 1:
        Survived1 += 1
    elif int(Survived) == 1 and int(Pclass) == 2:
        Survived2 += 1
    elif int(Survived) == 1 and int(Pclass) == 3:
        Survived3 += 1
print(Survived1, Survived2, Survived3)
print(Survived_List.count("1"))
