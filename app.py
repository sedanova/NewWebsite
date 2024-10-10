# app.py
from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def home():
    return """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>New Website</title>
                </head>
                <body>
                    <style>
                        div{
                            width: 100%;
                            height: 100vh;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                        }
                    </style>
                    <div>
                        <span>
                            Warrior x
                        </span>
                    </div>
                </body>
                </html>"""


if __name__ == '__main__':
    app.run()
