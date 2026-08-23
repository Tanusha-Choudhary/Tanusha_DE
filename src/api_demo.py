import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)
data_parsed = []
for row in data:
    data_parsed.append({
                "post_id":row["id"],
                  "user_id":row["userId"],
                  "title":row["title"]
                 })
    print(data_parsed)
