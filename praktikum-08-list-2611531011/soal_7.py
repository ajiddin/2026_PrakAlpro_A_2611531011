menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(number_of_days):
    daily_sales = []

    for menu in menus:
        portion = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(portion)
    sales.append(daily_sales)

print("Total per day:")

for i in range(number_of_days):
    daily_total = 0
    for j in range(len(menus)):
        daily_total += sales[i][j]
    print(f"Day {i + 1}: {daily_total}")

menu_totals = []

for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))

print("Total per menu:", menu_totals)

best_name = ""
best_total = -1

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")