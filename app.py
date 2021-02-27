from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
