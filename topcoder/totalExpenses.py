branding_Expenses = int(input("Enter branding expenses\n"))
travel_Expenses = int(input("Enter travel expenses\n"))
food_Expenses = int(input("Enter food expenses\n"))
logistics_Expenses = int(input("Enter logistics expenses\n"))

total_Expenses = (branding_Expenses + travel_Expenses + food_Expenses + logistics_Expenses)
print(f"Total expenses : Rs.{total_Expenses:.2f}")

branding_Percentage = (branding_Expenses / total_Expenses) * 100
travel_Percentage = (travel_Expenses / total_Expenses) * 100
food_Percentage = (food_Expenses / total_Expenses) * 100
logistics_Percentage = (logistics_Expenses / total_Expenses) * 100

print(f"Branding expenses percentage : {branding_Percentage:.2f}%")
print(f"Travel expenses percentage : {travel_Percentage:.2f}%")
print(f"Food expenses percentage : {food_Percentage:.2f}%")
print(f"Logistics expenses percentage : {logistics_Percentage:.2f}%")

'''
Sample Input:
Enter branding expenses
20000
Enter travel expenses
40000
Enter food expenses
15000
Enter logistics expenses
25000

Sample Output:
Total expenses : Rs.100000.00
Branding expenses percentage : 20.00%
Travel expenses percentage : 40.00%
Food expenses percentage : 15.00%
Logistics expenses percentage : 25.00%
'''
