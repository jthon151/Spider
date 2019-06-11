# -*- coding:utf-8 -*-
# author:XL_Liu
# datetime:2019.06.10 上午 10:31
import requests
import xlwt
import time  # 引入time模块
import xlrd
from xlutils.copy import copy
import smtplib
from email.mime.text import MIMEText


def email(subject, content):
    msg_from = '1441301638@qq.com'  # 发送方邮箱
    passwd = 'iyjvgdlzhgpmiici'  # 填入发送方邮箱的授权码
    msg_to = '1441301638@qq.com'  # 收件人邮箱

    subject = subject  # 主题
    content = content  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())

    except Exception as e:
        print(e)
    finally:
        s.quit()


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    try:
        workbook = xlrd.open_workbook(path)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    except:
        new_workbook = xlwt.Workbook()
        new_worksheet = new_workbook.add_sheet('sheet1')
        rows_old = 0
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


lenth = 0

book = xlwt.Workbook()  # 新建一个excel
sheet = book.add_sheet('1')  # 添加一个sheet页


def NameToXY(name, key):
    N_url = 'https://restapi.amap.com/v3/geocode/geo?' \
            'address={0}&output=json&key={1}'.format(name, key)
    data = requests.get(N_url).text
    print(data)


key = 'c33717d0e11d097e93208bf39c2a8fdf'

# print(NameToXY('长沙市开福区湘江中路589号',key))
wd_jw = [112.970952, 28.198891]
# print(NameToXY('长沙市芙蓉区解放西路188号',key))
ifs_jw = [112.976063, 28.192223]

# print(NameToXY('长沙市岳麓区麓山南路932号',key))
zn_jw = [112.932278, 28.169033]

# print(NameToXY('长沙市岳麓区文轩路27号',key))
lg_jw = [112.893237, 28.211371]

# print(NameToXY('长沙市岳麓区枫林一路',key))
xh_jw = [112.943070, 28.201558]

# print(NameToXY('长沙市雨花区植物园路111号',key))
zhy_jw = [113.020380, 28.102201]

# print(NameToXY('长沙市开福区三一大道485号',key))
sjzc_jw = [113.054787, 28.236436]

# print(NameToXY('长沙市芙蓉区东风路22号',key))
lsgy_jw = [112.991241, 28.205856]

# print(NameToXY('长沙市雨花区花候路',key))
qcnz_jw = [113.060491, 28.152234]

# print(NameToXY('长沙市长沙县机场大道',key))
hhjc_jw = [113.215531, 28.201371]

# print(NameToXY('长沙市天心区湘府西路8号',key))
szf_jw = [112.983600, 28.112743]

# name = '长沙市开福区三一大道459号湖南国际会展中心'
# NameToXY(name,key)


mg_jw = [113.049597, 28.234365]

url_mg = 'https://restapi.amap.com/v3/traffic/status/circle?' \
         'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, mg_jw[0], mg_jw[1])

url_wd = 'https://restapi.amap.com/v3/traffic/status/circle?' \
         'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, wd_jw[0], wd_jw[1])

url_ifs = 'https://restapi.amap.com/v3/traffic/status/circle?' \
          'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, ifs_jw[0], ifs_jw[1])

url_zn = 'https://restapi.amap.com/v3/traffic/status/circle?' \
         'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, zn_jw[0], zn_jw[1])

url_lg = 'https://restapi.amap.com/v3/traffic/status/circle?' \
         'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, lg_jw[0], lg_jw[1])

url_xh = 'https://restapi.amap.com/v3/traffic/status/circle?' \
         'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, xh_jw[0], xh_jw[1])

url_zhy = 'https://restapi.amap.com/v3/traffic/status/circle?' \
          'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, zn_jw[0], zhy_jw[1])

url_sjzc = 'https://restapi.amap.com/v3/traffic/status/circle?' \
           'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, sjzc_jw[0], sjzc_jw[1])

url_lsgy = 'https://restapi.amap.com/v3/traffic/status/circle?' \
           'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, lsgy_jw[0], lsgy_jw[1])

url_qcnz = 'https://restapi.amap.com/v3/traffic/status/circle?' \
           'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, qcnz_jw[0], qcnz_jw[1])

url_hhjc = 'https://restapi.amap.com/v3/traffic/status/circle?' \
           'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, hhjc_jw[0], hhjc_jw[1])

url_szf = 'https://restapi.amap.com/v3/traffic/status/circle?' \
          'location={1},{2}&radius=2000&output=json&level=5&extensions=all&key={0}'.format(key, szf_jw[0], szf_jw[1])
# df3 = pd.DataFrame(columns=('description', 'expedite', 'congested'
#                             , 'blocked,unknown', 'statusz', 'descriptionz',
#                             'name', 'status', 'direction', 'angle', 'speed',
#                             'lcodes', 'polyline'))



def get_JTzs(url, lenth):
    df = []
    try:
        data = requests.get(url).json()
        if int(data['infocode']) != 10000:
            print('error')
            return
        data = data["trafficinfo"]

        # 路况综述
        description = data['description']

        # 1路况评价
        evaluation = data['evaluation']
        # 2 畅通所占百分比
        expedite = evaluation['expedite']
        # 2 缓行所占百分比
        congested = evaluation['congested']
        # 2 拥堵所占百分比
        blocked = evaluation['blocked']
        # 2 未知路段所占百分比
        unknown = evaluation['unknown']
        # 2 路况
        '''
            0：未知
            1：畅通
            2：缓行
            3：拥堵
        '''
        statusz = evaluation['status']
        # 2 道路描述
        descriptionz = evaluation['description']
        # 1 道路信息
        roads = data['roads']

        for road in roads:
            # 2 道路名称
            name = road['name']
            # print(name)
            # 2 路况
            status = road['status']
            # 2 方向描述
            direction = road['direction']
            # 2 车行角度，判断道路正反向使用
            angle = road['angle']
            # 2 速度
            try:
                speed = road['speed']
            except:
                speed = 0  # 无行车速度
            # 2 即locationcode的集合，是道路中某一段的id，一条路包括多个locationcode
            lcodes = road['lcodes']
            # 2 道路坐标集，坐标集合
            polyline = road['polyline']
            # df3.loc[lenth] = [{'description': description, 'expedite': expedite, 'congested': congested,
            #                   'blocked': blocked, 'unknown': unknown,
            #                   'statusz': statusz, 'descriptionz': descriptionz,
            #                   'name': name, 'status': status, 'direction': direction,
            #                   'angle': angle, 'speed': speed, 'lcodes': lcodes, 'polyline': polyline}]
            df.append([time.time(), time.asctime(time.localtime(time.time())), description, expedite, congested
                          , blocked, unknown, statusz, descriptionz,
                       name, status, direction, angle, speed,
                       lcodes, polyline])
            lenth += 1
    except Exception as e3:
        print('整体错误：{0}'.format(e3))

    return df


while 3600:
    try:
        stus = get_JTzs(url_mg, lenth)
        write_excel_xls_append('data/芒果2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_wd, lenth)
        write_excel_xls_append('data/万达2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_ifs, lenth)
        write_excel_xls_append('data/ifs2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_zn, lenth)
        write_excel_xls_append('data/中南大学2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_lg, lenth)
        write_excel_xls_append('data/麓谷2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_xh, lenth)
        write_excel_xls_append('data/西湖公园2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_zhy, lenth)
        write_excel_xls_append('data/植物园2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_sjzc, lenth)
        write_excel_xls_append('data/世界之窗2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_lsgy, lenth)
        write_excel_xls_append('data/烈士公园2000.xls'.encode('utf-8'), stus)
        stus = get_JTzs(url_qcnz, lenth)
        write_excel_xls_append('data/长沙汽车南站2000'.encode('utf-8'), stus)
        stus = get_JTzs(url_hhjc, lenth)
        write_excel_xls_append('data/黄花机场2000'.encode('utf-8'), stus)
        stus = get_JTzs(url_szf, lenth)
        write_excel_xls_append('data/湖南省政府2000'.encode('utf-8'), stus)
        time.sleep(180)
    except Exception as e:
        print(e)
        time.sleep(180)
        email(subject='交通状态', content='error：{0}'.format(e))
