from flask import Flask
from flask import Flask, render_template, request, redirect


from bus_board_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/heartbeat')
def index():
    return 'Hello World!'

@app.route('/')
def home():
    return render_template('index.html',current_location="NW5 1TL")


if __name__ == '__main__':
    app.run()
