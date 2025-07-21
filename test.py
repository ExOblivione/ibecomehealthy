from smoke import stopSmoking
from handleUserData import get_user_data
from smokeagent import smokeagent

# Main execution
if __name__ == "__main__":
    # Get user data (either from JSON or terminal input)
    age, cigarettes_per_day, quit_date, quit_hour, quit_minute, cost_per_pack, cigarettes_per_pack = get_user_data()
    
    # Call the stopSmoking function with the user data
    calculation_results = stopSmoking(age, cigarettes_per_day, quit_date, quit_hour, quit_minute, cost_per_pack, cigarettes_per_pack) 
    # Call the Smoke Agent with the calculated values
    response = smokeagent(calculation_results, age)

    print(response)
    
    # Quit execution after results are provided
    exit()