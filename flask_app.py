from flask import Flask, stream_template, render_template

app = Flask(__name__, subdomain_matching=True, template_folder='html', static_folder='')


@app.route('/')
def home():
    return render_template('index.html')
    return stream_template('index.html')

@app.route('/', subdomain ='testsubdomain')
def testsubdomain():
    return stream_template('testsubdomain.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')