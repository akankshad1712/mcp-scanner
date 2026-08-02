from dataclasses import dataclass
from packaging.version import Version
from src.package_scanner import PackageScanner
from .package_scanner import PackageScanner


@dataclass
class PackageInfo:
    name: str
    version: str


class PackageScanner:
    def __init__(self, packages):
        self.packages = packages

    def scan(self):
        results = []

        for package in self.packages:
            results.append(
                PackageInfo(
                    name=package["name"],
                    version=package["version"],
                )
            )

        return results

    def check_version(self, current, minimum):
        return Version(current) >= Version(minimum)

    def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: mcp-scan <project-path>")
        return

    project_path = sys.argv[1]

    scanner = PackageScanner()

    result = scanner.scan(project_path)

    print(result)


if __name__ == "__main__":
    main()