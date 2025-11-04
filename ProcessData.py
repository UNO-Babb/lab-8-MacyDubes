#ProcessData.py
#Name: Macy Dubes
#Date: 11/3/2025
#Assignment: Lab 8

import random

def main():
    
  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]
    majorYear = makeMajorYear(major, year)
    student_id = makeID(first, last, idNum)
    output = last + ", " + first + ", " + student_id + ", " + majorYear + "\n"
    outFile.write(output)
    print(output)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)
  
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen - 3: ]
  #print(id)
  return id

def makeMajorYear(major, year):
  majorThree = major[:3]

  if year == "Freshman":
    yearTwo = "FR"
  elif year == "Sophomore":
    yearTwo = "SO"
  elif year == "Junior":
    yearTwo = "JR"
  elif year == "Senior":
    yearTwo = "SR"
  else:
    yearTwo = "XX"
  majorYear = majorThree + "-" + yearTwo
  return majorYear






if __name__ == '__main__':
  main()