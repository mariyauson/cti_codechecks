#####################################
# grabbing certain digits
#####################################
input = int(input())
i = 1
while i <= (len(str(input))):
   print(input%10**i//10**(i-1), end=" ")
   i = i+1





#####################################
# bowling
#####################################
inp = [int(e) for e in input().split()]
N = inp[0]
K = inp[1]
pins_start = []
for l in range(N):
    pins_start.append("I")
print(pins_start)

tries = []
for x in range(K):
    #input = input().split()
    current_try = [int(e) for e in input().split()]
    tries.append(current_try)
    for j in range(current_try[0], current_try[1]+1):
        print(j)
        pins_start[j-1] = "."
print(tries, "tries")
for i in pins_start:
    print(i, end="")

#####################################
N, K = [int(e) for e in input().split()]
pins_start = []
for l in range(N):
    pins_start.append("I")
print(pins_start)

for x in range(K):
    current_try = [int(e) for e in input().split()]
    for j in range(current_try[0], current_try[1]+1):
        print(j)
        pins_start[j-1] = "."
        
print("".join(pins_start))

#####################################
def update_bowling_configuration(pins, first, last):
    for i in range(first, last+1):
        pins[i-1] = "."
    
    
n, k = [int(str_numbers) for str_numbers in input().split()]
pins = ["I"] * n

for rolls in range(k):
    first, last = [int(str_numbers) for str_numbers in input().split()]
    update_bowling_configuration(pins, first, last)
    
print("".join(pins))


#####################################
#m,n = 3, 4
def func(m, n):
    array = []
    column = []
    for rows in range(m):
        column = [int(str) for str in input().split()]
        array.append(column)
    #print(array, "arrraay")

    c = int(input())
    output = [[array[j][i]*c for i in range(n)] for j in range(m)]
    
    return output

def main():
    m, n = [int(s) for s in input().split()]
    final_output = func(m,n)
    for i in final_output:
        print(*i)
    
main()





#####################################
# find maximum number in 2d list
#####################################
def create_array(m, n):
    array = []
    column = []
    for columns in range(m):
        column = [int(str) for str in input().split()]
        array.append(column)


    maximum = float('-inf')
    for x in range(m-1, -1, -1):
        for y in range(n-1, -1, -1):
            if array[x][y] >= maximum:
                maximum = array[x][y]
                a,b = x, y
    return a,b
 
def main():
    m, n = [int(s) for s in input().split()]
    print(*create_array(m,n))
main()
#####################################
def func(m, n):
    array = [[int(str) for str in input().split()] for columns in range(m)]
    maximum = float('-inf')
    for x in range(m-1,-1,-1):
        for y in range(n-1,-1,-1):
            if array[x][y]>=maximum:
                maximum = array[x][y]
                a,b = x,y
    return a,b
        
def main():
    m, n = [int(s) for s in input().split()]
    print(*func(m,n))
    
if __name__ == "__main__":
   main() 





#####################################
# diagonals
#####################################
def func(n):
    zero_place = 0
    lst = []
    for box_size in range(n):
        row = []
        for x_leftwards in range(zero_place, -1, -1):
           row.append(x_leftwards)
           #print("x_leftwards", x_leftwards)
        for x in range(1, n - zero_place):
           row.append(x) 
           #print("x",x)
        lst.append(row)
        #print("column", row)
        zero_place = zero_place + 1
    return lst

def main():
    n = int(input())
    output = func(n)
    for i in output:
        print(*i)

if __name__ == "__main__":
    main()





#####################################
# triangles
#####################################
def func(n):
    num_of_zeros = n-1
    num_of_twos = 0
    array = []
    #print([[0]*n]*n)
    for box_fill in range(n):
        row =  ["0 "* num_of_zeros, "1 ", "2 "*num_of_twos] 
        #spaced_column = "".join(column)
        num_of_twos = num_of_twos + 1
        num_of_zeros = num_of_zeros - 1
        array.append(row)
        #output = "".join(row[box_fill])
    
    return array
    
def main():
     n = int(input())
     output = func(n)
     for e in output: 
         print(*e, sep="")

main()





#####################################
# chessboard chess
#####################################
# chessboard chess
def main():
    n, m = [int(str) for str in input().split()]
    output = func(n,m)
    for e in output:
        print(*e)

def func(n,m):
    array = []
    for i in range(n):
        row = []
        for j in range(m):
            if i%2 != 0:
                if j%2 == 0:
                    row.append( "*")
                else:
                    row.append( ".")
            elif i%2 == 0:
                if j%2 == 0:
                    row.append(".")
                else:
                    row.append("*")
        array.append(row)
    return array

if __name__ == "__main__":
    main()





#####################################
# pascal's triangle
#####################################
def pascalTriangle(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(1)
        else:
            x = lst[i]+lst[i-1]
            result.append(x)

    result.append(1)
    print(*result)

def main():
    lst = [int(str) for str in input().split()]
    pascalTriangle(lst)
    
main()





#####################################
# snowflake
#####################################
#SNOWFLAKE
import math
def func(n):
    middle_row = math.ceil(n/2)
    #print(middle_row)
    low_star_pointer = 0
    high_star_pointer = n-1
    array = []
    for h in range(n//2):
        row = []
        for i in range(n):
            str = ""
            if i == low_star_pointer or i == high_star_pointer or i == middle_row-1:
                str = str + "*"
            else:
                str = str + "."
            row.append(str)
        low_star_pointer = low_star_pointer + 1
        high_star_pointer = high_star_pointer - 1
        array.append(row)
    #output = [[array[i][j] for i in range(n)] for j in range(n)]
    reversed_array = []
    for i in range(1, middle_row):
        reversed_array.append(array[-i])
    
    
    array.append(["*"] * n)
    output = array + reversed_array
    return output
    
def main():
    #n = int(input())
    n = 7
    output = func(n)
    for e in output:
        print(*e)





#####################################
# 2d list with list comprehension
#####################################
img = input()
newarray = []
for i in range(len(img)):
    first_flip = []
    for j in range(1, len(img) + 1):
        first_flip.append(img[i][-j])
    newarray.append(first_flip)
print("newarray:", newarray)

### IS THE SAME AS
new_arr = [[img[j][-i] for i in range(1,len(img)+1)] for j in range(len(image))]
print("NEW ARR", new_arr)
#####################################
array = [[1,1,0],[1,0,1],[0,0,0]]
for i in range(len(image)):
    first_flip = []
    for j in range(1, len(image) + 1):
        first_flip.append(image[i][-j])
    newarray.append(first_flip)
print("newarray:", newarray) #[[0, 1, 1], [1, 0, 1], [0, 0, 0]]

# same as above
new_arr = [[image[j][-i] for i in range(1,len(image)+1)] for j in range(len(image))]
print("NEW ARR", new_arr) #[[0, 1, 1], [1, 0, 1], [0, 0, 0]]





#####################################
# inverting image
#####################################
def func(image):
   
    #newarray = []
    #for i in range(len(image)):
    #    first_flip = []
    #    for j in range(1, len(image) + 1):
    #        first_flip.append(image[i][-j])
    #    newarray.append(first_flip)
    #print("newarray:", newarray)
    
    
    newarray = [[image[i][-j] for j in range(1,len(image)+1)] for i in range(len(image))]    
    
    output_array = []
    for i in range(len(image)):
        inverted_row = []
        for j in range(len(image)):
            if newarray[i][j] == 1:
                inverted_row.append(0)
            else:
                inverted_row.append(1)
        output_array.append(inverted_row)
        
    return output_array
     
def main():
    array = [[1,1,0],[1,0,1],[0,0,0]]
    array = []
    while True:
        a = [str for str in input().split()]
        if a == []:
            break
        else:
            array.append(a)
      
    func(array)
main()





#####################################
# leetcode excel
#####################################
#EXCEL
inp = "AZ"
length = len(inp)
sum = 0

for i in range(1,len(inp)+1):
    sum += (ord(inp[i-1])-64)*26**(length-1) 
    length -= 1
    
print(sum)

######################
# excel in cpp
#inp = "AB"
#length = len(inp)
#sum = 0

#for i in range(length):
#    sum += (ord(inp[i])-64)*26**(length-1) 
#    length -= 1
    
#print(sum)

#//excel in cpp
##include <string>
##include <cmath>
##include <iostream>
#using namespace std;
#int getColumnNumber(string columnString) 
#{
#  int columnNumber = 0;
#  
#  for (int i=columnString.size()-1; i>=0; --i) {
#    columnNumber += (columnString[i]-64)*pow(26, columnString.size()-i-1);
#  }
#  
#  return columnNumber;
#}
#
#int main()
#{
#  cout << getColumnNumber("DEF") << endl;
#  cout << "Expected: 2840" << endl;
#}






#####################################
# guess the number
#####################################

n = int(input())
all_nums = {i for i in range(1, n+1)}
removed = set()
possible = set()

while True:
    inp = {str for str in input().split()}
    if "HELP" in inp:
        print(*sorted(all_nums))
        break
    else:
        ints = {int(i) for i in inp}
        y_n = input()
        if "YES" in y_n:
            all_nums.intersection_update(ints)
        elif "NO" in y_n:
            all_nums.difference_update(ints)





#####################################
# dictioniaries dictionary
#####################################
inp = input().split()
dictionary = dict()

for i in inp:
    if i not in dictionary:
        dictionary[i] = 0
    else:
        dictionary[i] += 1
    print(dictionary[i], end = " ")
print("DICTIONARY", dictionary)
#####################################
n = 2
dic = dict()
for i in range(n):
    key, value = [str for str in input().split()]
    dic[key] = value
print(dic) 

inp = input()
if inp in dic:
    print(dic[inp])
else:
    for k, v in dic.items():
        if v==inp:
            print(k)
#####################################
n = 5
dic = dict()
for i in range(n):
    k, v = (str for str in input().split())
    int_v = int(v)
    if k not in dic:
        dic[k] = int_v
    else:
        dic[k] += int_v
        

for i in sorted(dic):
    print(i)
#####################################
n = 2
dictionary = dict()
for i in range(n):
    keys = input().split()
    for i in keys:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
            
print(dictionary)

max_val = 0
max_keys = []
for i in dictionary:
    if dictionary[i] >= max_val:
        max_val = dictionary[i]

for i in sorted(dictionary):
    if dictionary[i] == max_val:
        print(i)
        break





#####################################
# command / access rights
#####################################
n = int(input())
dictionary = dict()
for i in range(n):
    inp = input().split()
    k, v = inp[0], inp[1:]
    if k not in dictionary:
        dictionary[k] = v
        
m = int(input())
for i in range(m):
    v, k = (s for s in input().split())
    if v == "read":
        for i in dictionary:
            if i == k:
                if "R" in dictionary[i]:
                    print("OK")
                else:
                    print("Access denied")
    if v == "write":
        for i in dictionary:
            if i == k:
                if "W" in dictionary[i]:
                    print("OK")
                else:
                    print("Access denied")
    if v == "execute":
        for i in dictionary:
            if i == k:
                if "X" in dictionary[i]:
                    print("OK")
                else:
                    print("Access denied")
#####################################
n = int(input())
dictionary = dict()
for i in range(n):
    inp = input().split()
    k, v = inp[0], inp[1:]
    if k not in dictionary:
        dictionary[k] = v
        
m = int(input())
for i in range(m):
    v, k = (s for s in input().split())
    if v == "read":
        if "R" in dictionary[k]:
            print("OK")
        else:
            print("Access denied")
    if v == "write":
        if "W" in dictionary[k]:
            print("OK")
        else:
            print("Access denied")
    if v == "execute":
        if "X" in dictionary[k]:
            print("OK")
        else:
            print("Access denied")
#####################################
def func(operation, key, dictionary):
    if operation == "read":
        if "R" in dictionary[key]:
            print("OK")
        else:
            print("Access denied")
    if operation == "write":
        if "W" in dictionary[key]:
            print("OK")
        else:
            print("Access denied")
    if operation == "execute":
        if "X" in dictionary[key]:
            print("OK")
        else:
            print("Access denied")
            
def main():
    n = int(input())
    dictionary = dict()
    for i in range(n):
        inp = input().split()
        k, v = inp[0], inp[1:]
        if k not in dictionary:
            dictionary[k] = v
            
    m = int(input())
    for i in range(m):
        operation, key = (s for s in input().split())
        func(operation, key, dictionary)
        
main()





#####################################
# cities
#####################################
n = 2
dictionary = {}
for i in range(n):
    inp = input().split()
    k, v = inp[0], inp[1:]
    if k not in dictionary:
        dictionary[k] = v
        
   
m = 3
for i in range(m):
    city = input()
    output = [k for k in dictionary if city in dictionary[k]]
    
    print(*output)
#####################################
n = int(input())
dictionary = {}
for i in range(n):
    inp = input().split()
    k, v = inp[0], inp[1:]
    if k not in dictionary:
        dictionary[k] = v
        
   
m = int(input())
for i in range(m):
    city = input()
    for each_country in dictionary:
        if city in dictionary[each_country] == True:
            print(each_country, "COUNTRY")  
#####################################
n = 2
dictionary = {}
for i in range(n):
    inp = input().split()
    k, v = inp[0], inp[1:]
    if k not in dictionary:
        dictionary[k] = v
        
   
m = int(input())
for i in range(m):
    city = input()
    for key, value in dictionary.items():
         if city in value:
             print(key)





#####################################
# values and keys. latin - english dictionary
#####################################
n = int(input())
dictionary = {}
for i in range(n):
    inp = [str for str in input().split()]
    for j in inp:
        if j not in dictionary:
            dictionary[j] = 1
        else:
            dictionary[j] += 1


v_and_k = [[-dictionary[i], i] for i in dictionary]
#for i in dictionary:
#    v_and_k.append([dictionary[i], i])
v_and_k.sort()
for i in range(len(v_and_k)):
    for j in range(1):
        print(v_and_k[i][1], v_and_k[i][j]*-1)
#####################################
#####################################
# conor helped hehe
n = 2
e_to_l = {}
l_keys = []
dictionary = {}
for i in range(n):
    e, l = [str for str in input().split(" - ")]
    l_keys.append(l.split(","))
    if e not in e_to_l:
        e_to_l[e] = l

#items = e_to_l.items()
    
    for k, v in e_to_l.items():
        v_arr = v.split(",")
    
    
    for i in v_arr:
        if i not in dictionary:
            dictionary[i] = [k]
        else:
            dictionary[i].append(k)
print(dictionary)
#
#####################################
#####################################
n = int(input())
e_to_l = {}
l_keys = []
dictionary = {}
output = []
for i in range(n):
    e, l = [str for str in input().split(" - ")]
    if e not in e_to_l:
        e_to_l[e] = l.replace(" ","")

#items = e_to_l.items()
    
    for k, v in e_to_l.items():
        v_arr = v.split(",")
        v_arr.sort()
       # v_arr.replace(" ", "")
    
    
    for i in v_arr:
        if i not in dictionary:
            dictionary[i] = [k]
        else:
            dictionary[i].append(k) 
            

for k, v in dictionary.items():
    a = sorted(v)
    line = k + " - " + (', '.join(a))
    output.append(line)
   
output.sort()
for i in output:
    print(i)





#####################################
# highest frequency. song lyrics
#####################################
def highestFrequency(str):

   dictionary = {}
   a = str.split()
   lst = [s.replace(",", "") for s in a]
   
   for i in lst:
     a = i.replace(",","")
     
     if a not in dictionary:
         dictionary[a] = 1
     else:
         dictionary[a] += 1
   
   max = 0
   for v in dictionary.values():
     if v >= max:
         max = v
   
   keys = list(dictionary.keys())
   vals = list(dictionary.values())
    
   val_index = vals.index(max)
   return (keys[val_index])





#####################################
# prime numbers
#####################################
n = int(input())
primes = [True for i in range(n)]
i = 2
#divisible by 2 -> false, starting at 2
while(i * i < n):
        for j in range (i*i, n, i): #4, n, 2steps. turning false the multiples of i
            primes[j] = False
        i += 1
     
counter = 0
for i in range(2, len(primes)):
    if primes[i]:
        counter += 1
print(counter)
#####################################
def isPrime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
        return True
        
n = int(input())
counter = 0
for i in range(2, n+1):
    if (isPrime(i) == True):
        counter += 1
print(counter)





#####################################
# last factorial digit
#####################################
n = 9
def func(n):
    if n == 0:
        return(1)
    else:
        i = n-1 # 2
        while i != 1:
            n = n * i # 24
            i -= 1
    
        d = n%10
        z = 1
        while d == 0:
            d = n%(10**z)//(10**(z-1))
            print("d = ", d)
            z += 1
        return d

print(func(n))





#####################################
# countring trailing zeros. cpp
#####################################
##include <iostream>
##include <string>
#int trailingZeroesInFactorial(int N)
##{
#  
#  if (N == 0) 
#    return -1;
#    
#    int counter = 0;
#    
#    for (int i = 5; N/i >= 1; i *= 5)
#     counter += N/i;
#    
#    return counter;
#}
#
#int trailingZeroesInFactorial(int N);
#using namespace std;
#
#int main()
#{
#  std::cout << trailingZeroesInFactorial(3) << endl;
#  
#  std::cout << trailingZeroesInFactorial(8) << endl;
#  
#  std::cout << trailingZeroesInFactorial(18) << endl;
#}





#####################################
# end of 201 module
#####################################

