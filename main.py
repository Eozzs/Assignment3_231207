# print('To-Do List Options:')
# print('1. Add task')
# print('2. Display NOT COMPLETED tasks')
# print('3. Mark task as completed (BONUS)')
# print('4. Delete task')
# print('5. Search task (BONUS)')
# print('6. Edit task (BONUS)')
# print('7. Display COMPLETED tasks')
# print('8. QUIT')


done_list = []
todo_list = []

import my_modules

while True:

    option = int(input('Enter your choice: '))

    if option == 1:

        task_added = input('Enter > Task: ')
        date_added1 = input('Enter > Deadline (YYYY-MM-DD): ')

        date_added = my_modules.date_format(date_added1)

        if not task_added or not date_added:
            print("Task and/or deadline was not entered.")
            break

        todo_list.append({date_added: task_added})

    elif option == 2:

        print('Not completed tasks: ')
        print(my_modules.index_notcompleted(todo_list))

    elif option == 3:

        print('Not completed tasks: ')
        print(my_modules.index_notcompleted(todo_list))

        try:
            index_completed = int(input('Enter > Index number to mark the task as completed: '))
            if 0 <= index_completed < len(todo_list):
                done_list.insert(0, todo_list.pop(index_completed))
                print('Success: Task Completed!')
            else:
                print("Please enter a valid index.")
        except ValueError:
            print("Please enter a number.")

    elif option == 4:

        print('Not completed tasks: ')
        print(my_modules.index_notcompleted(todo_list))

        try:
            index_remove = int(input('Enter > Index number to remove the task: '))
            if 0 <= index_remove < len(todo_list):
                todo_list.pop(index_remove)
                print('Success: Task Removed!')
            else:
                print("Please enter a valid index.")
        except ValueError:
            print("Please enter a number.")

    elif option == 5:

        search_task = input('Search > Task: ')
        search_date1 = input('Search > Deadline (YYYY-MM-DD): ')

        if not search_date1:
            search_date = '0000-00-00'

        search_notcompleted = []
        search_completed = []

        if not search_task and not search_date:
            print("Task and deadline was not entered.")
            break

        for element in todo_list:
            for key, value in element.items():
                if search_date in key or search_task in value:
                    search_notcompleted.append({key: value})

        for element in done_list:
            for key, value in element.items():
                if search_date in key or search_task in value:
                    search_completed.append({key: value})

        print(f'A match in Completed tasks list: {search_completed}')
        print(f'A match in Not completed tasks list {search_notcompleted}')

    elif option == 6:

        print('Not completed tasks: ')
        print(my_modules.index_notcompleted(todo_list))

        try:
            index_edit = int(input('Enter > Index to edit the task: '))
            if 0 <= index_edit < len(todo_list):

                edit_task = input('Re-enter > Task: ')
                edit_date = input('Re-enter > Deadline (YYYY-MM-DD): ')

                if not edit_task or not edit_date:
                    print("Task and/or deadline was not entered.")
                    break

                todo_list[index_edit] = {edit_date: edit_task}
                print('Success: Task edited. ')

            else:
                print("Please enter a valid index.")

        except ValueError:
            print("Please enter a number.")

    elif option == 7:

        print('Completed tasks: ')
        print(my_modules.index_completed(done_list))

    elif option == 8:
        print('Exiting task list!')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 6.')


# Panasu, kad pasirenku sudetingesnius kelius, nors gali buti paprastesniu sprendimu, kuriu ivykdyti man dar nepavyksta.
# Dar ir googl'as nepadeda, nes vyksta step-by-step apdorojimas info is paskaitu...

# Aciu uz pastabas, bendra darba. Iki :)

# P.S. Bandziau itraukti daugiau moduliu, bet jie nepasiekdavo info is main.py ar kt. bedos.
# P.S. Kode daug atskiru optionu, kurie keicia darbinius listus - kaip suorganizuoti info saugojima failiuose, kad jie butu neperktauti, informatyvus ? ar veliau galimas failu info filtravimas?
