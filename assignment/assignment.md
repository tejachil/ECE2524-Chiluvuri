Assignment Assignment
=====================
*Nayana Teja Chiluvuri*

###Description
Write a bash script, or python script, in Linux that automates various tasks. Given a folder that contains multiple data files, source code files, subdirectories, have your bash script automate some tasks that need to be done on the files. 

####Examples of Tasks to be executed:
>Lets say the folder contains a GUI application made for a company named "Foo Inc." and has various instances of the string "Foo Inc." The bash script should replace all instances of this string with a string specified by the user at run time because the name of the company has changed to something like "Bar Ltd."

>For the same application, the data files contained in a folder keep track of various records. Lets say there is one data file that keeps track of all the employees of Foo Inc. indexed with a unique ID and the following data files provide information about each employee based on this ID. Script should go in and delete all records of a perticular employee, lets say "John Smith." It should find the line in the employees file and extract John Smith's ID, delete his entry, and then delete the entries of that ID in all other data files. Deleting an entry should just be deleting a line.

>There are two datafiles that have information organized in a particular manner for each employee and each entry identified by the employee's ID. The last task is to combine these two data files into one data files by combining the two sets of information by delimiting the data with tabs.

>One data file has data organized in which each line represents an entry and each entry is seperated into fields with a tab delimiter. This task is to change the order in which the data is stored. Basically change the order of the columns so the third field for each entry can be swapped with the first for example.

After running the bash or python script with the specified parameters, the application within the directory should be rebuilt and run without problems. The changes that were made to the data files and application should be seen within the application without any errors.