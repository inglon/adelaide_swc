#Test file
#Test boundary cases that are completely different
#Each test function named as test_meaningful_name
#1. Write tests for the function dna_starts_with in the file called
#dna_starts.py, the file should write a report
#2. Redirect terminal to the test folder and run the tests from the command line by typing nosetests

def dna_starts_with(sequence, tag):
    length = len(tag)
    return sequence[0:length] == tag

def test_dna_starts_with_itself():
    dna='acgtgtcgat'
    assert dna_starts_with(dna, dna)
    
def test_dna_starts_with_one():
    assert dna_starts_with('cgtgc', 'c')
    
def test_dna_starts_with_bigger():
   dna='acgtgtcgat'
   assert not dna_starts_with(dna, dna+dna)
    

#Nosetests is in package nose
#nosetests (at command line) will run all the files starting with test_.
#Each test_ function should have all the test functions to run.
#It will then give a report e.g. 
#Ran 3 tests in 0.005s 
#OK
#
#When you have tests in the same script as you have the function they
#are still there when you update the function.
#Also, the tests make it clear to others what the function should
#output for different e.g. boundary cases.

