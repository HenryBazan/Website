#Link to site on Render https://pythonwebsite01.onrender.com
#Link to site to push changes https://dashboard.render.com/web/srv-cgs2kt82qv20m9n6q6cg/deploys/dep-cgs3eq82qv20m9nb4o30
from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

@app.route("/")
def homepage():
    name="Henry Bazan"
    details = readDetails('PersonalSite\static\details.txt')
    return render_template('base.html',name=name, aboutMe=details)

#@app.route('/user/<name>')
#def greet(name):
 #   return f'<p>Hello,{name}. My Love!</p>'


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name=None
    if request.method=='POST':
        name = request.form['name']
        return render_template('form.html', name=name, aboutMe=[])
    
    return render_template('form.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
