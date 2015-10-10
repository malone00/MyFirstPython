#-*- coding:utf-8 -*-#
import urllib
import os
import re
#地址
url= 'http://www.gaoxiaola.com/p/gif/'
context = urllib.urlopen(url).read() #读取网页内容保存
res = re.findall('http://ww1.sinaimg.cn/mw690/[0-9a-z]*.gif',context)   #查找图片链接
os.chdir('D:\\ext') #图片存储路径 ,os.getcwd()可以读取路径
for i in range（len(res)）:
    name = str(i) + ‘.gif’
    f = open(name,'wb')
    f.write(urllib.urlopen(res[i]).read()) #下载到本地

f.close() //关闭文档占用
