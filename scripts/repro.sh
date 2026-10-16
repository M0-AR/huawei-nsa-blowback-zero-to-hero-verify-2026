#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m pip install -q -r requirements.txt
python3 -m src.run_all
python3 -m pytest -q
echo "REPRO OK — see benchmarks/RESULTS.json"
