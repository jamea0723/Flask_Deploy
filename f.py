from flask import flask, jsonify
import gdown

@app.route('/')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1hkPjTv36IZDooR_3LJc6LU5K39alluWP?usp=drive_link', 'tradingbot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
