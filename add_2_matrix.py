# /bin/python

# add two matrix

x = int(input("Enter the value of row : "))
y = int(input("Enter the value of column : "))

a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]

print("\nEnter elements of first matrix : ")
for i in range(x):
         for j in range(y):
             a[i][j]=int(input())

print("\nEnter the elements of second matrix : ")
for i in range(x):
         for j in range(y):
             b[i][j]=int(input())

print("\nElements of First matrix is : ")
for row in a:
     print(row)

print("\nElements of Second matrix is :")
for row in b:
     print(row)

# iterate through rows
for i in range(len(a)):
   # iterate through columns
   for j in range(len(a[0])):
       result[i][j] = a[i][j] + b[i][j]

#print the Sum of 2 matrix
print("\nSum of the two matrices is : ")
for r in result:
   print(r)


