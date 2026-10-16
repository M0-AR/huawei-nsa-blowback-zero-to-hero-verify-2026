# PhD Proposal Sketch: The Economics and Detectability of State-Implanted Network Backdoors

**Working title:** *Secret Doors, Stolen Keys: Measurement, Attribution, and Blowback in Supply-Chain Interdiction (2007–2027)*

## Problem
Public debate conflates three distinct states: (i) intentionally implanted backdoor, (ii) exploitable hygiene failure, (iii) clean. HCSEC (2010–2019) shows (ii) alone creates (i)-equivalent exposure, while Shotgiant + ANT show (i) is buildable and shelf-ready. No public method distinguishes (i) from (ii) at scale without build integrity.

## Research questions → chapters
- **Ch1 Measurement:** Can we score telecom firmware hygiene (memcpy-safety, sign/unsigned, warning suppression, reproducibility) into a predictive exploitability index? Data: HCSEC reports + NVD + R-Diff 50 targets + Lily fuzz trials.
- **Ch2 Attribution:** Under what build-integrity conditions is (i) vs (ii) distinguishable? Method: reproducible-builds pipeline + binary-equivalence checks + differential (delta-scan) static analysis.
- **Ch3 Economics:** What is the expected blowback cost of stockpiling vs disclosing one SMB-class bug? Data: WannaCry ($4–8B) + NotPetya ($10B+) + patch-lag distributions; model half-life of secrecy.
- **Ch4 Markets:** Event study — CSCO/supplier equities around 2014-05-12/19, 2019-05-16/20, 2020-07-14; Dell’Oro shares vs financing terms.
- **Ch5 Governance:** HCSEC as institutional design — what audit powers (source + engineers + binary equivalence + repeatable builds) are necessary/sufficient for risk management?

## Null hypotheses
- H0-1: Hygiene index does not predict exploitation in the wild.
- H0-2: Reproducible builds do not improve (i)/(ii) attribution.
- H0-3: Disclosure does not reduce systemic loss vs stockpiling.
- H0-4: Accusation headlines move share more than financing/availability.

## Datasets (all public)
timeline.csv + claims_matrix.csv (this repo), SEC EDGAR, NVD, Dell’Oro summaries, HCSEC PDFs, ANT catalog, WannaCry/NotPetya loss disclosures, OpenAlex 5G-governance corpus, SynthChain/Lily/R-Diff benchmarks.

## Contribution
First end-to-end falsifiable chain from interdiction photo → source theft → shelf-ready implant → independent audit → market shock → leaked-stockpile catastrophe, with live-data reproduction and H1–H5 hidden patterns as testable laws.

## Ethics
No new implants; only public docs + defensive detection (Lily-style delta fuzzing, reproducible builds). Responsible disclosure for any new hygiene findings.
