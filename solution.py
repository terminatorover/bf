#/usr/bin/python
import math 
input_f = open("input.txt","r")
output_f = open("output.txt","w+")


def yes_no( array):
    ##for all when the squares are black 
    #if we have an odd number of #'s then we can't have a square
    length = len(array)
#    print "Lengthhhhhhhhhhhh " + str(length )
    size = int(math.sqrt(length))
    
    count = 0 
    for char in array:
        if (char == "#"):
            count +=1 
    if ( type(math.sqrt(count))==type(3)):
        return False 
    sides_of_test_square = math.sqrt(count)
    no_test_for_buddies = (sides_of_test_square -1) * (sides_of_test_square)
    keep_testing = 0 
    index = 0 
    for char in array:
        if  char == "#":
            if ( index ) < (length - size):
                if ( keep_testing < no_test_for_buddies):
                    keep_testing += 1
                    if array[index+ size] == "#":
                        index+=1
                        continue
                    else:
                        return False 
        index +=1
    return True


#no_text_cases = input_f.readlines()
first = 0
case = 1
in_case = 0 
for line in input_f.readlines():

 
    if ( ("#" not in line ) and ("." not in line)):
        line.strip()
        N = int(line)
        if (first == 0):
            first +=1 
 #           print "the number of test cases are " + str( N)
        else :
#            print "the matrix size is :" + str(N)
            linear = []
            in_case = 0 
        #matrix = [[0 for x in range(N)]for y in range(N)]#setup the matrix 
    else :
        in_case +=1 
        #populate the matirx 
#        print line

        for char in line:
            if char != '\n':
                linear.append(char)
            

            
            
    if ( in_case == N):
        #check if the matrix is right 
#        print "checking if  true"
#        print "size of the matrix is: " + str( len(linear))
        
        check = yes_no(linear)

        if (check ):
            output_f.write("Case #%s: YES\n"%case)
        else:
            output_f.write("Case #%s: NO\n"%case)
    
        case += 1 
        
        


input_f.close()
output_f.close()
