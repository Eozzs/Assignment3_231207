import datetime

def date_format(date_input):
    date_list = []
    for date in date_input.replace('-' , ' ').split():
        date_list.append(int(date))
    date = datetime.datetime(date_list[0], date_list[1], date_list[2])
    return date.strftime("%Y %B %d (%A)")

def index_notcompleted(input_list):
    for index, date_task in enumerate(input_list):
        for date, task in date_task.items():
            index_task_date = print(f'Index {index} / {task} : due to {date} - Not completed')
    return index_task_date

def index_completed(input_list):
    for index, date_task in enumerate(input_list):
        for date, task in date_task.items():
            index_task_date = print(f'Index {index} / {task} : due to {date} - Completed')
    return index_task_date
