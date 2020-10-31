from datetime import datetime

object = "12.09.2020"
print("\nExample input: ", object)
print("****************************")
#First convert to valid datetime object by using correct % operator
#forhow they are currently formatted
#See https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#for full list
print("\nCode snippet to convert example object to datetime object")
print("object = datetime.strptime(object, %d.%m.%Y)")

object = datetime.strptime(object, "%d.%m.%Y")
print("****************************")
print("\nFormat of datetime object\n", object)


#Now that it is in a datetime object, we can extract words from it
#using strftime again but using different % operators
print("****************************\n")
print("Year: ", object.strftime("%Y"))
print("Month (By Name): ", object.strftime("%B"))
print("Day (By Name): ", object.strftime("%A"))
print("****************************")
print("\nWe can extract the date data in many different formats.")
print("Check out https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior for full list")
print("****************************")
