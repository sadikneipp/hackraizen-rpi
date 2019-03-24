from flask import Flask
from blink import *

app = Flask(__name__)

@app.route('/123123')
def change_red():
    set_color('r', 10)
    return 'vermelho'

@app.route('/666666')
def change_blue():
    set_color('b', 10)
    return 'azul'

@app.route('/000001')
def change_green():
    set_color('g', 10)
    return 'verde'

@app.route('/112233')
def change_yellow():
    set_color('y', 10)
    return 'amarelo'

@app.route('/321321')
def change_pink():
    set_color('p', 10)
    return 'rosa'