# 🧠 NEO System Audit

**Version:** 3.0.0  
**Author:** Neo Dotson (`bdotsonusn@gmail.com`)  
**Purpose:** Rapid environment and package inventory for Windows-based dev systems.

---

## ⚙️ Overview
The **NEO System Audit** script provides a complete snapshot of your local machine’s setup — capturing installed packages, drivers, environment variables, and key configuration data — then outputs it all in structured JSON for easy reporting or ingestion into other systems.

This tool helps ensure your development baseline is consistent across machines and provides version-controlled transparency for audit and rebuilds.

---

## 🚀 Features
- 🧩 Scans installed programs (registry-based + PowerShell inventory)
- 💽 Captures system and hardware details (RAM, CPU, OS version)
- 📦 Exports results in human-readable JSON
- 📊 Ready for data analysis or comparison
- 🧱 Integrates with Git for version tracking

---

## 📂 Files
| File | Description |
|------|--------------|
| `neo_system_audit_v3.py` | Main system audit script |
| `system_audit_report_v3.json` | Example output data |
| `README.md` | Project overview and usage guide |

---

## 🖥️ Usage

Run directly from PowerShell:
```powershell
python neo_system_audit_v3.py
