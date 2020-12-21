import json

from flask import Blueprint, Response, request

from server.app_sudoku.use_cases.post_solve import InvalidSudoku, solve_sudoku

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
