#!flask/bin/python


##python 3.6.8
#xgboost 1.3.3


from flask import Flask, request, render_template, jsonify  # 記得要import render_template
from flask_cors import CORS
import numpy as np
import model.model as model
app = Flask(__name__)
CORS(app)
# 網頁執行/，會導至index.html


@app.route('/', methods=["GET"])
def getdata():
 return render_template('index.html')




@app.route('/', methods=["POST"])
def submit():
    #vital_sign
    D1_temperature = request.form.get("D1_temperature")
    D2_temperature = request.form.get("D2_temperature")
    D3_temperature = request.form.get("D3_temperature")
    D3_SBP = request.form.get("D3_SBP")
    D3_DBP = request.form.get("D3_DBP")
    D3_SPO2 = request.form.get("D3_SPO2")
    D3_pulse = request.form.get("D3_pulse")
    D1_pulse = request.form.get("D1_pulse")
    
    #Lab
    BUN = request.form.get("BUN")
    NEUT = request.form.get("NEUT")
    PLT = request.form.get("PLT")
    ALB = request.form.get("ALB")
    LACTATE = request.form.get("LACTATE")
    BILT = request.form.get("BILT")
    CREAT = request.form.get("CREAT")
    
    ALKP= request.form.get("ALKP")
    WBC = request.form.get("WBC")
    HGB = request.form.get("HGB")
    PTP = request.form.get("PTP")
    

   
    #respirator
    
    D3_MAPS = request.form.get("D3_MAPS")
    D3_PAW = request.form.get("D3_PAW")
    
    #lo
    D3_Urine = request.form.get("D3_Urine")
    D2_Urine = request.form.get("D2_Urine")
    D1_Urine = request.form.get("D1_Urine")
    

    input = np.array([[D3_MAPS,PLT,D3_pulse,D2_temperature,D3_SPO2,PTP,ALB,BUN,D1_Urine,D2_Urine,D3_Urine,
                      D3_SBP,ALKP,D3_temperature,WBC,HGB,LACTATE,NEUT,
                      D3_DBP,D1_temperature,BILT,CREAT,D3_PAW,D1_pulse]])
    
    result = model.predict(input)

    
    return render_template('result.html',D3_MAPS=D3_MAPS,PLT=PLT,D3_pulse=D3_pulse,D2_temperature=D2_temperature,D3_SPO2=D3_SPO2,PTP=PTP,
                                         ALB=ALB,BUN=BUN,D1_Urine=D1_Urine,D2_Urine=D2_Urine,D3_Urine=D3_Urine,
                                         D3_SBP=D3_SBP,ALKP=ALKP,D3_temperature=D3_temperature,WBC=WBC,HGB=HGB,LACTATE=LACTATE,NEUT=NEUT,
                                         D3_DBP=D3_DBP,D1_temperature=D1_temperature,BILT=BILT,CREAT=CREAT,D3_PAW=D3_PAW,D1_pulse=D1_pulse,result=result[0][1]*100)   

if __name__ == '__main__':
 app.run(host="0.0.0.0", port=80debug=True)
