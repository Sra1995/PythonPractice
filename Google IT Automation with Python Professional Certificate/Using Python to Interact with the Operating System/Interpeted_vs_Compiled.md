# Interpreted vs. compiler

compiled program super fast to run, but the compilation process itself can take a bit of time. Some examples of commonly use compiled programming languages are C, C++, Go and Rust.

On the flip side, programs written in interpreted language generally rely on an intermediary program called an interpreter. These programs use interpreters to execute the instructions specified in the code. Rather than running them through a compiler first. So this makes the development cycle for a program written in an interpreted language much faster.
like Python, Ruby, JavaScript, Bash, PowerShell

### Java and C# use mixed approached rather than one way

#### here is the tricky part
* for example you have a program that's written in C, and you're running on Windows. But you want to run the program on the Linux server. To run the program on a different operating system than the one you're currently running on, you need to compile it on the destination OS. So in our example, that would mean you would need to compile a source code in Linux OS. And preferably one that has the same versions of the installed libraries on the destination server. You could run the program source code in Python instead. If you did that, it wouldn't matter if you're running on Windows, Mac OS or Linux. You could write and test the program locally and then just copy the script to the server and use it as is. The Python interpreter itself is a complied executable that's platform specific, but once you have it installed, you can run your scripts everywhere
