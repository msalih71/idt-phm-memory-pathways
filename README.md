# IDT-PHM memory pathways

Reproducibility materials for **Separating Memory Pathways in Bearing Monitoring: A Reproducible Evaluation of Model Response, Prediction and Causal Alarms**.

Mahgoub A. Salih and Mohamed Y. Shirgawi, Department of Physics, College of Science, Qassim University, Saudi Arabia. Correspondence: m.salih@qu.edu.sa; co-author: m.mohamed@qu.edu.sa.

## Scope and scientific limits

The study separates implemented memory feedback, direct readout, future-feature prediction and causal alarm-policy outcomes across NASA IMS, PRONOSTIA, XJTU-SY and the UPB/Paderborn time-varying run-to-failure campaign. Public measured-feature caches contain 53 paths and 86,144 snapshots; 49 paths qualify for the alarm assay and 46 for prediction. The measured data were previously exposed. The minimal non-clock prediction pairs are disclosed post-result diagnostics.

This is not evidence of general memory superiority, a physical memory mechanism, independent fault-onset labels or field deployment validity. Occupancy, episode counts, observed duration and record-end lead remain separate. Points outside a proxy window are not verified false alarms.

## Versioned downloads

Release **v2026.10.16**: https://github.com/msalih71/idt-phm-memory-pathways/releases/tag/v2026.10.16

- `IDT_PHM_Paper_Reproduction_20261016.zip`: compact evidence CSVs, table/figure-generation code, model-only equilibrium checks and saved-result verification.
- `IDT_PHM_Research_20261016.tar.xz`: unchanged complete computational audit archive, measured caches, causal observer/decision code, nested prediction probes, history/locks, historical reports and legacy manuscript records. The root retains the historical directory name `IDT_PHM_Research_20261013`. The archive is provided without rewriting its past record.

Raw waveform archives and the personal Arabic manuscript translation are not redistributed. The current journal submission PDF and author declaration are not included in these public downloads. No paper DOI or journal publication is claimed.

## Quick reproduction

```bash
python download_assets.py --asset paper --extract
python paper_reproduction/verify_saved_results.py
python paper_reproduction/analysis/build_tables.py
python paper_reproduction/analysis/equilibrium_sensitivity.py
python paper_reproduction/analysis/rebuild_journal_figures.py
```

The small package checks 252 alarm operating points, 66 predictive summaries and 303 model-only equilibrium settings. These are implementation checks, not independent scientific replications.

For model refitting and full sequential recomputation:

```bash
python download_assets.py --asset research --extract
pip install -r IDT_PHM_Research_20261013/cross_dataset/requirements.txt
python IDT_PHM_Research_20261013/decision_audit/code/decision_audit.py
python -m unittest discover -s IDT_PHM_Research_20261013/decision_audit/code -p 'test_*.py' -v
python IDT_PHM_Research_20261013/decision_audit/code/verify_measured_prefixes.py
python IDT_PHM_Research_20261013/decision_audit/code/verify_release.py
python IDT_PHM_Research_20261013/memory_mechanism/code/mechanism_audit.py
python IDT_PHM_Research_20261013/memory_mechanism/code/complete_minimal_pairs.py
python -m unittest discover -s IDT_PHM_Research_20261013/memory_mechanism/code -p 'test_*.py' -v
python IDT_PHM_Research_20261013/memory_mechanism/code/verify_mechanism_release.py
```

Run the mechanism audit before the explicitly post-result minimal-pair completion. Verification compares saved measured targets, predictions and nested selections. Historical hashes can be checked before recomputation; regenerated reports may differ in rendering or environment metadata. The small package requirements record one checked environment; other versions may vary.

## Colab

Open `IDT_PHM_GitHub_Colab.ipynb` in Google Colab. It downloads the versioned paper package, verifies its SHA-256 and reconstructs saved results. The optional final cell downloads the complete research archive; full refitting is opt-in. No live Colab execution is claimed.

## Original dataset references

- NASA IMS: H. Qiu et al., Journal of Sound and Vibration (2006), https://doi.org/10.1016/j.jsv.2005.03.007
- PRONOSTIA: P. Nectoux et al. (2012), https://hal.science/hal-00719503
- XJTU-SY: B. Wang et al., IEEE Transactions on Reliability (2020), https://doi.org/10.1109/TR.2018.2882682
- UPB run-to-failure: https://doi.org/10.5281/zenodo.10868257 and https://doi.org/10.36001/phme.2024.v8i1.4101

These sources describe the original datasets; the repository does not claim to own them or grant rights beyond their original terms. Read `NOTICE.md`.

## Funding and assistance

The Researchers would like to thank the Deanship of Graduate Studies and Scientific Research at Qassim University (https://www.qu.edu.sa) for financial support (QU-APC-2026). OpenAI ChatGPT/Codex assisted text, mathematical checks, Python implementation, table/figure generation and computational verification. Public measured inputs are distinguished from model-only interventions. Author interpretation and approval remain essential.
