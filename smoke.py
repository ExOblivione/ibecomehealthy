import datetime
from smokeagent import smokeagent

def stopSmoking(age, cigarettes_per_day, quit_date, quit_hour, quit_minute, cost_per_pack, cigarettes_per_pack):
    
    # count time in seconds from the last cigarette smoked
    if isinstance(quit_date, datetime.date) and not isinstance(quit_date, datetime.datetime):
        quit_date = datetime.datetime.combine(quit_date, datetime.time())
    
    quit_date = quit_date.replace(hour=quit_hour, minute=quit_minute, second=0, microsecond=0)
    now = datetime.datetime.now()
    time_since_quit = (now - quit_date).total_seconds()
    # Calculate the number of cigarettes not smoked
    cigarettes_not_smoked = (time_since_quit / 86400) * cigarettes_per_day
    # Calculate money saved
    money_saved = (cigarettes_not_smoked / cigarettes_per_pack) * cost_per_pack    
    
    # recalculate time_since_quit into years, months, weeks, days, minutes (hierarchical breakdown)
    remaining_seconds = time_since_quit
    
    years = int(remaining_seconds // 31536000) # 365 * 24 * 60 * 60
    remaining_seconds %= 31536000
    
    months = int(remaining_seconds // 2592000) # 30 * 24 * 60 * 60
    remaining_seconds %= 2592000
    
    weeks = int(remaining_seconds // 604800) # 7 * 24 * 60 * 60
    remaining_seconds %= 604800
    
    days = int(remaining_seconds // 86400) # 24 * 60 * 60
    remaining_seconds %= 86400
    
    hours = int(remaining_seconds // 3600) # 60 * 60
    remaining_seconds %= 3600
    
    minutes = int(remaining_seconds // 60)

    return years, months, weeks, days, hours, minutes, cigarettes_not_smoked, money_saved