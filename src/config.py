"""Central config: all URLs, snapshots, and thresholds are explicit and cited."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SNAP = DATA / "snapshots"
BENCH = ROOT / "benchmarks"

# Live endpoints (all public, no key). Each has a snapshot fallback.
SEC_CISCO_SUBMISSIONS = "https://data.sec.gov/submissions/CIK0000858877.json"
# Cisco CIK 858877 verified live via https://www.sec.gov/files/company_tickers.json 2026-10-16.
YAHOO_CSCO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/CSCO?interval=1mo&range=12y"
NVD_HUAWEI = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=huawei&resultsPerPage=20"
NVD_CISCO = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=cisco&resultsPerPage=20"

HEADERS = {"User-Agent": "blowback-verify-research/1.0 (research@test.com)", "Accept": "application/json"}

TIMEOUT = 20
