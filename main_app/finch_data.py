from flask import Flask, render_template

finches = [
    {'species': 'Galapagos Finch', 'beak_depth': 10, 'beak_width': 5, 'island': 'Galapagos'},
    {'species': 'Cactus Finch', 'beak_depth': 8, 'beak_width': 4, 'island': 'Galapagos'},
    {'species': 'Ground Finch', 'beak_depth': 7, 'beak_width': 3, 'island': 'Galapagos'},
    {'species': 'Tree Finch', 'beak_depth': 9, 'beak_width': 6, 'island': 'Galapagos'},
    {'species': 'Warbler Finch', 'beak_depth': 6, 'beak_width': 2, 'island': 'Galapagos'}
]

app = Flask(__name__)

@app.route('/')
def finch_list():
    return render_template('finch_list.html', finches=finches)
