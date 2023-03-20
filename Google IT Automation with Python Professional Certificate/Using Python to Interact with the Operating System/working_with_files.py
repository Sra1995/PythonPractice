import os
os.remove("novel.txt") # now the file is removed

os.remove("novel.txt") # Traceback (most recent call last): File "<stdin>", line 1, in <module>:


os.rename("first_draft.txt","finished_masterpiece.txt")

os.path.exists("first_draft.txt") # False
os.path.exists("finished_masterpiece.txt") # True