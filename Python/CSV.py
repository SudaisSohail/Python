import csv

with open("Cousins2.csv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    
    for line in reader:
        print(line)
    
with open("Cousins2.csv", "w") as file:
    writer = csv.writer(file, delimiter="\t")
    
    data = [["number", "Name", "Age"], ["8", "Sarah", "9"], ["1", "Ibrahim", "2"]]
    
    for line in data:
        writer.writerow(line)
        
with open("Cousins.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for line in reader:
        print(line)
        
with open("Cousins2.csv", "w") as file:
    fieldnames = ["Number", "Name", "Age"]
    
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
    
    writer.writeheader()
    data = [{"Number":"7", "Name":"Sarah", "Age":"7"}, {"Number":"9", "Name":"Ibrahim", "Age":"2"}]
    
    for line in data:
        writer.writerow(line)
        
with open("Cousins2.csv", "r") as file:
    reader = csv.DictReader(file, delimiter='\t')
    
    for line in reader:
        print(line)