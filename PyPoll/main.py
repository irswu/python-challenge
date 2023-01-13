import os
import csv

path = os.path.join("Resources", "election_data.csv")

with open(path, "r", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    csv_header = next(reader)

    total_count = 0
    candidates = []
    candidates_all = []
    for row in reader:
        total_count = total_count + 1
        candidates_all.append(row[2])

        if row[2] not in candidates:
            candidates.append(row[2])
  
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for c in range(len(candidates_all)):
        if candidates_all[c] == candidates[0]:
            count_1 = count_1 + 1
        if candidates_all[c] == candidates[1]:
            count_2 = count_2 + 1
        if candidates_all[c] == candidates[2]:
            count_3 = count_3 + 1
        

    percentage_candidate1 = "{:.3%}".format(count_1/total_count)
    percentage_candidate2 = "{:.3%}".format(count_2/total_count)
    percentage_candidate3 = "{:.3%}".format(count_3/total_count)
    winner_count = max(count_1, count_2, count_3)
    count_list = [count_1,count_2,count_3]
    winner = candidates[count_list.index(winner_count)] 

    print("Election Results")
    print("-------------------")
    print(f"Total Votes: ")
    print("-------------------")
    print(f"{candidates[0]}: {percentage_candidate1} ({count_1})")
    print(f"{candidates[1]}: {percentage_candidate2} ({count_2})")
    print(f"{candidates[2]}: {percentage_candidate3} ({count_3})")
    print("-------------------")
    print(f"Winner: {winner}")
    print("-------------------")
    