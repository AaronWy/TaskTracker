# Task-Tracker-CLI

## Install the required Python packages
1. pip install typer[all]
2. pip install PyInquirer
  (if you face any error try the below code)
  pip install prompt_toolkit==1.0.14
3. pip install rich

# To Use
# Adding a new task
python3 task.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python3 task.py update 1 "Buy groceries and cook dinner"
python3 task.py delete 1

# Marking a task as in progress or done
python3 task.py mark-in-progress 1
python3 task.py mark-done 1

# Listing all tasks
python3 task.py list

# Listing tasks by status
task-cli list DONE
task-cli list TODO
task-cli list IN-PROGRESS
