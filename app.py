import Database
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def display():
    """Laat de Start pagina zien."""
    return render_template("StartPagina.html")


@app.route("/Resultaten.html", methods=['POST', 'GET'])
def display_resultaten():
    """Geeft filter informatie door aan de database filter functie en laat de
    gekragen gegevens zien op de Resultaten pagina."""
    if request.method == 'POST':
        filteren = request.form['filter']
        checkbox_p = ('Protein_name' in request.form.keys())
        checkbox_s = ('Stam' in request.form.keys())
        checkbox_f = ('Function' in request.form.keys())
        checkbox_o = ('Organisme' in request.form.keys())
        if filteren == "":
            list_protein_name, list_lineage, list_description = \
                Database.database()
        else:
            list_protein_name, list_lineage, list_description = \
                Database.database_filter(filteren, checkbox_p, checkbox_s,
                                         checkbox_f, checkbox_o)
        length = list(range(len(list_protein_name)))
        return render_template("Resultaten.html", filter=filteren,
                               length=length,
                               list_protein_name=list_protein_name,
                               list_lineage=list_lineage,
                               list_description=list_description)
    else:
        return render_template("Resultaten.html")


if __name__ == '__main__':
    app.run()
