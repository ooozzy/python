
import os
import re
import requests
import urllib.request

product = input('请输入查找的物品信息：')
a = input('你要查找几页数据：')
print('''
====================
正在爬取数据
====================
''')
page=int(a)


#获取页面信息
def url_open(url):
	kv = {'cookie':'thw=cn; t=996acf017de100fc2b7bffb00d9ebf71; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=0d7fc03f1e6c7ef214a9902a3972fc05_1566576775571; _m_h5_tk_enc=c06ed4d06899e3ffda962fcbfa81778f; cna=OODmFeyCGCYCAbdf+8RDWyEq; uc3=nk2=tLwPfiZ8&id2=UUBfReP3ALLbEQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dBy3MNistZh1ZBD0o%3D; lgc=%5Cu795D%5Cu5FD7%5Cu5B89; tracknick=%5Cu795D%5Cu5FD7%5Cu5B89; _cc_=VT5L2FSpdA%3D%3D; tg=0; mt=ci=0_1; enc=0kOUoX0O%2F%2ByQK2HxOu%2BAdfttuT9FJ4t0G8etv8amOFtxMmrfzP2x7BjsVxC6BDxN4Q5Js9GrEL0mZGZbC4TC1A%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; uc1=cookie14=UoTaHoyzcDhwHg%3D%3D; cookie2=578208c69d890363ea41e63539dd0025; _tb_token_=7483e376e9eb3; JSESSIONID=4ECF78A53E30F1EF3BCBD47D07BAF0EF; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=cBEuuokVqzTyJp-LBOCanurza77OSIRYYuPzaNbMi_5K26Tsmh7OkoygIF96VjWdOYLB4aVvW6J9-etkZ4AfKV--g3fP.; isg=BEREM765xVXjp3Eb02DQTo3qFcL29Wmv4HYrZl7l0I_SieRThm04V3oryWH0iqAf; swfstore=176512',
		'user-agent':'Mozilla/5.0'}
	try:
		r = requests.get(url, headers=kv,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		# print(r.text)
		return r.text
	except:
		return ""


#获取页面商品信息
def get_goods(ilt, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


#获取信息并生成url，创建文件夹下载获取的信息
def download_TBproduct(product=product,folder='淘宝'+product+'数据',page=page):
	#判断文件夹是否存在
	if not os.path.exists(folder):
		os.mkdir(folder)
	else:
		pass
	infoList = []
	start_url = 'https://s.taobao.com/search?q=' + product
	for i in range(page):
		try:
			url = start_url + '&s=' + str(44 * i)
			html = url_open(url)
			get_goods(infoList,html)
			print(get_goods)
		except:
			continue
	printGoodsList(infoList)



download_TBproduct()

# #打印商品信息
# url_open('https://s.taobao.com/search?q=&s=44')
