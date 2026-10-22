# CRIMEMAP

- Practice flask project
- Realtime crime monitoring and reporting web app.

Learnt how to integrate Maps with my web app.
Basic CRUD operations with Flask and MySQL

## Runtime and dependencies

Use Python 3.11.17 (see `.python-version`) in an isolated environment:

```sh
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip==26.2.2 setuptools==84.2.1
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python -m compileall -q crimemap.py dbhelper.py db_setup.py
```

The Flask 3.1 dependency set includes patched Werkzeug and Jinja2, plus
PyMySQL 1.1.1 and cryptography 50.0.2. Date parsing remains provided by
dateparser; its Python-3-compatible dependencies are pinned too. Sanitized
descriptions remain strings with the existing ASCII character whitelist.
No database schema, connection settings, routes, or authentication were changed.

Local MySQL credentials belong in the ignored `dbconfig.py`; never commit them.
`db_setup.py` creates database objects and must not be imported for a smoke check.
The built-in debug server is for local development, not production.

The GitHub-hosted dependency compatibility workflow installs the pins on the
declared Python version and performs compile/import, date/sanitization, template
compilation, and non-database HTTP smoke checks. It uses dummy configuration and
does not connect to MySQL, load credentials, deploy, or call Google Maps.
This repository has no automated test suite or deployment workflow. These
checks do not establish a working MySQL/Google Maps integration.
Existing application limitations remain: `/` references an untracked
`home-test.html` rather than the committed `home.html`; `get_all_crimes` has a
misspelled longitude column and never fetches its rows; `/clear` calls an absent
`clear_all` method. These pre-existing defects are not dependency regressions.