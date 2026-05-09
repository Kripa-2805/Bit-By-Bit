from flask import Flask, render_template, jsonify

app = Flask(__name__)

TEAMS_DATA = {
    "Technical": {
        "lead": "Aryan Verma",
        "co_lead": "Sanya Malhotra",
        "core": ["Ishaan Singh", "Meera Rao", "Kabir Khan", "Ananya D."]
    },
    "PR and Outreach": {
        "lead": "Manav G.",
        "co_lead": "Sia K.",
        "core": ["Yash R.", "Tanya V.", "Omer S."]
    },
    "Design": {
        "lead": "Riya Kapoor",
        "co_lead": "Arjun Das",
        "core": ["Tara S.", "Zayn M.", "Kyra G."]
    },
    "Event Management": {
        "lead": "Armaan J.",
        "co_lead": "Nandini S.",
        "core": ["Pranav L.", "Deepak K.", "Simran M."]
    },
    "Social Media": {
        "lead": "Kiara Advani",
        "co_lead": "Varun D.",
        "core": ["Sneha W.", "Aditi P.", "Rahul J."]
    },
    "Content": {
        "lead": "Devansh S.",
        "co_lead": "Ipsita R.",
        "core": ["Siddharth B.", "Rohan M."]
    },
    "Finance": {
        "lead": "Raghav B.",
        "co_lead": "Esha T.",
        "core": ["Amit S.", "Gaurav P."]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/teams')
def get_teams():
    return jsonify(TEAMS_DATA)

if __name__ == '__main__':
    app.run(debug=True)
