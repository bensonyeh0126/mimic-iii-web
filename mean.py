#!flask/bin/python


##python 3.6.8
#xgboost 1.3.3


from flask import Flask, request, render_template, jsonify  # 記得要import render_template
from flask_cors import CORS
import numpy as np
import model.model as model
app = Flask(__name__)
CORS(app)
# 網頁執行/say_hello時，會導至index.html


@app.route('/', methods=["GET"])
def getdata():
 return render_template('index.html')

# index.html按下submit時，會取得前端傳來的username，並回傳"Hellold! "+name


@app.route('/', methods=["POST"])
def submit():
    D1_pulse = request.form.get("D1_pulse")
    D2_pulse = request.form.get("D2_pulse")
    D1_SPO2 = request.form.get("D1_SPO2")
    D2_SPO2 = request.form.get("D2_SPO2")
    D1_SBP = request.form.get("D1_SBP")
    D2_SBP = request.form.get("D2_SBP")
    D2_DBP = request.form.get("D2_DBP")
    D2_PAW = request.form.get("D2_PAW")
    D2_MAPS = request.form.get("D2_MAPS")
    WBC = request.form.get("WBC")
    PLT = request.form.get("PLT")
    BUN = request.form.get("BUN")
    NEUT = request.form.get("NEUT")
    HGB = request.form.get("HGB")
    ALB = request.form.get("ALB")
    ALKP = request.form.get("ALKP")
    BILT = request.form.get("BILT")
    LACTATE = request.form.get("LACTATE")
    PTP = request.form.get("PTP")
    CREAT = request.form.get("CREAT")
    Urine_D0 = request.form.get("Urine_D0")
    Urine_D1 = request.form.get("Urine_D1")
    Urine_D2 = request.form.get("Urine_D2")
    D0_temperature = request.form.get("D0_temperature")
    D1_temperature = request.form.get("D1_temperature")
    D2_temperature = request.form.get("D2_temperature")
    D1_FIO2 = request.form.get("D1_FIO2")
    D2_FIO2 = request.form.get("D2_FIO2")

    input = np.array([[D1_pulse,D2_pulse,D1_SPO2,D2_SPO2,D1_SBP,D2_SBP,D2_DBP,D2_PAW,D2_MAPS,WBC,PLT,BUN,NEUT,HGB,ALB,ALKP,BILT,
                      LACTATE,PTP,CREAT,Urine_D0,Urine_D1,Urine_D2,D0_temperature,D1_temperature,D2_temperature,D1_FIO2,D2_FIO2]])
    result = model.predict(input)

    
    return jsonify({"prediction":str(result)})

if __name__ == '__main__':
 app.run(debug=True, port=80)
