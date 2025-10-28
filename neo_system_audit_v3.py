import json
import platform
import subprocess
from datetime import datetime
from pathlib import Path


def run_ps(ps_cmd):
    """Run a PowerShell command and return stdout text."""
    try:
        completed = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                ps_cmd,
            ],
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except Exception as e:
        return f"ERROR: {e}"


def downloads_inventory():
    dl = Path.home() / "Downloads"
    items = []
    if dl.exists():
        for p in dl.iterdir():
            if p.is_file():
                items.append(
                    {
                        "name": p.name,
                        "size_MB": round(p.stat().st_size / (1024 * 1024), 2),
                        "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(
                            timespec="seconds"
                        ),
                    }
                )
    items.sort(key=lambda x: x["modified"], reverse=True)
    return items


def os_summary():
    return {
        "machine": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "version": platform.version(),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }


def installed_programs():
    ps = r"""
$paths = @(
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
)
$apps = foreach ($p in $paths) {
  Get-ItemProperty $p -ErrorAction SilentlyContinue |
    Where-Object { $_.DisplayName } |
    Select-Object DisplayName, DisplayVersion, Publisher
}
$apps | Sort-Object DisplayName | ConvertTo-Json -Depth 3
"""
    raw = run_ps(ps)
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def gpu_driver():
    ps = r"""
Get-CimInstance Win32_PnPSignedDriver |
  Where-Object { $_.DeviceClass -match 'DISPLAY' } |
  Select-Object DeviceName, DriverVersion, DriverDate |
  Sort-Object DeviceName | ConvertTo-Json
"""
    raw = run_ps(ps)
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def bios_info():
    ps = r"""
Get-CimInstance Win32_BIOS |
  Select-Object SMBIOSBIOSVersion, Manufacturer, ReleaseDate |
  ConvertTo-Json
"""
    raw = run_ps(ps)
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def monitors():
    ps = r"""
Get-CimInstance Win32_PnPEntity |
  Where-Object { $_.PNPClass -eq 'Monitor' } |
  Select-Object Name, Manufacturer, DeviceID | ConvertTo-Json
"""
    raw = run_ps(ps)
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def displaylink_version():
    ps = r"""
$keys = @(
 'HKLM:\SOFTWARE\DisplayLink Core',
 'HKLM:\SOFTWARE\WOW6432Node\DisplayLink Core'
)
$result = foreach($k in $keys){
  if(Test-Path $k){ Get-ItemProperty $k | Select-Object ProductVersion }
}
if($result){ $result | Select-Object -First 1 | ConvertTo-Json } else { '{}' }
"""
    raw = run_ps(ps)
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def write_report(data):
    desktop = Path.home() / "OneDrive" / "Desktop"
    if not desktop.exists():
        desktop = Path.home() / "Desktop"
    out = desktop / "system_audit_report_v3.json"
    out.write_text(json.dumps(data, indent=2))
    return out


if __name__ == "__main__":
    report = {
        "system": os_summary(),
        "downloads": downloads_inventory(),
        "installed_programs": installed_programs(),
        "gpu_driver": gpu_driver(),
        "bios": bios_info(),
        "monitors": monitors(),
        "displaylink": displaylink_version(),
    }
    path = write_report(report)
    print(f"✅ Audit complete: {path}")
