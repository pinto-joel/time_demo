def seconds_difference(time_1, time_2):
    return time_2 - time_1

def hours_difference(time_1, time_2):
    return ((time_2 - time_1) / 60) / 60

def to_float_hours(hours, minutes, seconds):
    return hours + (minutes / 60) + (seconds / 60 / 60)

def to_24_hour_clock(hours):
    return hours % 24

def get_hours(seconds):
    return to_24_hour_clock(seconds // 3600)

def get_minutes(seconds):
    return (seconds % 3600) // 60

def get_seconds(seconds):
    return (seconds % 3600) % 60

def time_to_utc(utc_offset, time):
    return to_24_hour_clock(time - utc_offset)

def time_from_utc(utc_offset, time):
    return to_24_hour_clock(time + (utc_offset))
