import sys
from pathlib import Path

from .package_scanner import PackageScanner


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."

    scanner = PackageScanner()

    result = scanner.scan(Path(target))

    print(result)


if __name__ == "__main__":
    main()