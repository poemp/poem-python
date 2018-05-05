# p14_4

import urllib.request
import urllib.parse
import json

data = {
    "question": "亲亲"
}

req = urllib.request.Request("http://127.0.0.1:8082/ask", urllib.parse.urlencode(data).encode("UTF-8"))

req.add_header("Referer", "http://127.0.0.1:8082")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
response = urllib.request.urlopen(req)
html = response.read().decode("UTF-8")
target = json.loads(html)

print("返回的信息是：%s" % target)
