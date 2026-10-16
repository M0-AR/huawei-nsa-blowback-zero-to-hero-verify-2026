"""Live-data fetcher with snapshot fallback.

Best practice (verified 2026-09 ACM Reproducibility + SynthChain + Lily/R-Diff):
- every live call has timeout + persistent snapshot fallback
- raw responses are saved under data/snapshots/
- run metadata records live vs fallback so benchmarks are auditable.
"""
import json
import time
from pathlib import Path
import requests

from .config import (HEADERS, TIMEOUT, SNAP, NVD_CISCO, NVD_HUAWEI,
                     SEC_CISCO_SUBMISSIONS, YAHOO_CSCO_CHART)

SNAP.mkdir(parents=True, exist_ok=True)


def _get(url: str, name: str):
    meta = {"url": url, "live": False, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        meta["live"] = True
        (SNAP / f"{name}_live.json").write_text(json.dumps(data)[:500000])
        return data, meta
    except Exception as e:
        meta["error"] = f"{type(e).__name__}: {e}"
        fb = SNAP / f"{name}_snapshot.json"
        if fb.exists():
            return json.loads(fb.read_text()), {**meta, "fallback": str(fb)}
        return None, meta


def fetch_all():
    out, metas = {}, {}
    for name, url in [
        ("sec_cisco", SEC_CISCO_SUBMISSIONS),
        ("yahoo_csco", YAHOO_CSCO_CHART),
        ("nvd_huawei", NVD_HUAWEI),
        ("nvd_cisco", NVD_CISCO),
    ]:
        data, meta = _get(url, name)
        out[name] = data
        metas[name] = meta
    return out, metas


def write_snapshots_from_verified_facts():
    """Seed snapshots from facts verified online (so offline runs still verify)."""
    # SEC Cisco fundamentals verified via openresearch_get_company_financials (SEC EDGAR 10-K)
    sec_fallback = {
        "source": "SEC EDGAR 10-K via verification 2026-10-16",
        "cik": "0000858871",
        "revenue": {"2022": 51557000000, "2023": 56998000000, "2024": 53803000000,
                    "2025": 56654000000, "2026": 63325000000},
        "net_income": {"2022": 11812000000, "2023": 12613000000, "2024": 10320000000,
                       "2025": 10180000000, "2026": 13267000000},
    }
    (SNAP / "sec_cisco_snapshot.json").write_text(json.dumps(sec_fallback, indent=2))
    # NVD counts: placeholders replaced by live fetch when online; structure only
    for n in ["nvd_huawei", "nvd_cisco"]:
        p = SNAP / f"{n}_snapshot.json"
        if not p.exists():
            p.write_text(json.dumps({"source": "NVD API fallback placeholder",
                                     "totalResults": None, "note": "live fetch preferred"}, indent=2))
    # Yahoo fallback: 2014 Cisco shock numbers from verified reporting
    yahoo_fb = {
        "source": "Verified reporting fallback (Vox/InfoWorld/CNBC May-Aug 2014)",
        "note": "Cisco Q3-2014: emerging orders -7%, Brazil -27%, Russia -28%; China <5% revenue (~$2B)",
        "yahoo_live_preferred": True,
    }
    (SNAP / "yahoo_csco_snapshot.json").write_text(json.dumps(yahoo_fb, indent=2))


if __name__ == "__main__":
    write_snapshots_from_verified_facts()
    data, metas = fetch_all()
    print(json.dumps(metas, indent=2))
