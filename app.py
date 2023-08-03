from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict',methods=['Get','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    choice = request.form['choice_radio']
    
    #return render_template('form.html', prediction_text='Value be be $ {}'.format(choice))

    if(str(choice) == str('Yes')):
        return render_template('index.html')
    elif(choice == 'No'):
        return render_template('form.html', prediction_text='Press yes')
    else:
        return render_template('form.html', prediction_text='Please, press yes.')

    
if __name__ == "__main__":
    app.run(debug=True)

#app.run(host='localhost',port=80)
    
