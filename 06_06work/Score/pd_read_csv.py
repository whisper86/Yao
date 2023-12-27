import warnings
import pandas as pd

warnings.filterwarnings("ignore")
# import data
data = pd.read_csv(r'chengji.csv', dtype="object", encoding='utf8')

# print(data.head())

y = data['姓名']
X = data.drop(['班级', "物理", "化学", "生物", "班级名次"], axis=1)
print(X.select_dtypes('float'))

cat_feat = X.select_dtypes('object').columns.values
X_cat = X[cat_feat]

print(X_cat)
