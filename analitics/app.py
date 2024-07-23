from flask import Flask

from analitics.views import home, dashboard
from analitics.core.config import settings


app = Flask(settings.APP_NAME)

app.add_url_rule("/", methods=["GET"], view_func=home)
app.add_url_rule("/dashboard", methods=["GET"], view_func=dashboard)

if __name__ == "__main__":
    print(f"loading analitic website {app.name} ...")
    app.run(debug=True)
