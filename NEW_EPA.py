"""
create table employee_logger(
    id int primary key,
    name varchar(25),
    department varchar(25),
    workhour int,
    output int,
    overtime int,
    output int,
    leaves int,
    error int,
    exp int,
    tr_fq float,
    log_time_stamp datetime
    );
"""
import datetime
import mysql.connector as ep


class EPHelper:

    def __init__(self):
        self.connection = ep.connect(user='root', password='Q0)(qwerty',
                                     host='127.0.0.1',
                                     database='gw2022pd1')
        print("EP CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
            # print(row[1], row[2])


class EmployeeLogger:

    ep_helper = EPHelper()

    def save_log(self):
        self.id = input("Enter Employee ID")
        self.name = input("Enter Name : ")
        self.department = input("Enter department: ")
        self.workhour = int(input("Enter work hour: "))
        self.overtime = int(input("Enter overtime: "))
        self.exp=int(input("Enter Experience in years"))
        self.leaves=int(input("Enter number of leaves in the given month"))
        self.last_training=int(input("Enter the number of months since the employee attended a training session"))
        self.error = int(input("Enter error % (allowed between 0-5) : "))
        self.output = int(input("Enter Output %: "))
        self.performance_rating=int(input("Enter performance rating (0-5)"))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "insert into employee_logger values('{id}', '{name}', " \
              "'{department}',{workhour},{overtime},{exp},{leaves},"\
              "{last_training},{error},{output},{performance_rating} ," \
              "'{log_time_stamp}')".format_map(vars(self))
        print(sql)

        save = input("Do you wish to Save the Record (yes/no)")
        if save == "yes":
            self.ep_helper.write(sql)


    def update_log(self):
        self.id = input("Enter Employee ID")
        self.name = input("Enter Name : ")
        self.department = input("Enter department: ")
        self.workhour = int(input("Enter workhour: "))
        self.overtime = int(input("Enter overtime: "))
        self.exp = int(input("Enter Experience in years"))
        self.leaves = int(input("Enter number of leaves in the given month"))
        self.last_training = int(input("Enter the number of months since the employee attended a training session"))
        self.error = int(input("Enter error % (allowed between 0-5) : "))
        self.output = int(input("Enter Output %: "))
        self.performance_rating = int(input("Enter performance rating (0-5)"))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "update employee_logger set" \
              "id='{id}',"\
              " name = '{name}', " \
              "department = {department}, workhour = {workhour}, overtime = {overtime},exp={exp},leaves={leaves},"\
              "last_training={last_training}," \
              "error={error},output = {output},performance_rating={performance_rating},"\
              "log_time_stamp = '{log_time_stamp}' " \
              "where id = {id}".format_map(vars(self))

        print(sql)

        update = input("Do you wish to Update the Record (yes/no)")
        if update == "yes":
            self.ep_helper.write(sql)

    def delete_log(self):
        self.id = int(input("Enter Log ID: "))

        sql = "delete from employee_logger where id = {id}".format_map(
            vars(self))

        print(sql)

        delete = input("Do you wish to Delete the Record (yes/no)")
        if delete == "yes":
            self.ep_helper.write(sql)

    def get_all_logs(self):
        sql = "select * from employee_logger"
        self.ep_helper.read(sql)

    def get_logs_by_name(self, name):
        sql = "select * from employee_logger where name = {}".format(name)
        self.ep_helper.read(sql)

print("~~~~~~~~~~~~~~~~~~~~")
print("WELCOME")
print("EMPLOYEE LOGGER APP")
print("~~~~~~~~~~~~~~~~~~~~")


while True:

    print("1: Insert a New Employee Log")
    print("2: Update an Existing Employee Log")
    print("3: Delete an Existing Employee Log")
    print("4: Get All Employee Logs")
    print("5: Get All Employee Logs By Phone")

    option = int(input("Enter Your Option: "))

    if option == 1:
        print("Create a New Employee Log")
        logger = EmployeeLogger()
        logger.save_log()

    elif option == 2:
        print("Update Existing Employee Log")

        logger = EmployeeLogger()
        logger.update_log()

    elif option == 3:
        print("Delete Existing Employee Log")

        logger = EmployeeLogger()
        logger.delete_log()

    elif option == 4:
        print("Get All Employee Logs")

        logger = EmployeeLogger()
        logger.get_all_logs()

    elif option == 5:
        print("Get All Employee Logs by Name")

        logger = EmployeeLogger()
        logger.get_logs_by_name(input("Enter Name: "))

    else:
        print("Invalid Option")

    choice = input("Would You Like to add another Employee Log... (yes/no)")
    if choice == "no":
        break