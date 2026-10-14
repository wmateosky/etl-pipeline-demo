import csv


def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
            
    ##These changes are done to test feature extract step branch
    ##This is the second change done to test feature extract step branch
    return rows
