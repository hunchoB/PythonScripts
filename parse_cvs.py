import csv

pathToFile = "D:\\vscodeProjects\\Python\\vipnet2020.csv"

file = open(pathToFile)
reader = csv.reader(file)
lines = len(list(reader))

print("File 2020 =   ",lines)

