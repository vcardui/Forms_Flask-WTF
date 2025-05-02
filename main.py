'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from wsgiref.validate import validator

# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: April 30th, 2025
# | Last update..: April 30th, 2025
# | WhatIs.......: Forms_Flask-WTF - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Flask-WTF Basic fields: https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields
# Flask-WTF Validators: https://wtforms.readthedocs.io/en/3.0.x/validators/#module-wtforms.validators

# Regex for Special Characters in Passwords: https://formulashq.com/the-ultimate-guide-to-regex-for-password-validation/

# ------------------------- Libraries -------------------------
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import email_validator
from wtforms.validators import DataRequired, InputRequired, Email, Length, Regexp


# ------------------------- Classes -------------------------
class LoginForm(FlaskForm):
    email = StringField("Email", [
        Length(min=6, max=25),
        InputRequired("Please enter your email address"),
        Email(
            message="This field requires a valid email address",
            granular_message=True,
        check_deliverability=True,
            allow_smtputf8=False
        )
    ])
    password = PasswordField('Password', [
        InputRequired("Please enter your password"),
        Regexp(
            regex="^(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$",
            message="The password must contain: alphanumeric characters, at least one special character and be between 8 and 16 characters long"
        )
    ])
#    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


# ------------------------- Variables -------------------------
app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
# app.config['SECRET_KEY'] = secrets.token_hex(16)

bootstrap = Bootstrap5(app)

# --------------------------- Code ----------------------------
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        print(login_form.password.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "aabb$12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        print("Validation not passed")
    return render_template("login.html", form=login_form)

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
