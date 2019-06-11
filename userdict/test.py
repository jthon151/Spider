# -*- coding:utf-8 -*-
# author:XL_Liu
# datetime:2019.06.05 上午 10:55
# 列表转换元组
# from numpy import array
import requests
import re
# num_list = array([[1,2,3,4,5],[1,2,3,4,5]]).T
# # print(type(num_list))
# # print(num_list)
# resule =[]
# for i in num_list:
#     resule.append(tuple(i))
#     # print(type(num_tuple))
# print(tuple(resule))
#
# #元组转换列表
# num_tuple_01 = (1,2,3,4,5)
# print(type(num_tuple_01))
# print(num_tuple_01)
# num_list_01 = list(num_tuple_01)
# print(type(num_list_01))
# print(num_list_01)

import MySQLdb


conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="baidu", charset="utf8")
cursor = conn.cursor()
from scrapy.selector import Selector
sql = 'select url from baidu_xinshao'
cursor.execute(sql)
data = cursor.fetchall()
print(len(data))
for i in range(len(data)):
    try:
        print('{0}第{1}个页面爬取{0}'.format('-' * 20, i))
        x = requests.get(data[i][0],headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    })
        x.encoding = 'utf-8'
        page = Selector(text=x.text)
        title1 = page.xpath('/html/body')

        title=(re.sub("[^\u4e00-\u9fa5]",'',title1.xpath('string(.)').extract_first()))
        # print(title)
        cursor.execute("insert data(url,page) VALUES('{0}','{1}')".format(data[i][0],title))
        conn.commit()
    except Exception as e:
        print(e)
#
# print(data)
cursor.close()


#
#
#
# def insert_baidu_xinshao(result):
#     cursor.executemany("insert baidu_xinshao VALUES(%s,%s,%s,%s)",(result))
#     return conn.commit()
# insert_baidu_xinshao([('http://www.xinshao.gov.cn/c536/index.html', '新邵县人民政府 - 扶贫政策', '2019年3月5日', '2019年3月5日\xa0-\xa0新政办发〔2018〕23号各乡镇人民政府,县政府各局、各直属机构:《新邵县电商产业扶贫工作实施方案》已经县人民政府同意,现印发给你们,请认真遵照执行。...'), ('http://www.xinshao.gov.cn/c537/index.html', '新邵县人民政府 - 扶贫信息', '2018年12月11日', '扶贫信息 2018年,新邵脱贫攻坚工作首次调度  1月22日,我县召开脱贫攻坚指挥部2018年第一次调度会。会议深入贯彻落实中央、省、市关于打赢脱贫攻坚战的决策部署,...'), ('http://zgsc.china.com.cn/2018-12/11/content_40606083.html', '新邵:吹响扶贫冲锋号 打赢脱贫攻坚战', '2018年10月14日', '2018年12月11日\xa0-\xa0为迎接湖南省扶贫工作组脱贫摘帽考核验收,11月29日,邵阳市新邵县寸石镇再次组织召开脱贫攻坚推进会,传达学习了县委、县政府近期扶贫工作相关要求。县...'), ('https://baijiahao.baidu.com/s?id=1614262702279228356&wfr=spider&for=pc', '湖南新邵县易地扶贫搬迁:“搬”来的美好生活', '2019年5月24日', '2018年10月14日\xa0-\xa0这不是大都市的名小区,而是湖南新邵县潭府乡一个名为潭府新城的易地扶贫搬迁集中安置点。 潭府新城里绿油油的草坪和崭新的柏油路。 王昊昊 摄 ...'), ('https://baijiahao.baidu.com/s?id=1634386486765349743&wfr=spider&for=pc', '新邵:打了一场漂亮的“脱贫”歼灭战', '2019年1月9日', '2019年5月24日\xa0-\xa05月22日,记者来到新邵县,探访其脱贫攻坚成果。  新邵县是武陵山片区区域发展和扶贫攻坚县。从2014年的贫困发生率17.3%下降到2018年的1.08%。实现了...'), ('http://sy.voc.com.cn/view.php?tid=51602&cid=7', '新邵:扶贫路上齐协力 一枝一叶总关情 华声在线邵阳频道', '2018年4月24日', '2019年1月9日\xa0-\xa0他们是新邵县潭府乡民政办及新邵一中的帮扶干部,在各自的帮扶岗位上,为...在脱贫攻坚的道路上贡献力量、奉献真心,共同绘出扶贫帮困为民服务的最美动...'), ('https://ts.voc.com.cn/note/view/41195.html', '新邵县扶贫办回复“我现在家庭情况能挪入扶贫?”_投..._投诉直通车', '2018年11月28日', '2018年4月24日\xa0-\xa0关于新邵县陈家坊下江村李维满相关问题调查处理汇报  省扶贫办:  2018年3月21日,我办接到省扶贫办交办的关于华声在线《投诉直通车》信访贴后,立即与陈...'), ('https://baijiahao.baidu.com/s?id=1618339553423124729&wfr=spider&for=pc', '新邵县全力推进脱贫攻坚工作纪实', '2018年1月11日', '2018年11月28日\xa0-\xa04年来,新邵县坚持与旅游开发、产业发展、小城镇建设相结合,高品位、高标准建设了白水洞、坪上高铁新城、潭府水口、太芝庙谭家湾等有影响、有品位的易地扶贫搬迁...'), ('https://hn.rednet.cn/c/2018/01/11/4527049.htm', '新邵护航易地扶贫 美好生活“搬”出来 - 湖南频道', 'NULL', '2018年1月11日\xa0-\xa0小区里道路通畅,休闲广场宽阔安静,规范整齐的社区里,家家户户室内窗明几净……在地处武陵山片区的新邵县潭府乡2016易地搬迁扶贫点水口村,易地扶贫...')])
# cursor.close()



# x = requests.get('http://zgsc.china.com.cn/2018-12/11/content_40606083.html')
# x.encoding = 'utf-8'
# page = Selector(text=x.text)
# title1 = page.xpath('/html/body')
# title = []
# for i in title1:
#     title.append(re.sub("[^\u4e00-\u9fa5]",'',i.xpath('string(.)').extract_first()))
# print(title)