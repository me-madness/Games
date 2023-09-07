from flask import Flask, render_template, redirect, request
import random
app = Flask(__name__)

rows = 3
cols = 9

def generate_random_fruits():
    fruits = [[] for row in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            r = random.randint(0, 8)
            if r < 2:
                fruits[row].append('apple')
            elif r < 4:
                fruits[row].append('banana')
            elif r < 6:
                fruits[row].append('orange')
            elif r < 8:
                fruits[row].append('kiwi')
            else:
                fruits[row].append('dynamite')
    return fruits            
                            
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
