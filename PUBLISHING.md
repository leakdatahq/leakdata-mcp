# Publishing status

Prepared on September 9, 2026. The official mcp-publisher 1.8.1 validation API accepted server.json. No LeakData entry was returned by the official registry search at the start of this task.

The prepared entry uses the GitHub-owned namespace `io.github.leakdatahq/leakdata-mcp`, the public Streamable HTTP endpoint and the existing 96×96 brand icon. The optional repository field is omitted because this metadata repository is not the hosted implementation's source code.

Before publishing:

1. Complete the authorized protected production rollout of MCP version 1.3.1.
2. Verify the actual client consent and tool flows; retain only sanitized evidence.
3. Run the official publisher validation against server.json.
4. Publish through GitHub Actions OIDC from the leakdatahq-owned metadata repository, using a main-only publishing job and the pinned official publisher binary.
5. Read the entry back from the official Registry API and record its version and receipt.

Official references:

- https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/remote-servers.mdx
- https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx

The pinned publisher is 1.8.1. The darwin-arm64 download was checked against GitHub's release SHA-256 digest. Its validate subcommand works independently of publishing; the subcommand help dispatcher currently omits its help text.
