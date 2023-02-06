from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'The code is working'
    return '''
        <form method="post">
            <input type="text" name="text">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run()
