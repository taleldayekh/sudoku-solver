from flask import Blueprint, Response, request

from server.app_sudoku.use_cases.post_validate import post_validate

sudoku_v1 = Blueprint("sudoku_v1", __name__)


@sudoku_v1.route("/validate", methods=["POST"])
def validate() -> Response:
    data = request.get_json()

    if post_validate(data) == True:
        return Response(status=200)
    else:
        return Response(status=400)
