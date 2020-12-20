# Table of Contents

- [API](#api)
  - [Sudoku Resource](#sudoku-resource)

# API

## Sudoku Resource

| HTTP Method | Description  | Resource                           | Success Code | Failure Code |
| ----------- | ------------ | ---------------------------------- | ------------ | ------------ |
| POST        | Solve sudoku | [api/v1/sudoku/solve](#post-solve) | 200          | 400          |

---

### `POST` Solve

#### Request

```shell
curl -X POST \
http://localhost:5000/api/v1/sudoku/solve \
-H "Content-Type: application/json" \
-d '{"sudoku": "<sudoku array>"}' 
```

#### Success Response

```shell
{"solved-sudoku": "<sudoku array>"}
```

```shell
{"not-solvable-sudoku": "Sudoku cannot be solved"}
```

### Error Response

```shell
{"invalid-sudoku": "Not a valid Sudoku"}
```
