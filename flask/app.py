# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

rdata = "recenze.json"

# def save_data():
#     with open("data/recenze.json", "r", encoding="UTF-8") as file:
#         json.dump(data, file, indent=4)


@app.route("/")
def home():
    return render_template("vitej.html")


@app.route("/form.html")
def form():
    if request.method == "GET":
        name = request.args.get("name")
        recenze = request.args.get("recenze")

    if name and recenze:
        print(name, recenze)
    
    data = {
        "Name": name,
        "Recenze": recenze
    }

    with open(rdata, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)

        print(data)

    # if recenze == "nic":
    #     zprava = "uživatel byl příliš líný na napsání recenze" 
    # print(zprava)
    #pak bych dala do render template zprava=zprava a do form.html napsala k recenze... promennou zprava

    return render_template("form.html", name=name, recenze=recenze)

# spouští hlavní funkci, pokud je main, app běží
if __name__ == "__main__": 
    app.run(debug=True) #enablue debug mode aby necrashoval pri nacteni souboru
