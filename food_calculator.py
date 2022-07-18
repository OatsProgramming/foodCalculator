# Food Calculator Attempt July 1st 2022
# Working on this project till the 7th for now
# Trying to create an original project with level of coding knowledge: >1 Month
# Last updated: July 6th 5:29 PM Central
# "Finished": July 6th 5:29 PM Central
 
# Check at the very bottom for monologues to myself as I kept updating the project
 
# To get ingredients cost per serving
import os
import pickle

os.system("clear")

# w is ingredient name
# x is cost per serving
# y is user's number of serving used in the meal
# z is total cost of ingredient (x * y)

w = []
x = []
y = []
z = []



original_pathway = os.getcwd()
directory_Food_Calculator = "Food Calculator"

# Need to fix this to show only meals folder at the start (directories) Jul 5
# This entire program only pickles one set of data for now. Still overwrites it.
def meals():
    os.chdir(original_pathway)
    os.chdir(directory_Food_Calculator)
    meal_list = [meal for meal in os.listdir() if 'meal' in meal]

    if len(meal_list) == 0:
        print("\nIt seems that there's nothing here. Quite barren. Let's head back to the main menu.")
        print("Going to main menu...\n")
        initiation()

    meal_folder = None
    while meal_folder == None:
        print("") # This is just to make the output look cleaner when listing all meal items in the meal list
        for mealItem in meal_list:
            print(mealItem) 
        meal_folder = input("\nWhich meal would you like to look at: ")
        try:
            os.chdir(meal_folder)
        except OSError:
            print(f"The meal, {meal_folder}, does not exist. Please try again.")
            meals()
        else:
            print(f"Opening {meal_folder} folder...\n")
            print(os.listdir())
            if 'ingredients' in os.listdir():
                dictionary = pickle.load(open("ingredients","rb"))
            print("Now accessing ingredients file...")
            # print(file)
        # else:
            # print("There's nothing in here. Let's go back to the main main menu.")
            # initiation()

    # for key in file:
        # print(file[key])
    
    w_dict = dictionary["Name of ingredient(s): "]
    x_dict = dictionary["Cost per serving: "]
    y_dict = dictionary["Amount of servings used: "] 
    z_dict = dictionary["Total cost per use: "]
    total = sum(z_dict)

    meal_files = None
    while not meal_files:
        meal_files = input(f"What would you like to look at: \n\nList of Ingredients (type list) \nIngredients Cost Per Serving (type cost) \nAmount of ingredient servings used in {meal_folder} (type servings) \nTotal Cost of {meal_folder} (type total cost) \nAll Info (type all info) \nReturn to main menu (type main menu) \n\nType here: ").lower().strip()
        if meal_files == "list": 
            print(f"\nList of ingredients:\n{w_dict}\n")
            meal_files = None
        elif meal_files == 'cost': 
            print(w_dict)
            for idx1, ingredient in enumerate(w_dict):
                for idx2, cost in enumerate(x_dict):
                    if idx1 == idx2:
                        print(f"\n{ingredient} Cost Per Serving:\n{cost}\n")
            meal_files = None
        elif meal_files == 'servings':
            for idx1, ingredient in enumerate(w_dict):
                for idx3, serving in enumerate(y_dict):
                    if idx1 == idx3:
                        print(f"\nAmount of {ingredient} servings used in {meal_folder}:\n{serving}\n ")
            meal_files = None
        elif meal_files == 'total cost':
            print(f"\nTotal Cost of {meal_folder}:\n{total}\n")
            meal_files = None
        elif meal_files == 'all info':
            print("Now listing all information...\n")
            print(f"\nList of ingredients:\n{w_dict}\n")
            for idx1, ingredient in enumerate(w_dict):
                for idx2, cost in enumerate(x_dict):
                    for idx3, serving in enumerate(y_dict):
                        if idx1 == idx2 == idx3:
                            print(f"{ingredient} Cost Per Serving:\n{cost}\n")
                            print(f"Amount of {ingredient} servings used in {meal_folder}:\n{serving}\n ")
            print(f"Total Cost of {meal_folder}:\n{total}\n")
            meal_files = None 
        elif meal_files == 'main menu':
            print("\nGoing to Main Menu...\n")
            initiation()
        else: 
            print("Sorry. I don't have autocorrect yet so I have no idea what youre saying.")
            meal_files = None
        


# To calculate the ingredient per serving and add it to the dictionary. 
def foodCalculator(w, x, y, z):
    user_ingredient_name = None
    user_ingredient_price = None
    user_ingredient_serving = None
    

    while user_ingredient_name == None:

        user_ingredient_name = input("Name: ")
        user_ingredient_price = input("Cost: ")
        user_ingredient_serving = input("Total serving: ")

        cost_per_serving = float(user_ingredient_price) / float(user_ingredient_serving)
        user_choice_of_serving = float(input("How many servings are you putting in? "))
        total_cost_of_serving = cost_per_serving * user_choice_of_serving

        if user_ingredient_name not in w:
            w.append(user_ingredient_name)
        if cost_per_serving not in x:
            x.append(cost_per_serving)
        if user_ingredient_serving not in y:
            y.append(user_choice_of_serving)
        if total_cost_of_serving not in z:
            z.append(total_cost_of_serving)

        d = (f"\nName of ingredient: {user_ingredient_name} \nPrice/Total Serving: {cost_per_serving} \nAmount of servings used: {user_choice_of_serving} \nTotal cost per use: {total_cost_of_serving}\n")
        isCorrect = None
        while isCorrect == None:
            isCorrect = input(f"Is the following correct: \n{d}\n(Type Y or N): ").lower()
            print(w)
            print(x)
            print(y)
            print(z)

            if isCorrect == "n":
                foodCalculator(w, x, y, z)
            elif isCorrect == "y":
                all_done = None
                while not all_done:
                    all_done = input("Is that all the ingredients for this meal (Y/N)?: ").lower() 
                    if all_done == "y":
                        print("Heading over to the 'folder and file' function")
                        meal_total_cost = sum(z)
                        createFolderandFile(w, x, y, z, meal_total_cost) # (w, x, y, z) will help transfer over ingredient data to createFolderandFile() function
                    elif all_done == 'n':
                        print("Gotcha. Lets add some more ingredients!")
                        foodCalculator(w, x, y, z)
                    else: 
                        print("Sorry. Idk what you said. Maybe a grammatical error? Please try again.")
                        all_done = None
            else:
                print("Invalid input. Try again")
                isCorrect = None
        return d


# To create meal folders and ingredient files 
# Note to self: by setting parameters, it can help transfer data from one function to another if needed
def createFolderandFile(w, x, y, z, total):

    d = {
    "Name of ingredient(s): ": w, 
    "Cost per serving: ": x, 
    "Amount of servings used: " : y, 
    "Total cost per use: " : z
    }


    print(d)
    # This is for now; still have to find a way to get the sum from "Total cost per serving" of all ingredients
    tempmealname = input("What is the name of your meal?: ").strip()
    mealname = tempmealname + " " + "meal"
    try:
        os.mkdir(mealname)
    except OSError:
        print(f"\n{mealname} folder could not be created. Please check Documents if it exists already\n")
        createFolderandFile(w, x, y, z, total)
    else:
        print(f"\n{mealname} folder was successfully made. Now adding ingredients info into the folder\n")
    
    os.chdir(mealname) # Goes to the mealname folder
    pickle.dump(d, open("ingredients","wb")) # Dumps all the ingredients data
    os.chdir(directory_Food_Calculator) # Goes back to the Food Calculator folder
    print (f"The sum of your {mealname} is {total}")
       

    
    choose_a_function = None
    while not choose_a_function:
        choose_a_function = input("What would you like to do? Add more meals (type more) or get meal list? (type meals) or end program (type end)?: ").lower()
        if choose_a_function == "more":
            foodCalculator(w, x, y, z)
            choose_a_function = None
        elif choose_a_function == "meals":
            meals()
            choose_a_function = None
        elif choose_a_function == "end":
            return ("Alright. Have a good day!")
        else:
            print("Invalid input. Try again")
            choose_a_function = None


def initiation():
    os.chdir(original_pathway)
    if directory_Food_Calculator not in os.listdir(original_pathway):
        print("Food Calculator folder not found. Creating new Food Calculator folder...\n")
        os.mkdir(directory_Food_Calculator)
        print(os.listdir())

    print(os.getcwd())
    if os.getcwd() != directory_Food_Calculator:
        # if directory_Food_Calculator not in os.listdir():
            # os.mkdir(directory_Food_Calculator)
            # print(os.listdir())
        os.chdir(directory_Food_Calculator)
        print(os.getcwd())
    
            
    initiateProgram = None
    while not initiateProgram:
        initiateProgram = input("How can I help you? (Type either food calculator or meals or end program): ").lower()
        if initiateProgram == "food calculator":
            print("Cool! Let's get started.")
            foodCalculator(w, x, y, z)
        elif initiateProgram == "meals":
            meals()
            initiateProgram = None
        elif initiateProgram == 'end program':
            return ("Alright, ending program. Till next time!")
        else:
            print("Sorry. I'm a computer with OCD; you got to type it out right. What was that again?")
            initiateProgram = None


# Just for good habits
if __name__ == "__main__":
    initiation()
   



# The following is just me monologuing to myself about the status of the program as I tinker it.
'''
Jul 3
Unknown Time
As of thus far, I've added a different function to initiate the whole program called "initiation". Ive also added function meal() to help save the meal data; 
however, it seems that it refreshes completely after ending the program; I need to find a way to save it even after the program ends. No, nvm. It does save it but it completely
completely overwrites it once it passes thru pickle.dump()

The last thing you were doing was updating get_info(). You could prolly delete the "Is that all your meals?" or whatever lines of code and it should still work. Test tmrw.

Ive also updated the get_info() a bit by adding more while loops and whatnot. Just compare it to the previous codes. No thats tedious and stupid to do. Idk. im tired

'''
'''
Jul 4
8:00 AM
Ive took out the end_function and "Is that all your meals" and replaced it with smaller lines of code. Going to try making a folder for the meals and their info (i.e. meal names, 
cost, ingredients, cost of ingredients, etc.) by creating a directory.
10:16 AM:
I've just learned what directories are and how to create/delete them (check CreatingandDeletingDirectories_Lesson.py). I'm rewriting the map for the way the data to be stored. 

User: Asks to make a meal -> The Food Program -> creates ingredient file(s) -> meal folder
                             The Food Program -> creates meal folder

User: Asks for meals -> Food Program -> meal folder -> ingredient file(s)
                 User: Asks for ingredients in meal -> ingredient file(s)
12:07 PM:
Going to try and incorporate the map into the program.
1:01 PM
I FUCKING FINALLY PUT THE FILE IN THE FOLDER! Fucking hell that was stupidly tedious. Check it:

            try:
                os.mkdir(mealname)
            except OSError:
                print(f"{mealname} folder could not be created. Please check Documents if it exists already")
            else:
                print(f"{mealname} folder was successfully made. Now adding ingredients info into the folder")
            
            os.chdir(mealname)
            pickle.dump(d, open("ingredients","wb"))


            print (f"The sum of your {mealname} is {total}")
        elif user_input != "no":
            print("Invalid input")

Heh. Im pretty proud of myself ngl. I pretty much make a folder first; then, since the current directory is in Documents, I changed the directory to the current meal 
folder via os.chdir(); then, I dumped the ingredients file. I'm not sure if this works with multiple iterations though. Imma check in a bit. I
also have to find a way to access the meals folder and ingredients after since I took out the list call out. Not sure how I'm gonna do that yet.

Update: After trying to add more than one meal, it turns out that the ingredients from the previous meal adds over to the next one. I need to find a way to isolate the dictionary. 
Also, when creating a new meal, the directory is still set to the previous meal directory; ultimately, creates a folder within a folder. Not good. I need to find a way to 
create a folder and revert it back to the original. 
1:46 PM
I've successfully revert it back to the original directory by changing the directory after dumping the ingredients file. Pretty stupidly simple, idk why I couldnt figure it out.
However, I still have the issue dealing with the ingredients keep adding with the other ingredients from the previous meal. 
3:43 PM
Ive switched around some loops and whatnot; Ive also changed some of the functions' names and their codes to their respective function. Currently having issues with foodCalculator()
function: managed to get all the data all in one place, but still having trouble adding on top of that without overwriting the other ingredient. 
'''
'''
Jul 5
7:36 AM
I'm still trying to fix the overwriting issue in foodCalculator() function. Been going back and forth with this one. I imported pandas to help create a dataframe that would suit
this particular thingamjig; however, as I've said before, still need to figure out how to fix the overwriting data issue. As of rn, I'm trying to restart the foodCalculator()
function without calling it recursively as I believe that might be the reason why its overwriting it. 

Update: I figured out a way to transfer the data from one function to another without having to setting it outside the function. Man, I really am a novice lol. I changed
createFolderandFile() to createFolderandFile(ingredients_info), having one parameter; this will get ingredient data from foodCalculator() function. I've also changed a few other
variables and loops since it was affecting other loops in other functions. BUT I STILL CANT FIND A WAY TO NOT OVERWRITE THE DATA.
11:06 AM
I'm currently tinkering with the directories in meals() function. So far it works; I just need to find a way to load up the files now. I've also incorporated end program and other
stuff. Idk. Kinda tired of trying to keep up with my little monologues. Ive found out that i can get the list of directories by os.listdir() and also that they can be treated as
a element(dumb dumb i am). This project is one hell of a learning experience ngl. Not sure how I'm going to incorporate all the things Ive learned from leetcode into such projects
though. Maybe in other projects. Oh yeah: Ive also made the whole output look cleaner than before. So, when using the terminal, its much easier to read. So, woo for me. 
I'm also wondering how I'm going to incorporate nutrition facts and barcodes into this thing. This is already a pain in my ass so imagine adding those features. It is a simple
concept though. Just web scrape with barcode and just use a bit of mathematics for nutrition facts. 
3:17 PM
Im getting a lil pissy lol. Ive been on and off with this project due to how its been hurting my lower back. Anyways, back to the actual part abt the program: I'm working on the
meals() and the line:

        if meal_files == "list":
            for key in file:
                if key == 'Name of Ingredients':
                    for idx in file[key]:
                        print("random")
                        print(idx)
                        meal_files = None

Doesn't fking work for some reason. Every time its executed, it goes back to the main menu, which is initiation(). I even put "print("random")" to see if it'll print, but no.
It completely skips it. I've been tinkering with everything else such as pickling and unpickling files, rerouting directories, etc. Simple little things. But I CANT GET THE DAMN
CODE TO WORK. I've tried other lines of code in meals() like these for example:


        elif meal_files == 'all info':
            print("Currently working on it") # Fix this later. Check the codes so far for now. Last ChkPoint Jul 5 11:17 AM
        elif meal_files == 'main menu':
            print("\nGoing to Main Menu...\n")
            initiation()
        else: 
            print("Sorry. I don't have autocorrect yet so you need to type it accurately.")
            meal_files = None

And they work perfectly fine! So it's definitely not me being absolutely bonkers or whatnot. It's bc I'm still too much of a novice to understand and that pisses me off. 
Update: I'm going to implement MARKERS into the code to see where it fails:

        if meal_files == "list": # LAST CHKPT Jul 5 3:26 PM
            for key in file:
                print("Step 1 working") # MARKER 1
                if key == 'Name of Ingredients':
                    print("Step 2 working") # MARKER 2
                    for idx in file[key]:
                        print("Step 3 working") # MARKER 3
                        print(idx)
                        meal_files = None

Lets see if it works
Update on that update: Turns out, its MARKER 1:

>>> Output:
Step 1 working
Step 1 working
Step 1 working
Step 1 working

It repeats 4 times. Most likely due to the amount of keys in the dictionary. At least now i know for sure that I can access the file's data. Just gotta figure out 
how to implement the data accordingly. 
4:08 PM
I FIGURED IT OUT:

        if meal_files == "list": # LAST CHKPT Jul 5 4:02 PM
            x_file = file["Name of ingredient(s): "]
            print(f"\nList of ingredients:\n{x_file}\n")
            meal_files = None

Turns out its super case sensitive and I accidentally put capital I in ingredients. I feel dumb lol. I think my brain is having a burn out. That might be the reason why.
But I am constricted on time: I only have a few months left till my savings go completely out and I have to apply for jobs soon. If only I can turn this into an app and make
money from it to make my savings last a bit longer. Besides that, I still need to find a way to save the data without overwriting it then pickling it. Only then we'll see if
the meals() work. Looking at it, the code does look a bit messy. I'll worry abt cleanliness later. I have to cook soon. 
7:53 PM
After figuring out how to properly dictionaries and the pickle module, things have gotten easier it seems. Will update tmrw.
'''
'''
Jul 6
8:47 AM
I'm going to go ahead and try to finish meals() and see what happens from there.
9:40 AM
I managed to finish meals() and now currently trying to fix the directory issue. Thus far, it's working out decently. At first, I was having issues with initiation():

def initiation():
    initiateProgram = None
    print(os.getcwd())
    directory_Food_Calculator = "Food Calculator"
    if os.getcwd() != directory_Food_Calculator:
        if directory_Food_Calculator not in os.getcwd():
            os.mkdir(directory_Food_Calculator)
            print(os.listdir())

Wondering why it kept giving me errors whenever I rebooted the program twice. I realized that I had to change "if directory_Food_Calculator not in os.getcwd():" to 
"if directory_Food_Calculator not in os.listdir():". Quite dumb of me not to get the list of directories instead of the current directory. Of course the Food Calculator directory
wouldnt be in the current directory: it's not a list. Anyways, it works nicely now until executing meals(). I had to delete the os.chdir(): the directory was already 
set in Food Calculator and executing os.chdir(directory_Food_Calculator) again would make it look for a Food Calculator folder within the Food Calculator folder. Stupid.
After, I tested the commands in meals() and, except for "main menu", they all work perfectly fine. Turns out, when going back to main menu, it does this:

>>> Output:
Going to Main Menu...

/Users/username/Documents/Food Calculator/random meal 3
['ingredients', 'Food Calculator']
/Users/username/Documents/Food Calculator/random meal 3/Food Calculator
How can I help you? (Type either food calculator or meals or end program): 

Although it works, it's not what I wanted: it opens a Food Calculator folder in the meal folder. I need to change the directory back to Food Calculator before going back
to the main menu. 

Update: Managed to fix the issue, but now, for some reason I have two items in random meal 3: "['.DS_Store', 'ingredients']". When I check the folder, as well as the other
random meal tests, I only see one item. But getting the info on random meal 3, I get back 2. But theres only one present. Wtf. It was working just fine till now. Weird.
I wonder if I have a computer virus. Welp, I'm gonna have to delete all those folders and files, and start again. That might mean I have to work on the createFolderandFile()
part, unless if it works perfectly. Then again, I still have the issue with OVERWRITING DATA. But, I've been contemplating abt it last night and I might have
the solution to the thing. Will keep updated.

Update on that update: turns out .DS_Store is not some weird nintendo virus but a Mac OS thing lol:



DS STORE INFORMATION (START):
What is a ".DS_Store" file?
A ".DS_Store" file is a hidden file that's generated by Mac OS X, and it has a hidden folder in a visible folder. The hidden folder contains a list of settings for the folder 
it's in, and you can't see it. If you delete the ".DS_Store" file in Finder, it goes away. Removing the direct connection with the Finder means you can open any file directly. 
Experiment around with what gets opened and see how it changes your workflow.

How do ".DS_Store" files help Mac OS X?
".DS_Store" files are created by the Mac OS X operating system to store custom attributes for folders. These files can sometimes be found in folders that you've downloaded 
from the Internet, but they shouldn't be deleted because they're necessary for Mac OS X to read the folder's attributes correctly.
While this is an issue that affects the iPad as well,”.DS_Store” files are created by the Mac OS X operating system, not iOS. Fortunately, theres a solution to it, without 
having to reinstall iOS or mess around with startup files.

Heres how to get rid of these mysterious files:

First, open System Preferences, and go to the Security & Privacy section.
Tap the Content Menu at the top right-hand corner of the window.
Scroll to the bottom of the list, find “Customize Disk,” and press the Delete key on your keyboard. Confirm when prompted that you want to delete the file.
Exit out of System Preferences and you should see a new file sitting there, .DS_Store.
The only thing you need to do now is create it whenever you want.
What happens if I delete my ".DS_Store" files?

In a nutshell, if you delete your ".DS_Store" files, your Mac may not operate properly. According to many posts and forums, Apples decision to remove the venerable “DS_Store” 
files from the operating system could potentially cause your iMac to be malfunctioning and unable to use the applications stored on it. As of now, there is no conclusive proof 
that the removal of the Registry entries causes any backlash or drastic consequences to the user experience, and many, genuinely reputable sources, have stated that the removal 
of these files could pose no threat to the user experience.
DS STORE INFORMATION (FIN)



So, n order to avoid confusion for the future, I'll just access the ingredients file by its name instead of searching for it, since all ingredients file will be named 
'ingredients' no matter what. I just hope this doesn't create a problem later down the line tho. If it does, oh well. Something to fix later. 

10:00 AM
Forgot to add a scenario where if there are no meals saved. Added this to meal():

if len(os.listdir()) == 0:
            print("It seems that you don't have any meals saved in here. Let's go back to the main menu.")
            initiation()

Update: Dumb dumb. Dumb af I am. 

>>> Output:
/Users/username/Documents/Food Calculator/Food Calculator

I got to remember to change the directory back. 

if len(os.listdir()) == 0:
            print("It seems that you don't have any meals saved in here. Let's go back to the main menu.")
            initiation()

Okay, I managed to rewrite some code in initiation() to set the the directory back to Food Calculator all the time. Now, it shouldnt create a Food Calculator within the Food 
Calculator folder, create a Food Calculator if there's none in the original directory and open that folder to begin with and so forth. Also, I don't have to add 
os.chdir(directory_Food_Calculator) every time in every situation that goes back to the main menu. So, wooooo:

    os.chdir(original_pathway)
    if directory_Food_Calculator not in os.listdir(original_pathway):
        os.mkdir(directory_Food_Calculator)
        print(os.listdir())

    print(os.getcwd())
    if os.getcwd() != directory_Food_Calculator:                             _
        # if directory_Food_Calculator not in os.listdir():                   |
            # os.mkdir(directory_Food_Calculator)                             |----------- These lines of code here I removed and moved it
            # print(os.listdir())                                            _|            to the upper lines of code, as you can see
        os.chdir(directory_Food_Calculator)
        print(os.getcwd())
10:43 AM
Still getting DS Store as an item and its affecting the scenario, "if theres no meal folders". Trying to assess it by adding "meal" to the end of every meal folder and
only show that when calling it. I've made three meals named random 1, 2,and 3, but:

>>> Output:
random 2 meal

It only shows one meal. Need to figure out why.
1:03 PM
Been tidying up the thingamajigs. After taking a step back, this code is hella messy technically. I might try to code it again from scratch to see if I can do it
after 7 days has been up. 
1:58 PM
The entire time, I could have avoided the DS Store issue by simply nitpicking all the meal folders that contain 'meal' in their name and add it to a list:

    if len(os.listdir()) == 0:
        print("There's nothing in here. Let's go back to the main main menu.")
        initiation()
    else:
        print(len(os.listdir()))
        meal_list = [meal for meal in os.listdir() if 'meal' in meal]
        print(meal_list)
        for meal in os.listdir():
            if 'meal' in meal:
                print("MARKER 2")
                print(len(os.listdir())) 
                print(meal)

The above code could've been avoided by doing this:

meal_list = [meal for meal in os.listdir() if 'meal' in meal]

And simply refer from that instead. I really don't know why I'm making such simple novice mistakes: it's either I'm still a big time novice rather than a simple novice or
I've been coding way too long on this particular project that I'm burning out. I think I've stated that once before. 

Update: I think I finally finished most of it as I'm not getting any errors no matter the cases or edge cases I give the program. It lists only the meal folders, does the 
calculation, no new Food Calculator folder, and so forth. Now, I just have to go focus on the foodCalculator() and tie up that frayed knot with OVERWRITING DATA. I think I'm
going to try to see if I can just have an array outside the function and keep adding to it, then pull from it. Though, I thought I did that already. 

2:30 PM
So, it turns out it doesn't overwrite. In fact, it's working fine it seems. However, when I transfer to meals() and try to get the data for
"Cost per serving" for each ingredient, I get this:

>>> Output:
Type here: cost

a Cost Per Serving:
0.16666666666666666


a Cost Per Serving:
0.5


a Cost Per Serving:
0.25


b Cost Per Serving:
0.16666666666666666


b Cost Per Serving:
0.5


b Cost Per Serving:
0.25


c Cost Per Serving:
0.16666666666666666


c Cost Per Serving:
0.5


c Cost Per Serving:
0.25

Hella long, right? Not only that, it's not printing to the right cost. If you look, one ingredient is assigned to all three costs and it repeats for the other 
ingredients. Gonna need to go over that. Starting to think I should've used Pandas DataFrame to begin with. Maybe once I finish up my resumé. This was the code that
gave that output:

        elif meal_files == 'cost': 
            for ingredient in w_dict:
                for cost in x_dict:
                    print(f"\n{ingredient} Cost Per Serving:\n{cost}\n")       

Or perhaps I can use linked lists next time. Wonder how that would go.
4:32 PM
The project is FINALLY COMPLETE. I just fixed the issue by returning enumerated object of said list and just matching each others indexes (if idx1 == idx2). I've ran
multiple scenarios to test for any bugs. So far, no bugs. The thing abt accessing the ingredients info, though, is that it doesn't give access which ingredient I want
to look at; instead, it shows all. I wonder if I should add that feature since I do technically have one more day to complete it. I mean, it is complete. I just want to 
add that cool neat feature. Wonder wonder. I'm just gonna test the program first. Then maybe tidy up a bit since there are still "MARKERS" in the program. 
5:04 PM
Okay, so apparently there were some loose ends, but they were fixed and now its fully functional and should output all the proper data. I hope. Besides that, I'm finally
done! WOOOOOOO! Messy, but completely functional! I feel proud of myself. Eventually, I will have to go back to this project and turn it into a proper program and app. 
This is merely phase 1 of the "Food Calculator" plan. 
'''
'''
Version 1 of Food Calculator for reference of the progress made:

d = {}
def ingredient(name, price, serving_total):
    cost_per_serving = float(price) / float(serving_total)
    user_choice_of_serving = float(input("How many servings are you putting in? "))
    total_cost_of_serving = cost_per_serving * user_choice_of_serving
    if name not in d:
        d[name] = total_cost_of_serving
    return d

user_ingredient_name = ""
user_ingredient_price = ""
user_ingredient_serving = ""

def get_info():
    user_input = ""
    while user_input != "yes":

        user_ingredient_name = input("Name: ")
        user_ingredient_price = input("Cost: ")
        user_ingredient_serving = input("Total serving: ")

        x = ingredient(user_ingredient_name, user_ingredient_price, user_ingredient_serving)
        print(x)
        user_input = input("Is that all? Yes or No?").lower()
        if user_input == "yes":
            print(x)
            meal_cost = mealCost()
            print (meal_cost) 
        elif user_input != "no":
            print("Invalid input")

    end_function = ""
    while end_function == "":
        end_function = input("Will that be all? Y/N: ").lower()
        if end_function == "n":
            print(d, meal_cost)


def mealCost():
    values = d.values()
    total = sum(values)
    mealname = input("What is the name of your meal?: ")
    return(f"The sum of your {mealname} is {total}")
    




get_info()
'''