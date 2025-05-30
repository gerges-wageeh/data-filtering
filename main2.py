import pandas as pd 

data = pd.read_csv("data_filtering.csv")

#جميع الموظفين اللي شغالين في قسم الـ IT، وساكنين في Cairo، ومرتبهم أكتر من 10000.
#print(data.head())
#data[(data['department']=='IT') & (data['city']=='Cairo') & (data['salary'] > 10000)]

#فلتر البيانات لاستخراج:
#الموظفين اللي:
#الموظفين اللي:
#وساكنين مش في القاهرة
#وأعمارهم بين 30 و 40 (شامل)
#print(data[((data['department'] == 'HR') | (data['department'] == 'Finance')) &
#            (data['city'] != 'Cairo') &
#              (data['age'] >=30) & (data['age'] <=40) ])


#🧠 استخرج:
#شغالين في قسم IT
#مرتبهم أعلى من المتوسط العام لجميع الموظفين
#أعمارهم أقل من 45
#المدينة مش Giza
# بعد الفلترة:
#رتبهم تنازليًا حسب المرتب
#واطبع فقط الأعمدة: name, age, salary, city
salary_mean = data['salary'].mean()
data2 = data[(data['department'] == 'IT') &
      (data['salary'] >= salary_mean) &
        (data['age'] <= 45) &
         (data['city'] != 'Giza') ].copy()
data2.sort_values(by=['salary'],ascending=False,ignore_index=True,inplace=True)
print(data2[['name','age','salary','city']])




