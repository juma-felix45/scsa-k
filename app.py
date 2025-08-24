from flask import Flask, render_template

app = Flask(__name__)

# Sample council members
council_members = [
    {"name": "John Doe", "position": "President", "photo": "john.jpg"},
    {"name": "Jane Smith", "position": "Vice President", "photo": "jane.jpg"},
]

# Sample events
events = [
    {
        "title": "Masinde University Event",
        "description": "Networking and knowledge sharing with students.",
        "image": "masinde_event.jpg",
    },
    {
        "title": "KCA University Event",
        "description": "Leadership and innovation workshop at KCA.",
        "image": "kca_event.jpg",
    },
]

@app.route("/")
def home():
    return render_template("index.html", council=council_members, events=events)

if __name__ == "__main__":
    app.run(debug=True)
