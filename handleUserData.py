import json
import datetime

def get_user_data():
    # get user id from terminal
    user_id = input("Enter your user ID: ").strip()
    
    # Ask if they want to record smoking (only if user exists)
    try:
        with open('user_health_data.json', 'r') as file:
            data = json.load(file)
        
        if user_id in data and 'smoking' in data[user_id]:
            record_smoking = input("I just smoked (y/n): ").strip().lower()
            if record_smoking == 'y' or record_smoking == 'yes':
                return handle_smoking_relapse(user_id, data)
    except FileNotFoundError:
        pass
    
    # get user health data from user_health_data.json or from terminal if id does not exist in the json file
    try:
        with open('user_health_data.json', 'r') as file:
            data = json.load(file)
        
        if user_id in data and 'smoking' in data[user_id]:
            # print(f"Found existing data for user {user_id}")
            user_data = data[user_id]['smoking']
            
            # Convert quit_date string to datetime.date
            quit_date = datetime.datetime.strptime(user_data['quit_date'], '%Y-%m-%d').date()
            return (
                user_data['age'],
                user_data['cigarettes_per_day'],
                quit_date,
                user_data['quit_hour'],
                user_data['quit_minute'],
                user_data['cost_per_pack'],
                user_data['cigarettes_per_pack']
            )
        else:
            print(f"No data found for user {user_id}. Please enter your information:")
            return get_user_input_from_terminal(user_id, data)
            
    except FileNotFoundError:
        print("user_health_data.json not found. Please enter your information:")
        return get_user_input_from_terminal(user_id, {})

def get_user_input_from_terminal(user_id, existing_data):
    # Get user input from terminal
    age = int(input("Enter your age: "))
    cigarettes_per_day = int(input("Enter cigarettes per day you used to smoke: "))
    
    quit_date_str = input("Enter quit date (YYYY-MM-DD): ")
    quit_date = datetime.datetime.strptime(quit_date_str, '%Y-%m-%d').date()
    
    quit_hour = int(input("Enter quit hour (0-23): "))
    quit_minute = int(input("Enter quit minute (0-59): "))
    cost_per_pack = float(input("Enter cost per pack: "))
    cigarettes_per_pack = int(input("Enter cigarettes per pack: "))
    
    # Save the new data to JSON file
    user_data = {
        'age': age,
        'cigarettes_per_day': cigarettes_per_day,
        'quit_date': quit_date_str,
        'quit_hour': quit_hour,
        'quit_minute': quit_minute,
        'cost_per_pack': cost_per_pack,
        'cigarettes_per_pack': cigarettes_per_pack
    }
    
    existing_data[user_id] = {'smoking': user_data}
    
    with open('user_health_data.json', 'w') as file:
        json.dump(existing_data, file, indent=2)
    
    print(f"Data saved for user {user_id}")
    
    return (age, cigarettes_per_day, quit_date, quit_hour, quit_minute, cost_per_pack, cigarettes_per_pack)

def modify_user_data(user_id, new_data):
    try:
        with open('user_health_data.json', 'r') as file:
            data = json.load(file)
        
        if user_id in data and 'smoking' in data[user_id]:
            data[user_id]['smoking'].update(new_data)
            with open('user_health_data.json', 'w') as file:
                json.dump(data, file, indent=2)
            print(f"Data updated for user {user_id}")
        else:
            print(f"No existing data found for user {user_id}.")
    
    except FileNotFoundError:
        print("user_health_data.json not found.")

def handle_smoking_relapse(user_id, data):
    """Handle when user wants to record that they smoked - reset quit time to now"""
    current_datetime = datetime.datetime.now()
    
    # Update quit date and time to current moment
    data[user_id]['smoking']['quit_date'] = current_datetime.strftime('%Y-%m-%d')
    data[user_id]['smoking']['quit_hour'] = current_datetime.hour
    data[user_id]['smoking']['quit_minute'] = current_datetime.minute
    
    # Save updated data
    with open('user_health_data.json', 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"Smoking recorded for user {user_id}. Quit time reset to {current_datetime.strftime('%Y-%m-%d %H:%M')}")
    
    user_data = data[user_id]['smoking']
    return (
        user_data['age'],
        user_data['cigarettes_per_day'],
        current_datetime.date(),
        user_data['quit_hour'],
        user_data['quit_minute'],
        user_data['cost_per_pack'],
        user_data['cigarettes_per_pack']
    )