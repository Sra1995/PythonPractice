## Using Python to Interact with the Operating System

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/): This book (available online and in print) includes a lot of practical programming exercises for beginners. You can refer to this content to read more about some of the things that we'll be discussing, and get inspired with more ideas of things that can be automated.

* [Hitchhiker’s Guide to Python](https://docs.python-guide.org/): This site (available online and in print) also covers a lot of what we can do with Python. Again, you can use this resource to learn more about the subjects we cover (and the ones we had to omit for time constraints).

* The [official language reference](https://docs.python.org/3/reference/index.html): Once you know what Python tool you'll be using to do a certain task, this technical reference of all Python language components can be a great   

* once a script is saved, which usually ends with " .py ", you can run the command "CAT" to view the contents of the file << on linux. To run a Python script saved on a Windows system, you can just type the name of your script and the operating system will recognize as the pipeline executable from the file extension. On Linux and Mac OS, you can execute the script by calling the pipeline interpreter followed by the name of the file. i.e. on Ubuntu you would type " python3 hello_word.py ". If you want to avoid typing python3 every single time you can add extra line to the file called 'shebang' . i.e on ubuntu you run nano(an editor) once the file is open you would add " #!/user/bin/env python3 " at the top of the script.

* To run the script directly without having to call the interpreter every time. We need to make that file executable using the chmod command. Remember that this command lets us change the file permissions. A file's possible permissions are read, write, and execute. To run the file directly, we want our file to be executable. " chmod +x hello_world.py ". once we mark the script as executable means that we can now run the file by just prefixing it with a " ./ " so in this case it would be ./hello_world.py

* You can create your own Modules simply like this. Imagine you have file called areas.py with 3 functions to calculate area of triangle, rectangle, and circle. You can do "import areas" then type areas.triangle(3,5) under the new file. This was simple concept. However, in some cases the code can be very complex. This is due to creating submodules files to reuse. to visually see this, we can check files that are installed on computer already. the request command for this is  ls-l command so like " ls-l /user/lib/python3/dist-packages/requests " requst is a module.

* IDEs (Integrated Development Environment) like VS code. You can use something that already installed on your computer instead like Notepad, TextEditor on Windows, TextEdit on Mac OS or nano on Linux. Advance IDEs  like Atom, Notepad++, sublime Text. Grpahically IDEs like PhCharm(I like this one) or Eclipse. \
        &nbsp;* [Eclipse](http://www.eclipse.org/)\
        &nbsp;* [PyCharm](https://www.jetbrains.com/pycharm/)\
        &nbsp;* [Sublime Text](http://www.sublimetext.com/)\
        &nbsp;* [Visual Studio Code](https://code.visualstudio.com/)\
        &nbsp;* Articles about IDEs [Python IDEs and Code Editors (Guide)](https://realpython.com/python-ides-code-editors-guide/#pycharm)  - [Best Python IDEs and Code Editors](https://www.softwaretestinghelp.com/python-ide-code-editors/) - [Top 5 Python IDEs for Data Science](https://www.datacamp.com/community/tutorials/data-science-python-ide)

* The Pareto Principle states that 20% of the system administration tasks you perform are responsible for 80% of your workload. Therefore, identifying and automating those tasks will put your productivity through the roof!

* [Reading and Writing Files Cheat-Sheet](https://docs.python.org/3/library/functions.html#open)

* there's plenty of other things we might need to do when working with files in our scripts. We may need to delete, rename or move files, or we might need information about a file, like the time it was last modified or its current size. For these operations, we'll be using functions provided by the OS module. This module provides a layer of abstraction between Python and the operating system. It allows us to interact with the underlying system without us knowing whether we're working on a Windows, Mac, Linux, or any other operating system supported by Python. THIS ALLOW US TO WRITE SCRIPT USABLE ACROSS SYSTEMS - HOWEVER, PATHS ARE DIFFERENT FROM ONE SYSTEM TO ANOTHER.

* Files and Directories Cheat-Sheet: \
        * https://docs.python.org/3/library/os.html \
        * https://docs.python.org/3/library/os.path.html \
        * https://en.wikipedia.org/wiki/Unix_time 
        
* HTML is a markup format which defines the content of a webpage. JSON is a data interchange format commonly used to pass data between computers on networks, especially the internet. CSV or comma separated values is a very common data format used to store data as segment of text separated by commas. In the Python standard library, you'll find classes and modules for working with many of these data formats, including CSV and HTML. 
