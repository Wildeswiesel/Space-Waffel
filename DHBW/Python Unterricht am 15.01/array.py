

transactions = [
{"type": "purchase","amount":50, "date": "2024-01-14"},
{"type": "sale","amount":540, "date": "2024-01-15"},
{"type": "purchase","amount":250, "date": "2024-01-14"},
]

transaction_type =transactions[0]["type"]
transaction_amount =transactions[0]["amount"]
transaction_date =transactions[0]["date"]


# def list_of(my_key):
#     amount_values = [transaction[my_key] for transaction in transactions]
# print(list_of("amount"))

def sum_up(my_type, transactions):
    amount_values = [transactions['amount'] for transactions in transactions 
if transactions['type'] == my_type]
    return sum(amount_values)


income = sum_up("purchase", transactions)
expenses = sum_up("sale", transactions)
print("Einnahmen =", income)
print("Ausgaben =", expenses)

if income > expenses:
    print("Sie haben Geld verdient.")
else:
    print("Sie haben Geld verloren.")


def find_all(my_key,my_value):

    values = [transactions for transactions in transactions if
    transactions[my_key] == my_value]
    return(values)



my_transactions = find_all("date","2024-01-14")

print("wie viele Transaktionen wurden durch geführt am 14.01:",len(my_transactions))

import re

def is_valid_date_format(date_string):
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return bool(date_pattern.match(date_string))


my_date = my_transactions[0]["date"]
print(my_transactions[0]["date"])
print(type(my_date))
print(is_valid_date_format(my_date))


