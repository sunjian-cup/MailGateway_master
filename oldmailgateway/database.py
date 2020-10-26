import sqlite3

class Database(object):

    def __init__(self):
        pass

    def connect(self):
        self.conn = sqlite3.connect('data.db')

    def createTable(self):
        cursor = self.conn.cursor()
        sql = "create table testMail (address varchar(30), server varchar(30), port varchar(10))"
        cursor.execute(sql)
        cursor.close()

    def getAllTestMail(self):
        cursor = self.conn.cursor()
        sql = "select * from testMail"
        cursor.execute(sql)
        values = cursor.fetchall()
        dict_test_mail_data = self.createAllTestMailDicData(values)
        cursor.close()
        return dict_test_mail_data

    def createAllTestMailDicData(self, tuple_data):
        dic_Data = []
        for data in tuple_data:
            dic_Data.append(
                {
                    'id': data[0],
                    'address': data[1],
                    'passwd': data[2],
                    'server': data[3],
                    'port': data[4]
                }
            )
        return dic_Data

    def close(self):
        self.conn.close()


    def runSql(self):
        cursor = self.conn.cursor()
        with open('data_test', 'r', encoding='utf-8') as f:
            sql_list = f.readlines()
            lineNum = 0
        for sql in sql_list:
            lineNum += 1
            sql = sql.strip('\n')
            if sql[0] != '#' and ';' in sql:
                cursor.execute(sql)
                print('已执行：{}'.format(sql))
            else:
                print('第{}行语句未执行'.format(lineNum))
        self.conn.commit()
        values = cursor.fetchall()
        cursor.close()
        self.conn.close()
        print('\n执行结果:')
        for value in values:
            print(value)

if __name__ == '__main__':
    db = Database()
    db.connect()
    db.runSql()