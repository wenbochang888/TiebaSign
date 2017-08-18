#!/home/chang/python3.6/bin/python3

import requests
import re
import time

def getCookies(cookies):
	for ck in cookies.split(";"):
		name, value = ck.strip().split('=',1)
		cookie[name] = value
	return cookie

def getMore():
	url = "http://tieba.baidu.com/mo/"
	html = requests.get(url = url, headers = headers, cookies = cookie).content.decode("utf-8")
	pa = re.compile("\"([^\"]+tab=favorite)\"")
	hrefList = pa.findall(html)
	# print(html)
	for href in hrefList:
		# print("http://tieba.baidu.com" + href.replace("&amp;", "&"))
		return "http://tieba.baidu.com" + href.replace("&amp;", "&")

def getLike():
	url = getMore()
	html = requests.get(url = url, headers = headers, cookies = cookie).content.decode("utf-8")
	pa = re.compile("kw.+?\">")
	hrefList = pa.findall(html)
	for href in hrefList:
		signList.append(url[:-21] + href[:-2])

def getTitle(url):
	html = requests.get(url = url, headers = headers, cookies = cookie).content.decode("utf-8")
	pa = re.compile("<title.+<.title>")
	titleList = pa.findall(html)
	for title in titleList:
		return title[7:-13]

def Sign():
	getLike()
	for url in signList:
		title = getTitle(url)
		html = requests.get(url = url, headers = headers, cookies = cookie).content.decode("utf-8")
		pa = re.compile("mo\/.+?\">签到")
		hrefList = pa.findall(html)
		if (len(hrefList) == 0):
			print(title + time.ctime() + "    已经签到\n")
			continue
		for href in hrefList:
			setSign(title, "http://tieba.baidu.com/" + href.replace("&amp;","&")[:-4])

def setSign(title, url):
	html = requests.get(url = url, headers = headers, cookies = cookie)
	print(title + "    在" + time.ctime() + "    签到成功\n")


print("程序开始运行时间  " + time.ctime() + "\n\n")
signList = []
cookie = {}
with open("/home/chang/cookies.txt", "r") as f:
    cookies = f.read()
cookie = getCookies(cookies)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"
}
#print(cookie)
Sign()
print("\n\n程序结束时间  " + time.ctime() + "\n\n")




