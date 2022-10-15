import subprocess as sp
import pymysql
import pymysql.cursors


def adduser():
    
    try:
        row = {}
        # q1  = "SELECT * FROM `customer`"
        # cur.execute(q1)
        # cur.fetchall()
        # rc = cur.rowcount
        print("Enter new user details: ")
        # row["cid"] = rc+1
        row["fav_drinkname"] = input("fav_drinkname: " )
        row["dob"] = input("Birth Date (YYYY-MM-DD): ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["fname"] = name[0]
        row["lname"] = name[1]
        query = "INSERT INTO customer(fav_drinkname,dob,fname,lname) VALUES('%s', '%s', '%s', '%s')" %(row["fav_drinkname"], row["dob"],row["fname"], row["lname"])
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return


def deleteuser():

    try:
        cid = int(input("Enter CID of Customer : "))
        # add oldcust
        query = "SELECT fname FROM customer WHERE cid=%d" %(cid)
        cur.execute(query)
        name = cur.fetchall()
        name = name[0]
        name = name['fname']
        query = "INSERT INTO oldcust(fname) VALUES('%s')" %(name)
        cur.execute(query)
        con.commit()
        #delete from from custguard
        query = "DELETE FROM custguard WHERE cid=%d" %(cid)
        cur.execute(query)
        con.commit()

        #delete from from drinktrans
        query = "DELETE FROM drinktrans WHERE cid=%d" %(cid)
        cur.execute(query)
        con.commit()

        #delete from from lovestogoto
        query = "DELETE FROM lovestogoto WHERE cid=%d" %(cid)
        cur.execute(query)
        con.commit()

        #delete from customer table
        query = "DELETE FROM customer WHERE cid=%d" %(cid)
        # adding to oldcust
        # cur.execute(query2)
        # con.commit()
        # old=cur.fetchall()
        # query3="INSERT"

        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print (">>>>>>>>>>>>>", e)

    return

def modifycustomer():
    try:
        cid = int(input("Enter the Customer ID : "))
        query="select cid from customer"
        cur.execute(query)
        lis2=cur.fetchall()
        con.commit()
        flag2=0
        for x in lis2:
            if x['cid']==cid:
                flag2=1
        if flag2==0:
            print("not in domain!!")
            return
        field = input("Enter the Attribute to modify : ")
        if field=="cid":
            print("Can't Change cid : It is Primary Key")
            return
        value = input("Enter the Attribute Value : ")
        query = "UPDATE `customer` SET %s = '%s' WHERE cid=%d" %(field,value,cid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to Update")
        print (">>>>>>>>>>>>>", e)

    return


def modifybar():
    try:
        bid = int(input("Enter the Bar ID : "))
        query="select bid from bar"
        cur.execute(query)
        lis3=cur.fetchall()
        con.commit()
        flag3=0
        for x in lis3:
            if x['bid']==bid:
                flag3=1
        if flag3==0:
            print("not in domain!!")
            return
        field = input("Enter the Attribute to modify : ")
        if field=="bid":
            print("Can't Change bar id : It is Primary Key")
            return
        if field=="contactno":
            value2= input("Enter contact no : ")
            query="select contactno from barcontact"
            cur.execute(query)
            lis7=cur.fetchall()
            con.commit()
            flag7=0
            for x in lis7:
                if x['contactno']==value2:
                    flag7=1
            if flag7==0:
                print("contact out of domain")
                return
            value = input("Enter the Attribute Value : ")
            query = "UPDATE barcontact SET %s='%s' WHERE bid=%d and contactno=%s" %(field,value,bid,value2)
            cur.execute(query)
            cur.fetchall()
            con.commit()
        else:
            value = input("Enter the Attribute Value : ")
            query = "UPDATE bar SET %s='%s' WHERE bid=%d" %(field,value,bid)
            cur.execute(query)
            cur.fetchall()
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to Update")
        print (">>>>>>>>>>>>>", e)

    return

def modifybarmanager():
    try:
        bid = int(input("Enter the Bar ID : "))
        mname = input("enter the manager name : ")
        query="select bid from bar_manager"
        cur.execute(query)
        lis4=cur.fetchall()
        con.commit()
        flag4=0
        for x in lis4:
            if x['bid']==bid:
                flag4=1
        query="select mname from bar_manager"
        cur.execute(query)
        lis5=cur.fetchall()
        con.commit()
        flag5=0
        for x in lis5:
            if x['mname']==mname:
                flag5=1
        if flag4==0 or flag5==0:
            print("not in domain!!")
            return
        field = input("Enter the Attribute to modify : ")
        if field=="bid":
            print("Can't Change bar id : It is Primary Key")
            return
        if field=="mname":
            print("Can't Change manager name : It is Primary Key")
            return    
        if field=="contactno":
            value2= input("Enter contact no : ")
            query="select contactno from mancontact"
            cur.execute(query)
            lis6=cur.fetchall()
            con.commit()
            flag6=0
            for x in lis6:
                if x['contactno']==value2:
                    flag6=1
            if flag6==0:
                print("contact out of domain")
                return
            value = input("Enter the Attribute Value : ")
            query = "UPDATE mancontact SET %s='%s' WHERE bid=%d and contactno=%s and mname='%s'" %(field,value,bid,value2,mname)
            cur.execute(query)
            cur.fetchall()
            con.commit()
            # print("haha")
        else:
            value = input("Enter the Attribute Value : ")
            query="select dname from drinks"
            cur.execute(query)
            lis=cur.fetchall()
            flag=0
            for x in lis:
                if value==x['dname']:
                    flag=1
            if flag==0:
                print("out of foreign key domain!!")
                return
            con.commit()
            query2 = "UPDATE `bar_manager` SET %s='%s' WHERE bid=%d and mname='%s'" %(field,value,bid,mname)
            cur.execute(query2)
            cur.fetchall()
            con.commit()
            
            # print("nanan")
    except Exception as e:
        con.rollback()
        print("Failed to Update")
        print (">>>>>>>>>>>>>", e)

    return

def cust_report():
    query = "SELECT fname,lname FROM `customer`"
    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    print(data)

def bar_report():
    query = "SELECT bname FROM `bar`"
    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    print(data)

def old_cust_report():
    query = "SELECT fname FROM `oldcust`"
    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    print(data)




def callfunc(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        adduser()
    elif(ch==2):
        deleteuser()
    elif(ch==3):
        modifycustomer()
    elif(ch==4):
        modifybar()
    elif(ch==5):
        modifybarmanager()
    elif(ch==6):
        cust_report()
    elif(ch==7):
        bar_report()
    elif(ch==8):
        old_cust_report()

    else:
        print("Error: Invalid Option")





while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='b',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)
        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Add Customer")
                print("2. Delete Customer")
                print("3. Modify Customer")
                print("4. Modify Bar")
                print("5. Modify Bar Manager")
                print("6. Customer Report")
                print("7. Bar Report")
                print("8. Old Customer Report")
                print("9. Logout")
                ch = int(input("Enter Choice > "))
                tmp = sp.call('clear', shell=True)
                if ch==9:
                    break
                else:
                    callfunc(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
