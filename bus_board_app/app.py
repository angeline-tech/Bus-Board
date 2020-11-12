from flask import Flask
from flask import Flask, render_template, request, redirect


from bus_board_app.flask_config import Config

from bus_board_app.services.transport_serivce import getLiveBusForATCO

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/heartbeat')
def index():
    return 'Hello World!'

@app.route('/')
def home():
    result = getLiveBusForATCO()
    return render_template('index.html', data=result)


if __name__ == '__main__':
    app.run()
