from dataclasses import dataclass
from packaging.version import Version


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