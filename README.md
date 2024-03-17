# WebHW03

Homework #3 for processes and threads (Web)
=====================================First part===================================
Create a program for processing folder "Rubish", that sorts out files by extension in the defined folder using several threads. Speed up the processing of large directories with many subfolder by traversing all folders in parallel in separate threads. The most time-consuming will be transerring a file and getting a list of files in a folder (iteration over the contents of the directory). To speed up file transfer, it can be done in a separate thread or thread pool. It is all the more convenient application and you can not collect. It is convenient because you don't process the result of this operation in the application and you don't need to collect any results. To speed up traversal of the contents of a directory with multiple levels of nesing, you can process each subdirectory in a separate thread or pass the processing to a thread poll.

------------------Quick description and instructions for file sorting programm-----------------------------:
Thre is a program in clean.py file intented to sort files in a specified folder (e.g rubish) by category.
Program can be called from command line with a command: <python sort.py /home/Documents/rubish>

- Create a separate function to move here folder processing
- Script calls itself (recurcive call) to be able to process folders on any level (function should recurcively call itself to process
  included subfolders)

Sample of categories by extension (letters after the period in filename):

- images ('JPEG', 'PNG', 'JPG', 'SVG');
- videos ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
- music ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');

All files and folders should be renamed deleting all symbols that could cause the issues.
For this purpose you can apply function <normalize>.
Files should be renamed in a way to change only filename (but not file extension)

Function normalize:

1. Transliterates cyrrilic alphabet to lathin
2. Changes all symbols, except lathin and numbers to '\_'

Requirements to normalize function:

- takes filename as a sting and returns normalized filename as a sting
- transliterates cyrrilic symbols to lathin ones
- changes all symbols, except lathin letters and digits to symbol '\_'
- transliteration should be readable
- The case of the letters should be adhered (lower case letters should remain lower case, upper case letter should be transliterated as capital letters)

Requirements to the task:

- All files should be renamed with <normalize> function
- extension of the files should not be changed
- empty folders should be deleted
- script should ignore folders archives, audio, documents, images;
- unpacked contents of the arhive should be moved to folder <archives> to the subfolder with the same name as unpacked archive(without extension)
- files with unknown extension should be left without changes

------------UPDATES regarding the threading task-------------

- It was imported the threading module to handle threading.
- Created a new thread (subfolder_thread) for each subfolder traversal.
- Each thread calls the handle_folder function with the appropriate subfolder path as an argument.
- Threads are started using the start() method of the thread object (subfolder_thread.start()).

======================================Second part=============================
Write implementation of a function "factorize", that takes list of numbers and returns lists of numbers, that can divide numbers from the source list can be divided without reminder.

Implement a synchronized version and calculate execution time.

Then improve the productivity of your function by using several processor cores for parallel calculations and measure the time of the execution again. For the cores number definition on the PC use function cpu_count() from "multithreading" package.

To verify correctness of your function results you can use test:

def factorize(\*number): # YOUR CODE HERE
raise NotImplementedError() # Remove after implementation

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
