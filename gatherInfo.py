# -*- coding: UTF-8 -*-
import MySQLdb
import json

db = MySQLdb.connect(host="yanxxcloud.cn", db="spider", user="yanwei", passwd="kxcneyt228",charset="utf8")

cursor = db.cursor()


def save_girl(girlDetail):
    catalog = girlDetail["source"]["catalog"]
    issue = girlDetail["issue"]
    girl=girlDetail['author']
    name = girl['nickname']
    area = girl['area']
    sex = girl['sex']
    height = girl['height']
    weight = girl['weight']
    birthday = girl['birthday']
    bwh = girl['bwh']
    imageulr="http://com-pmkoo-img.oss-cn-beijing.aliyuncs.com/picture/%s/%s/%s.jpg" % (catalog, issue, 1)
    sql = "insert into ugirl(name,area,sex,height,weight,birthday,bwh,imageurl) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (name,area,sex,height,weight,birthday,bwh,imageulr)
    print sql
    cursor.execute(sql)





def gath_girl_info():
    with open("data/info.txt", 'r') as f:
        for line in f:
            data = json.loads(line)
            girls = data['data']['list']
            for girl in girls:
                save_girl(girl)


if __name__=="__main__":
    gath_girl_info()
    db.commit()