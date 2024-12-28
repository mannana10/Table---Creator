import sqlite3

class Creator:

    def __init__(self):
        
        while True:
            name = input("შეიტანეთ ბაზის სახელი .db გაფართოებით, მაგ.:database.db : ").strip()
            if not name.endswith(".db"):
                print("შეიტანეთ ბაზის სახელი სწორი ფორმატით!")
                continue
            db_name = name
            break

        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()


    def creat_table(self):
        
        table_name = input("გთხოვთ შეიტანოთ ცხრილის სახელი: ")   

        while True:
            num = input("გთხოვთ შეიტანოთ ცხრილის სვეტების რაოდენობა რიცხვით ფორმატში: ")
            if not num.isdigit() or int(num) <= 0:
                print("შეიტანეთ ნულზე მეტი მთელი რიცხვი!")
                continue
            col_num = int(num)
            break

        columns = []
        while len(columns) < col_num:

            while True:
                col_name = input("შეიტანეთ სვეტის სახელი: ").strip()
                if not col_name:
                    print("სვეტის სახელი არ შეიძლება იყოს ცარიელი!")
                    continue
                break
            
            while True:
                col_type = input("შეიტანეთ სვეტის მონაცემის ტიპი (NULL, INTEGER, TEXT, REAL, BLOB): ").strip().upper()
                if not col_type in {"NULL", "INTEGER", "TEXT", "REAL", "BLOB"}:
                    print("შეიყვანეთ ტიპის სწორი მნიშნელობა (NULL, INTEGER, TEXT, REAL, BLOB)!")
                    continue
                break

            columns.append(f"{col_name} {col_type}")

        name_type = ", ".join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({name_type})")
        self.connection.commit()
        print(f"ცხრილი {table_name} წარმატებით შეიქმნა {self.db_name} ბაზაში!")

        self.cursor.close()
        self.connection.close()

table1 = Creator()
table1.creat_table()

        


    

