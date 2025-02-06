def add_time(start, duration, weekday=None):
    # Split start time into hours, minutes and period (AM/PM)
    start_hour, start_minute_period = start.split(':')
    start_minute, period = start_minute_period.split(' ')
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    
    # Adjust for 12-hour format (convert PM hours to 24-hour format)
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Split the duration into hours and minutes
    duration_hour, duration_minute = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)
    
    # Add the duration time to the start time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
    # Handle minutes overflow (e.g. 70 minutes becomes 1 hour and 10 minutes)
    if new_minute >= 60:
        new_hour += new_minute // 60
        new_minute = new_minute % 60
    
    # Handle hours overflow (e.g. 25 hours becomes 1 hour the next day)
    new_day_count = new_hour // 24
    new_hour = new_hour % 24
    
    # Convert back to 12-hour format
    if new_hour == 0:
        new_hour = 12
        period = 'AM'
    elif new_hour < 12:
        period = 'AM'
    elif new_hour == 12:
        period = 'PM'
    else:
        new_hour -= 12
        period = 'PM'
    
    # Determine the result string
    time_str = f"{new_hour}:{new_minute:02d} {period}"
    
    # If a weekday is provided, calculate the resulting weekday
    if weekday:
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        weekday = weekday.lower()
        starting_day_index = days_of_week.index(weekday)
        
        result_day_index = (starting_day_index + new_day_count) % 7
        result_day = days_of_week[result_day_index].capitalize()
        
        if new_day_count == 1:
            time_str += f", {result_day} (next day)"
        elif new_day_count > 1:
            time_str += f", {result_day} ({new_day_count} days later)"
        else:
            time_str += f", {result_day}"
    elif new_day_count == 1:
        time_str += " (next day)"
    elif new_day_count > 1:
        time_str += f" ({new_day_count} days later)"
    
    return time_str

print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
