from src.package_scanner import PackageScanner


def test_scan_packages():

    scanner = PackageScanner(
        [
            {
                "name": "requests",
                "version": "2.32.0"
            }
        ]
    )

    result = scanner.scan()

    assert result[0].name == "requests"


def test_version_check():

    scanner = PackageScanner([])

    assert scanner.check_version(
        "2.32.0",
        "2.30.0"
    )