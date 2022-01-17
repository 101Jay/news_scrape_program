import requests
res = requests.get("http://naver.com")
res.raise_for_status() # 정상이면 그대로 진행, 아니면 바로 오류냄 
# print(res.status_code) # 200 이면 정상
# if res.status_code == requests.codes.ok : # 200이랑 같은 의미
#     print("Good")
# else : 
#     print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")

print(len(res.text))

with open("mynaver.html", "w", encoding="utf-8") as f:
    f.write(res.text)