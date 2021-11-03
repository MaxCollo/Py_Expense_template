from PyInquirer import prompt
import csv


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    if (args):
        infos = {'amount': args[0], 'label': args[1], 'spender': args[2]}
    else:
        infos = prompt(expense_questions)

    # Error management
    if (type(infos.get('amount')) != int):
        print("Error. The amount must be a number !")
        return False
    if (type(infos.get('spender')) != str):
        print("Error. The spender must be a string !")
        return False


    csvfile = open('expense_report.csv', 'a', newline='')
    expensewriter = csv.writer(csvfile, delimiter=' '
                        , quotechar='|', quoting=csv.QUOTE_MINIMAL)
    expensewriter.writerow([infos.get('amount'), infos.get('label'), infos.get('spender')])
    print("Expense Added !")
    return True
