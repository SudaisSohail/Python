import time

#epoch is a date and time from where computer thinks time begins

print(time.time())  # Returns seconds since epoch 

print(time.time_ns())  # Returns nanoseconds since epoch

print(time.ctime(0))   # Returns time in readable form since epoch. Takes seconds as argument.

print(time.ctime(time.time()))

print(time.monotonic())  # Don't take any argument. Returns monotonic time

print(time.monotonic_ns())  # Returns monotonic time in nanoseconds

current_time = time.localtime()  # Returns struct time
current_time = time.gmtime()  # Returns struct time
print(current_time)


# Takes first format and then time(tuple or struct time) and convert time into format provided
current_readable_time = time.strftime("%B %d, %Y   %I:%M:%S", current_time)    
print(current_readable_time)

# Takes first time and then format of the time and convert it into struct time
time_string = "20 October, 2021"
time_object = time.strptime(time_string, "%d %B, %Y")  
#print(time_object)

# time tuple(year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)

time_tuple = (2021, 10, 2, 14, 56, 49, 5, 0, 0)  # Example of time tuple
time_string = time.asctime(current_time)  # coverts time tuple or struct time into time string
print(time_string)

time_tuple = (2021, 10, 2, 14, 56, 49, 5, 0, 0)  # Example of time tuple
time_string = time.mktime(current_time)  # coverts time tuple or struct time into seconds since epoch 
print(time_string)

time.sleep(1)  # delays the execution of code ahead for seconds given

print(time.strftime("\nDate: %B %d, %Y\nTime: %I:%M:%S %p", time.localtime())) # A perfect Date and Time representation
