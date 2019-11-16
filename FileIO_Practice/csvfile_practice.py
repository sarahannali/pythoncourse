from csv import writer, DictReader, reader

def add_user(First, Last):
    with open("file.csv","a", newline="") as File:
        csv_writer = writer(File)
        csv_writer.writerow([First,Last])

add_user("Dwayne","Johnson")

def print_users():
    with open("file.csv","r") as File:
        csv_reader = DictReader(File)
        for row in csv_reader:
            print(f'{row["First"]} {row["Last"]}')

print_users()

def find_user(givenFirst, givenLast):
    with open("file.csv") as File:
        found = False
        index = 1
        csv_reader = DictReader(File)
        for row in csv_reader:
            index += 1
            if row["First"] == givenFirst and row["Last"] == givenLast:
                print(index)
                found = True
                break
        if found == False:
            print(f"{givenFirst} {givenLast} was not found.")

find_user("Sarah","Ali")
find_user("Lebron","James")
find_user("Dwayne","Johnson")
find_user("Michelle","Obama")

def update_users(oldFirst, oldLast, newFirst, newLast):
    with open("file.csv") as File:
        count = 0
        csv_reader = reader(File)
        csvFile = list(csv_reader)
    with open("file.csv","w", newline="") as File:
        csv_writer = writer(File)
        for row in csvFile:
            if row[0] == "":
                pass
            elif row[0] == oldFirst and row[1] == oldLast:
                count += 1
                csv_writer.writerow([newFirst,newLast])
            else:
                csv_writer.writerow(row)
    return f"Users updated: {count}"

print(update_users("Sarah","Ali","New First","New Last"))

def delete_users(givenFirst, givenLast):
    with open("file.csv") as File:
        count = 0
        csv_reader = reader(File)
        csvFile = list(csv_reader)
    with open("file.csv","w", newline="") as File:
        csv_writer = writer(File)
        for row in csvFile:
            if row[0] == givenFirst and row[1] == givenLast:
                count += 1
            else:
                csv_writer.writerow(row)
    return f"Users deleted: {count}"

print(delete_users("Michelle","Obama"))