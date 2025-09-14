from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Cali Roleplay Network Python app is running!'

if __name__ == '__main__':
    app.run(debug=True)
