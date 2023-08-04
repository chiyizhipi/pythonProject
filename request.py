import requests
r = requests.get('https://www.baidu.com/')
#r = requests.get()、head()、post()、put()、patch()、delete()
r.encoding='utf-8'
print(r.headers)
#print(r.text)  r.status_code   r.encoding  r.apparent_encoding  r.content


#爬取网页通用代码
import requests
def getHTMLText(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HttpError异常
        r.encoding=r.apparent_encoding
        #return r.text   #若不加此行，会返回 None
        return r.request.headers   #请求头
        #return r.headers   响应头
    except:
        return "产生异常"
if __name__=="__main__":
    url="https://www.baidu.com"
    print(getHTMLText(url))


#百度搜索全代码
import requests
keyword = "python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    #print(r.text[-500:])
    print(r.status_code)
except:
    print("爬取失败")


#IP地址查询全代码
import requests
url = "http://m.ip138.com/iplookup.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")




