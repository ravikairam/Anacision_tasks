import pandas as pd
from tabulate import tabulate

data = pd.read_csv("personen.csv",sep=";")

dataSize = len(data)
n_Rec = 10

while(True):
    command = input("Enter a command:").upper()
    if command == "F":
        cur = 0
        print(cur)
        print(tabulate(data[cur:cur+n_Rec],headers="keys",tablefmt="psql",showindex =False))
    elif command == "P":
        cur = max(0,cur-n_Rec)
        print(cur)
        print(tabulate(data[cur:cur+n_Rec],headers="keys",tablefmt="psql",showindex =False))
    elif command == "N":
        cur = min(dataSize-n_Rec,cur+n_Rec)
        print(cur)
        print(tabulate(data[cur:cur+n_Rec],headers="keys",tablefmt="psql",showindex =False))
    elif command == "L":
        cur = dataSize-n_Rec
        print(cur)
        print(tabulate(data[cur:cur+n_Rec],headers="keys",tablefmt="psql",showindex =False))
    elif command == "E":
        print("Exiting")
        break
    else:
        print("Not a valid command. Please enter one of F/P/N/L/E")
