# MCQ  filler is for filling up my google spreadsheet in which ive written stuff like
    #book, test area, page noumber, right, wrong, unattempted, start time, endtime, date
# Created Date 
# Last Updated Date: 2022-09-24 21:08:24
# FileName: MCQFiller.py
# Change History (ctrl + shift + I)
    # 2022-09-24 20:09:19 : as of today prog take input of book name , right wrong unattempted and test area. 
    # 2022-09-24 21:19:11 : added percentage and start time and end time
#To do
    # add entry for start time and end time 
    # Add Looping mechnism 
    # The output should go into the text file
    # Do something for time taken




################################################################

#for todays input date
print("-------------------------------")

from datetime import date

today = date.today()
print("Today's date:", today)
print("-------------------------------")

#user Input
bookName = input("Book name: ")
TestArea = input("Test Area: ")
PageNum = input("Page Number: ")


#NoOfQuesAttempt = input("overall number of attempted questions: ")

#TIME ( start and end )
print("-------------------------------")
print ("To be written in 24 hour format eg: 0900, 0632, 1200, 1452, 1351")

StartTime = int(input("Start time: "))
EndTime = int(input("End time: "))
Timetaken = StartTime - EndTime

print("-------------------------------")

#create a loop for here
RightQues = int(input("Right: "))
WrongQues = int(input("Wrong: "))
UnattemptQues = int(input("Unattempted: "))
#to here

print("-------------------------------")
 
#to check wether the OVERALL NO. OF QUES is ok
sum = int(RightQues+WrongQues+UnattemptQues)

#for PERCENTAGE
percentage = (((RightQues * 3) - WrongQues) / sum)*100
print ("Right percentage: " + str(int(percentage)) + "%")

#for OVERALL QUESTIONS
print ("overall questions: " + str(int(sum)))

#to get time taken
print ("Time taken: " + str(int(Timetaken)))




