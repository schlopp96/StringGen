#!/usr/bin/env python3

#! Random-String-Generation CLI Tool
#TODO: Begin GUI development.
#TODO: Continue to work on new ideas.
#?+++++++++++++++++++++++++++++Libraries/Modules+++++++++++++++++++++++++++++?#
import secrets
from datetime import datetime as ct
from os import chdir as cwd
from os import remove, rename
from os.path import dirname as curFolder
from os.path import exists, abspath as getAbsPath
from sys import exit as ex
from time import sleep as s
from typing import Any, NoReturn

from PyLoadBar import load

#~ Set Program Directory
cwd(curFolder(curFolder(__file__)))

#?+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?#

__version__ = '0.8.0a'


#!+++++++++++++++++++++++++++++++++Functions+++++++++++++++++++++++++++++++++!#
def programStart() -> None:
    """
    Begin program start-up sequence.

    - Displays Current time Using (yyy-mm-dd hh:mm:ss) Format.
    - Displays Welcome Message.
    - Starts Application.
    :return: start-up sequence of program path.
    :rtype: Any | NoReturn
    """
    print(f'\nWelcome to StringGen v{__version__}\n')
    print(f'The Current Time Is:\n{ct.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


def get_LastGenerated() -> Any | NoReturn:
    """Prompt whether to return most recently saved string or continue to generator.

    :return: display contents of ".\generated\lastgenerated.txt" if able and/or continue to random string generator.
    :rtype: Any | NoReturn
    """

    #? Checks for/opens existing "last generated" file:
    try:
        if exists(r'.\generated\lastgenerated.txt'):
            lastGenerated: str = open(r'.\generated\lastgenerated.txt').read()

            while True:
                q_lastGenerated = input(
                    'Would you like to see your most recent saved entry? Y/N?\n> '
                )

                #* Yes:
                if q_lastGenerated.lower().startswith('y'):
                    load('Loading recently saved string', 'Ready...!')
                    print(
                        f'\nYour last saved string is {(len(lastGenerated))} characters long:\n{lastGenerated}'
                    )
                    break

                #! No:
                elif q_lastGenerated.lower().startswith('n'):
                    break

                #& Error/Invalid:
                else:
                    print(
                        '\nERROR:\nInvalid Input. Acceptable choices are:\n- "y" or "yes"\n- "n" or "no".\n'
                    )
                    s(1)
                    continue
        else:
            load('Loading String Generator', progressbar=False)
            return stringGenerator()

        load('\nLoading Menu', progressbar=False)
        return globalMenu()

    except FileNotFoundError:
        replaceFile = open(r'.\generated\lastgenerated.txt', 'x')
        replaceFile.close()
        print(
            '\nNo recently generated string detected.\nContinuing to random string generator.'
        )
        return stringGenerator()


def viewSaved_menu() -> None:
    """Displays options for editing saved strings.

    :return: menu listing all available slots/options.
    :rtype: None
    """

    print('\n', end='')
    print(7 * "-", "StringGen MENU", 7 * "-", "\n", end='')
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
    print(30 * "-")


def deleteAll() -> Any:
    """Delete all saved strings from containing file.

    :return: File containing saved strings will be cleared entirely.
    :rtype: Any
    """
    while True:
        print(
            '\nWARNING!\nTHIS ACTION CANNOT BE UNDONE. IF YOU CHOOSE TO CLEAR ALL PWs, THEY WILL BE GONE FOREVER AND EVER.'
        )
        amSure: str = input('\nARE YOU SURE? Y/N: ').lower()
        if str(amSure).startswith('y'):
            #! Deletes both recently saved, and last-generated pw files:
            #* Checks for saved entry list & deletes upon discovery:
            if exists(r'.\generated\saveslots.txt') == True:
                remove(r'.\generated\saveslots.txt')
            #* Checks for "recently generated" list & deletes upon discovery:
            if exists(r'.\generated\lastgenerated.txt') == True:
                remove(r'.\generated\lastgenerated.txt')
            load('\nClearing Saved Strings',
                 'All Strings Deleted Successfully!')
            return stringGenerator()
        elif str(amSure) == 'n':
            return view_saved()
        else:
            print('\nERROR:\nMUST ENTER ONLY "Y" or "N".')
            s(0.75)
            continue


def view_saved() -> Any:  # sourcery no-metrics
    """Process menu operations to view/modify saved strings and handle user input.

    :return: operations chosen by user
    :rtype: Any
    """

    while True:
        #? open "saveslots.txt" as a list of every line within file:
        saveSlots_FH = open(r'.\generated\saveslots.txt', 'r+').readlines()

        viewSaved_menu()
        menuChoice: str = input(
            'Enter [1-13] to make a selection, or enter "done" when finished.\n> '
        )
        try:
            #! Slot 1
            if menuChoice == '1':
                print(f'\nSave Slot 1:\n{saveSlots_FH[1]}')
                while True:
                    print(
                        'Press [ENTER] to continue, or type \"delete\" to erase slot.'
                    )

                    userChoice = input('> ').lower()

                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt', [0, 1, 2])

                        #& Deletes most recently generated string if saveslots.txt is empty.
                        if len(open(r'.\generated\saveslots.txt').read()) < 1:
                            remove(r'.\generated\lastgenerated.txt')
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

                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt', [3, 4, 5])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt', [6, 7, 8])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [9, 10, 11])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [12, 13, 14])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [15, 16, 17])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [18, 19, 20])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [21, 22, 23])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [24, 25, 26])
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
                    if userChoice.startswith('del') or userChoice == 'delete':
                        deleteFL(r'.\generated\saveslots.txt',
                                      [27, 28, 29])
                    break
                continue

            #^ Generate new string:
            elif menuChoice == '11':  #& Returns the Random Generator Function.
                load('\nLoading', 'Ok!', False)
                return stringGenerator()

            #* Return all occupied save-slots:
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

                    input('\nPress [ENTER] to continue.\n')
                    continue

                #& Display message when total saved strings < 10 and all existing saved strings have been returned:
                except IndexError:
                    print(
                        '\nFinished Loading Saved Strings!\nAll Remaining Save Slots Empty.\n'
                    )
                    input('\nPress [ENTER] to continue.\n')
                    continue

            #! DELETE ALL SAVED STRINGS:
            elif menuChoice == '13':
                deleteAll()

            elif menuChoice.lower() == 'done':
                #* Once done with the PW Menu, program moves on to PW gen function.
                load('\nLoading PW Generator', 'Done!')
                return stringGenerator()

            elif not menuChoice:
                print('\nERROR:\nBlank input - Must enter valid option.')
                s(1)

            else:
                print(f'\nERROR:\nInvalid input: {menuChoice}.')
                s(0.75)
                continue

        except IndexError:
            #! Return following string if request to load empty PW slot is called:
            print(f'\nERROR\nSave slot {menuChoice} is empty.')
            s(0.75)
            continue


def stringGenerator() -> Any:
    """Generate string consisting of up to 50 randomly-chosen words.

    - All available words are pulled from a dictionary file which contains over 1.5 MILLION words.
    - :return: pre-determined length of random words combined into a single string.
    - :rtype: Any
    """

    while True:
        q_strLen = input(
            '\nEnter the number of random words that you\'d like to generate.\nString Length [Enter 1-50 or \"E\" to Exit]: '
        )
        try:
            strLen: int = int(q_strLen)

            #! Restricts valid inputs to be integers within the specified range (1-30 words):
            if strLen > 50:
                print('\nThe max number of words is 50 words.')
                continue

            elif strLen <= 0:
                print(
                    '\nYou have to have at least 1 word. Come on man, you\'re messing with me, aren\'t you?\nStop it!'
                )
                continue

            #* Valid integer/input entry:
            else:
                break

        except ValueError:
            if q_strLen.lower() in ['e', 'exit']:
                cleanup(mode='full')

            else:
                print(
                    '\nERROR: Please enter a number in integer form.\nEntry cannot contain any letters, or punctuation marks (e.g. ,.?!AWf&*ck>y0U_81tcHl@^#)'
                )
                s(1)
                continue

    with open(r'.\Dictionary\RandomWordDictionary.txt') as dictionary:
        strList: list = [words.strip() for words in dictionary]
        str_FINAL: str = ' '.join(secrets.choice(strList) for _ in range(strLen)[:50])

    print(f'\nYour New Generated String:\n\n{str_FINAL}')
    return save_prompt(str_FINAL)


def save_prompt(string):
    """Prompt user whether or not to save latest generated string.

    :param string: string to save.
    :type string: str
    :return: save string or return to string generator.
    :rtype: Any
    """
    while True:  #? Begin Options to Save, New, or Exit:
        q_saveStr = input(
            '\nWould you like to save this Word?\nENTER "save", "new", or "exit" > '
        ).lower()

        if q_saveStr.startswith('save'):

            if exists(r'.\generated\saveslots.txt'):

                saveSlots_FL = open(r'.\generated\saveslots.txt').readlines(
                )  #? opens saveslots.txt and pulls out content into a list.

                #! If "saveslots.txt" is above capacity (30 lines), raise error:
                if len(saveSlots_FL) >= 30:
                    print(
                        '\nERROR:\nSave slots full. Please clear a slot to make some room.'
                    )
                    s(1)
                    #* Returns to saved pw menu so user may clear space if they wish.
                    return view_saved()

                #* Add result to both "saved" & "last generated" docs:
                saveSlots_FH = open(r'.\generated\saveslots.txt', 'a')
            else:
                saveSlots_FH = open(r'.\generated\saveslots.txt', 'x')
            saveSlots_FH.write(
                f'Time Saved: {ct.now().strftime("%Y-%m-%d %H:%M:%S")}\n{string}\n\n'
            )
            saveSlots_FH.close()
            with open(r'.\generated\lastgenerated.txt', 'w') as lastGenerated:
                lastGenerated.write(string)
            load('\nSaving to Open Slot', 'Successfully Saved!')

            return globalMenu()

        elif q_saveStr == 'new':
            return stringGenerator()

        elif q_saveStr == 'exit':
            return cleanup(mode='light')

        else:
            print('\nERROR\nInvalid input.')
            s(0.75)
            continue


def globalMenu() -> Any | NoReturn:
    """Ask user to choose next task.

    - Select option "1" to generate a new string.
    - Select option "2" to view/edit saved strings.
    - Select option "3" to exit the program.

    :return: user prompt to select next task from menu options or exit program.
    :rtype: Any | NoReturn
    """
    while True:
        user_inp: str = input(
            '_____________________________________\n| Would you like to:                |\n| 1.) Generate another word/phrase? |\n| 2.) View Your Saved Data?         |\n| 3.) Exit?                         |\n|___________________________________|\n\nENTER [1-3] > '
        ).lower()

        match user_inp:

            case '1':
                return stringGenerator()

            case '2':
                load('\nLoading Menu', 'Ok!', False)
                return view_saved()

            case '3':
                load('\nExiting Program', 'Good-Bye', False)
                s(0.75)
                return ex(0)

            case '':
                print('\nERROR:\nBlank input - Must enter valid option.')
                s(0.75)

            case _ :
                print(f'\nERROR\nInvalid input: "{user_inp}"')
                s(0.75)


def cleanup(mode: str = None) -> NoReturn:
    """Ensure any temporary or leftover files are cleaned up and restore appropriate directory states before exiting.

    Parameters:
        :param mode: the extensiveness of file-deletion/restoration to be done.
        :type mode: str
            - `if mode == "full":`
                - Check for both "saveslots.txt" and "lastgenerated.txt":
                    - 1). if "saveslots.txt" DOES exist:
                        - if "saveslots.txt" is blank:
                            - DELETE "saveslots.txt" AND "lastgenerated.txt"
                        - if ANY entries exist within "saveslots.txt":
                            - nothing is changed.
                            - exit program.
                    - 2). If "saveslots.txt" DOES NOT exist:
                        - ensure that there is NO "lastgenerated.txt" file, and delete if found
                        - exit program.
            - `if mode == "light":`
                - Check for existence of "saveslots.txt" file:
                    - 1). If file does NOT exist:
                        - delete "lastgenerated.txt"
                        - exit program.
                    - 2). If file DOES exist:
                        - nothing is changed
                        - exit program.
        :return: deletes temporary/leftover/unneeded files from program directories to prevent fatal errors before exiting program.
        :rtype: NoReturn
    """
    #~ Delete both "saveslots.txt" and "lastgenerated.txt", if former is empty.
    if mode not in ['full', 'light']:
        raise ValueError(
            f'\nERROR:\nInvalid *args choice - "{mode}".\nMust set parameter to "full" or "light" only.\n'
        )
    elif mode == 'full':
        #& Check for existence of "saveslots.txt" file, and deletes if blank:
        if exists(r'.\generated\saveslots.txt') == True:
            if len(open(r'.\generated\saveslots.txt').readlines()) < 1:
                remove(r'.\generated\saveslots.txt')

                #! Delete "lastgenerated.txt".
                if exists(r'.\generated\lastgenerated.txt') == True:
                    remove(r'.\generated\lastgenerated.txt')

        #& Check for existence of "saveslots.txt" file, and ensures "lastgenerated.txt" is also deleted:
        elif exists(r'.\generated\saveslots.txt') == False:
            if exists(r'.\generated\lastgenerated.txt') == True:
                remove(r'.\generated\lastgenerated.txt')

    elif mode == 'light':
        if (exists(r'.\generated\saveslots.txt') == False
                and exists(r'.\generated\lastgenerated.txt') == True):
            remove(r'.\generated\lastgenerated.txt')

    load('\nPreparing to close program', 'Goodbye!', False)
    ex()


def deleteFL(file_ORIGINAL: str, line_numbers: list) -> None:
    """Delete specific line-numbers from a *.txt document.

    - Make sure to include either DOUBLE SLASH MARKS, or a RAW-STRING LITERAL upon assigning `file_ORIGINAL (str)` parameter.
    - Examples of correct usage:
        - Absolute path with raw string literal:
            - >>> `delLines(r'c:/Users/Desktop/textfile.txt', [0, 1, 2])`
        - Relative path with escape characters
            - >>> `delLines(r'.//desktop//textfile.txt', [0, 1, 2])`

    - Lists have a starting index of ZERO.
    - Inclusive.
    - Example of correct usage:
        - >>> `del_FileLines(file_ORIGINAL, [0, 1, 2])`
            - This would delete the first three lines from the document `file_ORIGINAL`.

    Parameters:
    :param file_ORIGINAL: filepath of the document you wish to edit. Can be absolute or relative.
    :type file_ORIGINAL: str
    :param line_numbers: line numbers to delete.
    :type line_numbers: list
    :return: copy of `file_ORIGINAL` with predetermined line numbers removed.
    :rtype: None

    """

    #@ Success/Error flag:
    success: bool = True

    print("\nValidating file location...")
    s(1.25)

    #! File not found:
    if not exists(getAbsPath(file_ORIGINAL)):
        raise FileNotFoundError(
            f'"{file_ORIGINAL}" cannot be found, or does not exist.\nPlease check your spelling, ensure that the file extension and\or syntax is correct, then try again.\n'
        )

    print(f'Successfully validated "{getAbsPath(file_ORIGINAL)}"!\n')
    s(0.75)

    #* Create identical copy of original for modifying:
    file_TEMP: str = f'file_ORIGINAL{".bak"}'
    is_skipped: bool = False
    line_count: int = 0
    with open(file_ORIGINAL, 'r') as file_READ, open(file_TEMP,
                                                     'w') as file_WRITE:
        for line in file_READ:
            if line_count not in line_numbers:
                file_WRITE.write(line)
            else:
                is_skipped = True
            line_count += 1

    load(
        f'Deleting lines {line_numbers}...\n',
        f'-    Done!    -\n\nSuccessfully removed lines: {line_numbers}\nfrom document: "{getAbsPath(file_ORIGINAL)}".\n'
    )
    s(1.25)

    if is_skipped:  #^ OVERWRITE file_ORIGINAL with file_TEMP contents.
        remove(file_ORIGINAL)
        return rename(file_TEMP, file_ORIGINAL)
    else:  #^ Delete file_TEMP, do not overwrite file_ORIGINAL.
        return remove(file_TEMP)


def main():
    programStart()
    get_LastGenerated()


if __name__ == '__main__':
    main()
