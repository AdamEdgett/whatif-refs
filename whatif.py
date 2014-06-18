import httplib2, urlparse
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status = "200"
num = 1
refs = {}
while status == "200":
    response, content = http.request("http://what-if.xkcd.com/" + str(num))
    for link in BeautifulSoup(content, parseOnlyThese=SoupStrainer("a")):
        if link.has_key("href"):
            hostname = urlparse.urlparse(link["href"]).hostname
            if hostname is not None and not "xkcd" in hostname and hostname != "cgleason.org":
                if hostname not in refs:
                    refs[hostname] = 0
                refs[hostname] += 1
    status = response["status"]
    num += 1

for site in sorted(refs, key=refs.get, reverse=True):
    print(site + ": "  + str(refs[site]))
