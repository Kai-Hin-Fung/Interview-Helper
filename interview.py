"""
A program that helps you interview by showing what you should answer when searching for specific keywords

frontend: tkinker interface
backend: mongodb database
"""
database = {}

def search_item (keyword):
    for key, value in database.items():
        if key == keyword:
            return value

start_input = "yes"
start_search = "no"

#prompts the user to input q and a
print("Start Interview")
start_input = input("Input questions and answers accordingly (click enter to start)")

while True:
    keyword = input("What is the keyword? ")
    answer = input("What is the ans? ")
    database[keyword] = answer 
    go_on = input("Do you wish to add another word? (yes/no) ")
    if go_on == "no":
        break

#start the interview
print("start interview")

while True:
    #print out all of the keywords
    print('here are all the keywords:')
    for key, value in database.items():
        print(key)
    keyword = input("Type in the search: (stop the program by typing stop)")
    ans = search_item(keyword)
    para_ans = ans.split('. ')
    count = 1
    for i in para_ans:
        #each ans separated by a fullstop
        print('\n')
        print(str(count) + ". " + i +'\n')
        count += 1
    #user types na to stop the program
    if keyword == "stop":
        break





