from csv import reader

with open('names.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        string = ""
        for index in range(len(row)):
            string += str(len(row[index]))
            if index < len(row)-1:
                string += ","
        print(string)
