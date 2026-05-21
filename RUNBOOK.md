# Runbook

This runbook is the authoritative reviewer-facing command path for the paper
experiment. The public replay does not require a private source repository and
does not call an API.

## Setup

```bash
git clone <repo-url>
cd legal-extraction-eval-harness

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

Use exactly `'.[test]'` in zsh. The quotes prevent shell expansion issues.

## One-Command Reviewer Check

```bash
python scripts/reviewer_replay_check.py --repo-root .
```

This command verifies:

- Python version and package imports.
- Readiness status for the checked-in bounded HS source bundle.
- Required paper run directories.
- The integrated 38-artifact paper result.
- Public-release denylist guardrails.
- Full regression tests.

Expected paper-level result:

```text
paper_eval_20260520        positive baseline
paper_negative_20260520    controlled fault-injection run
paper_integrated_20260520  primary 38-artifact validator-driven paper run
```

Expected integrated result:

- 38 artifacts.
- 28 baseline artifacts and 10 fault-injection artifacts.
- Gate distribution: 22 `pass`, 8 `pass_with_notes`, 6
  `blocked_pending_research`, 2 `blocked_pending_rerun`.
- Detection aggregates: gate accuracy 1.0, micro recall 1.0, zero false
  negatives.

## Optional Regeneration

To regenerate reviewer-local runs without overwriting the canonical paper runs:

```bash
python scripts/reviewer_replay_check.py --repo-root . --regenerate
```

This creates:

- `runs/reviewer_negative_replay/`
- `runs/reviewer_integrated_replay/`

The script then checks the regenerated integrated run against the same
paper-level invariants.

Equivalent manual commands:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.readiness --repo-root . --json

PYTHONPATH=src python3 -m legal_extract_eval.negative_run \
  --repo-root . \
  --run-id reviewer_negative_replay \
  --base-run paper_eval_20260520 \
  --force

PYTHONPATH=src python3 -m legal_extract_eval.integrated_run \
  --repo-root . \
  --run-id reviewer_integrated_replay \
  --positive-run paper_eval_20260520 \
  --negative-run reviewer_negative_replay \
  --force
```

## No-Install Fallback

If editable install is unavailable, run from the repository root:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.readiness --repo-root .
PYTHONPATH=src python3 -m pytest -q
```

The editable install remains preferred because it prevents
`ModuleNotFoundError: legal_extract_eval` when reviewers run commands from a
different shell state.

## Troubleshooting

- **Python version error:** use Python 3.11 or newer.
- **`pytest` missing:** run `python -m pip install -e '.[test]'`.
- **`ModuleNotFoundError: legal_extract_eval`:** use the editable install or
  prefix commands with `PYTHONPATH=src` from the repository root.
- **Wrong working directory:** run commands from `legal-extraction-eval-harness`.
- **Private source repository requested:** omit `--source-repo-root` for public
  replay. The checked-in bounded source bundle is sufficient.
- **Reviewer replay directories already exist:** `--regenerate` overwrites only
  `reviewer_negative_replay` and `reviewer_integrated_replay`, not the canonical
  paper runs.
- **zsh install quoting issue:** use `python -m pip install -e '.[test]'`
  exactly.

## Maintainer-Only Rebuilds

Maintainers with a private exported source repository can rebuild the pre-HS
slice in copy-only mode:

```bash
PYTHONPATH=src python3 scripts/build_pre_hs_slice.py \
  --source-repo-root /path/to/private-source-repo \
  --harness-root .
```

This path is not required for AAAI/reviewer replay.
