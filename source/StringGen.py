# #^ StringGen - v0.4.0-Alpha Build
#! Random-String-Generation CLI Tool
#TODO: Begin GUI development.
#ADD:  #& Continue to work on new ideas.
#?++++++++++Libraries/Modules++++++++++#
import secrets
from datetime import datetime as ct
from os import chdir as cwd
from os import remove
from os.path import dirname as curFolder
from os.path import exists, abspath as getAbsPath
from sys import exit as ex
from time import sleep as s
from typing import Any, Union
from delFL import del_FileLines
from loadingSequence import load

cwd(curFolder(curFolder(__file__)))

#?++++++++++++++++++++++++++++++++++++?#


#!++++++++++Functions++++++++++#
def programStart() -> Any:
    """
    Starts Program Introduction.
    
    - Displays Current time Using (yyy-mm-dd hh:mm:ss) Format.
    - Displays Welcome Message.
    - Starts Application.
    """
    print('\nWelcome to StringGen v0.4.0-Alpha!\n')
    print(f'The Current Time Is:\n{ct.now().strftime("%Y-%m-%d %H:%M:%S")}'
          )  #? Displays time.
    return viewLastGenerated()


def viewLastGenerated() -> Union[Any, None]:
    """Returns last string that was saved, or continues to menu if not found.
    
    :rtype: Union[Any, None]
    """

    #? Checks for/opens existing "last generated" file:
    if exists(r'.\generated\lastgenerated.txt') == True:
        lastGenerated = open(r'.\generated\lastgenerated.txt').read()

        while True:
            q_lastGenerated = input(
                '\nWould you like to see your most recent saved entry? Y/N?\n> '
            ).lower()

            #* Yes:
            if q_lastGenerated.startswith('y'):
                print(
                    f'\nYour last saved string was {str(len(lastGenerated))} characters long:\n{lastGenerated}'
                )
                load('Loading Menu', 'Done!')
                return globalMenu()

            #! No:
            elif q_lastGenerated.startswith('n'):
                load('Loading menu', 'Done!')
                return globalMenu()

            #& Error/Invalid:
            else:
                print(
                    'ERROR:\nInvalid Input. Please enter "y" for "yes", or "n" for "no".\n'
                )
                s(0.75)
                continue

    #? No "lastgenerated.txt" found to exits:
    else:
        replaceFile = open(r'.\generated\lastgenerated.txt', 'x')
        replaceFile.close()
        print(
            'No recently generated string detected.\nContinuing to random string generator.\n'
        )
        return stringGenerator()


def viewSaved_menu() -> None:
    """Displays options for editing saved strings. 
    
    :rtype: (None)
    """

    print(30 * "=", "StringGen MENU", 30 * "=")
    print("[ ", "1.  View Save Slot 1 ", "    ]")
    print("[ ", "2.  View Save Slot 2 ", "    ]")
    print("[ ", "3.  View Save Slot 3 ", "    ]")
    print("[ ", "4.  View Save Slot 4 ", "    ]")
    print("[ ", "5.  View Save Slot 5 ", "    ]")
    print("[ ", "6.  View Save Slot 6 ", "    ]")
    print("[ ", "7.  View Save Slot 7 ", "    ]")
    print("[ ", "8.  View Save Slot 8 ", "    ]")
    print("[ ", "9.  View Save Slot 9 ", "    ]")
    print("[ ", "10. View Save Slot 10", "    ]")
    print("[ ", "11. Generate New Entry", "   ]")
    print("[ ", "12. View ALL Save Slots", "  ]")
    print("[ ", "13. CLEAR SAVE SLOTS", "     ]")
    print(74 * "=")


def view_saved() -> Any:
    """Return functional option menu to view/modify saved strings.
    
    :rtype: Any
    """

    while True:
        #? open "allsavedPWs.txt" as a list of every line within file:
        saveSlots_FH = open(r'.\generated\allSavedPWs.txt', 'r+').readlines()

        viewSaved_menu()
        menuChoice: str = input(
            'Enter [1-12] to make a selection, or enter "done" when finished.\n> '
        ).lower()

        try:
            #! Slot 1
            if menuChoice == '1':
                print(f'\nSave Slot 1:\n{saveSlots_FH[1]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )

                    userChoice = input('> ').lower()

                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [0, 1, 2])

                        #& Deletes most recently generated string if allsavedPWs.txt is empty.
                        if len(open(
                                r'.\generated\allSavedPWs.txt').read()) < 1:

                            remove(r'.\generated\lastgenerated.txt')
                        break

                    else:
                        break

                continue

            #! Slot 2
            elif menuChoice == '2':
                print(f'\nSave Slot 2:\n{saveSlots_FH[4]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()

                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [3, 4, 5])
                        break

                    else:
                        break

                continue

            #! Slot 3
            elif menuChoice == '3':
                print(f'\nSave Slot 3:\n{saveSlots_FH[7]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [6, 7, 8])
                        break
                    else:
                        break
                continue

            #! Slot 4
            elif menuChoice == '4':
                print(f'\nSave Slot 4:\n{saveSlots_FH[10]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [9, 10, 11])
                        break
                    else:
                        break
                continue

            #! Slot 5
            elif menuChoice == '5':
                print(f'\nSave Slot 5:\n{saveSlots_FH[13]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [12, 13, 14])
                        break
                    else:
                        break
                continue

            #! Slot 6
            elif menuChoice == '6':
                print(f'\nSave Slot 6:\n{saveSlots_FH[16]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [15, 16, 17])
                        break
                    else:
                        break
                continue

            #! Slot 7
            elif menuChoice == '7':
                print(f'\nSave Slot 7:\n{saveSlots_FH[19]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [18, 19, 20])
                        break
                    else:
                        break
                continue

            #! Slot 8
            elif menuChoice == '8':
                print(f'\nSave Slot 8:\n{saveSlots_FH[22]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [21, 22, 23])
                        break
                    else:
                        break
                continue

            #! Slot 9
            elif menuChoice == '9':
                print(f'\nSave Slot 9:\n{saveSlots_FH[25]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\generated\allSavedPWs.txt',
                                      [24, 25, 26])
                        break
                    else:
                        break
                continue

            #! Slot 10
            elif menuChoice == '10':
                print(f'\nSave Slot 10:\n{saveSlots_FH[28]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )
                    userChoice = input('> ').lower()
                    if userChoice.startswith('del'):
                        del_FileLines(r'.\allSavedPWs.txt', [27, 28, 29])
                        break
                    else:
                        break
                continue

            #! Slot 11
            elif menuChoice == '11':  #& Returns the Random Generator Function.
                load('Loading', 'Ok!')
                return stringGenerator()

            #! Slot 12
            elif menuChoice == '12':  #& Displays ALL SAVED PWs.
                try:
                    print('\n\nAll Saved PWs:\n')
                    print('\nSlot 1: ' + saveSlots_FH[1])
                    print('\nSlot 2: ' + saveSlots_FH[4])
                    print('\nSlot 3: ' + saveSlots_FH[7])
                    print('\nSlot 4: ' + saveSlots_FH[10])
                    print('\nSlot 5: ' + saveSlots_FH[13])
                    print('\nSlot 6: ' + saveSlots_FH[16])
                    print('\nSlot 7: ' + saveSlots_FH[19])
                    print('\nSlot 8: ' + saveSlots_FH[22])
                    print('\nSlot 9: ' + saveSlots_FH[25])
                    print('\nSlot 10: ' + saveSlots_FH[28])
                    continue

                #* Display message once all saved strings have been returned
                except IndexError:
                    print(
                        '\nAll saved strings viewed!\nOther Save Slots Empty.\n'
                    )
                    con: str = input('\nEnter anything to continue.\n')
                    continue

            #! Slot 13
            #! ERASES ALL FROM PW FILE!!
            elif menuChoice == '13':

                while True:
                    print(
                        '\nWARNING!\nTHIS ACTION CANNOT BE UNDONE. IF YOU CHOOSE TO CLEAR ALL PWs, THEY WILL BE GONE FOREVER AND EVER.\n'
                    )
                    amSure: str = input('\nARE YOU SURE? Y/N: ').lower()

                    if str(amSure).startswith('y'):
                        #! Deletes both recently saved, and last-generated pw files:

                        #* Checks for saved entry list & deletes upon discovery:
                        if exists(r'.\generated\allSavedPWs.txt') == True:
                            remove(r'.\generated\allSavedPWs.txt')
                        #* Checks for "recently generated" list & deletes upon discovery:
                        if exists(r'.\generated\lastgenerated.txt') == True:
                            remove(r'.\generated\lastgenerated.txt')

                        load('Clearing Saved Strings',
                             'All Strings Deleted Successfully!')
                        return stringGenerator()

                    elif str(amSure) == 'n':
                        return view_saved()

                    else:
                        print('ERROR:\nMUST ENTER ONLY "Y" or "N".\n')
                        s(0.75)
                        continue

            elif menuChoice == 'done':
                #* Once done with the PW Menu, program moves on to PW gen function.
                load('Loading PW Generator', 'Done!')
                return stringGenerator()

            else:
                print('\nERROR:\nInvalid input.')
                s(0.75)
                continue

        except IndexError:
            #! Displays following string if request for Empty PW Slot is called:
            print('\nERROR\nSave slot is empty.\n')
            s(0.75)
            continue


def stringGenerator() -> Any:
    """Generates Random Strings of up to 30 separate words.
    
    - All available words are pulled from a dictionary file, containing over 1.5 MILLION words.
    - :rtype: Any
    """

    while True:
        print(
            '\nEnter the number of random words that you\'d like to generate.')
        q_strLen = input(
            'String Length [Enter 1-30 or \"E\" to Exit]: ').lower()
        try:
            x: int = int(q_strLen)

            #! Restricts valid inputs to be integers within the specified range (1-30 words):
            if x > 30:
                print('\nThe max number of words is 30.\n')
                continue

            elif x <= 0:
                print(
                    '\nYou have to have at least 1 word. Come on man, you\'re messing with me, aren\'t you?\nStop it!\n'
                )
                continue

            #* Valid integer/input entry:
            else:
                break

        except ValueError:
            if q_strLen == 'e':
                cleanup(mode='full')
                load('Exiting Program', 'Good-Bye')
                ex(0)

            else:
                print(
                    '\nError: Please enter a number in integer form.\nEntry cannot contain any letters, or punctuation marks (e.g. ,.?!AWf&*ck>y0U_81tcHl@^#)\n'
                )
                continue

    with open(r'.\Dictionary\RandomWordDictionary.txt') as dictionary:
        strList: list = [words.strip() for words in dictionary]
        str_FINAL: str = ' '.join(
            secrets.choice(strList) for i in range(x)[:30])

    #? Closes File\Resets Buffer\Changes to Documents Take Effect:
    dictionary.close()

    print(f'\nYour New Generated String:\n\n{str_FINAL}')

    while True:  #? Begin Options to Save, New, or Exit:
        q_saveStr = input(
            '\nWould you like to save this Word?\nENTER "save", "new", or "exit" > '
        ).lower()

        if q_saveStr.startswith('save'):

            if exists(r'.\generated\allSavedPWs.txt') == True:

                pwFileLen = open(r'.\generated\allSavedPWs.txt').readlines(
                )  #? opens allsavedPWs.txt and pulls out content into a list.

                #! If the requested generative length is above capacity (30), raise error:
                if len(pwFileLen) >= 30:
                    print(
                        '\nERROR:\nSave slots full. Please clear a slot to make some room.\n'
                    )
                    s(2)
                    #* Returns to saved pw menu so user may clear space if they wish.
                    return view_saved()

                #* Add result to both "saved" & "last generated" docs:
                saveSlots_FH = open(r'.\generated\allSavedPWs.txt', 'a')
                saveSlots_FH.write(
                    f'Time Saved: {ct.now().strftime("%Y-%m-%d %H:%M:%S")}\n{str_FINAL}\n\n'
                )
                saveSlots_FH.close()
                lastGenerated = open(r'.\generated\lastgenerated.txt', 'w')
                lastGenerated.write(str_FINAL)
                lastGenerated.close()
                load('Saving to Open Slot', 'Successfully Saved!')

                return globalMenu()

            #* Create new "saved" file if none currently exist:
            else:
                saveSlots_FH = open(r'.\generated\allSavedPWs.txt', 'x')
                saveSlots_FH.write(
                    f'Time Saved: {ct.now().strftime("%Y-%m-%d %H:%M:%S")}\n{str_FINAL}\n\n'
                )
                saveSlots_FH.close()
                lastGenerated = open(r'.\generated\lastgenerated.txt', 'w')
                lastGenerated.write(str_FINAL)
                lastGenerated.close()
                load('Saving to Open Slot', 'Successfully Saved!')

                return globalMenu()

        elif q_saveStr == 'new':
            return stringGenerator()

        elif q_saveStr == 'exit':
            return cleanup(mode='light')

        else:
            print('\nERROR\nInvalid input.')
            s(0.75)
            continue


def globalMenu() -> Any:
    """Ask user to choose next task.
    
    - Select option "1" to generate a new string.
    - Select option "2" to view/edit saved strings.
    - Select option "3" to exit the program.
    
    :rtype: (Any)
    """
    while True:
        user_inp: str = input(
            '\n_____________________________________\n| Would you like to:                |\n| 1.) Generate another word/phrase? |\n| 2.) View Your Saved Data?         |\n| 3.) Exit?                         |\n|___________________________________|\n\nENTER [1-3] > '
        ).lower()

        if user_inp == '1':
            return stringGenerator()

        elif user_inp == '2':
            load('Loading Menu', 'Ok!')
            return view_saved()

        elif user_inp == '3':
            load('Exiting Program', 'Good-Bye')
            s(0.75)
            return ex(0)

        elif ValueError or TypeError:
            print(f'\nERROR\nInvalid input: "{user_inp}"\n')
            s(0.75)
            continue


def cleanup(mode: str = None) -> Any:
    """Ensures any temporary files are cleaned up, and any leftover files are removed from the './StringGen/generated' directory.

    Parameters:
    - :param mode: | Extensiveness of file-cleaning.
    - :type mode: | (str)
        - `if :param mode: == 'full':`
            - Check for both "allsavedPWs.txt" and "lastgenerated.txt".
                - 1). If "allSavedPWs" DOES exist:
                    - if "allSavedPWs.txt" is blank, then both "allSavedPWs.txt" AND "lastgenerated.txt" are deleted.
                    - else if ANY entries exist within "allSavedPWs.txt", nothing is changed.
                        - Exit program.
                - 2). If "allSavedPWs" DOES NOT exist, then the program ensures that there is NO "lastgenerated.txt" file, and deletes it if found.
                    - Exit program.
        - `if :param mode: == 'light':`
            - Check for existence of "allsavedPWs.txt" file.
                - 1). If file does NOT exist, then delete "lastgenerated.txt".
                    - Exit program.
                - 2). If file DOES exist, then nothing is changed.
                    - Exit program.
    - :rtype (Any):
    """
    #~ Delete both "allsavedPWs.txt" and "lastgenerated.txt", if former is empty.
    if mode == 'full':
        #& Check for existence of "allsavedPWs.txt" file, and deletes if blank:
        if exists(r'.\generated\allSavedPWs.txt') == True:
            if len(open(r'.\generated\allSavedPWs.txt').readlines()) < 1:
                remove(r'.\generated\allSavedPWs.txt')

                #! Delete "lastgenerated.txt".
                if exists(r'.\generated\lastgenerated.txt') == True:
                    remove(r'.\generated\lastgenerated.txt')

        #& Check for existence of "allsavedPWs.txt" file, and ensures "lastgenerated.txt" is also deleted:
        elif exists(r'.\generated\allSavedPWs.txt') == False:
            if exists(r'.\generated\lastgenerated.txt') == True:
                remove(r'.\generated\lastgenerated.txt')

    #~ Delete "lastgerated.txt" if "allsavedPWs.txt" doesn't exist:
    elif mode == 'light':
        if exists(r'.\generated\allSavedPWs.txt') == False:

            #! Delete "lastgenerated.txt"
            if exists(r'.\generated\lastgenerated.txt') == True:
                remove(r'.\generated\lastgenerated.txt')

    load('Exiting Program', 'Good-Bye')
    return ex(0)


programStart()
