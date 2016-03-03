# -*- coding: UTF-8 -*-

from urlparse import urlparse
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def root():
    base = "tellement.sexy"
    verbs = {
        "est": "est",
        "sont": "sont",
        "is": "is",
        "are": "are",
        "cest": "c'est",
    }

    host = urlparse(request.base_url).netloc.split(":", 1)[0]

    for verb, text in verbs.items():
        idx = host.rfind(".%s.%s" % (verb, base))
        if idx < 0:
            continue

        parts = host[:idx].split(".")

        name = " ".join([p.capitalize() for p in parts])
        return "%s %s tellement sexy ;)" % (name, text)

    abort(404)

if __name__ == "__main__":
    app.run()
