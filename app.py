import random
from flask import Flask, render_template, request, redirect
# Thanks to noelledaley on github and opentechschool
# for showing me how to use Flask
app = Flask(__name__)

story_num = list()
inputs = list()
story_num.append(1)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/nav", methods=["POST"])
def nav():
    story = request.form["story"]
    print("The story is '" + story + "'")
    return redirect("/story" + story)


@app.route("/complete", methods=["POST"])
def complete():
    inputs.append(request.form)
    return redirect("/story" + str(story_num[(len(story_num) - 1)]) + "output")


@app.route("/story1")
def story1():
    story_num.append(1)
    return render_template("story1inputs.html")


@app.route("/story1output")
def story1output():
    print(inputs)
    verb = inputs[0].get('verb0')
    nouns = list(inputs[0].get('noun0'))
    nouns.append(inputs[0].get('noun1'))
    nouns.append(inputs[0].get('noun2'))
    nouns.append(inputs[0].get('noun3'))
    nouns.append(inputs[0].get('noun4'))
    nouns.append(inputs[0].get('noun5'))
    plural_noun = inputs[0].get('plural_noun0')
    formofgovernment = inputs[0].get('formofgovernment0')
    adjectives = list(inputs[0].get('adjective0'))
    adjectives.append(inputs[0].get('adjective1'))
    adjectives.append(inputs[0].get('adjective2'))
    adjectives.append(inputs[0].get('adjective3'))
    past_verb = inputs[0].get('past_verb0')
    verbing = inputs[0].get('verbing0')
    adverbs = list(inputs[0].get('adverb0'))
    adverbs.append(inputs[0].get('adverb1'))
    superlative = inputs[0].get('superlative0')
    authority_figure = inputs[0].get('authority_figure0')
    proper_name = inputs[0].get('proper_name0')
    random.shuffle(nouns)
    random.shuffle(adjectives)
    random.shuffle(adverbs)
    words = {'verb': verb, 'nouns': nouns, 'plural_noun': plural_noun,
              'formofgovernment': formofgovernment, 'adjectives': adjectives,
              'past_verb': past_verb, 'verbing': verbing, 'adverbs': adverbs,
              'superlative': superlative, 'authority_figure': authority_figure,
              'proper_name' : proper_name}
    print(words)
    return render_template("story1output.html", words = words)


@app.route("/story2")
def story2():
    story_num = 2
    return render_template("story2inputs.html")


@app.route("/story3")
def story3():
    story_num = 3
    return render_template("story3inputs.html")


@app.route("/story4")
def story4():
    story_num = 4
    return render_template("story4inputs.html")


@app.route("/story5")
def story5():
    story_num = 5
    return render_template("story5inputs.html")


@app.route("/story6")
def story6():
    story_num = 6
    return render_template("story6inputs.html")


@app.route("/story7")
def story7():
    story_num = 7
    return render_template("story7inputs.html")


@app.route("/story8")
def story8():
    story_num = 8
    return render_template("story8inputs.html")


if __name__ == '__main__':
    app.run(debug=True)
