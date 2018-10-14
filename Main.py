#知乎文章分析
import requests
from lxml import etree
import nltk
import jieba.analyse
import json
import jsonpath
import re
import time
import matplotlib.pyplot as plt
text=''
def key_words(url):
	global text
	head={
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
	}
	for i in url:
		html=requests.get(i,headers=head)
		s=html.text
		s=json.loads(s)
		s=jsonpath.jsonpath(s, '$..content')
		pattern = re.compile(r'[\u4E00-\u9FA5]|[\uFE30-\uFFA0]+')#提取中文和标点符号
		s=str(s)
		s=''.join(pattern.findall(s))
		print(s)
		text+=s
		time.sleep(0.5)
def product_url(que_num,n):#问题编码和分析页数
	url=[]
	for i in range(n):
		url.append('https://www.zhihu.com/api/v4/questions/'+str(que_num)+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=1&offset='+str(i)+'&sort_by=default')
	return url

allow='n','ns','nr','nz','ng','nl','t','tg','v','vd','vt','vi','vl','z','a','ad','ag','al','an'
key_words(product_url(275351176,10))

s1=[i for i in jieba.cut(text)]

s2=[i for i in nltk.bigrams(s1)]
d=nltk.FreqDist(s2)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
k,l=[],[]

for i,j in d.items():
	k.append(i)
	l.append(j)
n=30
plt.yticks(range(n),k[:n])
plt.barh(range(n),l[:n], height=0.7, color='steelblue', alpha=0.8)
plt.show()
#d.plot(100)

#d.plot(50)
c=80
#'v','vi','vt','vl','adv','a',
l=jieba.analyse.extract_tags(text, topK=c, withWeight=False, allowPOS=('ns','nz','nl','ni'))
print('关键词',l)
print('高频词组',[i for i in d][:c])#统计连词搭配

f=open('C://article.txt','w')
f.write(text)
f.close()
# f=open('C://article.txt','r')
# text=f.read()
# f.close()
