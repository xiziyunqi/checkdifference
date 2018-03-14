#-*- coding utf8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.5
import urllib
import urllib2
import getEncoding
import sys


def downloadHtml(websize, savefile):
    '''
    this method is used download html,but if html contain chinese charateres
    should not use this method
    '''
    #At first check the encoding of html
    encoding = getEncoding.quick_getHtmlEncoding(websize)
    content = urllib2.urlopen(websize).read()
    type = sys.getfilesystemencoding()
    s = content.decode(encoding).encode(type)
    file = open(savefile, 'wb')
    file.write(s)
    file.close()
    
    
def retrieveHtml(url, savefile):
    '''
    retrieve a assign html
    '''
    f = urllib.urlopen(url)   
    o = open(savefile, 'wb')
    n = 0
    while 1:
        s = f.read(1024)
        if not s:
            break
        o.write(s)
        n = n + len(s)
    f.close()
    o.close()
    #print 'retrieved %d bytes from %s'%(n, f.url)



if __name__ == '__main__':
    websize = 'http://www.baidu.com'
    filename = 'E:\src.htm'
    downloadHtml(websize, filename)

