# launcher.py

import os

if __name__ == "__main__":
    os.system("uvicorn noyau_core:app --host 0.0.0.0 --port 8000 --reload")
