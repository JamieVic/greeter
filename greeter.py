import datetime

getDate = datetime.datetime.now()
day = getDate.strftime("%A")
username = input("Enter Name: ")
if day == "Sunday":
    print("Hello " + username + "! Today is " + day + ", don't panic the weekend isn't over.. yet.")
elif day == "Monday":
    print("Hello " + username + "! Today is " + day + ", it's time to go back to work (unfortunately).")
elif day == "Tuesday":
    print("Hello " + username + "! Today is " + day + ", at least it's not Monday.")
elif day == "Wednesday":
    print("Hello " + username + "! Today is " + day + ", happy hump day!")
elif day == "Thursday":
    print("Hello " + username + "! Today is " + day + ", looking forward to the weekend yet?")
elif day == "Friday":
    print("Hello " + username + "! Today is " + day + ", have a great weekend!")
elif day == "Saturday":
    print("Hello " + username + "! Today is " + day + ", hope you're having a fun weekend!")