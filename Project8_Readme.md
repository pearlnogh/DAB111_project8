# Gym Member Tracking App (Flask + SQLite)

A simple Flask web application to manage and display gym member information.
Users can add members details including Age, Gender, Weight (kg), Height (m),  Avg_BPM, Session_Duration (hours), Calories_Burned, Workout_Type, Water_Intake(liters), Workout_Frequency (days/week) ,and BMI.
All records are displayed on the datapage.

## Project Structure

```
DAB111_Project8/
├── Gym Members Tracking.csv             
├── load_member.ipynb             
├── gym_members_tracking.db     # Contains the SQLite DB   
├── app_member_track.py         # Flask web app       
├── templates/                  # HTML templates                
│   ├── home.html
│   ├── about.html
│   └── data.html
└── static/                   
│   └── style.css
├── requirements.txt                # Python dependencies              
└── README.md                     
```

## Setup

```bash
cd DAB111_Project8
pip install -r requirements.txt
python app_member_track.py
```

Then open `http://127.0.0.1:5000 ` in your browser.
