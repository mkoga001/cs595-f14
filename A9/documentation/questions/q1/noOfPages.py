import feedparser
import unicodedata

def gePagesCount(url):
    mainUrl = url.strip()
    d = feedparser.parse(url)
    pages = len(d['entries'])
    title = d['feed']['title'] 
    
    counter = 0
    if pages == 500:
        url = mainUrl +"&start-index=501"
       
        d = feedparser.parse(url)
        pages = int(pages) + int(len(d['entries']))
        
        
        
        if pages == 1000:
            url = mainUrl +"&start-index=1001"
            
            d = feedparser.parse(url)
            pages = int(pages) + int(len(d['entries']))
            
            if pages == 1500:
                url = mainUrl +"&start-index=1501"
               
                d = feedparser.parse(url)
                pages = int(pages) + int(len(d['entries']))
                
                if pages == 2000:
                    url = mainUrl +"&start-index=2001"
                    
                    d = feedparser.parse(url)
                    pages = int(pages) + int(len(d['entries']))
                    
                    if pages == 2500:
                        url = mainUrl +"&start-index=2501"
                        
                        d = feedparser.parse(url)
                        pages = int(pages) + int(len(d['entries']))
    
    print u'|'.join((str(pages),title)).encode('utf-8').strip()
    
def main():
    feedlist   = open('blogList-120-atom.txt').readlines()
    
    for url in feedlist:
        try:
            gePagesCount(url)
        except KeyError:
            pass      

if __name__ == '__main__':
    main()