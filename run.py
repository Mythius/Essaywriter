import urllib.request
src = input("What do you want to find? ")
try:
    fp = urllib.request.urlopen("https://www.wikipedia.org/wiki/"+src)
    mb = fp.read()
    s = mb.decode("utf8")
    fp.close()
    if s.find('may refer to:')!=-1:
        a=s.split('<ul>')[1].split('</ul>')[0].split('<li>')
        a.pop(0)
        i=0
        for b in a:
            i+=1
            c=b.split('">')[1].replace('</a>','').replace('</li>','')
            print('#'+str(i),c)
    else:
        a=s.split('toctitle')[1].split('#See_also')[0].split('toclevel-1')
        print('Suggested Outline: ')
        for b in a:
            if b.find('#')!=-1:
                c=b.split('#')[1].split('"')[0].replace('_',' ')
                print(c)
except:
    print('Not Found')
    
    
