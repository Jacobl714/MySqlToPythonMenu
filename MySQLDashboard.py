import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='COMPANY')


cursor = cnx.cursor(buffered=True)
databases = ("use COMPANY")
cursor.execute(databases)
databases = ("show tables")
cursor.execute(databases)
print("-------------------------\n|1 = add new employee     |\n|2 = View employee        |\n|3 = Modify mployee       |\n|4 = Remove employee      |\n|5 = Add new dependent    |\n|6 = Remove dependent     |\n|7 = Add new department   |\n|8 = View department      |\n|9 = Remove department    |\n|10 = Add dept location   |\n|11 = Remove dept location|\n-------------------------")
input1 = input()
#add new employee
if(input1 == "1"):
    print("Enter first name")
    fName = input()
    print("Enter Middle initial")
    Minit = input()
    print("Enter last name")
    lName = input()
    print("Enter SSN")
    sSn = input()
    print("Enter birthdate")
    bDate = input()
    print("Enter Address")
    Address = input()
    print("Enter sex")
    sex = input()
    print("Enter Salary")
    salary = input()
    print("Enter Supervisors SSN")
    super_ssn = input()
    print("Enter Dno")
    Dno = input()
    #print("Enter info seperated by space")
    #fName, Minit, lName, sSn, bDate, Address, sex, salary, super_ssn, Dno = input().split()
    if (len(sSn) != 9) or (len(Dno) != 1) or (len(super_ssn) != 9) or (len(sex) != 1) :
        print("Invalid Entry - Table not updated")
    else:    
        sql1 = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (fName, Minit, lName, sSn, bDate, Address, sex, salary, super_ssn, Dno)
        cursor.execute(sql1, val)
        cnx.commit()
        print("Done")
elif (input1 == "2"):
    print("Enter ssn of employee: ")
    ssnInput = input()
    if (len(ssnInput) != 9):
        print("Invalid SSN")
    else:
        #sql2 = "SELECT * FROM EMPLOYEE WHERE SSN =" + str(ssnInput)
        sql2 = "SELECT emp.Fname, emp.Minit, emp.Lname, emp.Ssn, emp.Bdate, emp.Address, emp.sex, emp.Salary, emp.Super_ssn, emp.Dno, sup.Fname, sup.Lname, Dname, Dependent_name FROM EMPLOYEE emp, EMPLOYEE sup, DEPARTMENT dep, DEPENDENT depen WHERE emp.Super_ssn = sup.Ssn AND Dep.Dnumber = emp.Dno AND depen.Essn = emp.Ssn AND emp.Ssn = " + str(ssnInput) 
        #val2 = (ssnInput)
        cursor.execute(sql2)
        result = cursor.fetchall()
        print(result)
elif (input1 == "3"):

    print("Enter SSN of Employee")
    ssnInput3 = input()
    sqlLock3 = "lock table EMPLOYEE write"
    cursor.execute(sqlLock3)
    sql3 = "SELECT * FROM EMPLOYEE WHERE Ssn = " + str(ssnInput3)
    cursor.execute(sql3)
    result = cursor.fetchall()
    print("Employee Information: " + str(result))
    print("Would you like to change address (Y/N)")
    input31 = input()
    if ((input31 == "Y") or (input31 == "y")):
        print("Enter new address")
        newAddr = input()
        newAddr = str(newAddr)
        #UPDATE `company`.`EMPLOYEE` SET `Address` = '123MRoad' WHERE (`Ssn` = '111111111');
        sql31 = "UPDATE EMPLOYEE SET Address = \'" + str(newAddr) + "\' WHERE (Ssn = " +str(ssnInput3)+")"
        sqlLock3 = "lock table EMPLOYEE write"
        cursor.execute(sql31)
        cnx.commit()
        print("Address Updated")
    elif ((input31 == "N") or (input31 == "n")):
        print("Address not updated")
    print("Would you like to change sex (Y/N)")
    input32 = input()
    if ((input32 == "Y") or (input32 == "y")):
        print("Enter new sex")
        newSex = input()
        #newAddr = str(newAddr)
        #UPDATE `company`.`EMPLOYEE` SET `Address` = '123MRoad' WHERE (`Ssn` = '111111111');
        sql32 = "UPDATE EMPLOYEE SET Sex = \'" + str(newSex) + "\' WHERE (Ssn = " +str(ssnInput3)+")"
        cursor.execute(sql32)
        cnx.commit()
        print("Sex Updated")
    elif ((input32 == "N") or (input32 == "n")):
        print("Sex not updated")
    print("Would you like to change salary (Y/N)")
    input33 = input()
    if ((input33 == "Y") or (input33 == "y")):
        print("Enter new salary")
        newSalary = input()
        #newAddr = str(newAddr)
        #UPDATE `company`.`EMPLOYEE` SET `Address` = '123MRoad' WHERE (`Ssn` = '111111111');
        sql33 = "UPDATE EMPLOYEE SET Salary = \'" + str(newSalary) + "\' WHERE (Ssn = " +str(ssnInput3)+")"
        cursor.execute(sql33)
        cnx.commit()
        print("Salary Updated")
    elif ((input33 == "N") or (input33 == "n")):
        print("Salary not updated")
    print("Would you like to change Super_ssn (Y/N)")
    input34 = input()
    if ((input34 == "Y") or (input34 == "y")):
        print("Enter new Super_ssn")
        newSuperSsn = input()
        #newAddr = str(newAddr)
        #UPDATE `company`.`EMPLOYEE` SET `Address` = '123MRoad' WHERE (`Ssn` = '111111111');
        sql34 = "UPDATE EMPLOYEE SET Super_ssn = \'" + str(newSuperSsn) + "\' WHERE (Ssn = " +str(ssnInput3)+")"
        cursor.execute(sql34)
        cnx.commit()
        print("Super_ssn Updated")
    elif ((input34 == "N") or (input34 == "n")):
        print("Super_ssn not updated")
    print("Would you like to change Dno (Y/N)")
    input35 = input()
    if ((input35 == "Y") or (input35 == "y")):
        print("Enter new Dno")
        newDno = input()
        #newAddr = str(newAddr)
        #UPDATE `company`.`EMPLOYEE` SET `Address` = '123MRoad' WHERE (`Ssn` = '111111111');
        sql35 = "UPDATE EMPLOYEE SET Dno = \'" + str(newDno) + "\' WHERE (Ssn = " +str(ssnInput3)+")"
        cursor.execute(sql35)
        cnx.commit()
        print("Dno Updated")
    elif ((input35 == "N") or (input35 == "n")):
        print("Dno not updated")
    sqlLock32 = "unlock table EMPLOYEE write"
    cursor.execute(sqlLock32)
elif(input1 == '4'):
    print("Enter ssn of employee: ")
    ssnInput4 = input()
    sql40 = "SELECT * FROM EMPLOYEE WHERE Ssn = " + str(ssnInput4)
    cursor.execute(sql40)
    result = cursor.fetchall()
    print(result)
    sql41 = "SELECT COUNT(Dependent_name) FROM DEPENDENT WHERE Essn = " + str(ssnInput4)
    cursor.execute(sql41)
    result1 = cursor.fetchall()[0][0]
    if (result1 > 0):
        print("\nWARNING:  This employee has " + str(result1) + " dependencies.  Remove them first")
    else:
        sqlLock3 = "lock table EMPLOYEE write"
        cursor.execute(sqlLock3)
        print("No dependencies found... OK to delete!\n")
        print("Are you sure you want to delete the employe (Y/N)")
        answer = input()
        if ((answer == "N") or (answer == "n")):
            print("Deletion cancelled")
        elif ((answer == "Y") or (answer == "y")):
            sql42 = "DELETE FROM Employee WHERE Ssn = " + str(ssnInput4)
            cursor.execute(sql42)
            cnx.commit()
            print("Employee Deleted")
    sqlLock42 = "unlock table EMPLOYEE write"
    cursor.execute(sqlLock42)
elif(input1 == "5"):
    print("Enter SSN of employee: ")
    ssnInput5 = input()
    sql5 = "SELECT Dependent_name FROM DEPENDENT WHERE Essn = " + str(ssnInput5)
    cursor.execute(sql5)
    result5 = cursor.fetchall()
    sqlLock5 = "lock table EMPLOYEE write"
    cursor.execute(sqlLock5)
    print("Dependents are: " + str(result5))
    print("Enter name of new dependent")
    nameNew = input()
    print("Enter sex of new dependent")
    sexNew = input()
    print("Enter bdate of new dependent")
    bdateNew = input()
    print("Enter relationship of new dependent")
    relNew = input()
    sql52 = "INSERT INTO DEPENDENT(Essn, Dependent_name, Sex, Bdate, Relationship) VALUES(%s, %s, %s, %s, %s) "
    val5 = (ssnInput5, nameNew, sexNew, bdateNew, relNew)
    cursor.execute(sql52, val5)
    cnx.commit()
    print(str(nameNew) + " added!")
    sqlLock51 = "unlock table EMPLOYEE write"
    cursor.execute(sqlLock51)
elif(input1 == "6"):
    print("Enter SSN of employee: ")
    ssnInput6 = input()
    sql6 = "SELECT Dependent_name FROM DEPENDENT WHERE Essn = " + str(ssnInput6)
    cursor.execute(sql6)
    result6 = cursor.fetchall()
    sqlLock6 = "lock table EMPLOYEE write"
    cursor.execute(sqlLock6)
    print("Dependents are: " + str(result6))
    print("Enter name of dependent to remove")
    nameDelete = input()
    sql6 = "DELETE FROM DEPENDENT WHERE Dependent_name = \'" + str(nameDelete) + "\' AND Essn = " + str(ssnInput6)
    cursor.execute(sql6)
    cnx.commit()
    print(str(nameDelete) + " has been deleted!")
    sqlLock6 = "unlock table EMPLOYEE write"
    cursor.execute(sqlLock6)
elif(input1 == "7"):
    print("Input the Dnumber for this new department")
    dnumInput = input()
    sql71 = "SELECT count(*) FROM DEPARTMENT WHERE Dnumber = " + str(dnumInput)
    cursor.execute(sql71)
    result7 = cursor.fetchall()
    print(str(result7[0][0]))
    if (str(result7[0][0]) != "0"):
        print("ERROR: Violates key principles.  Dnumber exists already")
    else:
        print("Valid Dnumber\n")
        print("Enter Department name")
        dnameNew = input()
        print("Enter manager SSN of new dept")
        mgrSsnNew = input()
        print("Enter manager start date")
        sdNew = input()
        sql72 = "INSERT INTO DEPARTMENT(Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES (%s, %s, %s, %s)"
        val7 = (dnameNew, dnumInput, mgrSsnNew, sdNew)
        cursor.execute(sql72, val7)
        cnx.commit()
        print("Department number " + str(dnumInput) + " added!")
elif(input1 == "8"):
    print("Enter Dnumber")
    dnumView = input()
    #dept , mgr name, loc
    sql8 = "SELECT Dname, Fname, Lname, Dlocation FROM DEPARTMENT, EMPLOYEE, DEPT_LOCATIONS WHERE EMPLOYEE.Ssn = DEPARTMENT.Mgr_ssn AND DEPARTMENT.Dnumber = DEPT_LOCATIONS.Dnumber AND DEPARTMENT.Dnumber = " + str(dnumView)
    cursor.execute(sql8)
    result8 = cursor.fetchall()
    print(result8)
elif(input1 == "9"):
    print("Enter Dnumber of department to remove")
    remDept = input()
    sql90 = "SELECT * FROM DEPARTMENT WHERE Dnumber = " + str(remDept)
    cursor.execute(sql90)
    result90 = cursor.fetchall()
    print(result90)
    sql91 = "SELECT COUNT(Dno) FROM DEPARTMENT, EMPLOYEE WHERE Dno = Dnumber and Dnumber = " + str(remDept)
    cursor.execute(sql91)
    result91 = cursor.fetchall()[0][0]
    print(result91)
    if (result91 > 0):
        print("WARNING:  Please resolve referential integrity constrain violations first")
    else:
        sqlLock9 = "lock table EMPLOYEE write"
        cursor.execute(sqlLock9)
        print("Are you sure you want to remove this department? (Y/N)")
        answ9 = input()
        if ((answ9 == "N") or (answ9=="n")):
            print("Deletion cancelled")
        elif ((answ9 == "Y") or (answ9=="y")):
            sql92 = "DELETE FROM DEPARTMENT WHERE Dnumber = " + str(remDept)
            cursor.execute(sql92)
            cnx.commit()
            print("Department Removed")
        sqlLock92 = "unlock table EMPLOYEE write"
        cursor.execute(sqlLock92)
elif(input1 == "10"):
    print("Enter Dnumber")
    dnum10 = input()
    sql10 = "SELECT Dlocation FROM DEPT_LOCATIONS WHERE Dnumber = " + str(dnum10)
    cursor.execute(sql10)
    result10 = cursor.fetchall()
    sqlLock101 = "lock table EMPLOYEE write"
    cursor.execute(sqlLock101)
    print("Locations are: " + str(result10))
    print("Enter new location")
    locNew = input()
    sql101 = "INSERT INTO DEPT_LOCATIONS(Dnumber, Dlocation) VALUES (%s, %s)"
    val101 = (dnum10, locNew)
    cursor.execute(sql101, val101)
    cnx.commit()
    print("Departnumber number " + str(dnum10) + " in " + str(locNew) + " has been added!")
    sqlLock102 = "unlock table EMPLOYEE write"
    cursor.execute(sqlLock102)
elif(input1 == "11"):
    print("Enter Dnumber")
    dnum11 = input()
    sql11 = "SELECT Dlocation FROM DEPT_LOCATIONS WHERE Dnumber = " + str(dnum11)
    cursor.execute(sql11)
    result11 = cursor.fetchall()
    sqlLock111 = "lock table EMPLOYEE write"
    cursor.execute(sqlLock111)
    print("Locations are: " + str(result11))
    print("Enter location to remove")
    remLoc = input()
    sql112 = "DELETE FROM DEPT_LOCATIONS WHERE Dlocation = \'" + str(remLoc) + "\' AND Dnumber = " + str(dnum11)
    cursor.execute(sql112)
    cnx.commit()
    print(str(remLoc) + " has been removed!")
    sqlLock112= "unlock table EMPLOYEE write"
    cursor.execute(sqlLock112)
cnx.close()
