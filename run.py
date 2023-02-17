from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_data = request.form
        # Do something with user_data, such as storing it in a database
        return 'Data submitted successfully!'
    else:
        return '''
        <form method="post">
            <label for="name">Name:</label>
            <input type="text" name="name"><br>
            <label for="email">Email:</label>
            <input type="email" name="email"><br>
            <button type="submit">Submit</button>
        </form>
        '''

if __name__ == '__main__':
    app.run()
