#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.5
import chardet
import urllib
from chardet.universaldetector import UniversalDetector


def getHtmlEncoding(websize):
    data = urllib.urlopen(websize).read()
    #print chardet.detect(data)
    return chardet.detect(data)['encoding']


def quick_getHtmlEncoding(websize):
    '''
    compare with getHtmlEncoding(),this method executed more quickly
    '''
    html = urllib.urlopen(websize)
    detector = UniversalDetector()
    for line in html.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    html.close()
    #print detector.result
    return detector.result['encoding']


def quick_getFileEncoding(filename):
    '''
    compare with getFileEncoding(),this method executed more quickly
    '''
    f = open(filename)
    detector = UniversalDetector()
    for line in f.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    f.close()
    #print detector.result
    return detector.result['encoding']


def getFileEncoding(filename):
    fdata = open(filename).read()
    #print chardet.detect(fdata)
    return chardet.detect(fdata)['encoding']


if __name__ == '__main__':
    websize ='http://www.baidu.com'
    print quick_getHtmlEncoding(websize)