#!/usr/bin/env python
#coding: utf-8 
import numpy as np
import os
#import sys

def insertion_sort(nums):  
    # ���������� �������� �� ������� ��������, �.�. ���������, ��� ������ ������� ��� ������������
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # ��������� ������ �� ������ ����������� ��������
        j = i - 1
        #�������� ���������������� �������� ���������� �����, ���� ��� ������ �������� ��� �������
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]

            j -= 1
        # ��������� �������
        nums[j + 1] = item_to_insert

def readFile(filename):
    filehandle=open(filename,'+wt')
    print(filehandle.read())
    filehandle.close()


def OpenFile(file_):
    fileDir=os.path.abspath(os.path.dirname(__file__))
    FileName=os.path.join(fileDir,fileDir+'\ '.rstrip()+file_)
    print("Path: "+FileName)
    readFile(FileName)
    return FileName
    

def readArrFile(filename, array):
   f=open(filename,encoding='utf-8')
   for line in f:
    array.append([int(x) for x in line.split()])
    #array.append(int(f.readline()))

def writeFile(fileName, array):
    resultFile=open(fileName,'w+',encoding = 'utf-8')
    for i in array:
                #print(str(i))
                resultFile.write(str(i)+"\n")
                #resultFile.write("\n")
    resultFile.close()
i=1
while(i!=2):
    print("Sorting an array. \n1.Start 2.Exit")
    i=int(input())
    if i==2:
        exit()
    #�������� �������� �����, ������������� � ������������ �������� �������
    print("\n Array length:")
    try:
        length=int(input())
    except ValueError as err:
        print("Could not convert data to an integer.")
        continue
    except Exception as err:
        print(err)
        continue
    print("\n Minimum array element:")
    try:
        min_num=int(input())
    except ValueError as err:
        print("Could not convert data to an integer.")
        continue
    except Exception as err:
        print(err)
        continue
    print("\n Maximum array element:")
    try:
        max_num=int(input())
    except ValueError as err:
        print("Could not convert data to an integer.")
        continue
    except Exception as err:
        print(err)
    if min_num>max_num:
        print("The minimum value cannot be greater than the maximum.")
        continue
    #���������� �������
    SortArr=[]
    SortArr=np.random.randint(min_num,max_num,length)
    #������ ������� � ����
    print("\nThe name of the file with the unsorted array (Example: filename ):")
    name=str(input()+".txt")
    try:
        #FileName=OpenFile(name)
        writeFile(name,SortArr)#FileName,SortArr)
    except Exception as err:
        print("Failed to create and fill in the file. Error:"+ err)
        continue
    
    SortArr=[]
    #������ ��������� ������ �� �����, � ������� ��� ��������
    try:
        #FileName=OpenFile(name)
        #FileName=OpenFile("test.txt")
        readArrFile(name,SortArr)
    except Exception as err:
        print("Could not read the file. Error:"+ err)
        continue
    #���������� �������
    insertion_sort(SortArr)  
    #������ ���������������� ������� � ����
    print("\nThe name of the file with the sorted array (Example: filename ):")
    name=str(input()+".txt")
    try:
        #FileName=OpenFile(name)
        
        writeFile(name,SortArr)
    except Exception as err:
        print("Failed to create and fill in the file. Error:"+ err)
        continue
    
    #print(SortArr)