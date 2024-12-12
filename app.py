from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/unit')
def unit():
    return render_template('unit.html')

@app.route('/flashcards')
def flashcards():
    subject = request.args.get('subject')
    flashcards_data = []
    if subject:
        csv_file = f'{subject}_flashcards_data.csv'
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                flashcards_data.append({'front': row[0], 'back': row[1]})
    return render_template('flashcards.html', flashcards=flashcards_data)

if __name__ == '__main__':
    app.run(debug=True)
