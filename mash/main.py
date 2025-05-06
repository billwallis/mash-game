"""
Entry point into the package.
"""

import pathlib
import random
import tomllib
from typing import Any

HERE = pathlib.Path(__file__).parent


def _print_results(results: dict[str:Any]):
    """
    Print the results of the game.
    """

    cat_len = max(len(category) for category in results.keys())
    for category, option in results.items():
        print(f"{category.rjust(cat_len)}: {option}")


def main() -> None:
    """
    Entry point into the module.
    """

    category_options = tomllib.loads(
        (HERE / "categories.toml").read_text(encoding="utf-8")
    )
    results = {
        category: random.choice(options)  # noqa: S311
        for category, options in category_options.items()
    }
    _print_results(results)


if __name__ == "__main__":
    main()
