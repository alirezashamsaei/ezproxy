import requests as req
import re
import socket


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


# Initial settings:
url = 'http://spys.one/en/socks-proxy-list/'
regex = '\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}'

# Request URL
response = req.get(url).text

# Extract IP and port from source
p = re.compile(regex)
results = p.findall(response)


alive = []
for i in range(0, 20):
    if is_open(results[i], '1080'):
        alive.append(results[i])


print(alive)

def gimmeprox():
    links = []
    for x in range(0,len(alive)):
        links.append('https://t.me/proxy?server=' + alive[int(x)] + '&port=1080')

    payload = '\n\n'.join(links)
    return payload
