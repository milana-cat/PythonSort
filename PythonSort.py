#!/usr/bin/env python
#coding: utf-8 
import time
import numpy as np
import os
    
class TimerError(Exception): 
    """Пользовательское исключение, используемое для сообщения об ошибках при использовании класса Timer"""
 
class Timer: 
 
    def __init__(self):
        self._start_time = None
 
 
    def start(self):
        """Запуск нового таймера"""
 
        if self._start_time is not None:
            raise TimerError(f"Таймер уже работает. Используйте .stop() чтобы его остановить")
 
        self._start_time = time.perf_counter()
 
 
    def stop(self):
        """Отстановить таймер и сообщить о времени вычисления"""
 
        if self._start_time is None:
            raise TimerError(f"Таймер не работает. Используйте .start() для его запуска")
 
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Вычисление заняло {elapsed_time:0.4f} секунд")

def insertion_sort(nums):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            # Сохраняем ссылку на индекс предыдущего элемента
            j = i - 1
            #Элементы отсортированного сегмента перемещаем вперёд, если они больше элемента для вставки
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]

                j -= 1
            # Вставляем элемент
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
    print(int(x) for x in line.split())
    array.append([int(x) for x in line.split()])
    #array.append(int(f.readline()))

def writeFile(fileName, array):
    resultFile=open(fileName,'w+',encoding = 'utf-8')
    for i in array:
                print(str(i))
                resultFile.write(str(i)+"\n")
                #resultFile.write("\n")
    resultFile.close()
i=1
while(i!=2):
    print("Sorting an array. \n1.Start 2.Exit")
    i=int(input())
    if i==2:
        exit()
    print("Create a new file with an array? 1. Yes 2. No")
    j=int(input())
    if(j==1):
            #Проверка введённых длины, максимального и минимального значений массива
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
        #заполнение массива
        SortArr=[]
        SortArr=np.random.randint(min_num,max_num,length)
        #Запись массива в файл
        print("\nThe name of the file with the unsorted array (Example: filename ):")
        name=str(input()+".txt")
        try:
            #FileName=OpenFile(name)
            writeFile(name,SortArr)#FileName,SortArr)
        except Exception as err:
            print("Failed to create and fill in the file. Error:"+ err)
            continue
    elif(j==2):
        print("\nThe name of the file with the unsorted array (Example: filename ):")
        name=str(input()+".txt")
        SortArr=[]
        #читаем рандомный массив из файла, в который его записали
        try:
            readArrFile(name,SortArr)
        except Exception as err:
            print("Could not read the file. Error:"+ err)
            continue
    else:
        print("Input error")
        continue
    #Замерка времени сортировки
    t=Timer()
    t.start()
    #Сортировка массива
    insertion_sort(SortArr) 
    t.stop()
    #Запись отсортированного массива в файл
    print("\nThe name of the file with the sorted array (Example: filename ):")
    name=str(input()+".txt")
    try:
        writeFile(name,SortArr)
    except Exception as err:
        print("Failed to create and fill in the file. Error:"+ err)
        continue

