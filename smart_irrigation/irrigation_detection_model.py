"""Legacy entry point retained for the project root; trains the five crop models."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
subprocess.check_call([sys.executable,str(root/"ml"/"generate_synthetic_data.py")],cwd=root/"ml")
subprocess.check_call([sys.executable,str(root/"ml"/"train_models.py")],cwd=root/"ml")
