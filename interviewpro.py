"""
A program that helps you interview by showing what you should answer when searching for specific keywords

frontend: tkinker interface
backend: mongodb database
"""
database = {}

#function for returning the answers relevant to the keyword
def search_item (keyword):
    for key, value in database.items():
        if key == keyword:
            return value

#function for splitting answers into headings and subheadings
def bullet_struct (ans_splitted):
    struct_ans = {}
    for i in ans_splitted:
        first_ele = i.split(', ')[0]
        other_ele = i.split(', ')[1:]
        struct_ans[first_ele] = other_ele
    return struct_ans

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
    for key in database.items():
        print(key)
    keyword = input("Type in the search: (stop the program by typing stop) ")
    ans = search_item(keyword)
    ans_splitted = ans.split('. ')
    #create a structured answer
    struct_ans = bullet_struct(ans_splitted)

    count = 1
    #start printing answers on a separate line
    print('\n')
    for key, value in struct_ans.items():
        #print the heading
        print(str(count) + ". " + key +'\n')
        #print subheadings
        for i in value:
            print("- " + i + '\n')
        print('\n')
        count += 1
    #user types na to stop the program
    if keyword == "stop":
        break





