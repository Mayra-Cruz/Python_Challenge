import os
import csv


total_months = []
total_revenue = []
average_change = [] 
greatest_increase = [] 
greatest_decrease = []


budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_months.append(row[0])
        total_revenue.append(int(row[1]))
    for i in range(len(total_revenue)-1):
        average_change.append(total_revenue[i+1]-total_revenue[i])

greatest_increase = max(average_change)
greatest_decrease = min(average_change)
month_great_increase = average_change.index(max(average_change))+1
month_great_decrease = average_change.index(min(average_change))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Revenue: ${sum(total_revenue)}")
print(f"Average Change in Revenue: ${round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Revenue: {total_months[month_great_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Revenue: {total_months[month_great_decrease]} (${(str(greatest_decrease))})")     

output = os.path.join("Analysis", "file.txt")
with open(output, "w") as text:
    text.write("Financial Analysis")
    text.write("\n")
    text.write(".....................................")
    text.write("\n")
    text.write(f"Total Months: {len(total_months)}")
    text.write("\n")
    text.write(f"Total Revenue: ${sum(total_revenue)}")
    text.write("\n")
    text.write(f"Average Change in Revenue: ${round(sum(average_change)/len(average_change),2)}")
    text.write("\n")
    text.write(f"Greatest Increase in Revenue: {total_months[month_great_increase]} (${(str(greatest_increase))})")
    text.write("\n")
    text.write(f"Greatest Decrease in Revenue: {total_months[month_great_decrease]} (${(str(greatest_decrease))})")

















    




    

