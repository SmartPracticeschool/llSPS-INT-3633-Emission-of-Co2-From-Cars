from flask import Flask,render_template,request,url_for
import pickle
model = pickle.load(open('CO2EMISSIONS.pkl','rb'))
app = Flask(__name__,)
@app.route('/')
def hello_world():
    return render_template("index1.HTML")
@app.route('/predict',methods=["POST"])
def fun2():
    MODELYEAR = request.form['MODELYEAR']
    ENGINESIZE = request.form['ENGINESIZE']
    CYLINDERS = request.form['CYLINDERS']
    FUELCONSUMPTION_CITY = request.form['FUELCONSUMPTION_CITY']
    FUELCONSUMPTION_HWY = request.form['FUELCONSUMPTION_HWY']
    FUELCONSUMPTION_COMB  = request.form['FUELCONSUMPTION_COMB']
    FUELCONSUMPTION_COMB_MPG = request.form['FUELCONSUMPTION_COMB_MPG']


    data = [[int(MODELYEAR),float(ENGINESIZE),int(CYLINDERS),float(FUELCONSUMPTION_CITY),float(FUELCONSUMPTION_HWY),float(FUELCONSUMPTION_COMB),int(FUELCONSUMPTION_COMB_MPG)]]
    pred = model.predict(data)
    print(pred)
    if(pred>256.99):
        return render_template("index1.HTML",y = "Your Vehicle Sezied Because Co2 Emission value is Higer, The Value is"+str(pred))
    else:
                return render_template("index1.HTML",y = "Your Vehicle Safe, Because less emission,The Value is"+str(pred))

if __name__== '__main__':
    app.run(debug =True) #wsgi local server url