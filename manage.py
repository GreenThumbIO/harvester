"""
manage.py - Manage your commands
"""
import subprocess
import sys
import os

from flask_migrate import MigrateCommand, upgrade
from flask_script import Server, Manager

from app import db, create_app

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0", port=5000))

@manager.command
def test():
    """Runs the unit tests"""
    db.create_all()
    result = subprocess.call([sys.executable, '-c', 'import tests; tests.run()'])
    sys.exit(result)

@manager.command
def routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = f"[{arg}]"

        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in output:
        print(line)

if __name__ == "__main__":
    manager.run()
