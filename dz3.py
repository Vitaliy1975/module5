import sys
from collections import *


def parse_log_line(line:str):
    date,time,level,message=line.split(" ",3)
    return {"date":date,"time":time,"level":level,"message":message.strip()}


def load_logs(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        list_unparsed=file.readlines()
    list_parsed=[]
    for line in list_unparsed:
        list_parsed.append(parse_log_line(line))
    return list_parsed


def filter_logs_by_level(logs, level):
    d=""
    for log in logs:
        if log["level"]==level:
            date=log["date"]
            time=log["time"]
            message=log["message"]
            d=d+f"{date} {time} - {message}\n"
    return d



def count_logs_by_level(logs):
    d=[]
    for log in logs:
        d.append(log["level"])
    dd=Counter(d)
    return dd


def display_log_counts(counts):
    a="Рівень логування"
    b="Кількість"
    print(f"{a:^16} | {b:^10}")
    print("-"*17+"|"+"-"*11)
    for key,val in counts.items():
        print(f"{key:<16} | {val:<10}")



def main():    
    try:
        path=sys.argv[1]
    except Exception as e:
        print(e)
    try:
        level=sys.argv[2]
    except Exception as e:
        print(e)
    display_log_counts(count_logs_by_level(load_logs(path)))
    if level:
        print()
        print(f"Деталі логів рівня '{level}':")
        print(filter_logs_by_level(load_logs(path),level))



if __name__=="__main__":
    main()
