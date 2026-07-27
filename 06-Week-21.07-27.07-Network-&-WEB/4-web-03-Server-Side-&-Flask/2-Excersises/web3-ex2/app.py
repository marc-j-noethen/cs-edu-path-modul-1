from flask import Flask, render_template

app = Flask(__name__)


@app.route('/user/<username>')
def hello(username):
    p_lang = 'Python'
    u_hobby = ['Gym', 'Coding', 'Hacking']

    return render_template("profile.html", username=username,p_lang=p_lang, u_hobby=u_hobby) 

if __name__ == "__main__":
    app.run(debug=True)
