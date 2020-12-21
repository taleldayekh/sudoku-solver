# Table of Contents

- [API](#api)
  - [Sudoku Resource](#sudoku-resource)

# API

## Sudoku Resource

| HTTP Method | Description  | Resource                           | Success Code | Failure Code |
| ----------- | ------------ | ---------------------------------- | ------------ | ------------ |
| POST        | Solve sudoku | [api/v1/sudoku/solve](#post-solve) | 200          | 400          |

---

### `POST` solve

#### Request

```shell
curl -X POST \
http://localhost:5000/api/v1/sudoku/solve \
-H "Content-Type: application/json" \
-d '{"sudoku": [<sudoku array>]}' 
```

#### Success Responses

```shell
{"data": [<sudoku array>]}
```

```shell
{"data": "Sudoku is unsolvable"}
```

#### Error Responses

```shell
{"error": "Not a valid Sudoku"}
```

```shell
{"error": "Invalid JSON key"}
```
