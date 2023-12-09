def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"], "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"path": file_path,
            "status": "passed" if len(errors) == 0 else "failed",
            "errors": [format_linter_error(error) for error in errors]
            }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(pth, er) for pth, er in linter_report.items()
    ]
