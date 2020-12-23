import pymssql #引入pymssql模块
import pandas as pd

def conn():
    connect = pymssql.connect('10.103.252.26', 'sa', '123456', 'NJCover3D') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
        return connect
    return None

def query(sql):
    connect = conn()
    df0 = pd.read_sql(sql, connect)
    df = pd.DataFrame(df0)

    print(df.columns)
    # cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
    # # sql = "select name, sex from C_test"
    # cursor.execute(sql)  # 执行sql语句
    # row = cursor.fetchone()  # 读取查询结果,
    # while row:  # 循环读取所有结果
    #     # print("Name=%s, Sex=%s" % (row[0], row[1]))  # 输出结果
    #     row = cursor.fetchone()
    #
    # cursor.close()
    # connect.close()



if __name__ == '__main__':
    sql = "SELECT * FROM tbGridFeature where inf_name in (select distinct inf_name from [NJCover3D].[dbo].[tbGridFeature] where dis=0)"
    query(sql)