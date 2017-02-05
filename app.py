# -*- coding: UTF-8 -*-

from urllib.parse import urlparse
from flask import Flask, request, abort

app = Flask(__name__)

BASE = "tellement.sexy"
VERBS = {
    "est": "est",
    "sont": "sont",
    "is": "is",
    "are": "are",
    "cest": "c'est",
    "ete": "été",
    "etre": "être",
    "etait": "était",
    "etais": "étais",
}
ALIASES = {
    "css": "CSS",
    "html": "HTML",
    "javascript": "JavaScript",
    "lisp": "LISP",
    "php": "PHP",
}


def pretty_word(word):
    if word in ALIASES:
        return ALIASES[word]

    return word.capitalize()

@app.route("/")
def root():
    host = urlparse(request.base_url).netloc.split(":", 1)[0]

    for verb, text in VERBS.items():
        idx = host.rfind(".%s.%s" % (verb, BASE))
        if idx < 0:
            continue

        parts = host[:idx].split(".")

        name = " ".join([pretty_word(w) for w in parts])
        return "%s %s tellement sexy ;)" % (name, text)

    abort(404)

if __name__ == "__main__":
    app.run()
