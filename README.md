# مشروع تصفية بيانات الموظفين - Data Filtering

## مقدمة
المشروع ده بيستعرض مهارات في تصفية وتحليل بيانات موظفين باستخدام مكتبة Pandas في بايثون.  
الهدف هو استخراج مجموعات معينة من الموظفين بناءً على شروط محددة على الأعمدة مثل القسم، المدينة، العمر، والمرتب.

## بيانات المشروع
- ملف البيانات: `data_filtering.csv`  
- الأعمدة الرئيسية في الملف:  
  - `name` : اسم الموظف  
  - `department` : القسم  
  - `city` : المدينة  
  - `salary` : المرتب  
  - `age` : العمر

## الخطوات المنفذة في الكود
1. استخراج الموظفين العاملين في قسم IT، ويقيمون في القاهرة، ومرتبهم أكبر من 10000.  
2. استخراج الموظفين العاملين في قسم HR أو Finance، الذين لا يعيشون في القاهرة، وأعمارهم بين 30 و40 سنة (شامل).  
3. استخراج الموظفين في قسم IT الذين:  
   - مرتبهم أعلى من المتوسط العام لجميع الموظفين  
   - أعمارهم أقل من 45 سنة  
   - لا يقيمون في مدينة Giza  
   - ترتيبهم تنازليًا حسب المرتب  
   - عرض الأعمدة: الاسم، العمر، المرتب، والمدينة فقط

## طريقة التشغيل
1. تأكد من وجود ملف `data_filtering.csv` في نفس المجلد الذي يحتوي على السكريبت.  
2. شغل السكريبت `data_filtering.py` أو استخدم Jupyter Notebook لتشغيل الكود.  
3. النتائج ستطبع مباشرة على الشاشة.

## الأدوات المستخدمة
- Python  
- مكتبة Pandas

---

لو عندك أي أسئلة أو اقتراحات لتحسين المشروع، تواصل معي!

