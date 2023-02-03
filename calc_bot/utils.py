from datetime import datetime

def calc(my_list):
    while '*' in my_list or '/' in my_list or '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = float(my_list.pop(i+1)) * float(my_list.pop(i-1))
                my_list[i-1] = result
                break
            elif my_list[i] == '/':
                result = float(my_list.pop(i-1)) / float(my_list.pop(i))
                my_list[i-1] = result
                break
            elif my_list[i] == '-':
                result = float(my_list.pop(i-1)) - float(my_list.pop(i))
                my_list[i-1] = result
                break
            elif my_list[i] == '+':
                result = float(my_list.pop(i+1)) + float(my_list.pop(i-1))
                my_list[i-1] = result
                break
    return my_list

def logwrite(note, message_text):
    operation_time = datetime.now().strftime('%H:%M')
    with open('log_file.txt', 'a') as data:
        data.write(f"{operation_time} {note}{str(message_text)}")
        data.write("\n")