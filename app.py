from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Dummy user credentials (for demo only)
USER = {"username": "user", "password": "music123"}


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/library')
def library_page():
    return render_template('library.html')


@app.route('/nowplaying')
def nowplaying_page():
    return render_template('nowplaying.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
