fileI = open("sum.in", "r");
fileO = open("sum.out", "w+");

# The sum of elements in any row n+1 is 2 times greater than in row n
# n - the row number we need the sum of
N = int(fileI.readline());

# As a result, we can calculate the sum of all the numbers on row n
# by using the following logic
# sumOfRow0 = 1
# sumOfRow1 = 2*sumOfRow0
# sumOfRow2 = 2*sumOfRow1 = 2*2*sumOfRow0
# sumOfRow3 = 2*sumOfRow2 = 2*2*2*sumOfRow0
# since sumOfRow0 is equal to 1, we can write the following expression as
# sumOfRowN = 2**N
sumOfRowN = 2**N

# Save the answer
fileO.write(str(sumOfRowN));
