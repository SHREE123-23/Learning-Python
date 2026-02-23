#Expense tracker application

expense =[] #list of dictionary in the  form of list
print ("WELCOME TO EXPENSE TRACKER APPLICATION")

while True:
    print("==Menu==")
    print("1.Add expense: ")
    print("2.View Expense:")
    print("3.View total expense: ")
    print("4.Exit: ")

#Add expense 

choice=int(input("Enter the Choice: "))
if choice==1:
    Date=input("Enter the date of expense: ")
    caterogery=input("Enter the category of Expense: ")
    Note=input("Enter the note of expense: ")
    Amount=float(input("Enter the amount of expense: "))

    expense={"Date":Date,
             "caterogery":caterogery,
             "Note":Note,
             "Amount":Amount}
    expense.append(expense)
    print("Expense added successfully")

#View Expense

elif choice==2:
     if(len(expense)==0):
          print("No expense found")

     else:
        for i in expense:
            print("Date :",i[Date])     
            print("caterogry: ",i[caterogery])
            print("Note:",i[Note])
            print("Amount:",i[Amount])
            i=i+1
            print("-------------")

#View Total Expense
elif choice==3:
    total=0
    for i in expense :
        total=total+i[Amount]
        print("Total Expense:",total)

#Exit
elif choice==4:
      print("Thank you for using the expense tracker application")
      break

else:
    print("Invalid choice: Please enter a valid choice")
    

    