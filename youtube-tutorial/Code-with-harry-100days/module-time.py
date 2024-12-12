"""\
The time module in Python provides various time-related functions that allow you to work with dates, timestamps, and perform operations like measuring time intervals, formatting dates, or pausing execution.

Code	    Description	            Example
%Y	            Year            (4 digits)	2024
%m	            Month (01-12)	      12
%d	        Day of the month	      07
%H	            Hour (00-23)	      13
%M	            Minute (00-59)	      50
%S	            Second (00-59)	      00
%a	           Abbreviated weekday	  Sat
%A	            Full weekday	    Saturday
%b	        Abbreviated month name	  Dec
%B	        Full month name	        December

Attributes in time module

time.timezone (Offset in seconds from UTC for the local standard time.) it returns output in secs if it is in negative then it represents east of utc
time.altzone (Offset in seconds from UTC for the local daylight saving time.) if negative east of UTC 
time.daylight (1 if daylight saving time is in effect; 0 otherwise.)
time.tzname (Tuple of names: (standard_time, daylight_saving_time).)

1. Clock manipulation and Timestamp
   1.1 time.time()
        it return total time from epoch (January 1, 1970, 00:00:00 UTC)
        in floating point value
        it dosent take any argument.
        it can be used with other methods as shown in eg.
    
   1.2 time.sleep(seconds)
        Pauses the program execution for the given number of seconds.

   1.3 time.localtime([timestamp])
        Converts a timestamp (seconds since the epoch) to a struct_time object representing local time. If no timestamp is provided, it uses the current time.
        Daylight Saving Time (isdst) 1:- applicable 0:- Not applicable -1:- No information avl
        If no timestamp provided it will use local time
        tm_yday :- day of the year
        tm_wday :- Weekday (0=Monday, 6=Sunday)
        A time.struct_time object is a named tuple
   
   1.4 time.gmtime([timestamp]) 
        same as previous method but it represents in UTC
   
   1.5 time.mktime([struct_time])
        Converts a struct_time object to a timestamp

   1.6 time.ctime([timestamp])
        Converts a timestamp (seconds since the epoch) into a readable string. If no timestamp is provided, it uses the current time.

   1.7 time.asc([struct_time])
        Converts a struct_time object into a readable string. If no struct_time is provided, it uses the current local time.

2. Formatting & Parsing

   2.1 time.strftime(format[, struct_time])
        Formatting refers to converting a struct_time object or timestamp into a readable string format.
        format is what we have defined in up struct time is format of time object
        
   2.2 time.strptime(string[, format])
          Parses a time string based on a specific format string.
          Input:
          string: A time string to parse (e.g., "2024-12-07 15:45:00").
          format: The expected format of the string.
          it will give output a struct time object

3. High-Resolution Timers

   3.1 time.perf_counter()
          Returns a high-resolution timer value (seconds as a float) with the highest available accuracy.
          Includes time spent during sleep or suspension of the system.
   
   3.2 time.perf_counter_ns()
          Returns the performance counter as an integer in nanoseconds, similar to time.perf_counter() but with higher resolution.

   
   3.3 time.monotonic()
          Returns the value of a monotonic clock, which cannot go backward. Useful for measuring durations.
   
   3.4 time.monotonic_ns()
          Returns the monotonic clock value as an integer in nanoseconds for high-resolution timing.

4. CPU and Thread Timing
   
   4.1 time.process_time()
          Returns the CPU time consumed by the current process (does not include sleep).

   4.2 time.process_time_ns()
          Similar to time.process_time() but returns the CPU time in nanoseconds.

   4.3 time.thread_time()
          Returns the CPU time (in seconds) used by the current thread.

   4.4 time.thread_time_ns() 
          Returns the CPU time for the current thread in nanoseconds.

  
5. Time Zone Management

   5.1 time.tzset()
        Resets the timezone based on the TZ environment variable.


"""
import time

print("Attributes **************** Starts")

print(time.timezone)
print(time.altzone)
print(time.daylight)
print(time.tzname)

print("Attributes **************** Ends")
print()
print()

print("Clock manipulation and timestamp **************** Starts")

timestamp = time.time()
readable_time = time.ctime(timestamp)
print(f"Readable time: {readable_time}")

print("Start")
time.sleep(3)  # Pauses for 3 seconds
print("End after 3 seconds delay")

local_time = time.localtime(timestamp)
print(f"Local time: {local_time}") 
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=9, tm_hour=10, tm_min=40, tm_sec=9, tm_wday=0, tm_yday=344, tm_isdst=0)
print(type(local_time))

utc_time = time.gmtime(timestamp)
print(f"UTC time: {utc_time}") 

local_time = time.localtime()
timestamp = time.mktime(local_time)
print(f"Timestamp: {timestamp}")

readable_time = time.ctime()
print(f"Current time (readable): {readable_time}")

struct_time = time.localtime()
readable_time = time.asctime(struct_time)
print(f"Readable local time: {readable_time}")


print("Clock manipulation and timestamp **************** Ends")
print()




print("Formatting & Parsing ******************** Start")
print()

current_time = time.localtime()

# Format the time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(f"Formatted Time: {formatted_time}")

time_string = "2024-12-07 15:45:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")

print(f"Parsed Time: {parsed_time}")

print()
print("Formatting & Parsing ******************** End")
print()


print()
print("High Resolution Timers ******************** Start")
print()

start = time.perf_counter()
for _ in range(1000000):
    pass
end = time.perf_counter()

print(f"Elapsed Time: {end - start} seconds")

start = time.perf_counter_ns()
time.sleep(1)
end = time.perf_counter_ns()
print(f"Elapsed: {end - start} nanoseconds")

start = time.monotonic()
time.sleep(1)
end = time.monotonic()
print(f"Elapsed: {end - start} seconds")

start = time.monotonic_ns()
time.sleep(1)
end = time.monotonic_ns()
print(f"Elapsed: {(end - start) / 1e9} seconds")

print()
print("High Resolution Timers ******************** Ends")
print()


print()
print("CPU and Thread Timing ******************** Start")
print()

start = time.process_time()
for _ in range(1000000):
    pass
end = time.process_time()

print(f"CPU Time Used: {end - start} seconds")

start = time.process_time_ns()
for _ in range(10**6):
    pass
end = time.process_time_ns()
print(f"CPU Time: {end - start} nanoseconds")

start = time.thread_time()
for _ in range(10**6):
    pass
end = time.thread_time()
print(f"Thread Time: {end - start} seconds")

start = time.thread_time_ns()
for _ in range(10**6):
    pass
end = time.thread_time_ns()
print(f"Thread Time: {end - start} nanoseconds")


print()
print("CPU and Thread Timing ******************** Ends")
print()


print("Time Zone Management **************** Starts")
print()
# import os
# os.environ['TZ'] = 'America/New_York'
# time.tzset()
# print(time.strftime('%X %x %Z', time.localtime()))

print("Time Zone Management **************** Ends")



