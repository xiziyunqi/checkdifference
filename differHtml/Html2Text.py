#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.5
import re
import StringIO

def filterHTMLTags(strhtml):
    '''
    This method can filter all tags of html and script
    '''
    #get rid of CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)
    s = re_cdata.sub('', strhtml)
    #get rid of script
    re_script_1 = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    re_script_2 = re.compile(r'<script type="text/javascript">.+</script>', re.I)
    re_script_3 = re.compile(r'<script>.+</script>', re.I)
    re_script_4 = re.compile(r'<!--\[if IE \d]>.+<!\[endif]-->', re.S)
    re_script_5 = re.compile(r'<!–\[if lte IE \d]>.+<!\[endif]->', re.S)
    s = re_script_1.sub('', s)
    s = re_script_2.sub('', s)
    s = re_script_3.sub('', s)
    s = re_script_4.sub('', s)
    s = re_script_5.sub('', s)
    #get rid of style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    s = re_style.sub('', s)
    #br will translate new line
    re_br = re.compile('<br\s*?/?>')
    s = re_br.sub('\n', s)
    s = re_br.sub('\n\n', s)
    s = re_br.sub('\r\n', s)
    #get rid of HTMLTags
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('', s)
    #get rid of HTMLcommond
    re_comment = re.compile('<!--[^>]*-->')
    s = re_comment.sub('', s)
    #get rid of DOCTYPE
    r_doctype = re.compile(r'(?m)(<!DOCTYPE[\t\n\r ]+\S+[^\[]+?(\[[^\]]+?\])?\s*>)')
    s = r_doctype.sub('', s)
    #get rid of whileline
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    #replace html punctuation
    s = replaceCharEntity(s)
    return s 


def replaceCharEntity(data):
    '''
    replace some special html punctuation
    '''
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
   
    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(data)
    while sz:
        entity = sz.group()
        key = sz.group('name')
        try:
            data = re_charEntity.sub(CHAR_ENTITIES[key], data, 1)
            sz = re_charEntity.search(data)
        except KeyError:
            data = re_charEntity.sub('', data, 1)
            sz = re_charEntity.search(data)
    return data


def Html2Txt(htmlfile, savename):
    '''
    extract context from html
    '''
    with open(htmlfile, 'r') as f:
        context = f.read()
        strtxt = filterHTMLTags(context)
        #use temporaty file save this not farmat file
        tempfile = StringIO.StringIO()
        tempfile.write(strtxt)
        tempfile.seek(0)
        lines = tempfile.readlines()
        with open(savename, 'w') as newfile:
            for line in lines:
                if line.split():
                    newfile.writelines(line.strip()+'\n')
        tempfile.close()


if __name__=='__main__':
    filename ='e:\\src.htm'
    savename ='e:\\src2txt.txt'
    Html2Txt(filename, savename)

