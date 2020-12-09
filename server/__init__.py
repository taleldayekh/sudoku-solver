from flask import Flask

from server.interfaces.api.sudoku.sudoku_controller import sudoku_v1


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(sudoku_v1, url_prefix="/api/v1/sudoku")

    return app
