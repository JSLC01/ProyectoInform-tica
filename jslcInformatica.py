# Nombre: Jhon Sebastián Londoño Cárdenas.
# Asignatura: Informática.
# Proyecto final de la asignatura.

import os
import random
#Jhon Sebastián Londoño Cárdenas.
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
    """This function creates a random DNA string with lenght
    defined by dnaLen.
    Args:
        dnaLen[int]: Lenght of the desired DNA string.
    Return:
        -1[int]: If lenght < 0.
        dnaString[str]: Randomly generated DNA string."""

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
    """This function creates a random RNA string with lenght
    defined by rnaLen.
    Args:
        rnaLen[int]: Lenght of the desired RNA string.
    Return:
        -1[int]: If lenght < 0.
        rnaString[str]: Randomly generated RNA string."""

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

#c = ["ACGT", "ACGUACGU"]
#print(invertOrComplement(c))

def compareSequence(genetic_list, pattern, percent):
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
    occurrences = 0
    for chainPos in range(len(genetic_list)):
        if(genetic_list[chainPos] == pattern):
            occurrences += 1
            print("Sequence Found at Position:", chainPos)

    if(occurrences == 0):
        print("No results found.")


def deleteSequence(genetic_list):
    if(len(genetic_list) > 0):
        genetic_list.pop()
        print("Last Sequence Deleted Successfully.")
    else:
        print("ERROR: Empty List.")
    
    return genetic_list


def createSequence(genetic_list):    
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
            userOperation = int(input("Select an operation from the menu: "))

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("The type of the input is not valid. Please, try again.")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if(userOperation < 1 or userOperation > 7):
                print("ERROR: Invalid Selection.")
            elif(userOperation == 1):
                createSequence(genetic_list)
            elif(userOperation == 2):
                deleteSequence(genetic_list)
            elif(userOperation == 3):
                while True:
                    patternOp3 = input("Enter the sequence you want to search in the list: ")
                    if(determineSeqType(patternOp3) == -1):
                        print("Invalid Sequence, try again...")
                    else:
                        break
                searchSequence(genetic_list, patternOp3)
            elif(userOperation == 4):
                while True:
                    patternOp4 = input("Enter the sequence you want to compare each element in the list: ")
                    if(determineSeqType(patternOp4) == -1):
                        print("Invalid Sequence, try again...")
                    else:
                        break
                while True:
                    percent = float(input("Enter the minimun similarity percentage (values between 0.0 and 1.0): "))
                    if(percent > 1.0 or percent < 0.0):
                        print("Invalid Percentage.")
                    else:
                        break
                compareSequence(genetic_list, patternOp4, percent)
            elif(userOperation == 5):
                invertOrComplement(genetic_list)
            elif(userOperation == 6):
                if(len(genetic_list) == 0):
                    print("The list is empty. There are no elements to display...")
                else:
                    print("""
                    ----- Sequences in the list ----- 
                    """)
                    for elem in genetic_list:                    
                        print(elem)

            elif(userOperation == 7):
                break

def pressAnyKey(option):
    if(option >= 1 and option <= 4):
        input("Press any key to return to the main menu...")

def mainMenu():
    genetic_list = []
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
            userOption = int(input("Welcome. Please, select an option from the previous menu: "))

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("The type of the input is not valid. Please, try again.")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')

            if(userOption < 1 or userOption > 6):
                print("ERROR: Invalid Selection.")
            
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

            elif(userOption == 3):
                print("""
            ---------------------------------What is SARS-CoV-2?----------------------------------
            
            Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is the virus that causes
            a respiratory disease called coronavirus disease 19 (COVID-19). SARS-CoV-2 is a member
            of a large family of viruses called coronaviruses. It is said that this disease is of
            zoonotic origin (transmision from animal to human).
                """)

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

            elif(userOption == 5):
                geneticSequenceMenu(genetic_list)

            elif(userOption == 6):
                print("End of the program...")
                break

            pressAnyKey(userOption)
mainMenu()