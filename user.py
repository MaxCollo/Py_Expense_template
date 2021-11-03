from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New User - Name: ",
    }
]

def add_user(*args):
    if (args):
        user = {'user': args[0] }
    else:
        user = prompt(user_questions)

    # Error management
    if (type(user.get('user')) != str):
        print("Error. The user name must be a string !")
        return False

    csvfile = open('users.csv', 'a', newline='')
    userwriter = csv.writer(csvfile, delimiter=' '
                        , quotechar='|', quoting=csv.QUOTE_MINIMAL)
    userwriter.writerow([user.get('user')])
    print("User Created !")
    return True
