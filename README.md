![CI](https://github.com/taleldayekh/sudoku-solver/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/taleldayekh/sudoku-solver/branch/develop/graph/badge.svg?token=IMBF7FXCAD)](https://codecov.io/gh/taleldayekh/sudoku-solver)

# Table of Contents

- [API](#api)
  - [Sudoku Resource Overview](#sudoku-resource-overview)
  - [Sudoku Resource Details](#sudoku-resource-details)

# API

## Sudoku Resource Overview

| HTTP Method | Description            | Resource               | Success Code | Failure Code |
| ----------- | ---------------------- | ---------------------- | ------------ | ------------ |
| POST        | Solve sudoku           | api/v1/sudoku/solve    | 200          | 400          |
| POST        | Sudoku solution hint   | api/v1/sudoku/hint     | 200          | 400          |
| POST        | Sudoku verify solution | api/v1/sudoku/verify   | 200          | 400          |
| GET         | Generate sudoku        | api/v1/sudoku/generate | 200          |              |

---

## Sudoku Resource Details

<details>
<summary>POST solve</summary>

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
{"data": "Not a valid sudoku"}
```

```shell
{"error": "Invalid JSON key"}
```
</details>

<details>
<summary>POST hint</summary>

#### Request

```shell
curl -X POST \
http://localhost:5000/api/v1/sudoku/hint \
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
{"data": "Not a valid sudoku"}
```

```shell
{"error": "Invalid JSON key"}
```
</details>

<details>
<summary>POST verify</summary>

#### Request

```shell
curl -X POST \
http://localhost:5000/api/v1/sudoku/verify \
-H "Content-Type: application/json" \
-d '{"sudoku": [<sudoku array>]}'
```

#### Success Responses

```shell
{"data": bool}
```

#### Error Responses

```shell
{"data": "Not a valid sudoku"}
```

```shell
{"error": "Invalid JSON key"}
```
</details>


<details>
<summary>GET generate</summary>

#### Request

```shell
curl http://localhost:5000/api/v1/sudoku/generate
```

#### Success Responses

```shell
{"data": [<sudoku array>]}
```

</details>
