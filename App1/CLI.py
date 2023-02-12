# prompt= " "#can be single quote (''), but if we use both we have to enclose them in double quotes

# Tasks = [] #although square brackets are useful for lists but it's not user friendly
from Modules.functions import read_tasks, write_tasks
from Modules import functions
import time
Now = time.strftime("%B %d,%Y %H:%M:%S")
print("Today is", Now)

while True:
    Action = input("add/show/exit/complete Tasks:")  # whitespace doesn't matter yet it makes code more readable and clean
    Action = Action.strip()  # remove whitespace for user mistakes

    if Action.startswith('add'):
        # Task = input("Add a new Task:") + "\n"
        # file = open('files/Tasks.txt', 'r') #open file to read existing data
        # Tasks = file.readlines()
        # file.close()
        Task = Action[4:]+"\n"

        Tasks = functions.read_tasks() #can replace the default argument by overriding ot

        Task = Task.capitalize()
        Tasks.append(Task)  # capitalize and print 1st letter in string
        # Task.title capitalize every letter in string
        # file = open('files/Tasks.txt', 'w') #append new data to file
        # file.writelines(Tasks)
        # file.close()
        functions.write_tasks(Tasks)

    elif Action.startswith('show') or Action.startswith('display'):
        Tasks= read_tasks()
        # new_todo=[] #create a new list having the stripped items of \n
        # for item in Tasks:
        #     temp_todo=item.strip("\n")
        #     new_todo.append(temp_todo)

        # new_todo = [item.strip("\n") for item in Tasks]

        for i, item in enumerate(Tasks):  # to print without brackets
            item = item.strip("\n")
            print(f"{i+1}.  {item}")  # f-string that makes no spaces and just prints the string
    elif Action.startswith('edit'):
        try:
            number= int(Action[5:])
            number = number - 1
            Tasks= read_tasks()

            new_task= input("Enter the new task")
            Tasks[number] = new_task.title() + "\n"  # adeem howa el = el gdeed msh el 3aks

            write_tasks(Tasks)
        except ValueError:
            print("Invalid command! please type which number of task to edit")

    elif Action.startswith('complete'):
        try:
            com_task= int(Action[9:])

            Tasks= read_tasks()

            com_task = com_task-1
            done_task = Tasks[com_task].strip('\n')
            Tasks.pop(com_task)

            write_tasks(Tasks)

            message=f"Todo {done_task} was removed Good Job!"
            print(message)
        except IndexError:
            print("Invalid command! no Task with that number")
        except ValueError:
            print("Invalid command! please type which number of task to complete")

    elif "exit" in Action:
        break
    else:
            print("Please Type a valid command")


print ("Have a day full of achievements!")






#print(type(Tasks))