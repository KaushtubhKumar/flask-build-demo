from flask import Flask

app = Flask(__name__)
def add(a, b):
    return a + b

@app.route("/")
def home():
    return "Hello from CodeBuild demo"

if __name__ == "__main__":
    app.run()
