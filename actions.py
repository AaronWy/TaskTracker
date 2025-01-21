import json
import os
from datetime import datetime

"""
Dictionary needs to have the FF Data
ID: INT incremental
NAME: STR 
STATUS: default todo, in-progress, done
CREATEDAT:Default once created  
UPDATEDAT: Once Updated

dict
"""


"""
# Adding a new task
[X] task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
[X] task-cli update 1 "Buy groceries and cook dinner"
[X] task-cli delete 1

# Marking a task as in progress or done
[X] task-cli mark-in-progress 1
[X] task-cli mark-done 1

# Listing all tasks
[X] task-cli list

# Listing tasks by status
[X] task-cli list done
[X] task-cli list todo
[X] task-cli list in-progress
"""

def init_JSON():
    default_Task = {
        "0": 
            {
                "NAME": "SAMPLE",
                "STATUS":"TODO",
                "CREATEDAT":str(datetime.now()),
                "UPDATEDAT":str(datetime.now())
            } 
    }   
    
    
    existingFile = "Task.json"
    if os.path.exists(existingFile):
        print("Writing to File")
    else:
        with open("Task.json", 'w') as file:
          json.dump(default_Task,file, indent=4)
        print("Not Exist")

# def get_num():
#     with open('Task.json','r') as file:
#         data = json.load(file)


#     return max(map(int,data.keys()))



def all_task():
    with open('Task.json','r') as file:
        data = json.load(file)

        return data

    


def add_task(NAME):
    curDate = str(datetime.now())
    with open('Task.json', 'r') as file:
        data = json.load(file)


    latestID = max(map(int,data.keys()))+1
    addTask = {     
        "NAME": NAME,
        "STATUS": "TODO",
        "CREATEDAT":str(datetime.now()),
        "UPDATEDAT":str(datetime.now())
    }
    #}
    data[str(latestID)] = addTask


    with open('Task.json','w') as file:
        json.dump(data,file,indent=4)

    return latestID

    
def update_task(ID,NAME): 
    with open('Task.json','r') as file:
        data = json.load(file)

    data[str(ID)]["NAME"] = NAME

    # print(data)

    with open('Task.json','w') as file:
        json.dump(data,file,indent=4)
    return data[str(ID)]

def delete_task(ID):
    with open('Task.json','r') as file:
        data = json.load(file)
    
    deleted_task = data[str(ID)]["NAME"]
    

    data.pop(str(ID))

    # Rearrange IDs
    update_seq = {}
    for new_id, (old_id, task) in enumerate(data.items()):
        update_seq[str(new_id)] = task  

    with open('Task.json','w') as file:
        data = json.dump(update_seq,file,indent=4)
    return deleted_task

def update_status_task(ID,STATUS):
    with open('Task.json','r') as file:
        data = json.load(file)

    if STATUS == 0:
        data[str(ID)]["STATUS"] = "IN-PROGRESS"
    elif STATUS == 1: 
        data[str(ID)]["STATUS"] = "DONE"

    with open('Task.json','w') as file:
        json.dump(data,file,indent=4)

    return data[str(ID)]   


def ret_status_task(STATUS):
    with open('Task.json','r') as file:
        data = json.load(file)


    TODO = {}
    IN_PROGRESS = {}
    DONE = {}
    for task in data: 
        if data[str(task)]["STATUS"] == "TODO":
            TODO.update({task : data[str(task)]})
        elif data[str(task)]["STATUS"] == "IN-PROGRESS":
            IN_PROGRESS.update({task : data[str(task)]})
        elif data[str(task)]["STATUS"] == "DONE":
            DONE.update({task : data[str(task)]})

    if STATUS == "TODO": 
        return TODO
    elif STATUS == "IN-PROGRESS": 
        return IN_PROGRESS
    elif STATUS == "DONE": 
        return DONE
  









init_JSON()







