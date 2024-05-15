start ../AirSimNH.exe -settings "{\"SettingsVersion\": 1.2, \"SimMode\": \"Multirotor\"}"
timeout /T 7
start "controller" /B python controller.py 
start python detection.py