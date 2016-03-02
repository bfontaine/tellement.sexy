# tellement.sexy

**tellement.sexy** is a tiny webapp that displays a message depending on the
subdomain used to access it.

It’s deployed at `http://tellement.sexy` with a wildcard A DNS record so that
any subdomain work.

## Run

    pip install -r requirements.txt
    gunicorn app:app

## About the name

“tellement sexy” means “so sexy” in French.
