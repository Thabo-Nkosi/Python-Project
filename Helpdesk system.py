
tickets = []

#Function to display the menu
def show_menu():
    print("*****IT HELP DESK MENU*****")
    print("1. Log a new issue")
    print("2. View all tickets")
    print("3. Update ticket status")
    print("4. exit!")

    #function to log a new issue
def log_issue():
    print("*****Log a new issue*****")
    username = input("Enter your name: ")
    department = input("Enter your department: ")
    issue = input("Describe the issue: ")

    ticket_id = len(tickets)+ 1
    ticket = {
        "id": ticket_id,
        "user": username,
        "department": department,
        "issue": issue,
        "status": "open"
        }
    tickets.append(ticket)
    print("Ticket ",ticket_id, "has been logged successfully!")

def view_tickets():
        print("*****All tickets*****")

        if not tickets:
            print("No tickets found!")
        else:
            for ticket in tickets:    
                print("Ticket ID: ",ticket['id'])
                print("Name: ", ticket['user'])
                print("Department: ",ticket['department'])
                print("Issue: ", ticket['issue'])
                print("Status: ",ticket['status'])

#Function to update ticket status
def update_status():
    if not tickets:
        print("No tickets to update!")
        return
    
    try:
        ticket_id =int(input("Enter the ticket id to update: "))
    except ValueError:
        print("invalid input.please enter a number!.")
        return

    for ticket in tickets:
        if ticket['id'] ==ticket_id:
            print("Current Status: ",ticket['status'])
            print("Update status to:")
            print("1.in progress")
            print("2. Resolved")
            status_choice = input("Enter choice( 1 or 2): ")

            if status_choice=="1":
                ticket['status'] = "In progress"
                print("Ticket ",ticket_id, " marked as in progress")

            elif status_choice== "2":
                ticket['status']= "Resolved"
                print("Ticket ", ticket_id, " marked as resolved")

            else:
                print("print invalid choice. status not updated.")
            return

        print("Ticket id ", ticket_id, " not found.")

        #main loop
while True:
    show_menu()
    choice = input("Enter your choice (1 to 4): ")

    if choice=="1":
        log_issue()

    elif choice == "2":
        view_tickets()

    elif choice=="3":
        update_status()

    elif choice =="4":
        print("Exiting the system Goodbye!")

        break
    else:
        
        print("Invalid choice. please chooce from 1 to 4.")


            

              
