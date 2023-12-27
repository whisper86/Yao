import csv

Number = 891
Age_List = []

with open("archive3/Titanic-Dataset.csv", "r", encoding="utf-8") as f:
    row = csv.reader(f)
    header = next(row)

    for data in row:
        try:
            Age = int(data[5])
        except ValueError:
            Number -= 1
            pass
        Age_List.append(Age)
        Age_List.sort()

print(Age_List)
print(Number)
