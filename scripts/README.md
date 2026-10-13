# Deployment scripts

Deploy the contract through GenLayer Studio's contract deployment interface.

1. Open https://studio.genlayer.com/
2. Select the Studio Network (Chain ID 61999).
3. Create a contract from `contracts/source_guard.py`.
4. Compile and deploy, providing no constructor arguments.
5. Save the deployed contract address and transaction details.
6. Call `register_claim`, add at least one HTTPS source with `add_evidence`,
   then call `resolve_claim`.
7. Verify the resulting state in the Studio explorer.

This folder intentionally does not contain an automated deployment script that
guesses the current Studio SDK or wallet configuration. Use the SDK version
documented by the Studio environment you are using.
