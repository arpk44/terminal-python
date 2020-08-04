import time
import random
import datetime  

#Data and Collection

apps = {"Desktop", "Downloads", "Uploads"}

in_Desktop = ("Appy", "img.sc.png", "jfj.sc.png")

in_Downloads = ("file_4.pz","file_2.pz", "file_43.pz", "file_2.pz")

in_Uploads = ("Filly")

def quit():
    print("You will quit")

def git():
    input("GitHub asks for you username")
    print("Because of suspicious activitiy we will have to stop here")

#User Sign
while True:
    
    command = input("free-terminal@pythonter33-pc: ").lower()

    if command == "ls":
        print("Listing..........")
        time.sleep(1)
        print(apps)
        print("In the Desktop:", in_Desktop)
        print("In the Downloads:", in_Downloads)
        print("In the Uploads:", in_Uploads)

    elif command == "math":
        print("Opening Calculator...")
        ask1 = input("Type the type of math ").lower()
        if ask1 == "addition":
            f1 = int(input("First Number:"))
            f2 = int(input("Second Number:"))
            final = f1 + f2
            print(final)
        elif ask1 == "subtraction":
            f1 = int(input("First Number:"))
            f2 = int(input("Second Number:"))
            final = f1 - f2
            print(final)
        elif ask1 == "multiplication":
            f1 = int(input("First Number:"))
            f2 = int(input("Second Number:"))
            final = f1 * f2
            print(final)
        elif ask1 == "division":
            f1 = int(input("First Number:"))
            f2 = int(input("Second Number:"))
            final = f1 / f2
            print(final)
        elif ask1 == "powers":
            f1 = int(input("First Number:"))
            f2 = int(input("Second Number:"))
            final = f1 ** f2
            print(final)
        elif ask1 == "pre-pay phon38":
            f1 = input("What is your phone number:")
        else:
            print("Command not found")

    elif command=="quit()":
        print("It was nice serving you")
        quit()
        break
    
    elif command == "time":
        current_time = datetime.datetime.now()
        print("The current time in London is..")
        print(current_time)

    elif command == "upload":
        uploaded_files = input("what would you like to upload?:")
        print("Item uploaded in 'Super Important Section'")
        print("In the super important section right now, these files are in:", uploaded_files, "My_files.pptx", "files.py")

        qu = input("To access them, please type 'cd' and then the file name.")

        if qu == "cd My_files.pptx":
            print("https://drive.google.com/file/d/1eV9mGDkXpbGBzEVBFd6_dB1m_Wo_oCOm/view?usp=sharing")
            print("Click that link to view the pptx")
        else:
            print("The file is being uploaded/is having time being uploaded please wait.")
            
    elif command == "git-establish":
        github_username = input("GitHub username:")
        github_password = input("GitHub password:")
        if github_username == "user1":
            if github_password == "flingingchinging":
                print("GitHub username found! Your code will be applied into github!")
                crossover = github_username + github_password
                data_collected = crossover + github_password + github_username + github_password + crossover + "7476457nvjfjfjdf" + github_username + github_password + github_password + github_username + github_password + crossover + "7476457nvjfjfjdf" + github_username + github_password
                repository = input("What repository would you like to create:")
                print("Repository created!")
                print("GO on https://github.com/", repository, "and you will find you GitHub repisotry. If not, please go on https://github.com/ and create one!")
            else:
                print("Failure")
        else:
            print("Failure")
    elif command == "git":
        git()
    else:
        print("No commands found. Please try again!")
