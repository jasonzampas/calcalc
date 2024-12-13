from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    answer = None

    if request.method == "POST":
        height = request.form['height'] 
        weight = request.form['weight'] 
        age = request.form['age'] 
        exercise = int(request.form['exercise'])

        if exercise == 1:
            answer = round(((10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5) * 1.2)
        elif exercise == 2:
            answer = round(((10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5) * 1.375)
        elif exercise == 3:
            answer = round(((10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5) * 1.55)
        elif exercise == 4:
            answer = round(((10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5) * 1.725)

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)