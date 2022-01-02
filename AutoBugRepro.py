import requests
from requests.auth import HTTPBasicAuth
import filecmp
import os
import time

#This function reproduces EI04 (loading time issue) when its called.

def scroll_1_to_10():
    print("\nthe automation will send requests to pages 1-10 and will print whenever it will get responounded. note how long it takes for pages 7,8 and 9 to load:\n")
    for x in range(1,11):     #in this for loop the terminal will display indication whenever the API send responses.

        #Sending request and printing the response
        res = requests.get('http://localhost:8000/players?page=' + str(x), auth=HTTPBasicAuth('admin', 'admin'))
        print('Page ' + str(x) + str(res))

    print("End of session")

#This function reproduces EI01 (refresh Issue) when its called.

def refresh():
    print("\nthe API will be requested twice the same page and the automation will compare the body responses right now...\n")
    time.sleep(3)
    for x in range(1,3):               #On this for loop two text output are created, containing page1 responses.
        res = requests.get('http://localhost:8000/players?page=1', auth=HTTPBasicAuth('admin', 'admin')) #Send request

        #creats a txt file as an output, containing the response body
        nameOfFile='output' + str(x)
        text_file = open(str(nameOfFile), "w")
        text_file.write(str(res.content))
        text_file.close()

        # This section compares between the two outputs. if Equal Pass. Else Fail.
    file1 = open("output1", "r")
    file2 = open("output2", "r")
    i = 0
    for l1 in file1:
        i += 1
        for l2 in file2:
            if l1 == l2:
                print("\nThe responses were the same. PASS\n")
            else:
                print("\nThe responses were not the same. FAIL\n")
    file1.close()
    file2.close()
    

print("############################################################################")                                                                        
print("\nThis script reproduces some of the EIs found during the API tests execution\n")
print("############################################################################")
print("\nPlese choose what EI would you like to reproduce.\nfor EI01 reproduction- the refresh Issue enter 1\nfor EI04 Reproduction- the loaing time issue of pages 7,8,9, enter 4")
while True: #ask the user to choose which EI to reproduce
    choice = input("Please Enter your choice:(1/4): ")
    if choice == '1':
        refresh()
        break
    elif choice == '4':
        scroll_1_to_10()
        break
    else:
        ex = input("Invalid input. to exit enter e, otherwise press any key:")
        if ex == 'e':
            break
    
        
        

