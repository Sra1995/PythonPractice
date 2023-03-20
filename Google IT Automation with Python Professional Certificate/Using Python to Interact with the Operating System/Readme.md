## Using Python to Interact with the Operating System

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/): This book (available online and in print) includes a lot of practical programming exercises for beginners. You can refer to this content to read more about some of the things that we'll be discussing, and get inspired with more ideas of things that can be automated.

* [Hitchhiker’s Guide to Python](https://docs.python-guide.org/): This site (available online and in print) also covers a lot of what we can do with Python. Again, you can use this resource to learn more about the subjects we cover (and the ones we had to omit for time constraints).

* The [official language reference](https://docs.python.org/3/reference/index.html): Once you know what Python tool you'll be using to do a certain task, this technical reference of all Python language components can be a great   

* once a script is saved, which usually ends with " .py ", you can run the command "CAT" to view the contents of the file << on linux. To run a Python script saved on a Windows system, you can just type the name of your script and the operating system will recognize as the pipeline executable from the file extension. On Linux and Mac OS, you can execute the script by calling the pipeline interpreter followed by the name of the file. i.e. on Ubuntu you would type " python3 hello_word.py ". If you want to avoid typing python3 every single time you can add extra line to the file called 'shebang' . i.e on ubuntu you run nano(an editor) once the file is open you would add " #!/user/bin/env python3 " at the top of the script.

* To run the script directly without having to call the interpreter every time. We need to make that file executable using the chmod command. Remember that this command lets us change the file permissions. A file's possible permissions are read, write, and execute. To run the file directly, we want our file to be executable. " chmod +x hello_world.py ". once we mark the script as executable means that we can now run the file by just prefixing it with a " ./ " so in this case it would be ./hello_world.py
