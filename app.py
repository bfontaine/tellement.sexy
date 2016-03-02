# -*- coding: UTF-8 -*-

from urlparse import urlparse
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def root():
    base = "tellement.sexy"

    prefixes = ["est", "sont", "is", "are"]

    host = urlparse(request.base_url).netloc.split(":", 1)[0]

    for prefix in prefixes:
        idx = host.rfind(".%s.%s" % (prefix, base))
        if idx < 0:
            continue

        parts = host[:idx].split(".")

        name = " ".join([p.capitalize() for p in parts])
        return "%s %s tellement sexy :)" % (name, prefix)

    abort(404)

if __name__ == "__main__":
    app.run()
