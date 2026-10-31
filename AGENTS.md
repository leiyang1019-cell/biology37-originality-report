# Independent 37-school biology report

This repository is ONLY for the independent report. Do not import or mix rules/memory from the original research project.

Read WORK_STATE.json, the current Chinese Markdown report, and the dataset dictionary before changing an analysis. The user currently prioritizes prose and tables; preserve completed figures and defer new drawing. Convert to Word only after the user approves the text.

Grade ONLY by the Chinese labels 高原创/较高原创/一般原创/低原创. 高原创 is not combined with 较高原创. Ignore all letter suffixes for grouping. Reference totals: 84,789 unique papers, 37 schools, grades 3,440 / 71,898 / 6,510 / 2,941.

Use WoS Categories as research directions; Research Areas is supplementary. Use full counting within directions, and 1/k fractional counting for concentration. Keep school-owner country statistics separate from all participating affiliation countries. Mainland China, Hong Kong, Macao and Taiwan are consolidated as China; cooperation between them is domestic.

JIF uses the existing 2024 JCR reference (metric year 2023). Keep JIF and 5-year JIF separate. Missing citation/JIF values are unknown, not zero. Cite thresholds >500 and >1000, if used, are not ESI highly-cited flags. CNS and high-citation report sections are deferred; CNS must be independently verified rather than inherited from older tags.

Chapter 4 is approved and analysed. Main cohort is authors with publication-time affiliations to the 37 schools. Use (1/m)^(m-1), and the same formula for corresponding-author order; take the maximum within an author/paper and then sum. Overall author/paper pairs are deduplicated. Rank at six decimals with ties; the current top-100-position observation set contains 107 authors. Preserve ORCID/ResearcherID/name conflict quarantines and verified identity links. Do not merge authors on names alone or assign all coauthors to a paper's owner school. Multi-institution/country counts can overlap.

Snapshot inputs are versioned baselines. Write revisions separately and document changed definitions. Keep the report formal: exclude local join pipelines, server paths and generic data-shortcoming prose from the main text; retain methodological scope and all uncertainties in the audit trail. Never add server passwords, SSH profiles, API keys or cloud credentials to the repository.

On a fresh Cloud task run `python restore_cloud_snapshot.py`, then `python scripts/cloud_data.py verify` and `python scripts/cloud_data.py summary`. Restore preserves files already present, so committed report changes are not overwritten. `python scripts/cloud_data.py init-db` builds a local working SQLite database. Store generated databases under work/, which is ignored by Git. Commit/save important report edits before ending tasks.
