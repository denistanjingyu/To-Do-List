#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Import libraries
import json
import os

#Open Json file and read the contents
def getlist():
    with open('C:\\Users\\user\\Desktop\\ToDo.json', "r") as file:
        return json.load(file)

#Function to add task input by user to list
def addtasks(task):
    to_Do_List = getlist()
    to_Do_List.append(task.capitalize())
    with open('C:\\Users\\user\\Desktop\\ToDo.json', "w") as file:
        json.dump(to_Do_List, file)

#Function to remove task number input by user from list
def removetasks(num):
    to_Do_List = getlist()
    del to_Do_List[num-1]
    with open('C:\\Users\\user\\Desktop\\ToDo.json', "w") as file:
        json.dump(to_Do_List, file)

#Execute various commands
#index+1 as python is zero indexed
def main():
    exit = ["q", "quit", "exit", "end"]
    while True:
        os.system('cls')
        to_Do_List = getlist()
        print("Tasks to Complete:")
        print("------------------")
        for index, todo in enumerate(to_Do_List):
            print(f"{index + 1}) {todo}")

        print("\nCommands: ")
        print("Add tasks: ")
        print("rm <#>\n")

        prompt = input("> ").strip().lower()
        if prompt in exit:
            break
        elif prompt.startswith("add"):
            task = prompt[4:]
            addtasks(task)
        elif prompt.startswith("rm"):
            num = int(prompt[3:])
            removetasks(num)
main()
