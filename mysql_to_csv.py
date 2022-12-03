import pandas as pd
import mysql.connector
db=mysql.connector.connect(user='root',password='Q0)(qwerty',host='127.0.0.1',database='gw2022pd1')
cursor=db.cursor()

query="select * from EmployeeLogger"
cursor.execute(query)
mydata=cursor.fetchall()

all_id=[]
all_phone=[]
all_department=[]
all_workhour=[]
all_overtime=[]
all_output=[]
all_log_time_stamp=[]
for id,phone,department,workhour,overtime,output,log_time_stamp in mydata:
    all_id.append(id)
    all_phone.append(phone)
    all_department.append(department)
    all_workhour.append(workhour)
    all_overtime.append(overtime)
    all_output.append(output)
    all_log_time_stamp.append(log_time_stamp)

dic={'id': all_id,'phone': all_phone,'department':all_department,'workhour':all_workhour,'overtime':all_overtime,'output':all_output,'TIMESTAMP':all_log_time_stamp}
df=pd.DataFrame(dic)
df_csv=df.to_csv('D:\MAJOR\datasample.csv')