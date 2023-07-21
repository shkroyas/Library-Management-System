#function.py
import mysql.connector
'''Library functions'''

#functions
def start1():
      print('''                                               Welcome to DPS Senior Library
                                                                   When in doubt, go to library!
Guidelines


General Rules

-No library material can be taken out of the library without permission. Unauthorized removal of anything belonging to the
 library will be treated as theft and dealt accordingly.
-Any  one  who  violates  the  rules  and  regulations  of  the  library  would  be  liable  to  lose  the  privilege  of
 library membership and may be debarred from using the library facilities.
-Suggestions on all aspects, of library services are welcome.
-The library remains open throughout the school timings but the books cannot be returned or issue during lunch break
 (11:30-12:30)
-The library may be closed during non-academic days of school.
-No student will be allowed to avail library facility without valid ID card and library card. The borrower cards are not
 transferable
-For availing library facility, students should be in proper uniform.

Issue/Return Rules

-Students are allowed to issue 2 maximum number of books, 15 maximum days of issue.

Fine for late return books/journals

-Books must be return on or before the due date otherwise the fine of Rs. 5 will be charged per day/book.
-At the time of deposition of late fine you must collect receipt for the payment from the library.
-Absence & illness are not acceptable excuses for exemption from paying overdue charges.
-If the Due Date falls on holiday declare by collage, then students may return their books on the next week on scheduled
 day.
-User(s) has to return all issued books when he/ she is out of station for more than fifteen days.
-In spite of repeated reminders, if the book is not returned, the borrowing facility may be withdrawn for a period
-decided by the authority. Also, if the student fails to deposit the issued book for more than 60 days from the date of
 due then he/she may have to pay the fine amount including the current MRP of the book.

Renewal of books

-Users can also renew the books again after the completion of charging period, subject to not being requested from
 some other user.


                             Login for Academic Year 2021-22''');
      user =input("User ID:")
      password=input("Password:")

      if user =="6230004" and password=="admin":
            main()
      else:
            print("Invalid credentials")
def main():
            print("Login Successful")
            print()
            print("1. Students details")
            print("2. Books details")
            print("3. Add books")
            print("4. Delete books")
            print("5. Submit books & Fine")
            print("6. Issue book")
            print("7. Total Penalty Collection")
            print("8. Logout")
            choice10=int(input("Enter your choice:"))
            if choice10==1:
                student2()
            if choice10==2:
                books()
            if choice10==3:
                add()                 
            if choice10==4:
                  dell()
            if choice10==5:
                  submit_books()
            if choice10==6:
                  issue_books()
            if choice10==7:
                  penalty()
            if choice10==8:
                  start()
def start():
      print('''                                               Welcome to DPS Senior Library
                                                                   When in doubt, go to library!
Guidelines


General Rules

-No library material can be taken out of the library without permission. Unauthorized removal of anything belonging to the
 library will be treated as theft and dealt accordingly.
-Any  one  who  violates  the  rules  and  regulations  of  the  library  would  be  liable  to  lose  the  privilege  of
 library membership and may be debarred from using the library facilities.
-Suggestions on all aspects, of library services are welcome.
-The library remains open throughout the school timings but the books cannot be returned or issue during lunch break
 (11:30-12:30)
-The library may be closed during non-academic days of school.
-No student will be allowed to avail library facility without valid ID card and library card. The borrower cards are not
 transferable
-For availing library facility, students should be in proper uniform.

Issue/Return Rules

-Students are allowed to issue 2 maximum number of books, 15 maximum days of issue.

Fine for late return books/journals

-Books must be return on or before the due date otherwise the fine of Rs. 5 will be charged per day/book.
-At the time of deposition of late fine you must collect receipt for the payment from the library.
-Absence & illness are not acceptable excuses for exemption from paying overdue charges.
-If the Due Date falls on holiday declare by collage, then students may return their books on the next week on scheduled
 day.
-User(s) has to return all issued books when he/ she is out of station for more than fifteen days.
-In spite of repeated reminders, if the book is not returned, the borrowing facility may be withdrawn for a period
-decided by the authority. Also, if the student fails to deposit the issued book for more than 60 days from the date of
 due then he/she may have to pay the fine amount including the current MRP of the book.

Renewal of books

-Users can also renew the books again after the completion of charging period, subject to not being requested from
 some other user.


                             Login for Academic Year 2021-22''');
      user =input("User ID:")
      password=input("Password:")

      if user =="6230004" and password=="admin":
            main()
      else:
            print("Invalid credentials")
def main1():
            print("Login Successful")
            print()
            print("1. Students details")
            print("2. Books details")
            print("3. Add books")
            print("4. Delete books")
            print("5. Submit books & Fine")
            print("6. Issue book")
            print("7. Total Penalty Collection")
            print("8. Logout")
            choice10=int(input("Enter your choice:"))
            if choice10==1:
                student2()
            if choice10==2:
                books()
            if choice10==3:
                add()                 
            if choice10==4:
                  dell()
            if choice10==5:
                  submit_books()
            if choice10==6:
                  issue_books()
            if choice10==7:
                  penalty()
            if choice10==8:
                  start()

def disabed_students():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM disabed_students;")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print("1. Disable")
        print("Go back")
        c=int(input("Enter your choice:"))
        if c==1:
                dis_roll=int(input("Enter the Student's roll no. you want to disable or 0 to exit"))
                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                mycursor = mydb.cursor()
                my_data=(dis_roll,)
                q="SELECT * FROM all_students WHERE Ad_No=%s"
                mycursor.execute(q,my_data)
                myresult = mycursor.fetchone()
                sql = "INSERT INTO disabed_students(Ad_No,Name,Class,Stream,Section,Phone_no,Status,Book_Issued,No_of_Books) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
                mycursor.execute(sql, myresult)
                mydb.commit()
                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                mycursor = mydb.cursor()
                my_data=(dis_roll,)
                q="UPDATE all_students SET status = 'DISABLED' WHERE AD_NO =%s"
                mycursor.execute(q,my_data)
                mydb.commit()
                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                mycursor = mydb.cursor()
                my_data=(dis_roll,)
                q="UPDATE disabed_students SET status = 'DISABLED' WHERE AD_NO =%s"
                mycursor.execute(q,my_data)
                mydb.commit()
                print("Operation successful")
                main1()
        else:
                student2()
def available_students():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM all_students where STATUS='ENABLED';")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print("1. Enable")
        print("Go back")
        c=int(input("Enter your choice:"))
        if c==1:
                ava_roll=int(input("Enter the Student's roll no. you want to enable or 0 to exit"))
                print("Operation successful")
                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                mycursor = mydb.cursor()
                my_data=(ava_roll,)
                q="UPDATE all_students SET status = 'ENABLED' WHERE AD_NO =%s"
                mycursor.execute(q,my_data)
                mydb.commit()
                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                mycursor = mydb.cursor()
                my_data=(ava_roll,)
                q="DELETE FROM disabed_students WHERE Ad_No=%s"
                mycursor.execute(q,my_data)
                mydb.commit()
                print("Operation successful")
        else:
                student2()
def search_roll():
        _roll=int(input("Enter the Student's roll no."))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_roll,)
        q="SELECT Ad_No,Name,Class,Stream,Section,Phone_no,Status,No_of_Books FROM all_students WHERE Ad_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        main1()
def search_name():
        _name=input("Enter the Student's name")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_name,)
        q="SELECT Ad_No,Name,Class,Stream,Section,Phone_no,Status,No_of_Books FROM all_students WHERE Name=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        main1()
def search_class():
        _class=input("Enter the Student's class")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_class,)
        q="SELECT Ad_No,Name,Class,Stream,Section,Phone_no,Status,No_of_Books FROM all_students WHERE CLASS=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        main1()
def search_stream():
        _stream=input("Enter the Student's stream")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_stream,)
        q="SELECT Ad_No,Name,Class,Stream,Section,Phone_no,Status,No_of_Books FROM all_students WHERE STREAM=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        main1()
def all_students():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM all_students;")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print("1. Search students")
        print("Go back")
        f=int(input("Enter your choice:"))
        if f==1:
            print("1. Search by Roll no.")
            print("2. Search by Name")
            print("3. Search by Class")
            print("4. Search by Stream")
            print("GO BACK")
            choice1=int(input("Enter your choice:"))
            if choice1==1:
                search_roll()
            elif choice1==2:
                search_name()
            elif choice1==3:
                search_class()
            elif choice1==4:
                search_stream()
            else:
                student2()
        else:
            student2()
def student2():
        print("1. Disable Students")
        print("2. Available Students")
        print("3. All Students")
        print("4. Go back")
        choice=int(input("Enter your choice:"))
        if choice==1:
            disabed_students()          
        if choice==2:
            available_students()
        if choice==3:
            all_students()
        else:
            main1()


def search_code():
        _code=int(input("Enter the Book's code no."))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_code,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP,AD_NO FROM ISSUE_BOOKS WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_title():
        _title=(input("Enter the Book's title"))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_title,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP,AD_NO FROM ISSUE_BOOKS WHERE TITLE=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_subject():
        _subject=input("Enter the Student's subject")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_subject,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP,AD_NO FROM ISSUE_BOOKS WHERE SUBJECT=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_author():
        _author=input("Enter the Student's author")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_author,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP,AD_NO FROM ISSUE_BOOKS WHERE AUTHOR=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
            
def issued_books():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM issue_books;")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        print("1. Search Issued Books")
        print("Go back")
        o=int(input("Enter your choice:"))
        if o==1:
            print("1. Search by Code no.")
            print("2. Search by Title")
            print("3. Search by Subject")
            print("4. Search by Author")
            choice2=int(input("Enter your choice:"))
            if choice2==1:
                search_code()
            elif choice2==2:
                search_title()
            elif choice2==3:
                search_subject()
            elif choice2==4:
                search_author()
            else:
                books()
        else:
            books()
def search_code1():
        _code=int(input("Enter the Book's code no."))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_code,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE STATUS='AVAILABLE' AND Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_title1():
        _title=(input("Enter the Book's title"))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_title,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE STATUS='AVAILABLE' AND TITLE=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_subject1():
        _subject=input("Enter the Book's subject")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_subject,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE STATUS='AVAILABLE' AND SUBJECT=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_author1():
        _author=input("Enter the Book's author")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_author,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE STATUS='AVAILABLE' AND AUTHOR=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def available_books():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM all_books WHERE STATUS='AVAILABLE';")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        print("1. Search Available Books")
        print("GO Back")
        c=int(input("Enter your choice:"))
        if c==1:
                print("1. Search by Code no.")
                print("2. Search by Title")
                print("3. Search by Subject")
                print("4. Search by Author")
                choice3=int(input("Enter your choice:"))
                if choice3==1:
                        search_code1()
                elif choice3==2:
                        search_title1()
                elif choice3==3:
                        search_subject1()
                elif choice3==4:
                        search_author1()
                else:
                        books()
        else:
                books()
def search_code2():
        _code=int(input("Enter the Book's code no."))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_code,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_title2():
        _title=(input("Enter the Book's title"))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_title,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE TITLE=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_subject2():
        _subject=input("Enter the Book's subject")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_subject,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE SUBJECT=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()
def search_author2():
        _author=input("Enter the Book's author")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_author,)
        q="SELECT Code_No,Title,Subject,Author,Edition,Status,MRP FROM ALL_BOOKS WHERE AUTHOR=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def all_books():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM all_books;")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        print("1. Search Available Books")
        print("GO Back")
        p=int(input("Enter your choice:"))
        if p==1:
            print("1. Search by Code no.")
            print("2. Search by Title")
            print("3. Search by Subject")
            print("4. Search by Author")
            choice4=int(input("Enter your choice:"))
            if choice4==1:
                search_code2()
            elif choice4==2:
                search_title2()
            elif choice4==3:
                search_subject2()
            elif choice4==4:
                search_author2()
            else:
                books()
        else:
            books()
def update_title():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        up_books=int(input("Enter the Book's code no. you want to update or 0 to exit"))
        my_data=(up_books,)
        q="SELECT * FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        title=input("Enter the new title:")
        aaa=(title,up_books,)
        mycursor = mydb.cursor()
        q="UPDATE all_books SET title = %s WHERE Code_no = %s"
        mycursor.execute(q,aaa)
        mydb.commit()
        print("Operation successful")
        main1()
def update_subject():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        up_books=int(input("Enter the Book's code no. you want to update or 0 to exit"))
        my_data=(up_books,)
        q="SELECT * FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        subject=input("Enter the new subject:")
        aaa=(subject,up_books,)
        mycursor = mydb.cursor()
        q="UPDATE all_books SET subject = %s WHERE Code_no = %s"
        mycursor.execute(q,aaa)
        mydb.commit()
        print("Operation successful")
        main1()
def update_author():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        up_books=int(input("Enter the Book's code no. you want to update or 0 to exit"))
        my_data=(up_books,)
        q="SELECT * FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        author=input("Enter the new author:")
        aaa=(author,up_books,)
        mycursor = mydb.cursor()
        q="UPDATE all_books SET author = %s WHERE Code_no = %s"
        mycursor.execute(q,aaa)
        mydb.commit()
        print("Operation successful")
        main1()
def update_edition():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        up_books=int(input("Enter the Book's code no. you want to update or 0 to exit"))
        my_data=(up_books,)
        q="SELECT * FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        edition=input("Enter the new edition:")
        aaa=(edition,up_books,)
        mycursor = mydb.cursor()
        q="UPDATE all_books SET edition = %s WHERE Code_no = %s"
        mycursor.execute(q,aaa)
        mydb.commit()
        print("Operation successful")
        main1()
def update_MRP():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        up_books=int(input("Enter the Book's code no. you want to update or 0 to exit"))
        my_data=(up_books,)
        q="SELECT * FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        MRP=input("Enter the new MRP:")
        aaa=(MRP,up_books,)
        mycursor = mydb.cursor()
        q="UPDATE all_books SET MRP = %s WHERE Code_no = %s"
        mycursor.execute(q,aaa)
        mydb.commit()
        print("Operation successful")
        main1()

def new_books():
        aa=int(input("Enter Code_No:"))
        bb=input("Enter Title:")
        cc=input("Enter Subject:")
        dd=input("Enter Author:")
        ee=input("Enter Edition:")
        ff=input("Enter MRP:")
        txt=(aa,bb,cc,dd,ee,ff)
        print(txt)
        pr=input("Do you want to continue? If yes, then enter y otherwise press any key")
        if pr=='y':
            mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
            mycursor = mydb.cursor()
            sql = "INSERT INTO all_books(Code_No,title,subject,author,Edition,MRP) VALUES (%s,%s,%s,%s,%s,%s)"
            myresult=(aa,bb,cc,dd,ee,ff)
            mycursor.execute(sql, myresult)
            mydb.commit()
            print("Operation successful")
        else:
            add()
def update_books():
        print("1. Update Title")
        print("2. Update Subject")
        print("3. Update Author")
        print("4. Update Edition")
        print("5. Update MRP")
        print("Go Back")
        choice6=int(input("Enter your choice:"))
        if choice6==1:
                update_title()
        elif choice6==2:
                update_subject()
        elif choice6==3:
                update_author()
        elif choice6==4:
                update_edition()
        elif choice6==5:
                update_MRP()
        

def add():
            print("1. New Books")
            print("2. Update Books")
            print("GO BACK")
            choice5=int(input("Enter your choice:"))
            if choice5==1:
                    new_books()
            if choice5==2:
                    update_books()
            else:
                main1()
        

def search_code3():
        _code=int(input("Enter the Book's code no."))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_code,)
        q="SELECT * FROM deleted_BOOKS WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def search_title3():
        _title=(input("Enter the Book's title"))
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_title,)
        q="SELECT * FROM DELETED_BOOKS WHERE TITLE=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def search_subject3():
        _subject=input("Enter the Book's class")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_subject,)
        q="SELECT * FROM DELETED_BOOKS WHERE SUBJECT=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def search_author3():
        _author=input("Enter the Book's author")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_author,)
        q="SELECT * FROM DELETED_BOOKS WHERE AUTHOR=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def search_dd():
        _dd=input("Enter the Book's date of deletion")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_dd,)
        q="SELECT * FROM DELETED_BOOKS WHERE DELETEDDATE=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def search_reason():
        _reason=input("Enter the Book's reason for deletion")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        my_data=(_reason,)
        q="SELECT * FROM DELETED_BOOKS WHERE reason=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        main1()

def books():
        print("1. Issued Books")
        print("2. Available Books")
        print("3. All Books")
        print("GO BACK")
        choice=int(input("Enter your choice:"))
        if choice==1:
            issued_books()                           
        if choice==2:
            available_books()   
        if choice==3:
            all_books()
        else:
            books()
            
def delete_books():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        del_books=int(input("Enter the Book's code no. you want to delete or 0 to exit"))
        my_data=(del_books,)
        q="SELECT Code_No,Title,Subject,Author,Edition,MRP FROM all_books WHERE Code_No=%s"
        mycursor.execute(q,my_data)
        myresult = mycursor.fetchone()
        print(myresult)
        yt=input("Do you want to continue? If yes, enter y otherwise enter any key")
        if yt=='y':
            bbb=input("Enter date of delete:")
            ccc=input("Enter reason of delete:")
            jj=(bbb,ccc,)
            ss=myresult+jj
            sql = "INSERT INTO deleted_books(Code_No,Title,Subject,Author,Edition,MRP,DeletedDate,Reason) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,ss)
            mydb.commit()
            mycursor = mydb.cursor()
            j="DELETE FROM ALL_BOOKS WHERE Code_No=%s"
            mycursor.execute(j,my_data)
            mydb.commit()
            mycursor = mydb.cursor()
            k="SELECT Code_No FROM ISSUE_BOOKS"
            mycursor.execute(k)
            myresult = mycursor.fetchone()
            t=len(myresult)
            for i in myresult[0:t]:
                if i == del_books:
                        mycursor = mydb.cursor()
                        z="DELETE FROM ISSUE_BOOKS WHERE Code_No=%s"
                        mycursor.execute(z,my_data)
                        mydb.commit()
                        print("Operation Suceessful")
        else:
            dell()
def search_delete():
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM deleted_books;")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print("1.Search")
        print("GO BACK")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print("1. Search by Code no.")
            print("2. Search by Title")
            print("3. Search by Subject")
            print("4. Search by Author")
            print("5. Search by Deleted Date")
            print("6. Search by Reason")
            print("GO BACK")
            choice8=int(input("Enter your choice:"))
            if choice8==1:
                    search_code3()
            elif choice8==2:
                    search_title3()
            elif choice8==3:
                    search_subject3()
            elif choice8==4:
                    search_author3()
            elif choice8==5:
                    search_dd()
            elif choice8==6:
                    search_reason()
            else:
                dell()
        else:
            dell()

def dell():
            print("1. Search Deleted Books")
            print("2. Delete Books")
            print("Go Back")
            choice7=int(input("Enter your choice:"))
            if choice7==1:
                search_delete()
            elif choice7==2:
                delete_books()
            else:
                main1()



def issue_books():
        print("1. Issue Book")
        print("GO BACK")
        we=int(input("Enter your choice:"))
        ww=[]
        if we==1:
            _issue=int(input("Enter the Book's Code No you want to issue"))
            mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
            mycursor = mydb.cursor()
            k="SELECT Code_No FROM ISSUE_BOOKS"
            mycursor.execute(k)
            myresult = mycursor.fetchall()
            #print(myresult)
            for row in myresult:
                  p=int(row[0])
                  print(p)
                  if p==_issue:
                        print("Sorry! Books already issued")
                        issue_books()
                        break
            else:
                    _adno=int(input("Enter the Student's Admission No to whom you want to issue"))
                    ap=[]
                    mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                    mycursor = mydb.cursor()
                    l="SELECT Ad_No FROM disabed_students"
                    mycursor.execute(l)
                    myresult = mycursor.fetchall()
                    for i in myresult:
                          q=int(i[0])
                          if q == _adno:
                              print("Sorry! Student disabled. Cannot issue book")
                              issue_books()
                    else:
                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                        mycursor = mydb.cursor()
                        ww=(_adno,)
                        p="SELECT No_of_Books FROM all_students where Ad_No=%s"
                        mycursor.execute(p,ww)
                        myresult = mycursor.fetchall()
                        for oo in myresult:
                              if oo[0]<1:
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my=("ISSUED",_issue,)
                                        cc="UPDATE all_books SET STATUS =%s WHERE Code_no = %s"
                                        mycursor.execute(cc,my)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my_data=(_issue,)
                                        q="SELECT Code_No,Title,Subject,Author,Edition,MRP FROM ALL_BOOKS WHERE Code_No=%s"
                                        mycursor.execute(q,my_data)
                                        myre = mycursor.fetchone()
                                        print(myre)
                                        bbbb=input("Enter date of issue:")
                                        yy=(bbbb,)
                                        mm=myre+yy
                                        sql = "INSERT INTO submit_books(Code_No,Title,Subject,Author,Edition,MRP,DateofIssue) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                                        mycursor.execute(sql,mm)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my_data=(_issue,)
                                        q="SELECT Code_No,Title,Subject,Author,Edition,MRP,status FROM ALL_BOOKS WHERE Code_No=%s"
                                        mycursor.execute(q,my_data)
                                        my_da = mycursor.fetchone()
                                        qq="INSERT INTO ISSUE_BOOKS(Code_No,Title,Subject,Author,Edition,MRP,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                                        mycursor.execute(qq,my_da)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my_dt=(_adno,_issue)
                                        ff="UPDATE issue_books SET Ad_no =%s WHERE Code_no = %s"
                                        mycursor.execute(ff,my_dt)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my_dd=(_adno,_issue)
                                        ff="UPDATE submit_books SET Ad_no =%s WHERE Code_no = %s"
                                        mycursor.execute(ff,my_dd)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        my=(_issue, _adno, )
                                        ii="UPDATE all_students SET Book_Issued =%s WHERE Ad_no = %s"
                                        mycursor.execute(ii,my)
                                        mydb.commit()
                                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                        mycursor = mydb.cursor()
                                        m=(1,_adno, )
                                        ii="UPDATE all_students SET  No_of_Books = %s WHERE Ad_no = %s"
                                        mycursor.execute(ii,m)
                                        mydb.commit()
                                        print("Operation Suceessful")
                                        main1()
                                        break
                              else:
                                    print("No. of Issued Books exceeded")
                                    issue_books()
        else:
            main1()
            



def submit_books():
        print("1. Submit Book")
        print("GO BACK")
        at=[]
        we=int(input("Enter your choice:"))
        if we==1:
            _submit=int(input("Enter the Book's Code No you want to submit"))
            mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
            mycursor = mydb.cursor()
            k="SELECT Code_No FROM ISSUE_BOOKS"
            mycursor.execute(k)
            myresult = mycursor.fetchall()
            for row in myresult:
                  p=int(row[0])
                  if p==_submit:
                        _dos=input("Enter the Book's date of submission")
                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                        mycursor = mydb.cursor()
                        q1=(_submit,)
                        k="SELECT DateofIssue FROM SUBMIT_BOOKS where Code_No=%s"
                        mycursor.execute(k,q1)
                        myresult = mycursor.fetchall()
                        for row in myresult:
                                a=row[0]
                        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                        mycursor = mydb.cursor()
                        q2=(_dos, a, )
                        k="SELECT DATEDIFF(%s,%s)"
                        mycursor.execute(k,q2)
                        myresult = mycursor.fetchall()
                        for row in myresult:
                                t1=int(row[0])
                                if t1<0:
                                        print("Invalid data for submission")
                                        submit_books()
                        else:
                                        if t1<=7:
                                                print("No Penalty")
                                                final=0
                                        elif t1>7 and t1<=60:
                                                print("Sorry!, Late to submit penalty will be charged")
                                                g=t1-7
                                                final=g*5
                                                print("Your total penalty is",final)
                                        elif t1>60:                                                
                                                print("Sorry!, too late to submit penalty will be charged along with MRP")
                                                g=t1-7
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q3=(_submit, )
                                                k="SELECT MRP FROM SUBMIT_BOOKS WHERE CODE_NO=%s"
                                                mycursor.execute(k,q3)
                                                myresult = mycursor.fetchall()
                                                for row in myresult:
                                                        u=row[0]
                                                final=u+g*5
                                                print("Your total penalty is",final)
                                        process=input("Do you wish to process further? If yes press y or else press any key ")
                                        if process=='y':
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q4=(_submit, )
                                                k="DELETE FROM issue_BOOKS WHERE CODE_NO=%s"
                                                mycursor.execute(k,q4)
                                                mydb.commit()
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q5=(_dos,_submit, )
                                                k="UPDATE SUBMIT_BOOKS SET DateofSubmission=%s WHERE CODE_NO=%s"
                                                mycursor.execute(k,q5)
                                                mydb.commit()
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q8=(final,_submit, )
                                                k="UPDATE SUBMIT_BOOKS SET FINE=%s WHERE CODE_NO=%s"
                                                mycursor.execute(k,q8)
                                                mydb.commit()
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q6=(_submit, )
                                                k="UPDATE ALL_BOOKS SET STATUS='AVAILABLE' WHERE CODE_NO=%s"
                                                mycursor.execute(k,q6)
                                                mydb.commit()
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q7=(_submit,)
                                                k="SELECT Ad_No FROM SUBMIT_BOOKS where Code_No=%s"
                                                mycursor.execute(k,q7)
                                                myresult = mycursor.fetchall()
                                                for row in myresult:
                                                        _A=row[0]
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q6=(_A, )
                                                k="UPDATE ALL_STUDENTS SET  Book_Issued='NULL' WHERE AD_NO=%s"
                                                mycursor.execute(k,q6)
                                                mydb.commit()
                                                mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
                                                mycursor = mydb.cursor()
                                                q8=(0,_A, )
                                                k="UPDATE ALL_STUDENTS SET   No_of_Books=%s WHERE AD_NO=%s"
                                                mycursor.execute(k,q8)
                                                mydb.commit()
                                                print("Operation Suceessful")
                                                main1()
                                                break
                                        else:
                                            main1()
            else :
                        print("Sorry! Book not issued")
                        main1()
        else:
            main1()

def penalty():
        ab=0
        za=input("Enter the starting date:")
        zx=input("Enter the ending date:")
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mb=(za,zx,)
        l="SELECT * FROM submit_books WHERE DateofSubmission BETWEEN %s AND %s"
        mycursor.execute(l,mb)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        mydb = mysql.connector.connect(host="localhost",user="root",password="library",database="library")
        mycursor = mydb.cursor()
        mb=(za,zx,)
        l="SELECT Fine FROM submit_books WHERE DateofSubmission BETWEEN %s AND %s"
        mycursor.execute(l,mb)
        myresult = mycursor.fetchall()
        for x in myresult:
            for row in x:
                      if row==None:
                            row=0
                            continue
            else:
                  ab=ab+row 
        print("Total penalty collected:",ab)
        main1()
        
                        
                        
        
                
        
        
        
        
