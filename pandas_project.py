import numpy as np 
import pandas as pd 
import csv
import datetime 


#function for total no. of assignments
def total_assignments():
    total = data['Status'].value_counts()
    print("total assignments =", data['Status'].count())
    print(total)

#function for assignment due today
def show_assignments1():
    mask1 = date_sorted['Due Date'] == today
    mask2 = date_sorted["Status"] == 'Pending'
    print("assignment due today:")
    print(date_sorted[mask1 & mask2])
    
#function for overdue assignment 
def show_assignments2():
    mask1 = date_sorted['Due Date'] < today
    mask2 = date_sorted["Status"] == 'Pending'
    print("assignments overdue:")
    print(date_sorted[mask1 & mask2])
    
#function for upcoming assignments 
def show_assignments3():
    mask1 = date_sorted['Due Date'] > today
    mask2 = date_sorted["Status"] == 'Pending'
    print("upcoming assignments:")
    print(date_sorted[mask1 & mask2])
    
#function for appending assignment 
def add_assignment():
    add = []
    sub = input("enter subject: ")
    name = input("enter assignment name: ")
    date = input("enter due date: ")
    priority = input("enter priority: high , medium , low: ") 
    add.append(sub)
    add.append(name)
    add.append(date)
    add.append("Pending")
    add.append(priority)
    with open("assignment_for_project.csv","a",newline="") as file:
        f1 = csv.writer(file)
        f1.writerow(add)
    
#function for updating assignment status
def update_status():
    update = input("enter assignment name whose status is to be updated: ")
    mask = date_sorted["Assignment Name"] == update 
    date_sorted.loc[mask,'Status'] = "Completed"
    print("assignment completed! \n Yayyyyy")
    date_sorted.to_csv("assignment_for_project.csv", index=False)
    
#function for deleting assignment
def delete_assignment():
    delete = input("enter assignment name to be deleted: ")
    mask = date_sorted['Assignment Name'] == delete
    date_sorted.drop(date_sorted[mask].index, inplace=True)
    print("assignment deleted")
    date_sorted.to_csv("assignment_for_project.csv", index=False)
    
data = pd.read_csv("assignment_for_project.csv")
data = data.dropna(subset=['Due Date'])
data['Due Date']= pd.to_datetime(data['Due Date'],format='%Y-%m-%d',errors='coerce').dt.date
#print(data["Due Date"])
#print(data["Due Date"].isna().sum())
today = datetime.date.today()
date_sorted = data.sort_values('Due Date')
# MENU 
print("Choose an option: \n 1. View all assignments \n 2. Add assignment \n 3. Update assignment status \n 4. Show assignment due today \n 5. Show overdue assignment \n 6. Show upcoming deadlines \n 7. delete an assignment \n 8. Exit")
while True: 
    n = int(input("enter option:"))
    if n == 1:
        print(data) 
        total_assignments()
    elif n == 2:
        add_assignment()
    elif n == 3:
        update_status()
    elif n == 4:
        show_assignments1()
    elif n == 5:
        show_assignments2()
    elif n == 6:
        show_assignments3()
    elif n == 7:
        delete_assignment()
    elif n == 8:
        break
    else:
        print(" invalid option \n Please try again")
    

        
