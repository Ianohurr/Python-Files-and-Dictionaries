'''
Author: Ian O'Heir
Date: 4/20/2017
Class: ISTA 130
Section Leader: Adrianna

Description:
Write a dictionary function to show weights of fishes
'''



#==========================================================
def load_fish(fish_dict, fish_data):
    '''
    This function loads the fish data into a dictionary
    
    Parameters:
    fish_dict:a dictionary for the fish
    fish_data: the file containing all the fish data

    
    
    Returns: none
    '''
    f = open(fish_data)
    fishNames = {'1': 'Bream', '2': 'Whitefish', '3': 'Roach','4': '?', '5': 'Smelt', '6': 'Pike', '7': 'Perch'}
    for line in f:
        line = line.strip().split()
        line[1]=fishNames[line[1]]
        if line[1] not in fish_dict:
            fish_dict[line[1]]=[]
            fish_dict[line[1]].append(float((line[2])))
        else:
            if (line[2]!="NA"):
                fish_dict[line[1]].append(float((line[2])))
    f.close()
    
    
def fish_dict_from_file(file):
    '''
    This function accepts a file with fishy data
    
    Parameters:
    file: the aforementioned fishy file

    
    
    Returns: none
    '''
    fishNames = {'1': 'Bream', '2': 'Whitefish', '3': 'Roach','4': '?', '5': 'Smelt', '6': 'Pike', '7': 'Perch'}
    fishmap = {}
    load_fish(fishmap, file)
    return(fishmap)
    
def main():
    '''
    When the file starts a dictionary is made from the method that returns a dictionary from a given data source
    afterwards a for loop iterates through printing details about the dictionary
    '''
    fishies=fish_dict_from_file("fishcatch.dat")
    number='#'
    name='NAME'
    meanWT='MEAN WT'
    fullWeight=0.0
    print(number.rjust(4),name.ljust(10),meanWT.rjust(10))
    for key in sorted(fishies):
        name=key
        number=str(len(fishies[key]))
        sumOfWeight=sum(fishies[key])
        fishCount=len(fishies[key])
        meanWT=round((sumOfWeight/fishCount),1)
        strWT=str(meanWT)+"g"
        print(number.rjust(4),name.ljust(10),strWT.rjust(10))

if __name__ == '__main__':
    main()
