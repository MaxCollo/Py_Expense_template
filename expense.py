from PyInquirer import prompt
import csv

def get_spenders(answers):
    users = []
    csvfile = open('users.csv', 'r', newline='')
    userreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in userreader:
        users.append(row[0])
    return users

def get_users_to_involve(answers):
    users_to_involve = []
    users = get_spenders([])
    for user in users:
        if (user == answers['spender_name']):
            users_to_involve.append({'name': user, 'checked': True})
        else:
            users_to_involve.append({'name': user})
    return users_to_involve

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
        'type': 'list',
        'name': 'spender_name',
        'message': 'New Expense - Spender: ',
        'choices': get_spenders
    },
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select involved users',
        'name': 'involved_users',
        'choices': get_users_to_involve
    }
]


def new_expense(*args):
    if (args):
        if args[2] in get_spenders([]):
            infos = {'amount': str(args[0]), 'label': args[1], 'spender_name': args[2]}
        else:
            return False
    else:
        infos = prompt(expense_questions)

    # Error management
    if (not(infos.get('amount').isdigit())):
        print("Error. The amount must be a number !")
        return False
    if (type(infos.get('label')) != str):
        print("Error. The label must be a string !")
        return False
    if (type(infos.get('spender_name')) != str):
        print("Error. The spender must be a string !")
        return False

    csvfile = open('expense_report.csv', 'a', newline='')
    expensewriter = csv.writer(csvfile, delimiter=' '
                        , quotechar='|', quoting=csv.QUOTE_MINIMAL)
    expensewriter.writerow([infos.get('amount'), infos.get('label')
                    , infos.get('spender_name'), infos.get('involved_users')])
    print("Expense Added !")
    return True
