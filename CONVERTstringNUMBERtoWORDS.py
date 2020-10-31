from datetime import datetime

object = "12.09.2020"
print("\033[1m" + "\nExample input: " + "\033[0m", object)

#First convert to valid datetime object by using correct % operator
#forhow they are currently formatted
#See https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#for full list
print("\033[1m" + "\nCode snippet to convert example object to datetime object"+ "\033[0m")
print("\033[4m" + "object = datetime.strptime(object, %d.%m.%Y)" + "\033[0m")

object = datetime.strptime(object, "%d.%m.%Y")

print("\033[1m" + "\nFormat of datetime object"+ "\033[0m", object, "\n")


#Now that it is in a datetime object, we can extract words from it
#using strftime again but using different % operators
print("\033[1m" + "Year: "+ "\033[0m", object.strftime("%Y"))
print("\033[1m" + "Month (By Name): "+ "\033[0m", object.strftime("%B"))
print("\033[1m" + "Day (By Name): "+ "\033[0m", object.strftime("%A"))

print("\nWe can extract the date data in many different formats.")
print("Check out " + "\033[4m" + "https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior" + "\033[0m" + " for full list")
