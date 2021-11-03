from PyInquirer import prompt
import csv
from expense import get_spenders

def get_expenses():
    expenses = []
    csvfile = open('expense_report.csv', 'r', newline='')
    userreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in userreader:
        expenses.append(row)
    return expenses

def show_report():
    report = {}
    users = get_spenders([])
    for user in users:
        report[user] = 0.0

    expenses = get_expenses()
    for expense in expenses:
        involved_users = expense[3].replace("'", "").strip('][').split(', ')
        amount_due = int(expense[0])/len(involved_users)
        for involved_user in involved_users:
            report[involved_user] -= amount_due
    print(report)
    return True