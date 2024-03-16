# WebHW03
Homework #3 for processes and threads (Web)
First part
Create a program for processing folder "Rubish", that sorts out files by extension in the defined folder  using several threads. Speed up the processing of large directories with many subfolder by traversing all folders in parallel in separate threads. The most time-consuming will be transerring a file and getting a list of files in a folder (iteration over the contents of the directory). To speed up file transfer, it can be done in a separate thread or thread pool. It is all the more convenient application and you can not collect. It is convenient because you don't process the result of this operation in the application and you don't need to collect any results. To speed up traversal of the contents of a directory  with multiple levels of nesing, you can process each subdirectory in a separate thread or pass the processing to a thread poll.

Second part
Write implementation of a function "factorize", that takes list of numbers and returns lists of numbers, that can divide numbers from the source list can be devided without  reminder. 

Implement synchronized version and calculate execution time.

Then impvoe productivity of your function by implementing usage of several cores of the processor for parallel calculations and mesure time of the execution again. For the cores number definition on the PC use function cpu_count() from "multithreading" package.

To verify correctness of your function results you can use test:

def factorize(*number):
    # YOUR CODE HERE
    raise NotImplementedError() # Remove after implementation


a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

