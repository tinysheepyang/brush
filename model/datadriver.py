# -*- coding: utf-8 -*-
import xlrd
import os, csv, sqlite3, MySQLdb
from model import env, log


class ExcelSheet:
    def __init__(self, excel, sheet):
        if env.EXCEL_DATA_PATH == "": 
            env.EXCEL_DATA_PATH = os.path.join(env.RESULT_PATH, "Data-Driven")
        
        self.data = xlrd.open_workbook(os.path.join(env.EXCEL_DATA_PATH, excel))
        self.table = self.data.sheet_by_name(sheet)
       

        #get titles
        self.row = self.table.row_values(0)

        #get rows number
        self.rowNum = self.table.nrows

        #get columns number
        self.colNum = self.table.ncols

        #the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1

        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True


class TXTHelper(object):
    
    def __init__(self, txt):
        if env.TXT_DATA_PATH == "": 
            env.TXT_DATA_PATH = os.path.join(env.RESULT_PATH, "Data-Driven")
        
        self.file = open(os.path.join(env.TXT_DATA_PATH, txt), 'r')
        self.row = self.file.readlines()
        
    def readFile(self):

        self.file.close()
        return self.row

class CsvHelper(object):
    
    def __init__(self, CSV):
        if env.TXT_DATA_PATH == "": 
            env.CSV_DATA_PATH = os.path.join(env.RESULT_PATH, "Data-Driven")

        self.file=open(os.path.join(env.CSV_DATA_PATH, CSV), 'r')
        self.reader=csv.reader(self.file)
        
    def readCsv(self,value1,value2):
        rows = []
        
        next(self.reader,None)
        for row in self.reader:
            rows.append(row)
        return ''.join(rows[value1][value2]).decode('gb2312')

class Xmlhelper(object):
    
    def __init__(self, xml):
        if env.TXT_DATA_PATH == "": 
            env.XML_DATA_PATH = os.path.join(env.RESULT_PATH, "Data-Driven")
        
        self.dom=xml.dom.minidom.parse(os.path.join(env.XML_DATA_PATH, xml), 'r')
        self.db=self.dom.documentElement

    def getXmlData(self,value):
        
        name=self.db.getElementsByTagName(value)
        nameValue=name[0]
        return nameValue.firstChild.data

    def getXmlUser(self,parent,child):
        itemlist=self.db.getElementsByTagName(parent)
        item=itemlist[0]
        return item.getAttribute(child)

class SqLite(object):
    def __init__(self, db_name):
        if env.SQLITE_DATA_PATH == "":
            env.SQLITE_DATA_PATH = os.path.join(env.RESULT_PATH, "Data-Driven")
        self.conn = sqlite3.connect(db_name)

    def close(self):
        """
        关闭Connection
        """
        self.conn.close()

    def create(self):
        """
        创建数据表
        """
        # 创建一个Cursor:
        cursor = self.conn.cursor()
        # 执行一条SQL语句，创建user表:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        # 继续执行一条SQL语句，插入一条记录:
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
        # 通过rowcount获得插入的行数:
        print cursor.rowcount
        # 关闭Cursor:
        cursor.close()
        # 提交事务:
        self.conn.commit()

    def show_tables(self):
        """
        显示数据库表名
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        cursor.close()
        print result
        return result

    def get_row(self):
        """
        获取多行数据
        :return:
        """
        cursor = self.conn.cursor()
        # 执行查询语句:
        cursor.execute('select * from user where id=?', '1')
        # 获得查询结果集:
        values = cursor.fetchall()
        cursor.close()
        print values
        return values


class MySQLHelper(object):
    def __init__(self):
        self.__conn=env.conn

    def selectMySQL(self,index1,index2):
        rows=[]
        try:
            conn=MySQLdb.connect(**self.__conn)
            cur=conn.cursor()
        except:
            log.step_fail('连接mysql数据库失败')
        else:
            cur.execute('select *  from element')
            data=cur.fetchall()
            for d in data:
                rows.append(d)
            return rows[index1][index2]
        finally:
            cur.close()
            conn.close()

    def get_One(self,sql,params):
        try:
            conn=MySQLdb.connect(**self.__conn)
            cur=conn.cursor()
            reCount=cur.execute(sql,params)
            data=cur.fetchone()
            return data
        except:
            log.step_fail('操作mysql数据库失败')
        finally:
            cur.close()
            conn.close()

    def insertMySQL(self,sql,params):
        try:
            conn=MySQLdb.connect(**self.__conn)
            cur=conn.cursor()
            cur.execute(sql,params)
            conn.commit()
        except:
            log.step_fail('操作mysql数据库失败')
        finally:
            cur.close()
            conn.close()











