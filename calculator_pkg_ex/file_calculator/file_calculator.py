import time
from pathlib import Path

from tqdm import tqdm

from ..calculator import Calculator

# from calculator_pkg_ex.calculator import Calculator


class FileCalculator(Calculator):
    def __init__(
        self,
        path: Path = Path(__file__).parent / "nums.csv",
        expected_lines: int = 3,
    ) -> None:
        self.path: Path = path
        self.expected_lines: int = 3

    def add_file(self) -> float | None:
        # -> Any
        # mylist: list[int] = [1, 2, 3]
        total: float = 0
        with open(self.path, "r") as f:
            for line in tqdm(
                f, total=self.expected_lines, desc="Summing lines in file"
            ):
                time.sleep(2)
                total += float(line)
        return total
