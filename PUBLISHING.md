# Publishing status

Updated September 10, 2026. The official mcp-publisher 1.8.1 validation API accepted server.json. No LeakData entry was returned by the official registry search before publication.

The prepared entry uses the GitHub-owned namespace `io.github.leakdatahq/leakdata-mcp`, the public Streamable HTTP endpoint and the existing 96×96 brand icon. The optional repository field is omitted because this metadata repository is not the hosted implementation's source code.

## Live acceptance

- [Protected production rollout succeeded](https://github.com/leakdatahq/leakdata/actions/runs/34419230479) for commit `45840a219a8764d630a3cf0be0ec1035ee7ec9cd`. Public discovery and initialization report MCP 1.3.2.
- Ten public checks passed, including exact tool schemas, read-only annotations, authentication challenge, domain rejection and origin validation.
- Actual ChatGPT web sessions passed five positive cases: implicit verified email, explicit controlled account email, uppercase and lowercase supplied prefixes, and a second supplied prefix. Actual request and response panels were checked.
- Three negative cases passed without tool calls: third-party private data and credentials, plaintext password guidance, and unsupported domains.
- Antigravity completed new OAuth consent and actual verified-email calls. Its full client package acceptance is recorded in the separate Google client repository. An older stored connection required reauthentication; its cause was not established.
- Native mobile clients, server-side revocation and every third-party MCP client have not been validated. Registry listing does not imply their compatibility or approval.

## Publish and verify

1. Run the official publisher validation against server.json.
2. Publish through GitHub Actions OIDC from the leakdatahq-owned metadata repository, using a main-only publishing job and the pinned official publisher binary.
3. Read the entry back from the official Registry API and record its version and receipt here. Publication is pending until that readback succeeds.

Official references:

- https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/remote-servers.mdx
- https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx

The pinned publisher is 1.8.1. The darwin-arm64 download was checked against GitHub's release SHA-256 digest. Its validate subcommand works independently of publishing; the subcommand help dispatcher currently omits its help text.
