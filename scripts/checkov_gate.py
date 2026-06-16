import json
import sys

with open("checkov-report.json") as f:
    data = json.load(f)

fail = False

for r in data["results"]["failed_checks"]:
    severity = r.get("severity", "UNKNOWN").upper()

    if severity in ["CRITICAL", "HIGH"]:
        print(f"❌ Blocking issue: {r['check_id']} - {severity}")
        fail = True
    elif severity == "MEDIUM":
        print(f"⚠️ Warning: {r['check_id']} - {severity}")
    else:
        print(f"ℹ️ Info: {r['check_id']} - {severity}")

if fail:
    sys.exit(1)