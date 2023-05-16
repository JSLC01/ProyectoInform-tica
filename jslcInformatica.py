# Nombre: Jhon Sebastián Londoño Cárdenas.
# Asignatura: Informática.
# Proyecto final de la asignatura:
import os
import random

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

def deleteSequence(genetic_list):
    if(len(genetic_list) > 0):
        genetic_list.pop()
        print("Last Sequence Deleted Successfully.")
    else:
        print("ERROR: Empty List.")
    
    return genetic_list

#c = ["ACGTACGTACGT", "ACGUACGU", "ACGT"]

def createSequence(genetic_list):
    userInput = input("Create sequence automatically? [Y/N] ")
    if(userInput == "Y" or userInput == "y"):
        chainLen = int(input("Please, enter the length of the sequence (min length = 20)"))
        seqType = input("Create DNA or RNA sequence?: ")
        if(seqType == "DNA" or seqType == "dna"):
            newDNA = generateRandomDNA(chainLen)
            genetic_list.append(newDNA)
            print("Sequence Added Successfully:", newDNA)
            
        elif(seqType == "RNA" or seqType == "rna"):
            newRNA = generateRandomRNA(chainLen)
            genetic_list.append(newRNA)
            print("Sequence Added Successfully:", newRNA)

        else:
            print("Invalid sequence type selected.")

    elif(userInput == "N" or userInput == "n"):
        userChain = input("Please, enter manually the genetic sequence: ")
        genetic_list.append(userChain)
        print("Sequence Added Successfully:", userChain)

    else:
        print("Invalid option.")

    return genetic_list


def geneticSequenceMenu(genetic_list):
    while True:
        print("""
        ----- Group_name-----
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
            userOperation = int(input("Select an operatio from menu: "))

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("The type of the input is not valid. Please, try again.")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if(userOperation < 1 or userOperation > 7):
                print("ERROR: Invalida Selection.")
            elif(userOperation == 1):
                print("loquesea")
            elif(userOperation == 2):
                print("loquesea")
            elif(userOperation == 3):
                print("loquesea")
            elif(userOperation == 4):
                print("loquesea")
            elif(userOperation == 5):
                print("loquesea")
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
            
            Severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2) is the virus that causes
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
                print("Aquí va lo de la 5")

            elif(userOption == 6):
                print("\n")
                print("\n")
                print("End of the program...")
                break
            pressAnyKey(userOption)
#mainMenu()

