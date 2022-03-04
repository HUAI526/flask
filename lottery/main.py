#!user/bin/python3.9
import random as rd
import sqlite3

def lottery():

    awesomeNum = set()
    while len(awesomeNum) < 7:
        awesomeNum.add(rd.randint(1, 49))

    awesomelist = sorted(awesomeNum)
    specia = awesomelist.pop(rd.randint(0, 6))
    return (awesomelist, specia)

def insertOneRowToSqlite(date, sixList, oneItem):
    con = sqlite3.connect('lottery.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO awesome(日期, num1, num2, num3, num4, num5, num6,特別號) VALUES (?, ?, ?, ?, ?, ?, ?,?)",(date, sixList[0], sixList[1], sixList[2], sixList[3], sixList[4], sixList[5],oneItem ))
    con.commit()
    con.close()
    print("inster 成功")


    print(date)
    print(sixList)
    print(oneItem)


if __name__ == "__main__":

    '''
    hm = int(input("大樂透電腦選號（幾組）："))

    for i in range(hm):
        six, one = lottery()
        print(f'第{i + 1}組')
        for num in six:
            print(num, end=',')
        print(f'特別號：{one}')
        print()
   '''
    dateList = ['20220107','20220108','20220109','20220110','20220111','20220112']

    for itemdate in dateList:
        six, one = lottery()
        insertOneRowToSqlite(itemdate, six, one)
