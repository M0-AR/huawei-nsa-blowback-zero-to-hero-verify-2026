import json
from pathlib import Path
from src.verify_claims import verify
from src.benchmark_blowback import benchmark as blow
from src.market_verify import benchmark as mkt
from src.cve_benchmark import benchmark as cve


def test_claims_all_confirmed():
    v = verify({})
    assert v["total_claims"] == 12
    assert v["confirmed"] == 12
    assert v["mean_strength_0_5"] >= 4.0


def test_blowback_math():
    b = blow()
    assert b["total_realized_mid_usd"] >= 10_000_000_000
    assert b["days_from_free_leak_to_wannacry"] == 28
    assert b["alleged_huawei_backdoor_public_docs_after_years_inside"] == 0


def test_market_shape():
    m = mkt({})
    assert "cisco_revenue_sec_edgar" in m
    assert m["2014_trust_shock"]["brazil"] == "-27%"


def test_cve_shape():
    c = cve({})
    assert "hcsec_2019_findings" in c
    assert len(c["hcsec_2019_findings"]) >= 4
