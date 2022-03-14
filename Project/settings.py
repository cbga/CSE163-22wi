import csv
global f
global wt


def init(new_file='data.csv'):
    global f
    global wt
    f = open(new_file, 'w', newline='', encoding="utf-8")
    wt = csv.writer(f)
