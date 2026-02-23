expenses = []

print("WELCOME TO EXPENSE TRACKER APPLICATION")

while True:
    print("\n== Menu ==")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Date = input("Enter date: ")
        category = input("Enter category: ")
        Note = input("Enter note: ")
        Amount = float(input("Enter amount: "))

        expense_item = {
            "Date": Date,
            "Category": category,
            "Note": Note,
            "Amount": Amount
        }

        expenses.append(expense_item)
        print("✅ Expense added successfully")

    elif choice == 2:
        if len(expenses) == 0:
            print("❌ No expense found")
        else:
            for exp in expenses:
                print("Date:", exp["Date"])
                print("Category:", exp["Category"])
                print("Note:", exp["Note"])
                print("Amount:", exp["Amount"])
                print("----------")

    elif choice == 3:
        total = 0
        for exp in expenses:
            total += exp["Amount"]
        print("💰 Total Expense:", total)

    elif choice == 4:
        print("👋 Thank you for using Expense Tracker")
        break

    else:
        print("❌ Invalid choice")