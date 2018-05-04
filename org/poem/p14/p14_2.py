# p14_2
import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {}
data["from"] = "AUTO"
data["to"] = "AUTO"
data["i"] = "爱你"
data["smartresult"] = "dict"
data["client"] = "fanyideskweb"
data["doctype"] = "json"
data["xmlVersion"] = "2.1"
data["keyfrom"] = "fanyi.web"
data["ue"] = "UTF-8"
data["typoResult"] = "true"
data["action"] = "FY_BY_REALTIME"
data["salt"] = "1525437242032"
data["sign"] = "8e3bd79a1b69ed33eccab6d2abe01b0b"
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url, data)
html = response.read().decode("utf-8")
print(html)
