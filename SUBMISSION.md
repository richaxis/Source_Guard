# SourceGuard — Submission Notes

## Summary
SourceGuard is a reusable Intelligent Contract primitive for evidence-backed resolution of public claims. It records published criteria, evidence URLs, a consensus-backed outcome, and a concise rationale.

## GenLayer usage
The contract fetches external source text through `gl.nondet.web.render`, evaluates the evidence with `gl.nondet.exec_prompt`, and uses `gl.eq_principle.strict_eq` to require equivalent normalized decisions.

## State design
Each claim records its text, criteria, status, outcome, rationale, evidence count, and challenge state. Evidence records are linked by claim ID.

## Validation and edge cases
- Empty claim fields are rejected.
- Invalid claim IDs are rejected.
- Evidence URLs must use HTTPS.
- Evidence cannot be added after a claim has left the open state.
- A claim cannot be resolved without at least one evidence source.
- Only resolved claims can be challenged, and each claim can be challenged once.
- The evaluator may return `insufficient` rather than forcing a yes/no conclusion.

## Deployment proof
Fill this section in after deploying to GenLayer Studio.

- Network: GenLayer Studio Network
- Chain ID: 61999
- Contract address: TODO
- Deployment transaction: TODO
- Test transaction(s): TODO
- Studio explorer link: TODO

Do not claim the contract is deployed until these fields are completed with real values.
