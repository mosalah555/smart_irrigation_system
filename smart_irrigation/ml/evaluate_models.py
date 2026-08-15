from pathlib import Path
import json
if __name__=="__main__":
 for f in sorted((Path(__file__).resolve().parents[1]/"model_results").glob("*.json")):print(json.loads(f.read_text()))
