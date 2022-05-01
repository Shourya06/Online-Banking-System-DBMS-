from distutils.util import execute
from importlib_metadata import Prepared
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    passwd = "Guddu@1998",
    database = "onlinebank"
)

my_cursor = mydb.cursor(prepared = True)

def showTables():
    my_cursor.execute("show tables")
    result = my_cursor.fetchall()
    return result
    
# print(showTables())

def Account(customerID, type):
    sql = "select A.accountNo, O.IFSC, A.balance from account as A, accountOpening as O where A.accountType = %s and A.accountNo = O.accountNo and O.customerID = %s"
    tup = (type, customerID)
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result[0]

# print(Account(1, 'current'))

def showTransactionHistory(customerID):
    sql = "SELECT T.transactionID, T.accountNo, T.recAccNo, T.mode, T.amount, T.time_Stamp from transaction T, accountOpening O WHERE O.customerID = %s and T.accountNo = O.accountNo"
    tup = (customerID, )
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result

print(showTransactionHistory(1))

def showloanHistory(customerID):
    sql = "SELECT * from Loan L where L.loanID in (SELECT B.loanID from borrow B where B.customerID = %s)"
    tup = (customerID, )
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result

print(showloanHistory(1))

def showFDHistory(customerID):
    sql = "SELECT * from fixeddeposit D where D.accountNo in (SELECT A.accountNo from accountopening A where A.customerID = %s)"
    tup = (customerID, )
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result

print(showFDHistory(1))

def card(customerID, type):
    sql = "SELECT C.cardNo, C.Expiry, C.CVV, C.spendLimit, A.balance FROM Card C, Account A WHERE C.accountNo in (SELECT O.accountNo FROM accountopening O WHERE O.customerID = %s) and C.cardtype = %s and A.accountNo = C.accountNo"
    tup = (customerID, type)
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result[0]

print(card(1, "credit"))

def addEmployee(empName, Street, Area, City, Pincode, custPhoneNo):
    sql = "insert into employee (employeeName, salary, street, area, city, pincode) values(%s, %s, %s, %s, %s, %s)"
    tup = (empName, 100000, Street, Area, City, Pincode)
    my_cursor.execute(sql, tup)
    result = my_cursor.fetchall()
    return result