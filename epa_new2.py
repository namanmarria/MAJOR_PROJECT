import datetime
import mysql.connector as ep


class EPHelper:

    def __init__(self):
        self.connection = ep.connect(user='root', password='---',
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
        self.id = None
        self.phone = input("Enter Phone Number: ")
        self.department = input("Enter department: ")
        self.workhour = int(input("Enter workhour: "))
        self.overtime = int(input("Enter overtime: "))
        self.output = int(input("Enter output: "))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "insert into EmployeeLogger values(null, '{phone}', " \
              "'{department}', {workhour}, {overtime}, {output}, " \
              "'{log_time_stamp}')".format_map(vars(self))
        print(sql)

        save = input("Do you wish to Save the Record (yes/no)")
        if save == "yes":
            self.ep_helper.write(sql)


    def update_log(self):
        self.id = int(input("Enter Log ID: "))
        self.phone = input("Enter Phone Number: ")
        self.department = input("Enter workhour: ")
        self.workhour = int(input("Enter workhour: "))
        self.overtime = int(input("Enter overtime: "))
        self.sugar = int(input("Enter Diabetes: "))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "update EmployeeLogger set" \
              " phone = '{phone}', " \
              "department = {department}, workhour = {workhour}, overtime = {overtime}, " \
              "output = {output}, log_time_stamp = '{log_time_stamp}' " \
              "where id = {id}".format_map(
            vars(self))

        print(sql)

        update = input("Do you wish to Update the Record (yes/no)")
        if update == "yes":
            self.ep_helper.write(sql)

    def delete_log(self):
        self.id = int(input("Enter Log ID: "))

        sql = "delete from EmployeeLogger where id = {id}".format_map(
            vars(self))

        print(sql)

        delete = input("Do you wish to Delete the Record (yes/no)")
        if delete == "yes":
            self.ep_helper.write(sql)

    def get_all_logs(self):
        sql = "select * from EmployeeLogger"
        self.ep_helper.read(sql)

    def get_logs_by_phone(self, phone):
        sql = "select * from EmployeeLogger where phone = {}".format(phone)
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
        print("Get All Employee Logs by Phone")

        logger = EmployeeLogger()
        logger.get_logs_by_phone(input("Enter Phone Number: "))

    else:
        print("Invalid Option")

    choice = input("Would You Like to add another Employee Log... (yes/no)")
    if choice == "no":
        break
