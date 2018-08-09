import subprocess
import os
from itertools import combinations
import time

directorypath = "C:/Users/User/Desktop/BitcoinDiamond-master_new/"

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

# assumes every file in the given directory is a file, not directory
def get_immediate_files(a_dir):
    return [name for name in os.listdir(a_dir)]

# given a line, gets percentage in integer format
def getpercentage(line):
    index = len(line)-4
    while (1):
        if (line[index:(index+1)] == " "):
            break
        index = index - 1
    percentage = line[(index+1):len(line)-2]
    return percentage
    
def rSubset(arr, r):
 
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

if __name__ == '__main__':
    coins = get_immediate_subdirectories(directorypath)
    combi = rSubset(coins, 2)
    for thiscombi in combi:
        print(thiscombi)
        start = time.time()
        
        coin1 = thiscombi[0]
        coin2 = thiscombi[1]
        
#         #
#         coin1 = "emp1"
#         coin2 = "emp2"
#         #
         
        
        coin1path = directorypath + coin1
        coin2path = directorypath + coin2
        coin1files = get_immediate_files(coin1path)
        coin2files = get_immediate_files(coin2path)
        coin1maxpercentages = []
        coin2maxpercentages = []
        
        for coin1file in coin1files:
            #this (coin1file) 's max similarity percentage when compared to all coin2file in coin2
            thisfilesmaxpercentage = 0
            coin1filepath = coin1path + "/" + coin1file
            for coin2file in coin2files:
                coin2filepath = coin2path + "/" + coin2file
                proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", coin1filepath , coin2filepath], stdout=subprocess.PIPE)
#                 proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", "C:\Users\User\Desktop\BitcoinDiamond-master_new\Allion-master\src_txdb-bdb.h" , "C:\Users\User\Desktop\BitcoinDiamond-master_new\Allion-master\src_txdb.h"], stdout=subprocess.PIPE)
#                 proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", "C:\Users\User\Desktop\Sherlock\emp\src_addrman.cpp", "C:\Users\User\Desktop\Sherlock\emp\src_addrman_copy.cpp"], stdout=subprocess.PIPE)
                
                output = proc.stdout.read()
#                 print(output)
                percentage = getpercentage(output)
                if (percentage > thisfilesmaxpercentage):
                    thisfilesmaxpercentage = percentage
            coin1maxpercentages.append(thisfilesmaxpercentage)
            
        for coin2file in coin2files:
            #this (coin2file) 's max similarity percentage when compared to all coin1file in coin1
            thisfilesmaxpercentage = 0
            coin2filepath = coin2path + "/" + coin2file
            for coin1file in coin1files:
                coin1filepath = coin1path + "/" + coin1file
                proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", coin2filepath , coin1filepath], stdout=subprocess.PIPE)
#                 proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", "C:\Users\User\Desktop\BitcoinDiamond-master_new\Allion-master\src_txdb-bdb.h" , "C:\Users\User\Desktop\BitcoinDiamond-master_new\Allion-master\src_txdb.h"], stdout=subprocess.PIPE)
#                 proc = subprocess.Popen(["C:\Users\User\Desktop\Sherlock\sherlock.exe", "-t", "0%", "C:\Users\User\Desktop\Sherlock\emp\src_addrman.cpp", "C:\Users\User\Desktop\Sherlock\emp\src_addrman_copy.cpp"], stdout=subprocess.PIPE)
                
                output = proc.stdout.read()
#                 print(output)
                percentage = getpercentage(output)
                if (percentage > thisfilesmaxpercentage):
                    thisfilesmaxpercentage = percentage
            coin2maxpercentages.append(thisfilesmaxpercentage)
            
        #average percentage of coin1 files 
        coin1percentagessum = 0.0
        for percentage in coin1maxpercentages:
            coin1percentagessum = coin1percentagessum + int(percentage)
        coin1percentageavg = coin1percentagessum / len(coin1maxpercentages)
        
        #average percentage of coin2 files 
        coin2percentagessum = 0.0
        for percentage in coin2maxpercentages:
            coin2percentagessum = coin2percentagessum + int(percentage)
        coin2percentageavg = coin2percentagessum / len(coin2maxpercentages)
        
        #avg of avgs
        thesimilarity = (coin1percentageavg + coin2percentageavg) / 2
        end = time.time()
        print(thesimilarity)
        print(end - start)
#         print(coin1maxpercentages)
#         print(coin2maxpercentages)
#         print(coin1percentageavg)
#         print(coin2percentageavg)