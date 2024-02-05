# Definiere die ursprüngliche Liste
mylist = [1, 3, 2, 4, 6, 8, 11, 99, 6, 1]

# Finde das Maximum in der Liste und gib es aus
max_value = max(mylist)
print("Das Maximum in der Liste ist:", max_value)

# Entferne Duplikate aus der Liste und gib die einzigartigen Werte aus
mylist = list(dict.fromkeys(mylist))
print("Die Liste nach Entfernen der Duplikate:", mylist)

# Überprüfe, ob die Liste nach dem Entfernen der Duplikate immer noch sortiert ist (optional)
if mylist == sorted(mylist):
    print("Die Liste ist sortiert.")
else:
    print("Die Liste ist nicht sortiert.")
