from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_data = request.form
        # Do something with user_data, such as storing it in a database
        return render_template('thanks.html')
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run()
