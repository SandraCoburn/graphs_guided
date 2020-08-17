'''The challenge: You are given a list of tasks, some of which depend on others. Write a function, order_tasks, which will takes a subset of those tasks and returns an ordered list of all the tasks to run. 
'''
order_tasks(
    {
        'eat lunch': ['make a sandwich'],
        'make a sandwich': ['buy groceries'],
        'buy groceries': ['go to store'],
        'go to store': [],
    },
    ['eat lunch']
)

def order_tasks(subset_task):
    for task in subset_task:
        print(task)

order_tasks(order_tasks)