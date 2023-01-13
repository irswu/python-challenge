import os
import csv

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    csv_header = next(reader)
    

    num_month = 0
    net_total = 0
    volumn = []
    date=[]
    for row in reader:
        num_month = num_month + 1               #total number of months
        net_total = net_total + int(row[1])      # net total amount of "Profit/Losses"

        volumn.append(int(row[1]))
        date.append(str(row[0]))
        

    change = 0
    change_list = []

    for x in range(len(volumn)):
        change = volumn[x] - volumn[x-1]
        change_list.append(int(change))
    
    del change_list[0]
    Average_change = round(sum(change_list) / len(change_list),2) #???????

    max_change = max(change_list)
    index_of_max = change_list.index(max_change)
    min_change = min(change_list)
    index_of_min = change_list.index(min_change)


    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {num_month} ")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${Average_change}")
    print(f"Greatest Increase in Profits:{date[index_of_max]} (${change_list[index_of_max]})")
    print(f"Greatest Decrease in Profits:{date[index_of_min]} (${change_list[index_of_min]})")
    
    
    
  
    
 
  
   

