from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Python program syntax update successfully.")
    print("Python program second line update successfully.")
    return "Hello from GitHub Actions and Azure Web App!"

if __name__ == "__main__":
    app.run()
