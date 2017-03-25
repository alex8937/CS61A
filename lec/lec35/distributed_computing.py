from socket import gethostbyname
from urllib.request import urlopen

print(gethostbyname('www.google.com'))
response = urlopen('http://www.google.com').read()
print(response[:15])