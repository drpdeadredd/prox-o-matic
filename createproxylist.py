# BIG BAD PROXY SERVER FIND, CHECK, and USE
# BY : DRPDEADREDD
# DATE : JULY 2020
# MENTIONS : GITHUB.COM/HYPERBEATS - MADE A FEW MODIFICATIONS AFTER I GOT THROUGH HIS "Encryption"
# MAINLY DID THE SAME WITH FEWER LINES OF CODE AND COMBINED ALL THREE 
#IMPORT
import requests
import os

#GLOBAL
newline = "\n"
cache_file = "cache.txt"
http_proxy = "http.txt"
socks4_proxy = "socks4.txt"
socks5_proxy = "socks5.txt"

#clean cache FUNCTION
def clean(f):
    while True:
        try:
            os.remove(f)
            break
        except:
            time.sleep(1)
#HTTP
urlh = ['https://api.openproxylist.xyz/http.txt','http://worm.rip/http.txt']
ht = [requests.get(u) for u in urlh]
http = ''.join([(h.text) for h in ht])
with open(cache_file, 'w+') as file:
    file.write(http)
with open (cache_file, 'r+') as file:
    lines = set(file.readlines())
    form = [x.strip() for x in lines]
    proxy = '\n'.join(form)
with open(http_proxy, 'w+') as file:
    file.write(proxy)
#SOCKS4
urls4 = ['https://api.openproxylist.xyz/socks4.txt','http://worm.rip/socks4.txt']
s4 = [requests.get(u) for u in urls4]
socks4 = ''.join([(s.text) for s in s4])
with open(cache_file, 'w+') as file:
    file.write(socks4)
with open (cache_file, 'r+') as file:
    lines = set(file.readlines())
    form = [x.strip() for x in lines]
    proxy = '\n'.join(form)
with open(socks4_proxy, 'w+') as file:
    file.write(proxy)
#WSOCKS
urls5 = ['https://api.openproxylist.xyz/socks5.txt','http://worm.rip/socks5.txt']
s5 = [requests.get(u) for u in urls5]
socks5 = ''.join([(so.text) for so in s5])
with open(cache_file, 'w+') as file:  
    file.write(socks5)
with open (cache_file, 'r+') as file:
    lines = set(file.readlines())
    form = [x.strip() for x in lines]
    proxy = '\n'.join(form)
with open(socks5_proxy, 'w+') as file:
    file.write(proxy)   

clean(cache_file)


