import pymysql
from dbutils.pooled_db import PooledDB

# 数据库链接池初始化 实体化
pooldb = PooledDB(
    pymysql,
    maxconnections=20,
    mincached=10,
    maxcached=20,
    host='localhost',
    port=3306,
    user='yix',
    password='269507',
    database='yix',
)


# 数据库查询
def cx(sql):
    coom = pooldb.connection()
    cur = coom.cursor()
    SQL = sql
    try:
        r = cur.execute(SQL)
    except:
        v0 = {"code": 400, "msg": "数据库查询错误"}
        coom.close()
        return v0
    re = cur.fetchall()
    desc = cur.description
    cur.close()
    coom.close()
    v0 = {}
    v1 = []
    # print(re)
    v = 0
    for ree in re:
        v0 = {}
        i = 0
        for c in desc:
            v0[c[0]] = ree[i]
            i += 1
        v1.append(v0)
        v += 1
    v0 = {"code": 200, "msg": "ok", "data": v1}
    return v0


# 数据库执行
def zx(sql):
    coon = pooldb.connection()
    cursor = coon.cursor()
    mysql = sql
    try:
        c = cursor.execute(mysql)
    except:
        v0 = {"code": 400, "msg": "数据库执行失败", }
        coon.close()
        return v0
    v0 = {"code": 200, "msg": "ok", "num": c}
    coon.close()
    return v0
