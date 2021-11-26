import csv

names = []

with open('acpc_2021.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[2] in names:
                pass
            else:
                print(rf'\n{row[2]}, {row[4]}', end = "")
                names.append(row[2])
            line_count += 1

