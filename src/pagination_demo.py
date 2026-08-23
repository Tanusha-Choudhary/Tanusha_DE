import requests

page =1
list_s =[]
# print(response.json())
while True:
    response = requests.get("https://jsonplaceholder.typicode.com/posts",
    params ={"_page":page,"_limits":5}
                            )
    if not response.json():
        break
    list_s.extend(response.json())
    page+=1
print(len(list_s))
