#! python

#--------------------Welcome-To-StringGen---------------------#
#-----------------V-----0----.----0-----4-------------------#
#                                                           #
#             Possible Future Implementations:              #
#                                                           #
#                   - GUI Development                       #
#-----------------------------------------------------------#

#++++++++++Libraries/Modules++++++++++#

import os
import secrets
from datetime import datetime as ct
from pprint import pp
from sys import exit as ex
from time import sleep as s

from loadingSequence import load


#++++++++++Functions++++++++++#
def programStart():
    '''Starts Program Introduction.
    \n- Displays Current time Using (yyy-mm-dd hh:mm:ss) Format.
    \n- Displays Welcome Message.
    \n- Starts Application.'''
    currentTime = str(ct.now())[:16]
    print('\nWelcome to Schlopp\'s Word/Phrase/String Generator!\n')
    print('The Current Time Is:\n{}'.format(currentTime))  # Displays time.
    viewLastOverwrite()


def viewLastOverwrite():
    '''Returns last string that was saved, or skips to string generator if there isn't one.'''

    if os.path.exists(r'.\StringGen\generated\lastgenerated.txt') == True:
        # File handle for returning most recently saved PW:
        lastGenerated = open('.\StringGen\generated\lastgenerated.txt').read()
        while True:
            q = input(
                '\nWould you like to see your most recently randomly generated string? Y/N: '
            ).lower()
            if q.startswith('y'):
                print('\nYour last saved string was {} characters long:\n{}'.
                      format(str(len(lastGenerated)), lastGenerated))
                load('Loading Menu', 'Done!')
                saveSlots()
            elif q.startswith('n'):
                load('Loading menu', 'Done!')
                saveSlots()
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
        wordGenerator()


def print_menu():  # Draws main menu.
    '''Displays Options for Saved String-Iterations'''
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
):  # Clears Specific Save Slots (lines from allsavedPWs.txt).
    """In a file (original_file), delete lines that match list of lines (line_numbers) user wants to delete."""
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
    '''Returns functional option menu to view/modify saved strings.'''

    while True:
        q = input(
            '\nWould you like to view/delete your SAVED PWs? Y/N?').lower()

        if q == 'y':

            while True:
                # opens "allsavedPWs.txt" as a list of every line in the file:
                saveSlots_FH = open(r'.\StringGen\generated\allSavedPWs.txt',
                                    'r+').readlines()

                print_menu()
                print(
                    'Enter [1-12] to make a selection, or enter "done" when finished.'
                )

                # PW Choice Logic:
                menuChoice = input('> ')

                try:
                    # Slot 1
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
                                    # Deletes most recently generated string if allsavedPWs.txt is empty.

                                    os.remove(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                    )
                                break

                            else:
                                break

                        continue

                    # Slot 2
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
                    # Slot 3
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
                    # Slot 4
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
                    # Slot 5
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
                    # Slot 6
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
                    # Slot 7
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
                    # Slot 8
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
                    # Slot 9
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
                    # Slot 10
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
                    # Slot 11
                    elif menuChoice == '11':  # Returns the Random Generator Function.
                        load('Loading', 'Ok!')
                        wordGenerator()
                    # Slot 12
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
                    # Slot 13
                    elif menuChoice == '13':
                        # ERASES ALL FROM PW FILE!!

                        while True:
                            print(
                                '\nWARNING!\nTHIS ACTION CANNOT BE UNDONE. IF YOU CHOOSE TO CLEAR ALL PWs, THEY WILL BE GONE FOREVER AND EVER.\n'
                            )

                            amSure = input('\nARE YOU SURE? Y/N: ').lower()

                            if str(amSure) == 'y':
                                # Deletes both recently saved, and last-generated pw files:

                                if os.path.exists(
                                        r'.\StringGen\generated\allSavedPWs.txt'
                                ) == True:
                                    os.remove(
                                        r'.\StringGen\generated\allSavedPWs.txt'
                                    )

                                if os.path.exists(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                ) == True:
                                    os.remove(
                                        r'.\StringGen\generated\lastgenerated.txt'
                                    )

                                load('Clearing PW List', 'All PWs Cleared!')
                                s(1)
                                wordGenerator()  # Proceeds to PW Generator.

                            elif str(amSure) == 'n':
                                # Start back at the beginning of current function.
                                saveSlots()

                            else:
                                # User IO Failsafe.
                                print(
                                    'ERROR: USER IS A DUMBASS.\nMUST ENTER ONLY "Y" or "N".\n'
                                )
                                s(0.75)
                                continue

                    elif menuChoice == 'done':
                        # Once done with the PW Menu, program moves on to PW gen function.
                        load('Loading PW Generator', 'Done!')
                        wordGenerator()

                    else:
                        print('\nERROR:\nUSER IS A DUMBASS.\nInvalid input.')
                        s(0.75)
                        continue

                except IndexError:
                    # Displays following string if request for Empty PW Slot is called:
                    print('\nERROR:\nSave Slot Empty.\n')
                    s(0.75)
                    continue

        elif q == 'n':
            # Skips Menu and continues to PW generator function.
            load('Loading PW Generator', 'Done!')
            wordGenerator()

        else:
            print('\nERROR:\nUSER IS A DUMBASS.\nInvalid input.')
            s(0.75)
            continue


def wordGenerator():  # Begin Word Generation Loop:
    '''Function Responsible for Generating Random Strings.'''

    # Stores the string-converted time format (yyyy-mm-dd hh:mm).
    wordSaveTime = str(ct.now())[:16]

    while True:
        # Loop for users to determine PW length or if they would like to exit the program.
        print(
            '\nEnter the number of random words that you\'d like to generate.')
        passLen = input('Pass Length [Enter 1-30 or \"E\" to Exit]: ').lower()

        try:
            # Restricts valid inputs to be integers within the specified range (1-30 words).
            x = int(passLen)

            if x > 30:
                print('\nThe max number of words is 30.\n')
                continue

            elif x <= 0:
                print(
                    '\nYou have to have at least 1 word. Come on mane. Don\'t do that dumb shit.\n'
                )
                continue

            else:
                # User enters a valid integer/input:
                break

        except:
            # User input is not an integer:

            if passLen == 'e':
                # Prevents blank files from being left behind, as bugs would result.

                # Blank "Saved PWs" file deletion:
                if os.path.exists(
                        r'.\StringGen\generated\allSavedPWs.txt') == True:
                    if len(
                            open(r'.\StringGen\generated\allSavedPWs.txt').
                            readlines()) < 1:
                        os.remove(r'.\StringGen\generated\allSavedPWs.txt')

                        # "Last generated string" file deletion:
                        if os.path.exists(
                                r'.\StringGen\generated\lastgenerated.txt'
                        ) == True:
                            os.remove(
                                r'.\StringGen\generated\lastgenerated.txt')

                load('Exiting Program', 'Good-Bye')
                s(0.75)
                ex(0)

            else:
                print(
                    '\nError: Please enter a number in integer form.\nEntry cannot contain any letters, or punctuation marks (e.g. ,.?!AWf&*ck>y0U_81tcHl@#^)\n'
                )
                continue

    with open(r'.\StringGen\Dictionary\RandomWordDictionary.txt'
              ) as dictionaryFile:  # Opens the random word dictionary file.

        word = [
            words.strip() for words in dictionaryFile
        ]  # List containing all 1.5 million potential words to be generated contained in dictionary.

        word = ' '.join(
            secrets.choice(word)
            for i in range(x)[:30]  # Inserts a space between each word.
        )  # The Word is generated by joining up to 30 randomly-chosen words together.

    dictionaryFile.close(
    )  # Closes File\Resets Buffer\Changes to Documents Take Effect.

    print('\nYour New Generated Word Phrase:\n\n{}'.format(word))

    while True:  # Begin Options to Save, New, or Exit:

        saveOrNah = input(
            '\nWould you like to save this Word? Type "save" or "new", or "exit".\n'
        ).lower()

        if saveOrNah == 'save':  # Save new PW choice:

            if os.path.exists(
                    r'.\StringGen\generated\allSavedPWs.txt') == True:

                pwFileLen = open(
                    r'.\StringGen\generated\allSavedPWs.txt'
                ).readlines(
                )  # opens allsavedPWs.txt and pulls out content into a list.

                if len(
                        pwFileLen
                ) >= 30:  #if the requested generative length is above capacity (30), raise error.

                    print(
                        'ERROR:\nPW file has exceeded capacity. Please delete some to make room.'
                    )

                    saveSlots(
                    )  #Returns to saved pw menu so user may clear space if they wish.

                saveSlots_FH = open(
                    r'.\StringGen\generated\allSavedPWs.txt', 'a'
                )  # File is opened in 'append mode' to add phrase to the end of "allSavedPWs.txt".

                saveSlots_FH.write(
                    'Time Saved: {}\n'.format(wordSaveTime)
                )  # Writes the time of saving word to the document.

                saveSlots_FH.write(
                    '{}\n\n'.format(word)
                )  # Writes the PW below the time saved, and includes a newline.
                saveSlots_FH.close()  # closes allsavedPW file.

                lastGenerated = open(
                    r'.\StringGen\generated\lastgenerated.txt', 'w'
                )  # File Handle opened in 'write' mode to overwrite the last entry inside 'lastGenerated' with the most recent saved PW.
                lastGenerated.write(word)  # Writes the PW
                lastGenerated.close()  # closes LastGenerated file.

                load('Saving to Open Slot', 'Successfully Saved!')

                while True:  # Asks user for next thing to do.

                    again = input(
                        '\nWould you like to:\n1.) Generate another word/phrase?\n2.) View Your Saved Data?\n3.) Exit?\nENTER [1-3] >'
                    ).lower()

                    if again == '1':  # Restarts entire PW generation process.
                        wordGenerator()

                    elif again == '2':  # Loads PW Menu
                        load('Loading Menu', 'Ok!')
                        saveSlots()

                    elif again == '3':  # Exits app
                        load('Exiting Program', 'Good-Bye')
                        s(0.75)
                        ex(0)

                    else:  # User Input Validation Failsafe:
                        print('\nERROR\nUSER IS A DUMBASS.\nInvalid input.')
                        s(0.75)
                        continue

            else:  # No passwords have been saved yet

                saveSlots_FH = open(
                    r'.\StringGen\generated\allSavedPWs.txt',
                    'x')  # Creates/Opens "allsavedPWs.txt" to be written to

                saveSlots_FH.write(
                    'Time Saved: {}\n{}\n\n'.format(wordSaveTime, word)
                )  # Writes the PW below the time saved, and includes a newline.
                saveSlots_FH.close()  # closes/buffers saved PW file.

                # File Handle opened in 'write' mode to overwrite the last entry inside 'lastGenerated' with the most recent generation:
                lastGenerated = open(
                    r'.\StringGen\generated\lastgenerated.txt', 'w')
                lastGenerated.write(word)  # Writes the PW
                lastGenerated.close()  # closes LastGenerated file.
                load('Saving to Open Slot', 'Successfully Saved!')

                while True:  # Asks user for next thing to do:

                    again = input(
                        '\nWould you like to:\n1.) Generate another word/phrase?\n2.) View Your Saved Data?\n3.) Exit?\nENTER [1-3] >'
                    ).lower()

                    if again == '1':  # Restarts entire generation process.
                        wordGenerator()

                    elif again == '2':  # Loads Menu
                        load('Loading Menu', 'Ok!')
                        saveSlots()

                    elif again == '3':  # Exits app
                        load('Exiting Program', 'Good-Bye')
                        s(0.75)
                        ex(0)

                    else:  # User Input Validation Failsafe:
                        print('\nERROR\nUSER IS A DUMBASS.\nInvalid input.')
                        s(0.75)
                        continue

        elif saveOrNah == 'new':  # Restarts Generator Function:
            wordGenerator()

        elif saveOrNah == 'exit':  # Exits app
            load('Exiting Program', 'Good-Bye')
            ex(0)

        else:  # User Input Validation Failsafe:
            print('\nERROR\nUSER IS A DUMBASS.\nInvalid input.')
            s(0.75)
            continue


programStart()  # Begin Program.
