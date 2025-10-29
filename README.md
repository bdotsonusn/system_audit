# ðŸ§  NEO System Audit


**Version:**   3.1.0  

[![CI](https://github.com/bdotsonusn/system_audit/actions/workflows/ci.yml/badge.svg)](https://github.com/bdotsonusn/system_audit/actions/workflows/ci.yml)


**Version:** 3.0.0  

**Author:** Neo Dotson (`bdotsonusn@gmail.com`)  
**Purpose:** Rapid environment and package inventory for Windows-based dev systems.

---

## âš™ï¸ Overview
The **NEO System Audit** script provides a complete snapshot of your local machineâ€™s setup â€” capturing installed packages, drivers, environment variables, and key configuration data â€” then outputs it all in structured JSON for easy reporting or ingestion into other systems.

This tool helps ensure your development baseline is consistent across machines and provides version-controlled transparency for audit and rebuilds.

---

## ðŸš€ Features
- ðŸ§© Scans installed programs (registry-based + PowerShell inventory)
- ðŸ’½ Captures system and hardware details (RAM, CPU, OS version)
- ðŸ“¦ Exports results in human-readable JSON
- ðŸ“Š Ready for data analysis or comparison
- ðŸ§± Integrates with Git for version tracking

---

## ðŸ“‚ Files
| File | Description |
|------|--------------|
| `neo_system_audit_v3.py` | Main system audit script |
| `system_audit_report_v3.json` | Example output data |
| `README.md` | Project overview and usage guide |

---
Â© 2025 Bradley Dotson.  
Released under the MIT License.  
Authored and maintained by **Neo Dotson** within the NEO Protocol System.

## ðŸ–¥ï¸ Usage

Run directly from PowerShell:
```powershell
python neo_system_audit_v3.py


