import subprocess
from sysvars import SysVars as svar

def naps2_scan():
    cmd = [
        svar.NAPS2_PATH,
        "scan",
        "--profile", svar.NAPS2_USER,
        "--output", svar.DATA_ROOT / "uploads" / "document.png",
        "--force"
    ]

    subprocess.run(cmd, check=True)
