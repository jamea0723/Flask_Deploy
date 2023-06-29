from flask import flask, jsonify
import gdown

@app.route('/')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1IQVPqnOrc3dIP7NrY0GPvMIGvKARbeXJ?usp=drive_link', 'tradingbot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
