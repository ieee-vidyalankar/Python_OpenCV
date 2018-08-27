#list comprehension - describing a list in a single pythonic line
# #1.
# squares = []
# for x in range(10):                       #Using For loop
#     squares.append(x**2)
# print(squares)   
# # ( OR )
# squares = [x**2 for x in range(10)]       #Using Lists Comprehension
# print(squares)


# #2.Using Loops
# pairs = []
# for x in [9,8,7]:                           #Using For loop
#     for y in [7,2,9]:
#         if x != y:
#             pairs.append((x, y))
# print(pairs)
# #( OR )
# pairs = [(x,y) for x in [9,8,7] for y in [7,2,9] if x!=y]   #Using Lists Comprehension
# print(pairs)

# #4.Evenlist
# evenList = [x for x in range(0,11) if x%2==0]
# print(evenList)

# #5. Nested list Comprehensions
# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12]]
# print(matrix)
# Transpose = [[row[i] for row in matrix] for i in range(4)]            #to transpose the matrix
# print(Transpose)