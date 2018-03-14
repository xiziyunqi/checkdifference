#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.5
 
import downloadHtml
import differFile
import Html2Text
import os.path
#提示框
import tkMessageBox

def isExists(saveFile):
    '''
    check file whether existed
    '''
    return os.path.isfile(saveFile)


def monitorHtml(websize, savehtml, savetxt, originaltxt):
    '''
    monitor assign html, if context of html has changed then output details
    '''
    downloadHtml.downloadHtml(websize, savehtml)
	
    if isExists(originaltxt):
        Html2Text.Html2Txt(savehtml, savetxt)
        if(differFile.isDiff(originaltxt, savetxt)):
            print 'These two files are equal.'
            #tkMessageBox.showinfo(title = 'Tip', message = '活动没有更新')
        else:
            print 'These two files are different:'
            tkMessageBox.showinfo(title = 'Tip', message = '活动更新了')
            differFile.getDetails(originaltxt, savetxt, 'notall')
            Html2Text.Html2Txt(savehtml, originaltxt)					
    else:
        Html2Text.Html2Txt(savehtml, originaltxt)
    
if __name__ == '__main__':
    websize1 = 'http://10.104.0.225/plugin.php?id=xj_event:event_list&pc=1'
    srcname1 = 'D:\differHtml\orginal.txt'
    htmlname1 = 'D:\differHtml\src.htm'
    txtname1 = 'D:\differHtml\src2txt.txt'
    monitorHtml(websize1, htmlname1, txtname1, srcname1)