from function import *
import mysql.connector
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

-Students are allowed to issue 1 maximum number of book, 7 maximum days of issue.

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

start()


                  

    
                  
                       
