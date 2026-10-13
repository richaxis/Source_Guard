# SourceGuard

SourceGuard is a standalone GenLayer Intelligent Contract for resolving evidence-backed public claims. A user registers a claim and publishes the criteria that should determine its outcome, then attaches HTTPS source URLs. GenLayer's nondeterministic evaluation reads the sources and assesses the claim; `gl.eq_principle.strict_eq` requires validators to agree on the normalized decision.

## Why it is useful

- Creates an on-chain record of the claim, criteria, evidence links, outcome, and reasoning.
- Supports three outcomes: `supported`, `refuted`, and `insufficient`.
- Requires evidence before resolution.
- Allows a resolved claim to be challenged once and sent through a new resolution.
- Keeps basic state checks deterministic while using consensus for interpretation of external evidence.

## Repository layout

```text
SourceGuard/
├── contracts/
│   └── source_guard.py
├── scripts/
│   └── README.md
├── tests/
│   └── test_design_checks.py
├── README.md
├── SUBMISSION.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
└── requirements.txt
```

## Contract workflow

1. `register_claim(title, claim_text, resolution_criteria)` creates an open claim.
2. `add_evidence(claim_id, source_url, note)` attaches an HTTPS source.
3. `resolve_claim(claim_id)` renders registered sources and evaluates them through GenLayer consensus.
4. `challenge_claim(claim_id, reason)` marks a resolved claim as challenged.
5. `resolve_claim(claim_id)` can then evaluate the challenged claim again.
6. `get_claim`, `get_claims`, and `get_evidence` expose contract state.

## Deploy on GenLayer Studio

The requested target is GenLayer Studio Network, Chain ID `61999`, RPC `https://studio.genlayer.com/api`, explorer `https://explorer-studio.genlayer.com`.

Deploy `contracts/source_guard.py` in Studio using the dependency declaration at the top of the source file. The constructor takes no arguments. After deployment, record the contract address and test transaction hashes in `SUBMISSION.md` or your project notes.

## Example

- Title: `Is the release affected by CVE-YYYY-NNNN?`
- Claim: `Version 2.4.1 of ExamplePackage is affected by CVE-YYYY-NNNN.`
- Criteria: `Use the vendor advisory and a recognized vulnerability database. Return supported only if the cited evidence explicitly identifies the package and affected version.`
- Evidence: the official vendor advisory URL and a CVE database URL.

Use real, relevant sources in an actual deployment. The example identifiers are placeholders.

## Run local design checks

These are source-level checks only, not a GenLayer VM simulation:

```bash
python -m unittest discover -s tests
```

## Important limitations

- The contract stores source URLs and the evaluator's reasoning; it does not guarantee that a website is truthful, available forever, or free from manipulation.
- Strict equivalence helps validators converge on the same decision, but does not guarantee the decision is factually correct.
- A challenge is a re-review workflow, not a cryptographic appeal court or an automatic financial penalty.
- No funds or rewards are held or transferred by this contract.
- Review and test the source in the current Studio environment before treating it as production-ready.
