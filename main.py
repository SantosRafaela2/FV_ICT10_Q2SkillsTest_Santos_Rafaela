from flask import Flask, render_template

app = Flask(__name__)

# Dictionary of clubs
clubs = {
    "Marching Band": {
        "description": "A performance group specializing in musical marching routines.",
        "meeting_time": "Tuesday and Wednesday 03:00–4:30 PM",
        "location": "Band Room",
        "moderator": "Mr. Emilio Alumno",
        "category": "Performing Arts"
    },
    "Glee Club": {
        "description": "A vocal group for students who enjoy singing and choral music.",
        "meeting_time": "Monday 03:00–05:00 PM",
        "location": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "category": "Performing Arts"
    },
    "Dance Club": {
        "description": "A club for students who love performing and exploring dance.",
        "meeting_time": "Tuesday 03:00–05:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "category": "Performing Arts"
    },
    "Math Club": {
        "description": "A club that enhances mathematical skills through challenges and activities.",
        "meeting_time": "Monday 02:30–03:00 PM",
        "location": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "category": "Academic"
    },
    "Science Club": {
        "description": "A club for students who love experiments and scientific exploration.",
        "meeting_time": "Tuesday 03:00–04:00 PM",
        "location": "Room 404",
        "moderator": "Ms. Jameelyn Maramag",
        "category": "STEM"
    },
    "Communications Arts Club": {
        "description": "A club focusing on creative writing, public speaking, and media arts.",
        "meeting_time": "Wednesday 03:00–04:00 PM, Friday 03:00–04:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "category": "Arts & Literature"
    },
  
}


@app.route("/")
def index():
    return render_template("index.html", clubs=clubs)


if __name__ == "__main__":
    app.run(debug=True)

