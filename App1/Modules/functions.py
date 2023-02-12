def read_tasks(file_path="../files/Tasks.txt"):

    with open(file_path, 'r') as file:
        Tasks = file.readlines()  # with contact manager for a shorter code and avoiding complications
    return Tasks



def write_tasks(Tasks,filepath="../files/Tasks.txt"):
    with open(filepath, 'w') as file:
        file.writelines(Tasks)

# To only run the function when trying to test this python file
if __name__=="__main__":
    print(read_tasks())
    print("Hello")