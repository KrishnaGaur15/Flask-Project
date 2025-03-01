from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print('home Page')
    return 'welcome to flask app!'

if __name__ == '__main__':
    print('Entering into the application')
    app.run(debug=True)