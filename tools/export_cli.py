import argparse
from pathlib import Path


def _fake_report():
    # Fallback if system_audit.run_audit isn't available
    return {
        "status": "ok",
        "message": "fallback report (connect to your real audit pipeline)",
    }


def _get_report():
    try:
        import system_audit  # your package

        if hasattr(system_audit, "run_audit"):
            return system_audit.run_audit()  # type: ignore[attr-defined]
        # Try a nested cli module contract
        if hasattr(system_audit, "cli") and hasattr(system_audit.cli, "run_audit"):
            return system_audit.cli.run_audit()  # type: ignore[attr-defined]
    except Exception:
        pass
    return _fake_report()


def main():
    from system_audit.exports.json_exporter import JSONExporter

    exporters = {"json": JSONExporter()}
    parser = argparse.ArgumentParser(
        prog="export_cli", description="NEO System Audit export"
    )
    parser.add_argument(
        "--format", dest="fmt", choices=exporters.keys(), default="json"
    )
    parser.add_argument("--out-dir", dest="out_dir", default="dist/audit")
    args = parser.parse_args()
    report = _get_report()
    out = exporters[args.fmt].export(report, Path(args.out_dir))
    print(f"Exported {args.fmt} -> {out}")


if __name__ == "__main__":
    main()
