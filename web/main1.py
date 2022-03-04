import sqlalchemy
#connect 連線不同資料庫
from sqlalchemy import create_engine
engine = create_engine('sqlite:///pm25.db', echo=False)#True的話會回傳ＳＱＬ語法可供檢查

# 自訂一個類別, 這個類別對應到我們資料庫的資料表
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date

Base = declarative_base()


class pm25(Base):
    __tablename__ = '每日25'
    id = Column(Integer, primary_key=True, autoincrement=True)
    siteid = Column(Integer)
    sitename = Column(String(10), nullable=False)
    county = Column(String(10), nullable=True)  # 他的預設就是True,所以可以不設
    itemname = Column(String(20))
    itemengname = Column(String(10))
    itemunit = Column(String(10))
    monitordate = Column(Date)
    concentration = Column(Float)

    def __repr__(self):
        return "<PM25(sitename='%s', county='%s', monitordate='%s', concentration='%f')>" % (
        self.sitename, self.county, self.monitordate, self.concentration)

from sqlalchemy.orm import sessionmaker
from datetime import date
Session = sessionmaker(bind=engine)
session = Session()
x = input("你想查詢哪個城市：")
y = input("你想查詢哪個地區：")

search = session.query(pm25).filter_by(county=x, sitename=y)


for item in search:
    print(item.county, item.sitename, item.monitordate, item.concentration)

#for instance in session.query(pm25):
#    print(instance.sitename)

#print(item.county, item.sitename, item.monitordate, item.concentration)




