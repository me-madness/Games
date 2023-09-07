from flask import Flask, render_template, redirect, request
import random
app = Flask(__name__)

rows = 3
cols = 9

fruits = generate_random_fruits()

score = 0
game_over = False

@app.route('/')
def index():
	return render_template('index.html')
	rows=rows, cols=cols, fruits=fruits,
	game_over=game_over, score=score

if __name__ == '__main__':
	app.run()
