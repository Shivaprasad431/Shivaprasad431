from datetime import datetime

import psycopg2
from colorama import Back, Fore, Style

hostname='localhost'
database='contacts'
username='postgres'
pwd='shiva'
port_id=5432

connection=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id)
connection.autocommit = True # "autcommit" set to True, so you don't have to commit your queries.
cursor = connection.cursor()

# Create Database Query
# Suppose we are asking user to choose, name of the database,


x=str(input("If you have account type Y and if you dont have account type N \n"))
if x=="y" or x=="Y":
    
        name=str(input("Enter your name\n"))
        fetch_loginid=f'''
             
             SELECT login_id FROM details WHERE login_id='{name}' 
             
        '''
        cursor.execute(fetch_loginid)
        for row in cursor:
          if name==row[0]:
            continue
          else:
            print(Fore.RED+"Wrong login_id")
            exit()
        password=str(input("Enter your Password\n"))
        fetch_password=f'''

            SELECT password FROM details WHERE  password='{password}'
        '''
        cursor.execute(fetch_password)
        for row in cursor:

          if password==row[0]:
           print("USER LOGIN SUCCESSFULL")
           dt=datetime.today();
           print(dt)
          else:
           print(Fore.RED+"Incorrect password")
           dt=datetime.today();
           print(dt)
           exit()
        



else:
    name=str(input("Enter a name\n"))
    password=str(input("enter your password\n"))
    insert=f'''
      insert into details values('{name}','{password}')
   
    
    '''
    cursor.execute(insert)
   
    name=str(input("Enter your name\n"))
    
    fetch_loginid=f'''
             
             SELECT login_id FROM details WHERE login_id='{name}' 
             
        '''
    cursor.execute(fetch_loginid)
    for row in cursor:
          if name==row[0]:
            continue
          else:
            print(Fore.RED+"Wrong login_id")
            dt=datetime.today();
            print(dt)
            exit()
    password=str(input("__Enter your Password\n__"))
    fetch_password=f'''

            SELECT password FROM details WHERE  password='{password}'
        '''
    cursor.execute(fetch_password)
    for row in cursor:
          if password==row[0]:
           print("\033[1;32m USER LOGIN SUCCESSFULL")
           dt=datetime.today();
           print(dt)
          else:
           print(Fore.RED+"Incorrect password")
           
           dt=datetime.today();
           print(dt)
           exit()

print("Add 1\nRead 2\nUpdate 3\nDelete 4\nExit 5")
change=int(input("enter the above one which one you have to change\n"))

if change==1:
    for _ in range(int(input("Enter no of contacts you want to insert\n"))):
      contact_id=int(input("Enter  contact_id\n"))
      First_name=str(input("Enter contact first name\n"))
      Last_name=str(input("Enter contact last name\n"))
      email=str(input("Enter contact Email\n"))
      PhoneNumber=int(input("Enter contact phone number\n"))
      inserting_details=f'''

         INSERT INTO contactinfo values ({contact_id},'{First_name}','{Last_name}','{email}',{PhoneNumber})
      '''
      cursor.execute(inserting_details)
      print("DATA INSERTED SUCCESFULLY")
      dt=datetime.today();
      print(dt)
      exit(())
elif change==2:
      knowing=str(input("enter all to print all your contacts or \nenter one for single contact\n"))
      try:
        if knowing=="all" or knowing=="All"  or knowing=='ALL':
          fetch_user=f'''
         SELECT * FROM contactinfo 
         '''
          cursor.execute(fetch_user)
          for row in cursor:
           print(row)
        else:
          single=str(input("Enter the first name of the contact\n"))
          fetch_user=f'''
          SELECT * FROM contactinfo WHERE first_name='{single}'
          '''
          cursor.execute(fetch_user)
          for row in cursor:
           print(row)
      except Exception as e:
        print(e)
elif change==3:
    
      try:
       update_input=str(input("Enter what you want update \n contact_id \n first_name \n last_name \n email \n phone_number \n"))
       old_detail=input("Enter old value\n")
       new_detail=input("enter new value\n")
       updating_details=f'''
     UPDATE contactinfo SET {update_input}='{new_detail}' WHERE {update_input}='{old_detail}'
      '''
       cursor.execute(updating_details)
      except Exception as e:
        print(e)
elif change==4:
     all_delete=str(input("Enter all to delete all the contacts\n"))
     if all_delete=="all" or all_delete=="All" or all_delete=="ALL":
      delete_details=f'''
      DELETE FROM contactinfo
      '''
      cursor.execute(delete_details)
     else:
      fname=str(input("enter the first name of the contact ypu want to delete\n"))
      delete_one=f'''
      DELETE FROM contactinfo WHERE firstname={fname}
      '''
elif change==5:
    exit()
dt=datetime.today();
print(dt)

