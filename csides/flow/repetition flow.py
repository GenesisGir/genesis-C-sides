"""
πΆπ΄π½π΄ππΈπ πΆπ΄π½π΄ππΈπ πΆπ΄π½π΄ππΈπ

βββββββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββββββ


βββββββββββββββββββββββββββββββββββββ ββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββ ββββββββββββββββββ.py


This programs lets the user choose how many times they would like to call the number set by users input
the program uses the various functions set out. The use of importing modules are used as well and is being 
used to choose when the program should end with the sys.exit() function call that calls to the sys module
its really amazing what you can do with string concatanation and converters like str() that converts anything you enter 
within it into the string data type! check out this seaside its short and simple but ultimately we are using for
loops and functions to make this porject breathe life into the program. Parameters are being implemented also
its being used within the print line on line 30 to insert the phone_number constant into its parenthesis () and the
use of  functions are used in lines 24/31 to store the data and source code to be used anywhere in the code later on
this helps to have to copy/paste code over and over again!


δΈγγ©ε°ΊβΌπββΌγαͺπββ»δΈ«βαΆπππδΈθ? δΈβαΆθ? ε°Ί

πΆπ΄π½π΄ππΈπ πΆπ΄π½π΄ππΈπ πΆπ΄π½π΄ππΈπ
"""

# define con()
def con():
    global phone_number
    # constants
    phone_number = str(3546453425)

import sys

def phone(num):
    call = input('How many times would you like to call? ')
    for ring in range(int(call)):
        print('called ' 
              + num 
              + ' (' 
              + str(ring) 
              + ') times!'
              )

"""
ββββββββββββ βββββββββββββββββββββββββββββββββββββββββ
ββββββββββββ βββββββββββββββββββββββββββββββββββββββββ

def statements create functions to use later in your programs to store source code so it can be reused later in your 
scripts and can be very useful for alot of things to declutter code and remove the problem of copy/paste novices
run into and can be used anywhere in code and these functions are excuted with function calls! 

follow the steps below to create a def statement

eg. def genesis():
        print('Hello genesis!')

what this indicates is that we created a function and we can now call those functions with the function call
genesis() while we can name our function calls basically anything its good practice to keep it short and simple for
cleaner code in the long run!
"""
# phone() is the function calling to the function phone(num)                    
phone(phone_number)

"""
β β β β β β β β β β β β β β β β β β β β β β β β β β β β β’ β‘β β β β β β β‘β β β β β β β β β β β β β 
β β β β β β β β β β β β β β β β β β β β β β β β β β β β β’Έβ‘β β β‘β β‘β β‘β β β β β β β β β β β β β 
β β β β β β β β β β β β β β β β β β β β β β β β β β β β β’Έβ‘β β β β β β‘ β β β β β β β β β β β β β β 
β β β β β β β β β β β β β β β β β β β β β β β β β β β β β’Έβ£Ώβ£Ώβ£€β£Ύβ‘Ώβ β β β β β β β β β β β β β β β 
β β β β β β β β β β£β£β£β‘β β β β β β β β β’β£β£β£β£β£β£β β β β β β’β£β£β£β‘β β β β β β β β β β β β 
β β β β β β β β β β‘β β β Ώβ’¦β €β €β£€β €β €β‘€β €β’Όβ‘§β €β’Όβ β β Ώβ €β‘β‘ β €β ΄β Ώβ‘β β β §β €β£β β β β β β β β β β 
β β β β β β β β β β‘β β β β’Έβ β β£Ώβ β β‘β β’Έβ‘β β’Έβ β β β β‘β β β β β‘β β β β β β’³β β β β β β β β β 
β β β β β β β β β β‘β β β Ώβ’Ώβ β β Ώβ β β β β’Έβ‘β β’Έβ β β Ώβ Ώβ‘β β Έβ Ώβ Ώβ‘β β β£Ώβ β β’Έβ β β β β β β β β 
β β β β β β β β β β ³β£β β β’Έβ β β β β β β’β£Όβ‘β β’Έβ£β β β β£§β‘β β β β‘β β β£Ώβ β β’Έβ β β β β β β β β 
β β β β β β β β β β β β β Ώβ£Ώβ£Ώβ£Ώβ£Ώβ£Ώβ£Ώβ£Ώβ£Ώβ‘Ώβ£Ώβ£Ώβ£Ώβ’Ώβ£Ώβ£Ώβ‘Ώβ’Ώβ£Ώβ£Ώβ£Ώβ’Ώβ£Ώβ‘Ώβ’Ώβ£Ώβ£Ώβ β β β β β β β β β β 

 
Thank you for downloading this .py find more sea sides at my githu and learn something new everyday and rememeber
to not give up on coding! its an artform and anbody can be skileld enough to achieve greatness in your code
make sure to check out my twitch streams below!

Twitch: https://www.twitch.tv/genesisgir 
Github: https://github.com/GenesisGir

thank you to everyone on twitch who participated in the making of this .py!
"""