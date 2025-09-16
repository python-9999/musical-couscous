from rich.console import Console
from rich.table import Table
from random import choice

console = Console()

number_of_columns = 2 # количество столбцов, по умолчанию стоит 2, можно менять

list_name = ["дима", "иван", "вася", "петя"]
list_age = list(range(1, 19))

table = Table(title="фейк данные")

table.add_column("Name", justify="center", no_wrap=True)
table.add_column("Age", justify="center", no_wrap=True)

for _ in range(number_of_columns):
    table.add_row(choice(list_name), str(choice(list_age)))

console.print(table) # выводим таблицу в консоль

# p.s программу запускал, все работает правильно