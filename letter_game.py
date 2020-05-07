name=input("Enter your name").title().strip() #strip() spaces will be delted b/w the namees
print("welcome",name)

message=input("enter a msg")
letter=input("enter a letter")

message=message.lower()
letter=letter.lower()

letter_count=message.count(letter)
print("you have "+letter +" of "+str(letter_count))   #letter_count is integer so converting it to str
