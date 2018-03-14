#coding=utf-8
import chardet 
import urllib 
   
# 可根据需要，选择不同的数据 
TestData = urllib.urlopen('http://10.104.0.225/plugin.php?id=xj_event:event_list&pc=1&offlineclass=1').read() 
print chardet.detect(TestData) 
   
# 运行结果： 
# {'confidence': 0.99, 'encoding': 'GB2312'} 
#运行结果表示有99%的概率认为这段代码是GB2312编码方式。 
   
import urllib 
from chardet.universaldetector import UniversalDetector 
usock = urllib.urlopen('http://10.104.0.225/plugin.php?id=xj_event:event_list&pc=1&offlineclass=1') 
# 创建一个检测对象 
detector = UniversalDetector() 
for line in usock.readlines(): 
# 分块进行测试，直到达到阈值 
	detector.feed(line) 
	if detector.done: 
		break
# 关闭检测对象 
detector.close() 
usock.close() 
# 输出检测结果 
print detector.result