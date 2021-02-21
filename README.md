![CI](https://github.com/taleldayekh/sudoku-solver/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/taleldayekh/sudoku-solver/branch/develop/graph/badge.svg?token=IMBF7FXCAD)](https://codecov.io/gh/taleldayekh/sudoku-solver)

# Table of Contents

- [API](#api)
  - [Sudoku Resource Overview](#sudoku-resource-overview)
  - [Sudoku Resource Details](#sudoku-resource-details)
- [Architecture](#architecture)
  - [App](#app)

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

# Architecture

## App

### View

1. **View**  

   _*Views*_ are the touching points for users, they receive user input and displays output. A _*View*_ is considered "dumb" (presentational) and does not contain any application logic.

   When a user interacts with a _*View*_ events are triggered and passed on to a _*ViewController*_. A _*View*_ will then change its visual state based on the response from the _*ViewController*_.

   _*Views*_ should only be used for displaying data and may contain related subviews.

2. **ViewController**  

   A _*ViewController*_ controls a _*View*_ and its subviews, i.e. `SudokuBoardView` with the subview `SudokuCellView`. The _*ViewController*_ is smart and contains all _*View*_ related logic. _*ViewControllers*_ work as the "glue" between the application and what users see on the screen.

   The _*ViewControllers*_ resides between the _*Views*_ and the _*ViewModels*_.

   A _*View*_ is never aware of any _*ViewModels*_. Events like user inputs are not passed directly from the _*View*_ to a _*ViewModel*_, they get passed to a _*ViewController*_ which in turn prepares the data and passes it on to the _*ViewModel*_.

   A _*ViewController*_ can reference many different _*ViweModels*_.
