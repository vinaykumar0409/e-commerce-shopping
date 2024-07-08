import pickle as pkl
from flask import Flask, request, render_template
app =Flask(__name__)
model=pkl.load(open('class.pkl','rb'))
sc=pkl.load(open('scale.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/prediction')
def predict():
    return render_template('prediction.html')
@app.route('/output', methods=['POST'])
def output():
    Warehouse_block=eval(request.form["Warehouse_block"])
    Mode_of_Shipment=eval(request.form["Mode_of_Shipment"])    
    Customer_care_calls=eval(request.form["Customer_care_calls"])
    Customer_rating=eval(request.form["Customer_rating"])
    Cost_of_the_Product=eval(request.form["Cost_of_the_Product"])
    Prior_purchases=eval(request.form["Prior_purchases"])
    Product_importance=eval(request.form["Product_importance"])
    Gender=eval(request.form["Gender"])
    Discount_offered=eval(request.form["Discount_offered"])
    Weight_in_gms=eval(request.form["Weight_in_gms"])

    preds=[[Warehouse_block,Mode_of_Shipment,Customer_care_calls,Customer_rating,Cost_of_the_Product,Prior_purchases,Product_importance,Gender,Discount_offered,Weight_in_gms]]
    result=model.predict(sc.transform(preds))
    prob=model.predict_proba(sc.transform(preds))[0]
    reach=prob[0]
    reach=prob[1]
    result='There is a {0:.2f}  chance that your product will reach in time'.format(reach*100)
    return render_template("output.html", p =result)
    
if __name__== '__main__':
     app.run(debug=True)