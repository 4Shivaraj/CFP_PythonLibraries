Python Libraries

NumPy -

1. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
   Expected Output:
   Original List: [12.23, 13.32, 100, 36.32]
   One-dimensional numpy array: [ 12.23 13.32 100. 36.32]

2. Create a 3x3 matrix with values ranging from 2 to 10. Expected Output:
   [[2 3 4]
[ 5 6 7]
[ 8 9 10]]

3. Write a Python program to create a null vector of size 10 and update sixth value to 11. [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   Update sixth value to 11
   [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

4. Write a Python program to reverse an array (first element becomes last). Original array:
   [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
   Reverse array:
   [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

5. Write a Python program to create a 2d array with 1 on the border and 0 inside. Expected Output:
   Original array: [[1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]]

1 on the border and 0 inside in the array [[1. 1. 1. 1. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 1. 1. 1. 1.]]

6. Write a Python program to add a border (filled with 0's) around an existing array. Expected Output:
   Original array:
   [[1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
   1 on the border and 0 inside in the array [[0. 0. 0. 0. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 0. 0. 0. 0.]]

7. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern. Checkerboard pattern:
   [[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]]

8. Write a Python program to convert a list and tuple into arrays. List to array:
   [1 2 3 4 5 6 7 8]
   Tuple to array:
   [[8 4 6]
[1 2 3]]

9. Write a Python program to append values to the end of an array. Expected Output:
   Original array: [10, 20, 30]

After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]

10. Write a Python program to find the real and imaginary parts of an array of complex numbers.
    Expected Output:
    Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
    Real part of the array:
    [ 1. 0.70710678]
    Imaginary part of the array:
    [ 0. 0.70710678]

11. Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.
    Expected Output:
    Size of the array: 3
    Length of one array element in bytes: 8
    Total bytes consumed by the elements of the array: 24

12. Write a Python program to find common values between two arrays. Expected Output:
    Array1: [ 0 10 20 40 60]
    Array2: [10, 30, 40]
    Common values between two arrays:
    [10 40]

13. Write a Python program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
    Expected Output:
    Array1: [ 0 10 20 40 60 80]
    Array2: [10, 30, 40, 50, 70, 90]
    Set difference between two arrays:
    [ 0 20 60 80]

14. Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays. Array1: [ 0 10 20 40 60 80]
    Array2: [10, 30, 40, 50, 70]
    Unique values that are in only one (not both) of the input arrays: [ 0 20 30 50 60 70 80]

15. Write a Python program compare two arrays using numpy. Array a: [1 2]
    Array b: [4 5] a > b
    [False False] a >= b [False False] a < b
    [ True True] a <= b
    [ True True]

16. Write a Python program to save a NumPy array to a text file.

17. Write a Python program to create a contiguous flattened array. Original array:
    [[10 20 30]
[20 40 50]]
    New flattened array:
    [10 20 30 20 40 50]

18. Write a Python program to change the data type of an array. Expected Output:
    [[2 4 6]
[ 6 8 10]]
    Data type of the array x is: int32 New Type: float64
    [[2. 4. 6.]
[ 6. 8. 10.]]

19. Write a Python program to create a 3-D array with ones on a diagonal and zeros elsewhere.
    Expected Output:
    [[1. 0. 0.]
[ 0. 1. 0.]
[ 0. 0. 1.]]

20. Write a Python program to create an array which looks like below array. Expected Output:
    [[ 0. 0. 0.]
    [ 1. 0. 0.]
    [ 1. 1. 0.]

[ 1. 1. 1.]]

20. Write a Python program to concatenate two 2-dimensional arrays. Expected Output:
    Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
    Expected Output:
    [[0 1 3 0 2 4]
[ 5 7 9 6 8 10]]

21. Write a Python program to make an array immutable (read-only). Expected Output:
    Test the array is read-only or not:
    Try to change the value of the first element:
    Traceback (most recent call last):
    File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in x[0] = 1
    ValueError: assignment destination is read-only

22. Write a Python program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.
    Expected Output:
    Original array elements:
    [[0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]
    New array elements:
    [[0 3 6 9]
[12 15 18 21]
[24 27 30 33]]

23. Write a Python program to convert a NumPy array into Python list structure. Expected Output:
    Original array elements:
    [[0 1]
[2 3]
[4 5]]
    Array to list:
    [[0, 1], [2, 3], [4, 5]]

24. Write a Python program to convert a NumPy array into Python list structure. Expected Output:

Original array elements:
[ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
0.35399976 0.99469633 0.0694458 0.54711478]
Print array values with precision 3:
[ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]

25. Write a Python program to suppresses the use of scientific notation for small numbers in numpy array.
    Expected Output:
    Original array elements:
    [ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
    Print array values with precision 3:
    [ 0. 1.6 1200. 0.235]

26. Write a Python program to how to add an extra column to an numpy array.

Expected Output:
[[10 20 30 100]
[ 40 50 60 200]]

27. Write a Python program to remove specific elements in a numpy array.

Expected Output:
Original array:
[ 10 20 30 40 50 60 70 80 90 100]
Delete first, fourth and fifth elements:
[ 20 30 60 70 80 90 100]

Pandas

1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

2. Write a Python program to convert a Panda module Series to Python list and it's type.
3. Write a Python program to add, subtract, multiple and divide two Pandas Series. Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

4. Write a Python program to get the powers of an array values element-wise. Note: First array elements raised to powers from second array
   Expected Output:
   Original array [0 1 2 3 4 5 6]

First array elements raised to powers from second array, element-wise: [ 0 1 8 27 64 125 216]

5. Write a Python program to create and display a DataFrame from a specified dictionary data which has the index labels.
   Sample Python dictionary data and list labels:

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

6. Write a Python program to display a summary of the basic information about a specified Data Frame and its data.
   Sample Python dictionary data and list labels:

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

7. Write a Python program to get the first 3 rows of a given DataFrame. Sample Python dictionary data and list labels:
   exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
   'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
   'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
   'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
   labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

8. Write a Python program to select the 'name' and 'score' columns from the following DataFrame.
   Sample Python dictionary data and list labels:
   exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
   'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
   'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
   'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

9. Write a Python program to select the specified columns and rows from a given data
   frame.
   Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame. exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
   'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
   'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
   'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
   labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

10. Write a Python program to select the rows where the number of attempts in the examination is greater than 2.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

11. Write a Python program to count the number of rows and columns of a DataFrame. Sample data:
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

12. Write a Python program to select the rows where the score is missing, i.e. is NaN. exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

13. Write a Python program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

14. Write a Python program to change the score in row 'd' to 11.5.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',

'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

15. Write a Python program to calculate the sum of the examination attempts by the students.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

16. Write a Python program to calculate the mean score for each different student in DataFrame.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

17. Write a Python program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] Values for each column will be:
    name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

18. Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

19. Write a Python program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

20. Write a Python program to delete the 'attempts' column from the DataFrame. exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

21. Write a Python program to insert a new column in existing DataFrame. exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

22. Write a Python program to iterate over rows in a DataFrame.

23. Write a Python program to get list from DataFrame column headers. Sample data:
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

Python Matplotlib

1. Write a Python program to draw a line with suitable label in the x axis, y axis and a title

2. Write a Python program to draw a line using given axis values with suitable label in the x axis
   , y axis and a title

3. Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
   Test Data:
   test.txt 1 2
   2 4
   3 1

4. Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
   Sample Financial data (fdata.csv):
   Date,Open,High,Low,Close
   03-10-16,774.25,776.065002,769.5,772.559998
   04-10-16,776.030029,778.710022,772.890015,776.429993
   05-10-16,779.309998,782.070007,775.650024,776.469971
   06-10-16,779,780.47998,775.539978,776.859985
   07-10-16,779.659973,779.659973,770.75,775.080017

5. Write a Python program to plot two or more lines on same plot with suitable legends of each line.

6. Write a Python program to plot two or more lines with legends, different widths and colors.

7. Write a Python program to plot two or more lines with different styles

8. Write a Python program to plot two or more lines and set the line markers.

9. Write a Python program to display the current axis limits values and set new axis values.

10. Write a Python program to plot quantities which have an x and y position.

11. Write a Python program to plot several lines with different format styles in one command using arrays.

12. Write a Python program to create multiple types of charts

13. Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
    Date,Close
    03-10-16,772.559998
    04-10-16,776.429993
    05-10-16,776.469971
    06-10-16,776.859985
    07-10-16,775.080017

14. Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn off ticks.

15. Write a Python program to create multiple plots.

Matplotlib Barchart

1. Write a Python programming to display a bar chart of the popularity of programming Languages.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

2. Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

3. Write a Python programming to display a bar chart of the popularity of programming Languages. Use uniform color.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

4. Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

5. Write a Python programming to display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity (float value). Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

6. Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar.

Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

7. Write a Python programming to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

8. Write a Python programming to display a bar chart of the popularity of programming Languages. Select the width of each bar and their positions.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

9. Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

10. Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
    Sample Data:
    Means (men) = (22, 30, 35, 35, 26)
    Means (women) = (25, 32, 30, 35, 29)

11. Write a Python program to create bar plot from a DataFrame. Sample Data Frame:
    a b c d e
    2 4,8,5,7,6
    4 2,3,4,2,6
    6 4,7,4,7,8
    8 2,6,4,8,6
    10 2,4,3,3,2

12. Write a Python program to create bar plots with error bars on the same figure. Sample Date Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
    Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645

13. Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means (integer value).
    Sample Data
    Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
    Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645

Matplotlib Piechart

1. Write a Python programming to create a pie chart of the popularity of programming Languages.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

2. Write a Python programming to create a pie chart with a title of the popularity of programming Languages.
   Sample data:
   Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
3. Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.
   Sample data: medal.csv country,gold_medal United States,46 Great Britain,27 China,26 Russia,19

Germany,17

Matplotlib Scatterplot

1. Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.

2. Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other.

3. Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.

4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.

Test Data:

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]

science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

5. Write a Python program to draw a scatter plot for three different groups camparing weights and heights.

Seaborn Bar plot

1. Write a program to draw bar plot of sex against survived for a dataset given in the url https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv
   Seaborn pointplot

1. Write a program to draw a point plot for sex against survived for a dataset given in url https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

Seaborn Scatterplot

1. Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url

https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

Seaborn Violin Plot

1. Write a program to draw a violin plot of sex against total_bill for a given dataset https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
2. Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url

https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

Seaborn BoxPlot

1. Write a program to draw box plot of life expectancy by continent for a data set given in a url
   https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapmind er-FiveYearData.csv
2. Write a program to draw a box plot of day by tips for a dataset given in a url https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

Seaborn Swarm Plot

1. Write a program to draw a swarm plot of total bill against size for a given dataset https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
2. Write a program to draw swarm plot of “total bill” against day for a dataset given in url https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

Plotly Scatterplot

1. Write a program to draw a scatter plot for random 1000 x and y coordinates

2. Write a program to draw line and scatter plots for random 100 x and y coordinates

3. Write a program to draw a scatter plot for random 500 x and y coordinates and style it

4. Write a program to draw a scatter plot for a given dataset and show datalabels on hover https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv