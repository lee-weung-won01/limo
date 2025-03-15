import datetime

class Temp:
    month = int()



def main():
    now = datetime.datetime.now()
    if now.hour <12 :
        print(f"now {now.hour}, morning")
    if now.hour >=12:
        print(f"now {now.hour}, afternoon")

    now =Temp()
    now.month = 1

    if 2 < now.month < 6:
        print(f"this month {now.month}, spring")
    elif 5< now.month < 9:
        print(f"this month {now.month}, summer")
    elif 8< now.month < 12:
        print(f"this month {now.month}, fall")
    else:
        print(f"this month {now.month}, winter")    
if __name__=="__main__":
    main()
