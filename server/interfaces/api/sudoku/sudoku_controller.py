import json

from flask import Blueprint, Response, request

from server.app_sudoku.use_cases.get_generate import generate_sudoku
from server.app_sudoku.use_cases.post_hint import get_hint
from server.app_sudoku.use_cases.post_solve import InvalidSudoku, solve_sudoku
from server.app_sudoku.use_cases.post_verify import verify_sudoku

sudoku_v1 = Blueprint("sudoku_v1", __name__)


@sudoku_v1.route("/solve", methods=["POST"])
def solve_endpoint() -> Response:
    content_type = "application/json"
    data = request.get_json()

    try:
        sudoku_board = data["sudoku"]
        solved_sudoku = solve_sudoku(sudoku_board)

        if solved_sudoku:
            return Response(
                response=json.dumps({"data": solved_sudoku}),
                status=200,
                mimetype=content_type,
            )
        return Response(
            response=json.dumps({"data": "Sudoku is unsolvable"}),
            status=200,
            mimetype=content_type,
        )
    except KeyError:
        return Response(
            response=json.dumps({"error": "Invalid JSON key"}),
            status=400,
            mimetype=content_type,
        )
    except InvalidSudoku as err:
        return Response(
            response=json.dumps({"error": str(err)}),
            status=400,
            mimetype=content_type,
        )


@sudoku_v1.route("/hint", methods=["POST"])
def hint_endpoint() -> Response:
    content_type = "application/json"
    data = request.get_json()

    try:
        sudoku_board = data["sudoku"]
        hint = get_hint(sudoku_board)

        if hint:
            return Response(
                response=json.dumps({"data": hint}),
                status=200,
                mimetype=content_type,
            )
        return Response(
            response=json.dumps({"data": "Sudoku is unsolvable"}),
            status=200,
            mimetype=content_type,
        )
    except KeyError:
        return Response(
            response=json.dumps({"error": "Invalid JSON key"}),
            status=400,
            mimetype=content_type,
        )
    except InvalidSudoku as err:
        return Response(
            response=json.dumps({"error": str(err)}),
            status=400,
            mimetype=content_type,
        )


@sudoku_v1.route("/verify", methods=["POST"])
def verify_endpoint() -> Response:
    content_type = "application/json"
    data = request.get_json()

    try:
        sudoku_board = data["sudoku"]
        verify = verify_sudoku(sudoku_board)

        return Response(
            response=json.dumps({"data": verify}),
            status=200,
            mimetype=content_type,
        )
    except KeyError:
        return Response(
            response=json.dumps({"error": "Invalid JSON key"}),
            status=400,
            mimetype=content_type,
        )
    except InvalidSudoku as err:
        return Response(
            response=json.dumps({"error": str(err)}),
            status=400,
            mimetype=content_type,
        )


@sudoku_v1.route("/generate", methods=["GET"])
def generate_endpoint() -> Response:
    content_type = "application/json"
    sudoku = generate_sudoku()

    return Response(
        response=json.dumps({"data": sudoku}),
        status=200,
        mimetype=content_type,
    )
