#-*-coding:utf-8-*-
import MySQLdb
class MysqlConnection():
    def connection_mysql(self, host, port, user, passwd, db, charset,sql):
        self.conn = MySQLdb.connect(host=host,user=user,
                             passwd=passwd,port=port, db=db,charset=charset)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)

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
                print result
                # print("selects_list %s" % row)
        except:
            print('MySQL connect fail...')

        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.conn.close()
    def count_mysql(self, host, port, user, passwd, db, charset,sql):
        self.conn = MySQLdb.connect(host=host,user=user,
                             passwd=passwd,port=port, db=db,charset=charset)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            a=self.cursor.fetchone()
            print a
            return a
        except:
            print('MySQL connect fail...')

        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.conn.close()

    def del_mysql(self, host, port, user, passwd, db, charset,sql):
        self.conn = MySQLdb.connect(host=host,user=user,
                             passwd=passwd,port=port, db=db,charset=charset)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            # print self.cursor.fetchall()
            # return self.cursor.fetchall()

        except:
            print('MySQL connect fail...')

        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.conn.close()