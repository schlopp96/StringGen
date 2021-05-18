## #!StringGen - v0.1.2-Alpha
#! CLI String-Generation Tool
#TODO:
#? Reorganize/Modernize code to be MUCH more readable.
#* Implement a global menu function that users can use to navigate, rather than being directed through functions.
#! Fix "View all save slots" option to not include unnecessary "ERROR: Save slot empty" after returning slots.
#* Break down giant functions (take stringGenerator() for example) into smaller, more efficient & reusable functions.

#?++++++++++Libraries/Modules++++++++++#

import os
import secrets
from datetime import datetime as ct
from sys import exit as ex
from time import sleep as s

from loadingSequence import load


#!++++++++++Functions++++++++++#
def programStart() -> None:
    """
    Starts Program Introduction.
    
    - Displays Current time Using (yyy-mm-dd hh:mm:ss) Format.
    - Displays Welcome Message.
    - Starts Application.
    """
    currentTime = str(ct.now())[:16]
    print('\nWelcome to StringGen v0.1.2-Alpha!\n')
    print('The Current Time Is:\n{}'.format(currentTime))  # Displays time.
    viewLastGenerated()


def viewLastGenerated():
    '''
    Returns last string that was saved, or continues to string generator if there isn't one.
    
    '''
    #? Checks for existing "last generated" file:
    if os.path.exists(r'.\StringGen\generated\lastgenerated.txt') == True:
        lastGenerated = open('.\StringGen\generated\lastgenerated.txt').read()
        while True:
            choice_lastGenerated = input(
                '\nWould you like to see your most recent saved entry? Y/N?\n> '
            ).lower()
            if choice_lastGenerated.startswith('y'):
                print('\nYour last saved string was {} characters long:\n{}'.
                      format(str(len(lastGenerated)), lastGenerated))
                load('Loading Menu', 'Done!')
                return saveSlots()
            elif choice_lastGenerated.startswith('n'):
                load('Loading menu', 'Done!')
                return saveSlots()
            else:
                print(
                    'ERROR:\nInvalid Input. Please enter "y" for "yes", or "n" for "no".\n'
                )
                s(0.75)
                continue
    else:
        lastGenerated = open('.\StringGen\generated\lastgenerated.txt', 'x')
        lastGenerated.close()
        print(
            'No recently generated string detected.\nContinuing to random string generator.\n'
        )
        return stringGenerator()


def displaySaves():
    """
    Displays Options for Saved String-Iterations
    
    """

    print(30 * "-", "StringGen MENU", 30 * "-")
    print("| ", "1.  View Save Slot 1 ", "    |")
    print("| ", "2.  View Save Slot 2 ", "    |")
    print("| ", "3.  View Save Slot 3 ", "    |")
    print("| ", "4.  View Save Slot 4 ", "    |")
    print("| ", "5.  View Save Slot 5 ", "    |")
    print("| ", "6.  View Save Slot 6 ", "    |")
    print("| ", "7.  View Save Slot 7 ", "    |")
    print("| ", "8.  View Save Slot 8 ", "    |")
    print("| ", "9.  View Save Slot 9 ", "    |")
    print("| ", "10. View Save Slot 10", "    |")
    print("| ", "11. Generate New Entry", "   |")
    print("| ", "12. View ALL Save Slots", "  |")
    print("| ", "13. CLEAR SAVE SLOTS", "     |")
    print(74 * "-")


def deleteFileLines(
    original_file, line_numbers
) -> None:  # Clears Specific Save Slots (lines from allsavedPWs.txt).
    """
    In a file (original_file), delete lines that match list of lines (line_numbers) user wants to delete.
    
    """
    is_skipped = False  # if marked "True", delete from the original file/don't include in new file.
    counter = 0  # Line Count
    # Create name of dummy / temporary file
    dummy_file = original_file + '.bak'
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file,
                                                    'w') as write_obj:
        # Line by line, copy data from original file to dummy file
        for line in read_obj:
            if counter not in line_numbers:  # If counter (int) is not included in line_numbers (list of specified lines to be skipped and deleted), then write to write_obj (include in new file, aka, don't delete).
                write_obj.write(line)
            else:
                is_skipped = True  # If current line number (string) exists in the list provided by user (line_numbers), then skip copying that line(str).

            counter += 1  # Move to next line.

    if is_skipped:  # If any line is skipped (deleted) then rename dummy file as original file (Overwrite old file).
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:  # Otherwise, delete dummy file and leave original as is.  (Do not overwrite original file).
        os.remove(dummy_file)


def saveSlots():
    """
    Returns functional option menu to view/modify saved strings.
    
    """

    while True:
        q = input(
            '\nWould you like to view/delete your SAVED PWs? Y/N?').lower()

        if q == 'y':

            while True:
                # opens "allsavedPWs.txt" as a list of every line in the file:
                saveSlots_FH = open(r'.\StringGen\generated\allSavedPWs.txt',
                                    'r+').readlines()

                displaySaves()
                menuChoice: str = input(
                    'Enter [1-12] to make a selection, or enter "done" when finished.\n> '
                ).lower()

                try:
                    #! Slot 1
                    if menuChoice == '1':
                        print('\nSave Slot 1:\n{}'.format(saveSlots_FH[1]))

                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )

                            userChoice = input('> ').lower()

                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [0, 1, 2])

                                if len(
                                        open(
                                            r'.\StringGen\generated\allSavedPWs.txt'
                                        ).read()) < 1:
                                    #? Deletes most recently generated string if allsavedPWs.txt is empty.

                                    os.remove(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                    )
                                break

                            else:
                                break

                        continue

                    #! Slot 2
                    elif menuChoice == '2':
                        print('\nSave Slot 2:\n{}'.format(saveSlots_FH[4]))

                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()

                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [3, 4, 5])
                                break

                            else:
                                break

                        continue

                    #! Slot 3
                    elif menuChoice == '3':
                        print('\nSave Slot 3:\n{}'.format(saveSlots_FH[7]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [6, 7, 8])
                                break
                            else:
                                break
                        continue

                    #! Slot 4
                    elif menuChoice == '4':
                        print('\nSave Slot 4:\n{}'.format(saveSlots_FH[10]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [9, 10, 11])
                                break
                            else:
                                break
                        continue

                    #! Slot 5
                    elif menuChoice == '5':
                        print('\nSave Slot 5:\n{}'.format(saveSlots_FH[13]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [12, 13, 14])
                                break
                            else:
                                break
                        continue

                    #! Slot 6
                    elif menuChoice == '6':
                        print('\nSave Slot 6:\n{}'.format(saveSlots_FH[16]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [15, 16, 17])
                                break
                            else:
                                break
                        continue

                    #! Slot 7
                    elif menuChoice == '7':
                        print('\nSave Slot 7:\n{}'.format(saveSlots_FH[19]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [18, 19, 20])
                                break
                            else:
                                break
                        continue

                    #! Slot 8
                    elif menuChoice == '8':
                        print('\nSave Slot 8:\n{}'.format(saveSlots_FH[22]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [21, 22, 23])
                                break
                            else:
                                break
                        continue

                    #! Slot 9
                    elif menuChoice == '9':
                        print('\nSave Slot 9:\n{}'.format(saveSlots_FH[25]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [24, 25, 26])
                                break
                            else:
                                break
                        continue

                    #! Slot 10
                    elif menuChoice == '10':
                        print('\nSave Slot 10:\n{}'.format(saveSlots_FH[28]))
                        while True:
                            print(
                                'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                            )
                            userChoice = input('> ').lower()
                            if userChoice.startswith('del'):
                                deleteFileLines(
                                    r'.\StringGen\generated\allSavedPWs.txt',
                                    [27, 28, 29])
                                break
                            else:
                                break
                        continue

                    #! Slot 11
                    elif menuChoice == '11':  # Returns the Random Generator Function.
                        load('Loading', 'Ok!')
                        stringGenerator()

                    #! Slot 12
                    elif menuChoice == '12':  # Displays ALL SAVED PWs.
                        print('All Saved PWs:\n')

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

                    #! Slot 13
                    #! ERASES ALL FROM PW FILE!!
                    elif menuChoice == '13':

                        while True:
                            print(
                                '\nWARNING!\nTHIS ACTION CANNOT BE UNDONE. IF YOU CHOOSE TO CLEAR ALL PWs, THEY WILL BE GONE FOREVER AND EVER.\n'
                            )
                            amSure = input('\nARE YOU SURE? Y/N: ').lower()

                            if str(amSure).startswith('y'):
                                #! Deletes both recently saved, and last-generated pw files:

                                #* Checks for saved entry list & deletes upon discovery:
                                if os.path.exists(
                                        r'.\StringGen\generated\allSavedPWs.txt'
                                ) == True:
                                    os.remove(
                                        r'.\StringGen\generated\allSavedPWs.txt'
                                    )
                                #* Checks for "recently generated" list & deletes upon discovery:
                                if os.path.exists(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                ) == True:
                                    os.remove(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                    )

                                load('Clearing PW List', 'All PWs Cleared!')
                                s(1)
                                return stringGenerator()

                            elif str(amSure) == 'n':
                                return saveSlots()

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
                    print('\nERROR:\nSave Slot Empty.\n')
                    s(0.75)
                    continue

        elif q == 'n':
            #* Skips Menu and continues to PW generator function.
            load('Loading PW Generator', 'Done!')
            return stringGenerator()

        else:
            print('\nERROR:\nInvalid input.')
            s(0.75)
            continue


def stringGenerator():
    '''
    Function Responsible for Generating Random Strings.
    
    '''

    #? Stores the string-converted time format (yyyy-mm-dd hh:mm).
    timeSaved = str(ct.now())[:16]

    while True:
        #* Loop for users to determine PW length or if they would like to exit the program.
        print(
            '\nEnter the number of random words that you\'d like to generate.')
        passLen = input('Pass Length [Enter 1-30 or \"E\" to Exit]: ').lower()

        #! Restricts valid inputs to be integers within the specified range (1-30 words):
        try:
            x = int(passLen)

            if x > 30:
                print('\nThe max number of words is 30.\n')
                continue

            elif x <= 0:
                print(
                    '\nYou have to have at least 1 word. Come on man, you\'re messing with me, aren\'t you?\n'
                )
                continue

            #? User enters a valid integer/input:
            else:
                break

        except ValueError:
            if passLen == 'e':
                #! Prevents blank files from being left behind, as bugs would result.

                #? Checks for existence of saved entries, and deletes "last generated" if there are none:
                if os.path.exists(
                        r'.\StringGen\generated\allSavedPWs.txt') == True:
                    if len(
                            open(r'.\StringGen\generated\allSavedPWs.txt').
                            readlines()) < 1:
                        os.remove(r'.\StringGen\generated\allSavedPWs.txt')

                        #? "Last generated string" file deletion:
                        if os.path.exists(
                                r'.\StringGen\generated\lastgenerated.txt'
                        ) == True:
                            os.remove(
                                r'.\StringGen\generated\lastgenerated.txt')

                #? Checks for existence of "saved entries" file, and deletes "last generated" if former doesn't exist:
                elif os.path.exists(
                        r'.\StringGen\generated\allSavedPWs.txt') == False:
                    if os.path.exists(
                            r'.\StringGen\generated\lastgenerated.txt'
                    ) == True:
                        os.remove(r'.\StringGen\generated\lastgenerated.txt')
                load('Exiting Program', 'Good-Bye')
                s(0.75)
                ex(0)

            else:
                print(
                    '\nError: Please enter a number in integer form.\nEntry cannot contain any letters, or punctuation marks (e.g. ,.?!AWf&*ck>y0U_81tcHl@#^)\n'
                )
                continue

    with open(
            r'.\StringGen\Dictionary\RandomWordDictionary.txt') as dictionary:
        wordList: list = [
            words.strip() for words in dictionary
        ]  #* List containing all 1.5 million potential words to be generated contained in dictionary.
        final_STRING: str = ' '.join(
            secrets.choice(wordList) for i in range(x)[:30])

    #? Closes File\Resets Buffer\Changes to Documents Take Effect:
    dictionary.close()

    print('\nYour New Generated Word Phrase:\n\n{}'.format(final_STRING))

    while True:  #? Begin Options to Save, New, or Exit:
        saveOrNah = input(
            '\nWould you like to save this Word?\nType "save" or "new", or "exit".\n> '
        ).lower()

        if saveOrNah == 'save':

            if os.path.exists(
                    r'.\StringGen\generated\allSavedPWs.txt') == True:

                pwFileLen = open(
                    r'.\StringGen\generated\allSavedPWs.txt'
                ).readlines(
                )  #? opens allsavedPWs.txt and pulls out content into a list.

                #! If the requested generative length is above capacity (30), raise error:
                if len(pwFileLen) >= 30:
                    print(
                        'ERROR:\nSaved string file has exceeded capacity. Please clear a slot to make some room.\n'
                    )

                    #* Returns to saved pw menu so user may clear space if they wish.
                    saveSlots()

                #* Add result to both "saved" & "last generated" files:
                saveSlots_FH = open(r'.\StringGen\generated\allSavedPWs.txt',
                                    'a')
                saveSlots_FH.write('Time Saved: {}\n{}\n\n'.format(
                    timeSaved, final_STRING))
                saveSlots_FH.close()
                lastGenerated = open(
                    r'.\StringGen\generated\lastgenerated.txt', 'w')
                lastGenerated.write(final_STRING)
                lastGenerated.close()
                load('Saving to Open Slot', 'Successfully Saved!')

                #! Asks user for next task:
                while True:
                    again = input(
                        '\nWould you like to:\n1.) Generate another word/phrase?\n2.) View Your Saved Data?\n3.) Exit?\nENTER [1-3] > '
                    ).lower()

                    if again == '1':
                        return stringGenerator()

                    elif again == '2':
                        load('Loading Menu', 'Ok!')
                        return saveSlots()

                    elif again == '3':
                        load('Exiting Program', 'Good-Bye')
                        s(0.75)
                        return ex(0)

                    else:
                        print('\nERROR\nInvalid input.')
                        s(0.75)
                        continue

            #! Creates new "saved" file if No passwords have been saved yet:
            else:
                saveSlots_FH = open(r'.\StringGen\generated\allSavedPWs.txt',
                                    'x')
                saveSlots_FH.write('Time Saved: {}\n{}\n\n'.format(
                    timeSaved, final_STRING))
                saveSlots_FH.close()
                lastGenerated = open(
                    r'.\StringGen\generated\lastgenerated.txt', 'w')
                lastGenerated.write(final_STRING)
                lastGenerated.close()
                load('Saving to Open Slot', 'Successfully Saved!')

                #! Asks user for next task:
                while True:
                    again = input(
                        '\nWould you like to:\n1.) Generate another word/phrase?\n2.) View Your Saved Data?\n3.) Exit?\nENTER [1-3] > '
                    ).lower()

                    if again == '1':
                        return stringGenerator()

                    elif again == '2':
                        load('Loading Menu', 'Ok!')
                        return saveSlots()

                    elif again == '3':
                        load('Exiting Program', 'Good-Bye')
                        s(0.75)
                        return ex(0)

                    else:
                        print('\nERROR\nInvalid input.')
                        s(0.75)
                        continue

        elif saveOrNah == 'new':
            return stringGenerator()

        elif saveOrNah == 'exit':
            #? Checks for existence of "saved entries" file, and deletes "last generated" if former doesn't exist:
            if os.path.exists(
                    r'.\StringGen\generated\allSavedPWs.txt') == False:
                if os.path.exists(
                        r'.\StringGen\generated\lastgenerated.txt') == True:
                    os.remove(r'.\StringGen\generated\lastgenerated.txt')
            load('Exiting Program', 'Good-Bye')
            return ex(0)

        else:
            print('\nERROR\nInvalid input.')
            s(0.75)
            continue


programStart()
