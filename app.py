from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "sad": "I'm sorry you're feeling sad. Remember to take care of yourself.",
    "stress": "Try taking a short break and drinking water.",
    "anxiety": "Take a deep breath. You are doing your best.",
    "happy": "That's wonderful to hear!"
}

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        user_input = request.form["message"].lower()

        for key in responses:
            if key in user_input:
                reply = responses[key]
                break

        if reply == "":
            reply = "I'm here for you. Please talk to a trusted person if needed."

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)