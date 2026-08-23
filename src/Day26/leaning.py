import random
import pandas as pd
list_1 = [2,3,4]
list_2 =[n+1 for n in list_1]
# print(list_2)
name ="Angela"
new_list = [letter for letter in name]
# print(new_list)
short_name =['Alex','Berli','Anne','Eleanor','SophiaAl','Freddie']
# long_name=[i.upper() for i in short_name if len(i)> 5]
# print(long_name)
student_score = { _:random.randint(0,100) for _ in short_name}
# print(student_score)
passed_score = {student:score for (student,score) in student_score.items() if score >=60}
# print(passed_score)
student_dict ={"student":["Anne","marry","joly"],
               "score":[23,45,89]}
df =pd.DataFrame(student_dict)
print(df)
df1 = { for (index,row) in df.iterrows()}
print(df1)