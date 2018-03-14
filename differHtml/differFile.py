#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.5
import difflib


def isDiff(srcfile, tarfile):
    '''
    compare with two files,if equal then return ture
    '''
    # src = file(srcfile).read().split(' ')
    # tar = file(tarfile).read().split(' ')
	#readlines读取的是个列表
    src_ori = file(srcfile).readlines()
    tar_ori = file(tarfile).readlines()
    src=[]
    tar=[]
    src.append(src_ori[18])
    src.append(src_ori[19])
    src.append(src_ori[20])
    src.append(src_ori[21])
    tar.append(tar_ori[18])
    tar.append(tar_ori[19])
    tar.append(tar_ori[20])
    tar.append(tar_ori[21])
    # src.append(src_ori[45])
    # tar.append(src_ori[45])
    ret = 1
    # ignore blank lines
    temp = difflib.SequenceMatcher(lambda x: len(x.strip()) == 0, src, tar)
    for tag, i1, i2, j1, j2 in temp.get_opcodes():
        #print tag
        if tag != 'equal':
            ret = 0
            break
    return (True if ret == 1 else False)


def getDetails(srcfile, tarfile, flag = 'all'):
    '''
    compare wtih two files,if different then output details
    '''
    temp1_context = file(srcfile).read()
    temp2_context = file(tarfile).read()
    file1_context = temp1_context.splitlines()
    file2_context = temp2_context.splitlines()
    diff = difflib.Differ().compare(file1_context, file2_context)
    if flag == 'all':
        #output all context
        print "\n".join(list(diff))
    else:
        #only output different part of context
        linenum = 1
        for line in diff:
            if line[0] != ' ':
                print 'line:%d %s'%(linenum, line)
            else:
                linenum = linenum + 1


if __name__ == '__main__':
    src ='E:/src.txt'
    target ='e:\target.txt'
    if(isDiff(src, target)):
        print 'These two files are equal.'
    else:
        print 'These two files are different:'
        getDetails(src, target, 'notall')