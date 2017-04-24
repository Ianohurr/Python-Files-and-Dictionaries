'''
Author: Ian O'Heir
Date: 4/20/2017
Class: ISTA 130
Section Leader: Adrianna

Description:
Write a dictionary program that counts the amount of times emoticons occurred in various tweets
'''



#==========================================================
def load_emoticons_to_ids(emoticon_dict, emoticon_data):
    '''
    This function loads the emoticon data into an id dictionary
    
    Parameters:
    emoticon_dict:a dictionary for the fish
    emoticon_data: the file containing all the fish data

    
    
    Returns: none
    '''
    f = open(emoticon_data)
    for line in f:
        line=line.replace('"', '')
        line = line.strip().split()
        if line[0] not in emoticon_dict:
            emoticon_dict[line[0]]=[]
            emoticon_dict[line[0]].append((line[2]))
        else:
            if (line[2]!="NA"):
                emoticon_dict[line[0]].append((line[2]))
    f.close()

def load_ids_to_emoticons(emoticon_dict, emoticon_data):
    '''
    This function loads the id data into an emoticon dictionary
    
    Parameters:
    emoticon_dict:a dictionary for the fish
    emoticon_data: the file containing all the fish data

    
    
    Returns: none
    '''
    f = open(emoticon_data)
    for line in f:
        line=line.replace('"', '')
        line = line.strip().split()
        if line[2] not in emoticon_dict:
            emoticon_dict[line[2]]=[]
            emoticon_dict[line[2]].append((line[0]))
        else:
            if (line[0]!="NA"):
                emoticon_dict[line[2]].append((line[0]))
    f.close()
    
    
def load_twitter_dicts_from_file(file,emoticons_to_ids,ids_to_emoticons):
    '''
    This function accepts a file with twitter data
    
    Parameters:
    file: twitter data
    emoticons_to_ids: an empty dictionary
    ids_to_emoticons: an empty dictionary

    
    
    Returns: none
    '''
    load_emoticons_to_ids(emoticons_to_ids,file)
    load_ids_to_emoticons(ids_to_emoticons,file)
    
def find_most_common(dictionary):
    '''
    This function finds the most common emoticon
    
    Parameters:
    dictionary: a filled dictionary file

    
    
    Returns: the most popular key
    '''
    largest=0
    keyName=""
    for key in dictionary:
        if (largest<len(dictionary[key])):
            largest=len(dictionary[key])
            keyName=key
    print (keyName.ljust(20), "occurs" , str(largest).rjust(8), "times")
    return keyName
    
    

    
def main():
    '''
    When the file starts two dictionaries are made, then filled with keys and values. Afterwards the amount of emoticons is counted, then the UserIds. Then the five most popular emoticons are shown.
    '''
    
    emoticons_to_ids = {}
    ids_to_emoticons = {}
    load_twitter_dicts_from_file("twitter_emoticons.dat",emoticons_to_ids,ids_to_emoticons)
    print("Emoticons:",len(emoticons_to_ids))
    print("UserIDs:  ",len(ids_to_emoticons))
    for i in range (5):
        emoticons_to_ids.pop(find_most_common(emoticons_to_ids))
    

if __name__ == '__main__':
    main()
