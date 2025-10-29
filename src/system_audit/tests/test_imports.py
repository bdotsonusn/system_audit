import importlib


def _import_ok(dotted: str) -> bool:
    importlib.import_module(dotted)
    return True


def test_import_top_level():
    assert _import_ok("system_audit")


def test_import_exports_pkg():
    assert _import_ok("system_audit.exports")


def test_import_exports_modules():
    for m in ["system_audit.exports.base", "system_audit.exports.json_exporter"]:
        assert _import_ok(m)
