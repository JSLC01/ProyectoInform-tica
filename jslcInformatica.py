# Nombre: Jhon Sebastián Londoño Cárdenas.
# Asignatura: Informática.
# Proyecto final de la asignatura.

import os
import random

def determineSeqType(string):
    """
    Objective: this function determines if a string is a DNA, RNA or none of the previous.
    Input: a string that can be DNA, RNA of something else.
    Output: 1 if it is a DNA string, 2 if it is a RNA string or -1 if it is something different.
    """
    ans = -1 # the variable that stores the answer.
    # If the argument is a string and is not an empty string then go ahead with the process.
    if(type(string) == str and len(string) > 0):
        
        adnBases = ['A', 'T', 'C', 'G'] #Define a list with the bases for the DNA.
        arnBases = ['A', 'U', 'C', 'G'] #Define a list with the bases for the RNA.
        adn = True # boolean value to determine if it is or not DNA string.
        arn = True # boolean value to determine if it is or not RNA string.
        # Go through all the letters.
        for i in string:
            #If the letter is not part of the DNA list then put the boolean variable in False.
            if(i not in adnBases):
                adn = False                
            #If the letter is not part of the RNA list then put the boolean variable in False.
            if(i not in arnBases):
                arn = False
        # if adn = True, then ans is 1.
        if(adn):
            ans = 1
        # if arn = True, then ans is 2.
        elif(arn):
            ans = 2

    return ans

def generateInverted(rnaSeq):
    """
    Objective: takes a RNA sequence and generates the inverted sequence using the agreed rules.
    Input: rnaSeq is a string that contains "A", "U", "C" and "G".
    Output: newRna is the inverted sequence for the input.
    """
    newRna = ""
    for base in rnaSeq:
        if(base == "A"):
            newRna += "C"
        elif(base == "U"):
            newRna += "G"
        elif(base == "C"):
            newRna += "U"
        else:
            newRna += "A"
    
    return newRna


def generateComplement(dnaSeq):
    """
    Objective: takes a DNA sequence and generates the complementary sequence using the agreed rules.
    Input: dnaSeq is a string that contains "A", "T", "C" and "G".
    Output: newDna is the complementary sequence for the input.
    """
    newDna = ""
    for base in dnaSeq:
        if(base == "A"):
            newDna += "T"
        elif(base == "T"):
            newDna += "A"
        elif(base == "C"):
            newDna += "G"
        else:
            newDna += "C"
    
    return newDna


def generateRandomDNA(dnaLen):
    """
    This function creates a random DNA string with lenght
    defined by dnaLen.
    Args:
        dnaLen[int]: Lenght of the desired DNA string.
    Return:
        -1[int]: If lenght < 0.
        dnaString[str]: Randomly generated DNA string.
    """

    if dnaLen < 0:
        return -1

    dnaString = ""

    for i in range(dnaLen):
        randomNumber = random.randint(1, 4)
        if randomNumber == 1:
            dnaString += "A"
        elif randomNumber == 2:
            dnaString += "C"
        elif randomNumber == 3:
            dnaString += "G"
        else:
            dnaString += "T"
    
    return dnaString


def generateRandomRNA(rnaLen):
    """
    This function creates a random RNA string with lenght
    defined by rnaLen.
    Args:
        rnaLen[int]: Lenght of the desired RNA string.
    Return:
        -1[int]: If lenght < 0.
        rnaString[str]: Randomly generated RNA string.
    """

    if rnaLen < 0:
        return -1

    rnaString = ""

    for i in range(rnaLen):
        randomNumber = random.randint(1, 4)
        if randomNumber == 1:
            rnaString += "A"
        elif randomNumber == 2:
            rnaString += "C"
        elif randomNumber == 3:
            rnaString += "G"
        else:
            rnaString += "U"

    return rnaString


def invertOrComplement(genetic_list):
    """
    Objective: Takes the last sequence in genetic_list and generates the complementary sequence if its DNA.
    If its a RNA sequence, the function generates the inverted sequence.
    Input: genetic_list, the list where all sequences are stored.
    Output: the genetic_list modified (the complementary or the inverted sequence is added)
    """
    if(len(genetic_list) > 0):
        if('U' in genetic_list[-1]):
            invertedChain = generateInverted(genetic_list[-1])
            genetic_list.append(invertedChain)
            print("Creation of the Inverted Chain Completed:", invertedChain)
        else:
            complementChain = generateComplement(genetic_list[-1])
            genetic_list.append(complementChain)
            print("Creation of the Complementary Chain Completed:", complementChain)
    else:
        print("Empty List.")
    
    return genetic_list


def compareSequence(genetic_list, pattern, percent):
    """
    Objective: Compare pattern with each element in genetic_list and show the sequences that have a similarity
    equal or greater than percent.
    Input:
        - genetic_list: the list where all the sequences are stored.
        - pattern: the sequence that is going to be compare with each element in the genetic_list.
        - percent: the minimun similarity percentage.
    Output: Nothing is returned.
    """
    countSequences = 0
    for chainPos in range(len(genetic_list)):
        countBases = 0
        if(len(pattern) == len(genetic_list[chainPos])):
            for baseIdx in range(len(genetic_list[chainPos])):
                if(genetic_list[chainPos][baseIdx] == pattern[baseIdx]):
                    countBases += 1
        similarity = countBases / len(pattern)
        if(similarity >= percent):
            countSequences += 1
            print("There is a similar sequence in:", chainPos)

    if(countSequences == 0):
        print("No results found.")


def searchSequence(genetic_list, pattern):
    """
    Objective: searchs the pattern in the genetic_list. If it is in the list show the position, if not show
    a negative message.
    Input: 
        - genetic_list: the list where all the sequences are stored.
        - pattern: the sequence that is going to be seach in the genetic_list.
    Output:
    """
    occurrences = 0
    for chainPos in range(len(genetic_list)):
        if(genetic_list[chainPos] == pattern):
            occurrences += 1
            print("Sequence Found at Position:", chainPos)

    if(occurrences == 0):
        print("No results found.")


def deleteSequence(genetic_list):
    """
    Objective: Deletes the last sequence from the list.
    Input: the list where all the sequence are going to be store.
    Output: returns the genetic list without the last sequence.
    """
    if(len(genetic_list) > 0):
        genetic_list.pop()
        print("Last Sequence Deleted Successfully.")
    else:
        print("ERROR: Empty List.")
    
    return genetic_list


def createSequence(genetic_list):
    """
    Objective: Creates DNA or RNA sequences automatically if indicated by the user. Allows the user to input a sequence manually.
    Input: the list where all the sequence are going to be store.
    Output: returns the genetic list with the new sequence.
    """    
    while True:
        userInput = input("Create sequence automatically? [Y/N] ")
        if(userInput == "Y" or userInput == "y"):
            chainLen = int(input("Please, enter the length of the sequence (min length = 20): "))            

            while True:
                seqType = input("Create DNA or RNA sequence?: ")
                if(seqType == "DNA" or seqType == "dna"):
                    newDNA = generateRandomDNA(chainLen)
                    genetic_list.append(newDNA)
                    print("Sequence Added Successfully:", newDNA)
                    break
                    
                elif(seqType == "RNA" or seqType == "rna"):
                    newRNA = generateRandomRNA(chainLen)
                    genetic_list.append(newRNA)
                    print("Sequence Added Successfully:", newRNA)
                    break

                else:
                    print("Invalid Input.")
            break

        elif(userInput == "N" or userInput == "n"):
            while True:
                userChain = input("Please, enter manually the genetic sequence: ")
                if(determineSeqType(userChain) == -1):
                    print("Invalid Sequence, try again...")
                else:
                    break
            genetic_list.append(userChain)
            print("Sequence Added Successfully:", userChain)
            break

        else:
            print("Invalid Input.")

    return genetic_list


def geneticSequenceMenu(genetic_list):
    """
    Objective: this function displays the genetic sequence menu and contains the logic that request the option to
    the user and directs the user to the selected option.
    Input: Receives the genetic list that is going to be use to store and handle genetic sequences.
    Output:
        - 1: creation of a genetic sequence.
        - 2: delete the last genetic sequence in the list.
        - 3: search a genetic sequence in the list.
        - 4: compare all the sequences in the list with other sequence according to a similarity percentage.
        - 5: Take the last sequence of the list and generates the complementary or inverted sequence.
        - 6: Show all the sequences in the list.
        - 7: Exits the genetic sequence menu.
        Nothing is returned.
    """
    #This cycle ensure correct data entry.
    while True:
        print("""
        ----- Group_name -----
        ----- App_name -----
        ----- Genetic Sequence Menu -----
        1. Create Genetic Sequence.
        2. Delete Genetic Sequence.
        3. Search Genetic Sequence.
        4. Compare Genetic Sequence.
        5. Build Complementary Genetic Sequence.
        6. Display Stored Genetic Sequences.
        7. Go back to the previous menu.
        """)
        try:
            userOperation = int(input("Select an operation from the menu: ")) #Request an option to the user.
        # This exception occurs when the type of the input is not correct.
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the console to avoid too much information on the screen.
            print("The type of the input is not valid. Please, try again.") # Show exception message.
        #If the exception does not occur.
        else:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the console to avoid too much information on the screen.
            # If the user option is of the correct type but not a valid option.
            if(userOperation < 1 or userOperation > 7):
                print("ERROR: Invalid Selection.")
            # Access to the 1st option.
            elif(userOperation == 1):
                createSequence(genetic_list)
            # Access to the 2nd option.
            elif(userOperation == 2):
                deleteSequence(genetic_list)
            # Access to the 3rd option.
            elif(userOperation == 3):
                #This cycle ensure correct data entry.
                while True:
                    patternOp3 = input("Enter the sequence you want to search in the list: ") # Request the pattern we are going to search in the list.
                    # If the pattern is neither DNA nor RNA, then show an error message and ask again.
                    if(determineSeqType(patternOp3) == -1):
                        print("Invalid Sequence, try again...")
                    else:
                        break # If its a valid sequence break the cycle and continue the process.
                searchSequence(genetic_list, patternOp3) # Call the function that contains the logic for the 3rd option.
            # Access to the 4th option.
            elif(userOperation == 4):
                #This cycle ensure correct data entry.
                while True:
                    patternOp4 = input("Enter the sequence you want to compare each element in the list: ")# Request the pattern for the 4th option.
                    # If the pattern is neither DNA nor RNA, then show an error message and ask again.
                    if(determineSeqType(patternOp4) == -1):
                        print("Invalid Sequence, try again...")
                    else:
                        break # If its a valid sequence break the cycle and continue the process.
                #This cycle ensure correct data entry.
                while True:
                    percent = float(input("Enter the minimun similarity percentage (values between 0.0 and 1.0): ")) #Request the minimun similarity percentage.
                    # If the percentage is out of the accepted range, show an error message and ask again.
                    if(percent > 1.0 or percent < 0.0):
                        print("Invalid Percentage.")
                    else:
                        break # If its a valid sequence break the cycle and continue the process.
                compareSequence(genetic_list, patternOp4, percent) # Call the function that contains the logic for the 4th option.
            #Access to the 5th option.
            elif(userOperation == 5):
                invertOrComplement(genetic_list) # Call the function that contains the logic for the 5th option.
            #Access to the 6th option.
            elif(userOperation == 6):
                #If the list is empty, show an error message.
                if(len(genetic_list) == 0):
                    print("The list is empty. There are no elements to display...")
                #If not, show all the sequences in the list.
                else:
                    print("""
                    ----- Sequences in the list ----- 
                    """)
                    for elem in genetic_list:                    
                        print(elem)
            # Access to the 7th option.
            elif(userOperation == 7):
                break # Ends the cycle.

def pressAnyKey(option):
    """
    Objective: If the option selected is between 1 and 4, then displays a message and waits for the user's answer.
    Input: receives the option given by the user.
    Output: nothing is returned.
    """        
    if(option >= 1 and option <= 4):
        input("Press any key to return to the main menu...")

def mainMenu():
    """
    Objective: This function displays the main menu of the app and contains the logic that request data from the
    user and directs the user to the selected option.
    Input: Nothing.
    Output: 
        - 1: information about COVID-19.
        - 2: symptoms of COVID-19.
        - 3: information about SARS-CoV-2.
        - 4: genetic sequence of SARS-CoV-2.
        - 5: Access to the genetic sequence menu.
        - 6: Ends the program.
        Nothing is returned.
    """
    genetic_list = [] # This is the list that is going to store all the genetic sequence created in the app.
    #This cycle ensure correct data entry.
    while True:
        print("""
        ----- Group_name -----
        ----- App_name -----
        ----- Main Menu -----
        1. What is COVID-19?
        2. What symptoms does COVID-19 cause?
        3. What is SARS-CoV-2?
        4. Genetic Sequence of SARS-CoV-2.
        5. Genetic Sequence Analysis.
        6. Close program. 
        """)
        try:    
            userOption = int(input("Welcome. Please, select an option from the previous menu: ")) # Request an option to the user.
        #An exception occurs when the option is different from the expected type,
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the console to avoid too much information on the screen.
            print("The type of the input is not valid. Please, try again.")

        else:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the consolo to avoid too much information on the screen.
            #When the option is of the correct type but not a valid option, show an error message.
            if(userOption < 1 or userOption > 6):
                print("ERROR: Invalid Selection.")
            #Access to the 1st option.
            elif(userOption == 1):
                print("""
            -----------------------------------What is COVID-19?---------------------------------------

            COVID-19 (coronavirus disease 2019) is a disease caused by a virus named SARS-CoV-2.
            It can be very contagious and spreads quickly.

            COVID-19 spreads when an infected person breathes out droplets and very small particles
            that contain the virus. Other people can breathe in these droplets and particles, or 
            these droplets and particles can land on their eyes, nose, or mouth. In some circumstances,
            these droplets may contaminate surfaces they touch.

            Most people infected with the virus will experience mild to moderate respiratory
            illness and recover without requiring special treatment. However, some will become
            seriously ill and require medical attention. Older people and those with underlying
            medical conditions like cardiovascular disease, diabetes, chronic respiratory disease,
            or cancer are more likely to develop serious illness.
                """)
            #Access to the 2nd option.
            elif(userOption == 2):
                print("""
            -------------------------COVID-19 Symptoms-------------------------

            COVID-19 affects different people in different ways. The following
            are some of the main symptoms:

            Most common symptoms:
            -Fever
            -Cough
            -Tiredness
            -Loss of taste or smell.

            Less common symptoms:
            -Sore throat
            -Headache
            -Aches and pains
            -Diarrhoea
            -A rash on skin, or discolouration of fingers or toes
            red or irritated eyes.

            Serious symptoms:
            -Difficulty breathing or shortness of breath
            -Loss of speech or mobility, or confusion
            -Chest pain.
                """)
            #Access to the 3rd option.
            elif(userOption == 3):
                print("""
            ---------------------------------What is SARS-CoV-2?----------------------------------
            
            Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is the virus that causes
            a respiratory disease called coronavirus disease 19 (COVID-19). SARS-CoV-2 is a member
            of a large family of viruses called coronaviruses. It is said that this disease is of
            zoonotic origin (transmision from animal to human).
                """)
            #Access to the 4th option.
            elif(userOption == 4):
                print("""
            ---------------------SARS-CoV-2 Genetic Sequence----------------------

            ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT
            TACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGT
            TTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTCCAATGTTACTTGGTTCCATGCTATACATGTC
            TCTGGGACCAATGGTACTAAGAGGTTTGATAACCCTGTCCTACCATTTAATGATGGTGTTTATTTTGCTT
            CCACTGAGAAGTCTAACATAATAAGAGGCTGGATTTTTGGTACTACTTTAGATTCGAAGACCCAGTCCCT
            ACTTATTGTTAATAACGCTACTAATGTTGTTATTAAAGTCTGTGAATTTCAATTTTGTAATGATCCATTT
            TTGGGTGTTTATTACCACAAAAACAACAAAAGTTGGATGGAAAGTGAGTTCAGAGTTTATTCTAGTGCGA
            ATAATTGCACTTTTGAATATGTCTCTCAGCCTTTTCTTATGGACCTTGAAGGAAAACAGGGTAATTTCAA
            AAATCTTAGGGAATTTGTGTTTAAGAATATTGATGGTTATTTTAAAATATATTCTAAGCACACGCCTATT
            AATTTAGTGCGTGATCTCCCTCAGGGTTTTTCGGCTTTAGAACCATTGGTAGATTTGCCAATAGGTATTA
            ACATCACTAGGTTTCAAACTTTACTTGCTTTACATAGAAGTTATTTGACTCCTGGTGATTCTTCTTCAGG
            TTGGACAGCTGGTGCTGCAGCTTATTATGTGGGTTATCTTCAACCTAGGACTTTTCTATTAAAATATAAT
            GAAAATGGAACCATTACAGATGCTGTAGACTGTGCACTTGACCCTCTCTCAGAAACAAAGTGTACGTTGA
            AATCCTTCACTGTAGAAAAAGGAATCTATCAAACTTCTAACTTTAGAGTCCAACCAACAGAATCTATTGT
            TAGATTTCCTAATATTACAAACTTGTGCCCTTTTGGTGAAGTTTTTAACGCCACCAGATTTGCATCTGTT
            TATGCTTGGAACAGGAAGAGAATCAGCAACTGTGTTGCTGATTATTCTGTCCTATATAATTCCGCATCAT
            TTTCCACTTTTAAGTGTTATGGAGTGTCTCCTACTAAATTAAATGATCTCTGCTTTACTAATGTCTATGC
            AGATTCATTTGTAATTAGAGGTGATGAAGTCAGACAAATCGCTCCAGGGCAAACTGGAAAGATTGCTGAT
            TATAATTATAAATTACCAGATGATTTTACAGGCTGCGTTATAGCTTGGAATTCTAACAATCTTGATTCTA
            AGGTTGGTGGTAATTATAATTACCTGTATAGATTGTTTAGGAAGTCTAATCTCAAACCTTTTGAGAGAGA
            TATTTCAACTGAAATCTATCAGGCCGGTAGCACACCTTGTAATGGTGTTGAAGGTTTTAATTGTTACTTT
            CCTTTACAATCATATGGTTTCCAACCCACTAATGGTGTTGGTTACCAACCATACAGAGTAGTAGTACTTT
            CTTTTGAACTTCTACATGCACCAGCAACTGTTTGTGGACCTAAAAAGTCTACTAATTTGGTTAAAAACAA
            ATGTGTCAATTTCAACTTCAATGGTTTAACAGGCACAGGTGTTCTTACTGAGTCTAACAAAAAGTTTCTG
            CCTTTCCAACAATTTGGCAGAGACATTGCTGACACTACTGATGCTGTCCGTGATCCACAGACACTTGAGA
            TTCTTGACATTACACCATGTTCTTTTGGTGGTGTCAGTGTTATAACACCAGGAACAAATACTTCTAACCA
            GGTTGCTGTTCTTTATCAGGATGTTAACTGCACAGAAGTCCCTGTTGCTATTCATGCAGATCAACTTACT
            CCTACTTGGCGTGTTTATTCTACAGGTTCTAATGTTTTTCAAACACGTGCAGGCTGTTTAATAGGGGCTG
            AACATGTCAACAACTCATATGAGTGTGACATACCCATTGGTGCAGGTATATGCGCTAGTTATCAGACTCA
            GACTAATTCTCCTCGGCGGGCACGTAGTGTAGCTAGTCAATCCATCATTGCCTACACTATGTCACTTGGT
            GCAGAAAATTCAGTTGCTTACTCTAATAACTCTATTGCCATACCCACAAATTTTACTATTAGTGTTACCA
            CAGAAATTCTACCAGTGTCTATGACCAAGACATCAGTAGATTGTACAATGTACATTTGTGGTGATTCAAC
            TGAATGCAGCAATCTTTTGTTGCAATATGGCAGTTTTTGTACACAATTAAACCGTGCTTTAACTGGAATA
            GCTGTTGAACAAGACAAAAACACCCAAGAAGTTTTTGCACAAGTCAAACAAATTTACAAAACACCACCAA
            TTAAAGATTTTGGTGGTTTTAATTTTTCACAAATATTACCAGATCCATCAAAACCAAGCAAGAGGTCATT
            TATTGAAGATCTACTTTTCAACAAAGTGACACTTGCAGATGCTGGCTTCATCAAACAATATGGTGATTGC
            CTTGGTGATATTGCTGCTAGAGACCTCATTTGTGCACAAAAGTTTAACGGCCTTACTGTTTTGCCACCTT
            TGCTCACAGATGAAATGATTGCTCAATACACTTCTGCACTGTTAGCGGGTACAATCACTTCTGGTTGGAC
            CTTTGGTGCAGGTGCTGCATTACAAATACCATTTGCTATGCAAATGGCTTATAGGTTTAATGGTATTGGA
            GTTACACAGAATGTTCTCTATGAGAACCAAAAATTGATTGCCAACCAATTTAATAGTGCTATTGGCAAAA
            TTCAAGACTCACTTTCTTCCACAGCAAGTGCACTTGGAAAACTTCAAGATGTGGTCAACCAAAATGCACA
            AGCTTTAAACACGCTTGTTAAACAACTTAGCTCCAATTTTGGTGCAATTTCAAGTGTTTTAAATGATATC
            CTTTCACGTCTTGACAAAGTTGAGGCTGAAGTGCAAATTGATAGGTTGATCACAGGCAGACTTCAAAGTT
            TGCAGACATATGTGACTCAACAATTAATTAGAGCTGCAGAAATCAGAGCTTCTGCTAATCTTGCTGCTAC
            TAAAATGTCAGAGTGTGTACTTGGACAATCAAAAAGAGTTGATTTTTGTGGAAAGGGCTATCATCTTATG
            TCCTTCCCTCAGTCAGCACCTCATGGTGTAGTCTTCTTGCATGTGACTTATGTCCCTGCACAAGAAAAGA
            ACTTCACAACTGCTCCTGCCATTTGTCATGATGGAAAAGCACACTTTCCTCGTGAAGGTGTCTTTGTTTC
            AAATGGCACACACTGGTTTGTAACACAAAGGAATTTTTATGAACCACAAATCATTACTACAGACAACACA
            TTTGTGTCTGGTAACTGTGATGTTGTAATAGGAATTGTCAACAACACAGTTTATGATCCTTTGCAACCTG
            AATTAGACTCATTCAAGGAGGAGTTAGATAAATATTTTAAGAATCATACATCACCAGATGTTGATTTAGG
            TGACATCTCTGGCATTAATGCTTCAGTTGTAAACATTCAAAAAGAAATTGACCGCCTCAATGAGGTTGCC
            AAGAATTTAAATGAATCTCTCATCGATCTCCAAGAACTTGGAAAGTATGAGCAGTATATAAAATGGCCAT
            GGTACATTTGGCTAGGTTTTATAGCTGGCTTGATTGCCATAGTAATGGTGACAATTATGCTTTGCTGTAT
            GACCAGTTGCTGTAGTTGTCTCAAGGGCTGTTGTTCTTGTGGATCCTGCTGCAAATTTGATGAAGACGAC
            TCTGAGCCAGTGCTCAAAGGAGTCAAATTACATTACACATAA
                """)
            # Access to the 5th option.
            elif(userOption == 5):
                geneticSequenceMenu(genetic_list) #Call the function that displays the genetic sequence menu.
            # Access to the 6th option.
            elif(userOption == 6):
                print("End of the program...") # Displays a program termination message.
                break # Breaks the cycle and end the program.

            pressAnyKey(userOption) # Call the function that displays the "Pres any key" message and waits for the user's answer.
mainMenu() #Call to the main function.