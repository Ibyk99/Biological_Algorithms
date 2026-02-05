#This class uses the Smith Waterman Algorithm as an example of how to implement an algorithm in Python.
#In this  class we review key Python features and then modify an existing Smith-Waterman implementation
#This is expected to be a refresher for most people and we do not cover all commands used in the code

#But you don't need much knowledge of Python here- we use small subset of the language

#You need to understand, indexing strings, counters, defining fuctions, passing  and returning values from functions
#You need to understand assignment and equivalence
#You need to understand simple loop structures
#In this example we index a Python list and treat it like an array, we make a list of list and this is a matrix
#We will explore other ways to define a matrix-like data structure in a later classes
#For the exercises you need to know how to read and parse a file

#Version 1.9 SRT


#Q1: Indexing Strings
testsequence="AGCGATDTTT"

#Q1a: How do you obtain the third character of testsequence and print it to screen?
print(testsequence[2])
#Q1B: How do you return the second and third characters?
print(testsequence[2:4])
#Q1C: How do you change the last character of "testsequence" to an "A" using Python code?
testsequence = testsequence[:-1] + 'A'
print(testsequence)
#Q1D: What value does testsequence[-1] equal?
print(testsequence[-1])
#Q1E: Will "testsequence[len(testsequence)]" (without quotes)  generate an error?  If so why?
# Yes - we index at 0 so max value we could use is len(testsequence)-1
print(testsequence[len(testsequence)-1])

#Q2 Change counters
x=1
x+1
print(x) 

#Q2A: What is the value of x printed?  Why?
# 1 -  x+1 is not assigned back to x

x=1
x+=1
print(x) 


#Q3: Define Functions

y=1
def myfunction(aval):
    aval=4
    return (y+1)

#Q3A: Call this function with "myfunction(y)", what is the value of y after this call
# 2
#Q3B: What is the value of "aval" after the call to myfunction ??
# 4 but it doesn't exist outside of the function

#Q4: Passing and returning values
#Q4A Define a function that is passed  an integer and returns this integer incremented by one
def add_one(in_num):
     return in_num+1

#Q5: Assignment and equivalence
z=4
if(z==True):
    print(z)
#Will "z" print in this code?
# Yes, because z has a value

#Q6: Simple loops
count=0
for i in range(1, 10):
         for j in range(1, 2):
             count=count+1

#What is the value of count?
# 9

#Q7: Parse a file
#Modify the code below to write a function that reads a fasta file
#and returns the sequence, ignoring the header
#"afile" and "bfile" are 

#Use Biopython for real projects that read fasta!!!
def read_fasta_filename(filename):
   seq=""

   with open(filename, 'r') as filehandle:
       for line in filehandle:
           if line[0] != '>':
                seq += line.replace('"',"").replace("\n","")
       return seq

#Q8: Command line
#Below is a code example of how to parse the command line using argparse.  
#Modify this code so that you can pick up the settings for SmithWaterman.py as parameter passed to the application
#Build a modified SmithWaterman.py Python programme

import argparse

parser = argparse.ArgumentParser(description='Aligning sequences...')
parser.add_argument('seq1',action="store",help="First sequence")
parser.add_argument('seq2',action="store",help="Second sequence")
parser.add_argument('anum',action="store",help="A number",type =int)

args = parser.parse_args()
print(args)
print(args.seq1)


#Q9: Load the SmithWaterman.py code and run the aligner.
#Read the code and determine how to change the input parameters including the files to be aligned.
#Change the code to align a different set of sequences.  
#Does the aligner give consistent results to the water programme online?
import SmithWaterman
SmithWaterman

#Q10: SmithWaterman.py Code Questions
#Q10A: Read the code of SmithWaterman.py and identify how the matrix is initialised, where is the recurrence relationship defined?
# Matrix intitialised in the create_matrix function
#Q10B: What does the "range" command specify?
# Used to specify 0 to num of cols/rows
#Q10C:
#In the line 41 "sc = seqmatch if sequence2[x - 1] == sequence1[y - 1] else seqmismatch" why are indexes x and y offset by -1?
# To account for the fact that we begin indexing at 0
#Q10D: Why "mymatrix[0]" in the code from line 510  "cols=len(mymatrix[0])"?
# Length of vector mymatrix[0] to get num of cols
#Q10E: What does the command at line 85 do  "return [mrow, TypeB.END, mcol]"?
# Returns max row and max col, TypeB.END is an enumeration object of type END
#Q10F: Line 100 "print("\n",end="")" what does "\n" specify?
# New line
#Q10G: Line 106 "print("%02d\t" % (mymatrix[i][j]),end="")" what does the "%" specify?
# Remainder left after dividing num 1 by num 2
#Q10H: Line 203 "global  seqmatch" why "global"?
# Values are defined outside the function and are global so we want to reference them
#Q10I Could you remove the call to  "perform_smith_waterman()", line 200, and still run the code?
# The function call actions everything - won't work without this call








