import requests
import re
import time

def getCookies(cookies):
	for ck in cookies.split(";"):
		name, value = ck.strip().split('=',1)
		cookie[name] = value
	return cookie

def getTbs():
	url = "https://tieba.baidu.com/index.html";
	html = requests.get(url = url, headers = headers, cookies = cookie).content.decode("utf-8")
	pa = re.compile("PageData.tbs.+?;")
	contentList = pa.findall(html)
	for content in contentList:
		return content[16:-2]

def Sign():
	tbs = getTbs()
	data = {
		"ie" : "utf-8",
		"tbs" : tbs
	}
	# print(tbs)
	url = "https://tieba.baidu.com/tbmall/onekeySignin1"
	res = requests.post(url = url, headers = headers, cookies = cookie, data = data)
	print(tbs + "  " + str(res))


print("程序开始运行时间  " + time.ctime() + "\n\n")
cookie = {}
with open("cookies.txt", "r") as f:
    cookies = f.read()
cookie = getCookies(cookies)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"
}
Sign()
print("\n\n程序结束时间  " + time.ctime() + "\n\n")

