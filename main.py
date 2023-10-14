from flask import Flask, render_template , request , redirect , url_for
from pymongo import MongoClient 
from flask_pymongo import PyMongo 

app = Flask('__name_')

client = MongoClient('mongodb://localhost:27017/ResBac')
app.config["MONGO_URI"] = "mongodb://localhost:27017/ResBac"
mongo = PyMongo(app)
db = client['ResBac']
collection = db['BAC_2023']



@app.route('/')
def index():
    major_BAC_C = mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"M"}).sort("MOYBAC", -1).limit(5)
    major_BAC_D =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"SN"}).sort("MOYBAC", -1).limit(5)
    major_BAC_LO =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"LO"}).sort("MOYBAC", -1).limit(5)
    major_BAC_LM =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"LM"}).sort("MOYBAC", -1).limit(5)
    major_BAC_T =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"TM"}).sort("MOYBAC", -1).limit(5)
    major_BAC_TS =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"TS"}).sort("MOYBAC", -1).limit(5)
    major_BAC_LA =  mongo.db.BAC_2023.find({"Decision": "Admis " , "SERIE":"LA"}).sort("MOYBAC", -1).limit(5)
    
    return render_template('layout.html' ,m = major_BAC_C , sn = major_BAC_D , lo = major_BAC_LO , lm = major_BAC_LM , tm = major_BAC_T , ts = major_BAC_TS , la = major_BAC_LA )

@app.route('/resultat' , methods = ['POST' , 'GET']) 
def res():
    if request.method == 'POST':
        numero = request.form['num_bac']
        return redirect(url_for("resbac" , numero = numero))
    return redirect(url_for('/'))
         

    
@app.route('/resultat/<numero>')
def resbac(numero):
    moyenne_etud = collection.find_one({'NODOSS': int(numero)})
    if moyenne_etud:
        moyenne_etud['NODOSS'] = str(moyenne_etud['NODOSS']).zfill(5)
        return render_template('layout.html' , etudiant = moyenne_etud )
    else:
        return render_template('layout.html' , erreur = 'تحقق من الرقم الذي قمت بالبحث عنه')
    

@app.route("/ResBAC2023/filter" , methods = ['POST'])
def filter_bac():
    if request.method == 'POST':
        serie_bac = request.form['serie_bac']
        return redirect(url_for("display_serie" , serie = serie_bac))
    return redirect (url_for('/'))


@app.route("/ResBAC2023/<serie>" , methods = ['POST' , 'GET'])
def display_serie(serie):
    if serie == str('all_serie'):
        return redirect(url_for('index'))
    elif serie:
        filter_serie = mongo.db.BAC_2023.find({"$or" : [{"Decision": "Admis "} , {"Decision" : "Sessionnaire"}] , "SERIE": str(serie)}).sort("rank_N", 1).limit(200)
        c = serie.lower()
        s = serie
        return render_template('layout.html' ,  filter_serie = filter_serie , c = c , s = s)
    return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(debug=True) 

