# Security considerations

- Treat external webpages as untrusted input. The evaluation prompt explicitly instructs the model not to follow page instructions.
- Use trusted, relevant sources where possible and publish clear resolution criteria before adding evidence.
- The contract does not authenticate the truthfulness or authorship of an external source.
- Evidence URLs must use HTTPS, but this does not guarantee that the host is trustworthy.
- The contract does not hold funds or implement rewards.
- Review storage limits, web rendering behavior, type support, and consensus API compatibility in the current GenLayer Studio version before deployment.
- Do not use SourceGuard as the sole authority for legal, medical, financial, or other high-stakes decisions.
- The bundled tests are offline source/design checks, not security audits or a GenLayer VM test suite.
