##Author Soomin Lee
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")
from d0_makelist_column import MakeList_column


def rawdata_histogram(filename, BIN=8):
    histo_list= MakeList_column(filename)
    for ii in range(len(histo_list)):
        if ii == 0:   ##pass 'DATE' list like as 201312,201401 ...
            continue
        else:
            list_A=(histo_list[ii])



        list_float=[]
        for i in range(len(list_A)):
            if i== 0:
                continue
            else: 
                list_float.append(float(list_A[i]))

#        print(list_float)
        title = (str(list_A[0]))


        AVG = sum(list_float,0.0)/len(list_float)
#        print (AVG)
        AVG = ("%.3f" % round(AVG,3))    
        plt.hist(list_float,bins=BIN,label = 'mean = '+ (str(AVG)))
        plt.title(title)
        plt.ylabel('Frequency')
        plt.xlabel(title + '__score')
        plt.legend()
        plt.show()


def main():
    BIN1 = 8
    filename1 = "/home/soomin/Desktop/group_study/Project-pre/data_txt/ALL_DATA/Aqi_Beijing_WIND.txt"
    rawdata_histogram(filename=filename1, BIN=BIN1)
    
if __name__ =="__main__":
    main()    
