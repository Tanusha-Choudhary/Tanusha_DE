import time,requests,json
retry= 3
for attempt in range(retry):
    try:
        response = requests.get("https://jsonplaceholder1.typicode.com/posts")
        response.raise_for_status()
        print("request successful")
        break
    except Exception as e:
        print(f"Attempt {attempt +1 } failed")
        time.sleep(2)