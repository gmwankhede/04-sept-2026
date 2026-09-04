from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Python program Ganesh and Sonu successfully.")
    print("Python program second line update by  Ganesh and Sonu  successfully.")
    return "Push by Sonu"

if __name__ == "__main__":
    app.run()
