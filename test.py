import requests
url = "http://www.baidu.com/v2/api/?login"
data = {
  "name": "Tom",
  "class": 20,
}
r = requests.post(url,data=data)
print(r.status_code)
print(r.headers)
#print(r.cookies)
#print(r.content)
print(r.text)
print("github")
print("github2")
print("github3")
print("github4")