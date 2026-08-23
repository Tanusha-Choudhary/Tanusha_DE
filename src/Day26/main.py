# dictionary comprehension
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
df1= {row.letter:row.code for index,row in df.iterrows()}
# print(df1)

# answer = [(i,df1[i]) for i in user_name.upper() if i in df1.keys()]
# OR
def generate_phonetic_alphabet():
    user_name = input("whats your name: ")
    try:
        answer = [df1[i] for i in user_name.upper()]
        print(answer)
    except KeyError:
        print("Sorry,only letters in the alphabets please")
    else:
        print(answer)
generate_phonetic_alphabet()
# for i in user_name.upper():
#     if i in df1.keys():
#         print(i,"for",df1[i])
