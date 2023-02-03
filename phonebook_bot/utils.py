def insert_data(data, sep):
    with open("phonebook.txt", 'a+') as file:
        if sep == '-':
            for i in data:
                file.write(f"{i}\n")
            file.write("\n")
        else:
            file.write(sep.join(data))
            file.write("\n")

def export_data():
    with open("phonebook.txt", 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data