# -*- coding:utf-8 -*-
###目前这种封装方法还不能正常使用，有待优化
import MySQLdb
class CreateConnectionMysql():
    def connection_mysql(self, host, port, user, passwd, db, charset):
        self.conn = MySQLdb.connect(host=host,user=user,
                             passwd=passwd,port=port, db=db,charset=charset)
        return self.conn()
    def cureors(self):
        # 通过连接数据来获取游标
        self.cursor = self.conn.cursor()
        return self.cursor()

    def selects(self, sql=None):
        try:
            return self.cursor.execute(sql)

            # 好像是打印字段的属性
            index = self.cursor.description

            result = []

            # fetchall():接收全部的返回结果行.
            for res in self.cursor.fetchall():

                row = {}

                # range(x):表示从0到x，不包括x
                # len:返回字符串、列表、字典、元组等长度
                for i in range(len(index)):
                    # index[i][0] 获取字段里属性中的局部信息
                    row[index[i][0]] = res[i]
                result.append(row)
                # print("selects_list %s" % row)
            return result
        except:
            print('MySQL connect fail...')

    def closes(self):
        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.conn.close()