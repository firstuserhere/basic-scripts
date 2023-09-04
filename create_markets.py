import requests
import json
import datetime
import time

def datetime_to_epoch_milliseconds(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000.0)

# API endpoint and authorization key
BASE_URL = "https://manifold.markets/api/v0"
AUTH_KEY = ""  # Replace with your key

def create_match_market(teamA, teamB, closeTime=None):
    close_time = datetime_to_epoch_milliseconds(closeTime)

    # Prepare the market data
    data = {
        "outcomeType": "MULTIPLE_CHOICE",
        "question": f"{teamA} vs {teamB} : Premier League 2023-24",
        "answers": [f"{teamA} wins", f"{teamB} wins", "Draw"],
        "closeTime": close_time
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Key {AUTH_KEY}"
    }

    # Send the request to create the market
    response = requests.post(f"{BASE_URL}/market", headers=headers, data=json.dumps(data))
    
    return response.json()

if __name__ == "__main__":
    # Dictionary of matches organized by date
    matches_by_date = {
        #September
        datetime.datetime(2023, 9, 24): [("Crystal Palace", "Fulham"), ("Luton", "Wolves"), ("Manchester City", "Nottingham Forest"), ("Brentford", "Everton")],
        datetime.datetime(2023, 9, 25): [("Burnley", "Man United"), ("Arsenal", "Tottenham Spurs"), ("Brighton", "Bournemouth"), ("Chelsea", "Aston Villa"), ("Liverpool", "West Ham"), ("Sheffield United", "Newcastle")],
        datetime.datetime(2023, 9, 30): [("Aston Villa", "Brighton"), ("Bournemouth", "Arsenal"), ("Everton", "Luton"), ("Man United", "Crystal Palace"), ("Newcastle", "Burnley"), ("West Ham", "Sheffield United"), ("Wolves", "Manchester City"), ("Tottenham Spurs", "Liverpool")],
        
        #October
        
    }

    for date, matches in matches_by_date.items():
        for match in matches:
            result = create_match_market(match[0], match[1], date)
            print(result)
            time.sleep(3)
