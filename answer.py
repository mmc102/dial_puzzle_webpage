import os

with open("words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)
vowels = set('aeiou')
def is_english_word(word):
    return word.lower() in english_words

not vowels.isdisjoint('bcd')
        


print is_english_word("ham")
dial_1 = 'twtmactnwbtof'
dial_2 = 'uonihehonahai'
dial_3 = 'relisdlovttle'
dial_4 = 'nipsgcstpiuih'
dial_5 = 'taolhebggiofe'
dial_6 = 'hanwtrttmaarr'
dial_7 = 'ebzpatttwtsae'
dial_8 = 'tsehehokksyal'
dial_9 = 'apebeneearree'
dial_10 = 'bmaelidxysame'
dial_11 = 'lnoioytigaubp'
dial_12 = 'ettunuohnirso'
dial_13 = 'sgrusdnstwroh'
#two part list, string of the dial and its position
init_dials = [[dial_1,0],[dial_2,0],[dial_3,0],[dial_4,0],[dial_5,0],[dial_6,0],[dial_7,0],[dial_8,0],[dial_9,0],[dial_10,0],[dial_11,0],[dial_12,0],[dial_13,0]]
#dial_positions = [0,0,0,0,0,0,0,0,0,0,0,0,0]

#the number of words each row needs to generate (provided from the puzzle)
num_words_per_row = [2,3,2,2,2,2,3,2,4,4,3,4]


#takes the dials and aligns them based on their positon
def read_the_dials(list1): 
    aligned_dials = []  
    for dial in list1:
        aposition = dial[1]
        aligned_dials.append(dial[0][-aposition:] + dial[0][:-aposition])
    current_dial_reading = []
    the_range = list(range(0,13))
    for position in the_range:
            temp_answer = ''
            for dial in aligned_dials:
                temp_answer = temp_answer + dial[position]
            current_dial_reading.append(temp_answer)   
    return current_dial_reading

def incriment_the_dials(list1):   
    if list1[1][1] <=11:
        list1[1][1] += 1
    
    else: 
        #list1[2][1] += 1
        list1[1][1] = 0
    
        if list1[2][1] <=11:
            list1[2][1] += 1
        
        else: 
            #list1[3][1] += 1
            list1[2][1] = 0

            if list1[3][1] <=11:
                list1[3][1] += 1
            
            else: 
                #list1[4][1] += 1
                list1[3][1] = 0
            
                if list1[4][1] <=11:
                    list1[4][1] += 1
                
                else: 
                    #list1[5][1] += 1
                    list1[4][1] = 0
                
                    if list1[5][1] <=11:
                        list1[5][1] += 1
                    
                    else: 
                        #list1[6][1] += 1
                        list1[5][1] = 0

                        if list1[6][1] <=11:
                            list1[6][1] += 1
                        
                        else: 
                            #list1[7][1] += 1
                            list1[6][1] = 0

                            if list1[7][1] <=11:
                                list1[7][1] += 1
                            
                            else: 
                                #list1[8][1] += 1
                                list1[7][1] = 0

                                if list1[8][1] <=11:
                                    list1[8][1] += 1
                                
                                else: 
                                    #list1[9][1] += 1
                                    list1[8][1] = 0

                                    if list1[9][1] <=11:
                                        list1[9][1] += 1
                                    
                                    else: 
                                        #list1[10][1] += 1
                                        list1[9][1] = 0

                                        if list1[10][1] <=11:
                                            list1[10][1] += 1
                                        
                                        else: 
                                           # list1[11][1] += 1
                                            list1[10][1] = 0

                                            if list1[11][1] <=11:
                                                list1[11][1] += 1
                                            
                                            elif list1[12][1] <=11:
                                                list1[12][1] += 1
                    

   # blah= []
   # for i in list1:
    #    blah.append(i[1])
        
   #print(blah)
    return list1

def check_for_words(list1,two_word_row_to_check,orientations_to_check):
    successful_dial_orientations = []
    counter_one = 0
    if orientations_to_check == []:
        while list1[12][1] <= 12:  #make this while the "odometer" is not maxed out 
            
            row_to_check = read_the_dials(list1)[two_word_row_to_check]
            length_of_words = list(range(1,13))
            
            
            for i in length_of_words:
                first_word =row_to_check[:i]
                second_word =row_to_check[-(13-i):]
                
                #print(first_word,second_word)
                #check for vowels in the word, if none, then skip this word
                if not vowels.isdisjoint(first_word):
                    if not vowels.isdisjoint(second_word):
                        #checks the dictionary for the words 
                        if is_english_word(first_word):

                            if is_english_word(second_word):
                                print('found combination in this dial orintation 1 ')
                               # print(first_word,second_word)
                                successful_dial_orientations.append(list1)
                                print(len(successful_dial_orientations),'out of', counter_one)
                        
            
        
            list1 = incriment_the_dials(list1)
            counter_one += 1
            
        return successful_dial_orientations 
    else:
        for i in orientations_to_check:
            row_to_check = read_the_dials(orientations_to_check[i])[two_word_row_to_check]  #make me better. basically check the lists that pass the first critera 
            length_of_words = list(range(1,13))
            
            
            for i in length_of_words:
                first_word =row_to_check[:i]
                second_word =row_to_check[-(13-i):]
                if is_english_word(first_word):

                    if is_english_word(second_word):
                        print('found combination in this dial orintation SMALLER LIST ')
                       # print(first_word,second_word)
                        successful_dial_orientations.append(list1)
                        print(len(successful_dial_orientations))
        
            list1 = incriment_the_dials(list1)
        #print('hi')

        #add a thing here that only checks the dial positions for the values in "orientations to check "

idx_rows_with_two_words = [0,2,3,4,5,7]


viable_orientations = [[],]   #used to record the successful orientations of the dials and pass them back into the check function
counter = 0                            # to be checked against the next step. maybe make a list of a list to only check the latest entry
for i in idx_rows_with_two_words:
    viable_orientations.append(check_for_words(init_dials,i,viable_orientations[0]))
    counter +=1
    



#check the first two word row for all possible combiations that yield two words 
    #i think you need to actually check all combos, but maybe there is an optimization you can do once you find one word
    #map the locations of the dials at the positions that "pass" the first condition 

#check the passes from the first "two line" check for words in the next two line row  
    #map these successes again, elimiating the failure. 

