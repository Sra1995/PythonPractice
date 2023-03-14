"mountains".Upper()
'MOUNTAINS'
"MOUNTAINS".lower()
'mountains'

#-------------------------------------------------------------------

answer = "Yes"
if answer.lower() == "yes":
    print("User said yes")
    
Uswer said yes

#-------------------------------------------------------------------
" yes ".strip() # should be 'yes' no space
" yes ".lstrip() # should be 'yes ' remove space on left not right
" yes ".rstrip() # should be ' yes' remove space on right not left

#-------------------------------------------------------------------

"The number of times e occurs in this string is 4".count("e") # should be 4


#-------------------------------------------------------------------

"Forest".endswith("rest") # True 

#-------------------------------------------------------------------

"12345".isnumeric() # True

#-------------------------------------------------------------------

int("12345") + int("54321") #66666

#-------------------------------------------------------------------

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]) # 'This is a phrase joined by spaces'

#-------------------------------------------------------------------

"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]) # "This...is...a...phrase...joined...by...triple...dots"

#-------------------------------------------------------------------

"This is another example".split() # ['This', 'is', 'another', 'example']
