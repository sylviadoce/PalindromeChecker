#
# Sylvia Chin
#
# Tests whether a string is a palindrome (reads forwards and backwards the
    # same regardless of punctuation or white space)
#
# import the graphics library and the Button class
from graphics import *
from Button import Button

def main():

    # Create a graphics window called 'Palindrome Tester' and save it to
        # variable 'win'
    win = GraphWin("Palindrome Tester", 400, 400)

    # Create and draw text to instruct the user to type their word/phrase
    Text(Point(100, 30), "Type your word or phrase in here:").draw(win)
    # Create and draw an Entry box that receives user input in the
        # variable 'test'
    test = Entry(Point(195, 60), 50)
    test.draw(win)

    # Create three buttons to test, retry, and quit the program
    testbutton = Button(win,Point(200,140),80,50,"Test")
    retrybutton = Button(win,Point(200,230),80,50,"Try Another")
    quitbutton = Button(win,Point(200,320),80,50,"Quit")

    # Activate the quit button always
    quitbutton.activate()

    # Create a variable 'testfailed' that keeps track of how many failed tests
    testfailed = 0

    # Create text to display whether it is or is not a palindrome
    result = Text(Point(200, 90), "")
    result.draw(win)

    # Activate the test button
    testbutton.activate()

    # Continue while the number of failed attempts is less than or equal
        # to 3
    while testfailed <= 3:

        # Expect a mouse click in variable 'pt'
        pt = win.getMouse()

        # If the test button is both active/clicked and not failed
        if testbutton.activeandclicked(pt) and testfailed < 3:
            # Get the user's input in the Entry box AFTER the click
            testval = test.getText()

            # If the user input is empty
            if testval == "":
                # Close the window
                win.close()
                # Re-run the program
                main()
            else:
                # Deactivate the test button
                testbutton.deactivate()
                
                # Remove all spaces and punctuation marks using the string
                    # method replace, and replace with an empty string
                testval = testval.replace(" ", "")
                testval = testval.replace("!", "")
                testval = testval.replace("@", "")
                testval = testval.replace("#", "")
                testval = testval.replace("$", "")
                testval = testval.replace("%", "")
                testval = testval.replace("^", "")
                testval = testval.replace("&", "")
                testval = testval.replace("*", "")
                testval = testval.replace("(", "")
                testval = testval.replace(")", "")
                testval = testval.replace("-", "")
                testval = testval.replace("_", "")
                testval = testval.replace("=", "")
                testval = testval.replace("+", "")
                testval = testval.replace(";", "")
                testval = testval.replace(":", "")
                testval = testval.replace("/", "")
                testval = testval.replace("?", "")
                testval = testval.replace(".", "")
                testval = testval.replace(">", "")
                testval = testval.replace(",", "")
                testval = testval.replace("<", "")
                testval = testval.replace("|", "")
                testval = testval.replace("]", "")
                testval = testval.replace("[", "")
                testval = testval.replace("}", "")
                testval = testval.replace("{", "")
                testval = testval.replace("'", "")
                # Use one quotes around the double quote
                testval = testval.replace('"', '')

                # Make each character lowercase
                testval = testval.lower()
                
                # Initialize the total number of characters as 0 in 'numofch'
                numofch = 0
                # Use a for loop to go through each character and add to
                    # character count 'numofch'
                for ch in testval:
                    numofch += 1

                # Check if the number of characters is an even number by 
                    # checking if its remainder when dividing by 2 is 0
                if numofch % 2 == 0:
                    # Find the first half of the string by indexing from the
                        # beginning until half the string length
                    firsthalf = testval[:(len(testval)//2)]
                    # Find the second half of the string by indexing from 
                        # half the string length until the end
                    secondhalf = testval[(len(testval)//2):]

                    # Create an empty list 'reversedlistsecondhalf'
                    reversedlistsecondhalf = []
                    # Set the number of characters to the length of the
                        # second half
                    numofch2 = len(secondhalf)
                    # Keep looping while the number of characters is greater
                        # than 0
                    while numofch2 > 0:
                        # Add the characters of 'secondhalf' backwards to 
                            # the list 'reversedlistsecondhalf'
                        reversedlistsecondhalf += secondhalf[numofch2-1]
                        # Every time reduce the number of characters
                            # remaining so the loop stops when there are no
                            # characters left
                        numofch2 = numofch2 - 1

                    # Create an empty string 'reversedstrsecondhalf'
                    reversedstrsecondhalf = ""
                    # For each item in the list 'reversedlistsecondhalf'
                    for i in reversedlistsecondhalf:
                        # Add each to the string so it's now a string
                        reversedstrsecondhalf += i

                    # If the first half is the same as the second half
                        # reversed
                    if firsthalf == reversedstrsecondhalf:
                        # Change the text to let the user know it was a
                            # successful palindrome
                        result.setText("This IS a palindrome!")
                        # Reset the 'testfailed' counter to 0
                        testfailed = 0
                        # Activate the try again button
                        retrybutton.activate()
                    # If the first half is not the same as the second half
                        # reversed
                    else:
                        # Change the text to let the user know it was not
                            # a successful palindrome
                        result.setText("This is NOT a palindrome. Try again.")
                        # Add 1 to the 'testfailed' counter
                        testfailed += 1
                        # Activate the try again button
                        retrybutton.activate()

                # Check if the number of characters is an odd number by 
                    # checking if its remainder when dividing by 2 is not 0      
                else:
                    # Find the first half of the string by indexing from the
                        # beginning until half the string length
                    firsthalf = testval[:(len(testval)//2)]
                    # Find the second half of the string by indexing from 
                        # half the string length until the end
                    secondhalf = testval[(len(testval)//2)+1:]

                    # Create an empty list 'reversedlistsecondhalf'
                    reversedlistsecondhalf = []
                    # Set the number of characters to the length of the
                        # second half
                    numofch2 = len(secondhalf)
                    # Keep looping while the number of characters is greater
                        # than 0
                    while numofch2 > 0:
                        # Add the characters of 'secondhalf' backwards to 
                            # the list 'reversedlistsecondhalf'
                        reversedlistsecondhalf += secondhalf[numofch2-1]
                        # Every time reduce the number of characters
                            # remaining so the loop stops when there are no
                            # characters left
                        numofch2 = numofch2 - 1
                    
                    # Create an empty string 'reversedstrsecondhalf'
                    reversedstrsecondhalf = ""
                    # For each item in the list 'reversedlistsecondhalf'
                    for i in reversedlistsecondhalf:
                        # Add each to the string so it's now a string
                        reversedstrsecondhalf += i

                    # If the first half is the same as the second half
                        # reversed
                    if firsthalf == reversedstrsecondhalf:
                        # Change the text to let the user know it was a
                            # successful palindrome
                        result.setText("This IS a palindrome!")
                        # Reset the 'testfailed' counter to 0
                        testfailed = 0
                        # Activate the try again button
                        retrybutton.activate()
                    # If the first half is not the same as the second half
                        # reversed
                    else:
                        # Change the text to let the user know it was not
                            # a successful palindrome
                        result.setText("This is NOT a palindrome. Try again.")
                        # Add 1 to the 'testfailed' counter
                        testfailed += 1
                        # Activate the try again button
                        retrybutton.activate()

        # If the try again button is both active and clicked
        if retrybutton.activeandclicked(pt):
            # Deactivate the try again button
            retrybutton.deactivate()
            # Change the result text to an empty string
            result.setText("")
            # Change the entry box text to an empty string
            test.setText("")
            # Activate the test button
            testbutton.activate()

        # If the user fails three times in a row, close the window
        if testfailed == 3:
            # Deactivate the try again button
            retrybutton.deactivate()
            # Deactivate the test button
            testbutton.deactivate()
            # Change the result text to let the user know they need to quit
            result.setText("3 failed attempts. Click 'Quit' to Quit.")

        # If at any time the quit button is clicked, close the window
        if quitbutton.clicked(pt):
            win.close()

# run the main function
main()
