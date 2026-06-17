import json
import sys

with open("reports/checkov.json") as f:
    data = json.load(f)

fail = False

for report in data:
    for r in report["results"]["failed_checks"]:
        severity = str(r.get("severity") or "UNKNOWN").upper()

        if severity in ["CRITICAL", "HIGH"]:
            print(f"❌ Blocking issue: {r['check_id']} - {severity}")
            fail = True
        elif severity == "MEDIUM":
            print(f"⚠️ Warning: {r['check_id']} - {severity}")
        else:
            print(f"ℹ️ Info: {r['check_id']} - {severity}")

if fail:
    sys.exit(1)