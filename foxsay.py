'''CS 180E, May 2018. Midterm Exam by Holy Davies'''
# What does the fox say? You're going to find out!
'''This program takes in input (animal sounds) and matches that input
to known animal sounds. If the words cannot
be matched, then we know it's what the fox said.''' 

def main():
    # Find out how many test cases follow
    T = int(input())
   
    x = 0
    testList = []

    # Receive all test cases from input and put in a list
    for x in range(T):
        testList.append(str(input()))
    #print('debug %s' % testList)

    # Get all know information
    knownList = []
    knownSounds = ''
    print('Enter known information. Ask "what does the fox say?" to find out.')
    while knownSounds != 'what does the fox say?':
        knownSounds = str(input())
        knownList.append(knownSounds)

    # Remove last element of list since it's the 'd'
    del knownList[-1]
    #print('debug knowList %s' % knownList)

    sounds = []
    for x in knownList:
        getSound = x.split()
        sounds.append(getSound[-1])
        #print('debug sounds %s' % sounds)

    foxList = []
    for testCase in testList:
        test = testCase.split()
        #print('debug test %s' % test)
        for t in test:
            if t not in sounds:
                foxList.append(t)
    
        for fox in foxList:
            print(fox, end=' ')
        print()
        foxList.clear()
 
if __name__=="__main__":
    main()

