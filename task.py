import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
import json
import os
import actions
app = typer.Typer()

## Check if the JSON File exist or not
def make_JSON():
    with open("task.JSON", 'w') as file: 
        print(file.read)


@app.command("help")
def func_help(): 
    rprint("add")
    rprint("update")
    rprint("list")
    rprint("check")





    

@app.command("check")
def ret_func(id:int): 
    task = db_func.ret_task(id)
    rprint(f"{task}")

@app.command("list")
def list_func(
    filter_by: str = typer.Argument(None, help="Optional Filter: ('TODO,'IN-PROGRESS,'DONE')")):
    if filter_by is None: 
        tasks_json = actions.all_task()
        for ID,task in tasks_json.items(): 
            rprint(f"ID: {ID} NAME :{task['NAME']} ")
    elif filter_by == "TODO":
        tasks_json = actions.ret_status_task("TODO")
        rprint(f"--------- Tasks that are still in TODO --------")
        for task in tasks_json:
            rprint(f" TASK:{tasks_json[str(task)]["NAME"]}")
    elif filter_by == "IN-PROGRESS":
        tasks_json = actions.ret_status_task("IN-PROGRESS")
        rprint(f"--------- Tasks that are still in IN-PROGRESS --------")
        for task in tasks_json:
            rprint(f" TASK:{tasks_json[str(task)]["NAME"]}")
    elif filter_by == "DONE":
        tasks_json = actions.ret_status_task("DONE")
        rprint(f"--------- Tasks that are still in DONE --------")
        for task in tasks_json:
            rprint(f" TASK:{tasks_json[str(task)]["NAME"]}")
    else: 
        typer.echo("Invalid filter. Only 'TODO,'IN-PROGRESS,'DONE' are allowed.")



@app.command("update")
def update_func(id:int,name:str): 
    tasks_retr = actions.update_task(id,name)
    rprint(f"Task: [bold]{tasks_retr["NAME"]}[bold] is successfully updated!")

@app.command("delete")
def delete_func(id:int):
    tasks_del = actions.delete_task(id)    

    rprint(f"TASK {tasks_del} was deleted")

    
@app.command("mark-in-progress")
def status_func(id:int):
    task = actions.update_status_task(id,0)
    rprint(f"TASK: {task["NAME"]} STATUS: {task["STATUS"]}")

@app.command("mark-done")
def done_func(id:int):
    task = actions.update_status_task(id,1)
    rprint(f"TASK: {task["NAME"]} STATUS: {task["STATUS"]}")

@app.command("add")
def add_func(task:str):
    ID = actions.add_task(task)
    rprint(f"The Task is added [blue]{task}[blue] ID:{ID}")


if __name__ == "__main__":
    # actions.init_JSON()
    # make_JSON()
    app()    