import urllib.request
import os
import random
import time


def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400')
	
	# proxies = ['119.57.108.65:53281','101.89.132.131:80','124.205.155.151:9090']
	# proxy = random.choice(proxies)

	# proxy_support = urllib.request.ProxyHandler({'http':proxy})
	# opener = urllib.request.bulid_opener(proxy_support)
	# urlib.request.install_opener(opener)

	response = urllib.request.urlopen(url)
	html = response.read()

	return html

def get_page(url):
	html = url_open(url).decode('utf-8')

	a = html.find('current-comment-page') + 23
	b = html.find(']',a)

	return html[a:b]


def find_imgs(url):
	html = url_open(url).decode('utf-8')
	img_addrs = []
	
	a = html.find('img src=')
	
	while a != -1:
		b = html.find('.jpg',a,a+255)
		if b != -1:
			img_addrs.append('http:'+html[a+9:b+4])
		else:
			b = a + 9

		a = html.find('img src=',b)
	# for each in img_addrs:
	# 	print(each)
		return img_addrs

def save_img(folder,img_addrs):
	for each in img_addrs:
		filename = each.split('/')[-1]
		with open(filename,'wb') as f:
			img = url_open(each)
			f.write(img)


def download_pt(folder='ooxx1',pages=10):
	os.mkdir(folder)
	os.chdir(folder)

	url = 'http://jandan.net/ooxx/'
	page_num = int(get_page(url))

	for i in range(pages):
		page_num -= i
		page_url = url + 'page-' + str(page_num) + '#comments'
		img_addrs = find_imgs(page_url)
		save_img(folder,img_addrs)
		time.sleep(3)


if __name__ == '__main__':
	download_pt()

