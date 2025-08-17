from flask import Flask, render_template, request

from model import regressor_model

app = Flask(__name__)

@app.route('/bill', methods=['GET', 'POST'])
def Calculate_bill():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        u = int(request.form['units'])
        c = float(request.form['charges'])
        bill = u * c
        return f"Your bill is {bill}"


@app.route('/Sem', methods=['GET', 'POST'])
def Calculate_Semester():
    if request.method == 'GET':
        return render_template('semester.html')
    elif request.method == 'POST':
        u = int(request.form['Marks1'])
        c = int(request.form['Marks2'])
        avg = u + c / 2
        total = 200
        per = (u + c) / total * 100
        return f"Your Average  is {avg}"
        return f"Your Percentage is {per}%"

@app.route('/', methods=['GET', 'POST'])
def Sales():
    if request.method == 'GET':
        return render_template('Salespredictor.html')
    elif request.method == 'POST':
        t = float(request.form['TV'])
        r = float(request.form['Radio'])
        n = float(request.form['Newspaper'])
        op= regressor_model.predict([[t, r, n]])
        Y_pred = round(op[0],2)
        return render_template('Result.html', Predicted_sales =Y_pred)

if __name__ == '__main__':
    app.run(debug=True)