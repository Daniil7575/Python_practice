url = input()
key = input()
url = url.split("?")[1].split("&")

for i in url:
    i = i.split("=")

url = dict(url)
print(url[key])



