import feedparser
import collections
import re
import operator 


def getwords(html):
    text  = re.compile(r'<[^>]+>').sub('', html)
    words = re.compile(r'[^A-z^a-z]+').split(text)

    return [word.lower() for word in words if word]

def getwordcounts(url):
    d = feedparser.parse(url)
    #print d
    wc = collections.defaultdict(int)
    stopwords = []
    stopWordList = open('stopWordList.txt').readlines()
    
    for stopWord in stopWordList:
        stopWord = stopWord.strip()
        stopwords.append(stopWord)
    
    
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        words = getwords('%s %s' % (e.title, summary))
        for word in words:
            if word not in stopwords:
                #print word
                wc[word] += 1

    if 'title' not in d.feed:
        print 'Invalid url', url
        return 'bogus data', wc    

    return d.feed.title, wc

def main():

    # XXX: break this up into smaller functions, write tests for them

    apcount    = collections.defaultdict(int)
    wordcounts = {}
    
    feedlist   = open('blogList-10.txt').readlines()
    
    totalWordCount = {}
    
        
    for url in feedlist:
        title, wc = getwordcounts(url)
        wordcounts[title] = wc
        
        for word, count in wc.iteritems():
            if count > 1:
                apcount[word] += 1
                
                try:
                    totalWordCount[word] += count
                except KeyError:
                    totalWordCount[word] = count
    
    
    wordlist = []
    
    
    for w, bc in apcount.iteritems():
        frac = float(bc)/len(feedlist)
        #print frac
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)
    
    countOfWords = []
    
    for word in wordlist:
        countOfWords.append((word,totalWordCount[word]))
        
            
    countOfWords.sort(key=lambda rating: rating[1], reverse = True )
    
    for words in countOfWords[0:500]:
        print words[0] , words[1]     
    
    out = file('blogdata-10-500.txt', 'w')
    out.write('Blog')
    
    
            
    for w in countOfWords[0:500]:
        #print w
        out.write('\t' + w[0])
        
        
    out.write('\n')
    
    for blogname, counts in wordcounts.iteritems():
        blogname = blogname.encode('UTF-8')
        out.write(blogname)     
        
        for w in countOfWords[0:500]:
            word = w[0]
            if w in counts:
                out.write('\t%d' % counts[word])
            else:
                out.write('\t0')
        
        out.write('\n')
    
    out.close()

if __name__ == '__main__':
    main()