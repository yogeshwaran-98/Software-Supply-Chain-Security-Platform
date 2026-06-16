import subprocess

subprocess.run(
    request.args.get("cmd"),
    shell=True
)