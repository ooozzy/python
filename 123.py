import urllib.request
import urllib.parse
import json
import time

while True:
	content = input('请输入需要翻译的内容("输入q!退出")：')
	if content == 'q!':
		break

	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'

	# head = {}
	# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'
	data = {}
	data ['i'] = content
	data ['from'] = 'AUTO'
	data ['to'] = 'AUTO'
	data ['smartresult'] = 'dict'
	data ['client'] = 'fanyideskweb'
	data ['salt'] = '15549799470019'
	data ['sign'] = '1d46165dcd1df3a4f9b106c4360ecc2a'
	data ['ts'] = '1554979947001'
	data ['bv'] = '529420c5d93057aa354a57033c6efa7d'
	data ['doctype'] = 'json'
	data ['version'] = '2.1'
	data ['keyfrom'] = 'fanyi.web'
	data ['action'] = 'FY_BY_REALTlME'
	data = urllib.parse.urlencode(data).encode('utf-8')

	req = urllib.request.Request(url,data)
	response = urllib.request.urlopen(req)
	html = response.read().decode('utf-8')

	req.add_header=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400')

	target = json.loads(html)
	print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

	time.sleep(1)