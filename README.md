<img src="https://leakdata.io/logo-fallback.png" alt="LeakData" width="240">

# Check exposure from your AI workspace

Connect your LeakData account to check breach exposure for your verified email and company domains. Get a concise account-linked summary without requesting raw breach records.

**Release preparation:** this repository prepares LeakData's remote MCP Registry entry. Version 1.3.1 is awaiting production deployment and live client verification. Registry publication has not occurred.

[Create an account](https://leakdata.io/register?utm_source=mcp_registry&utm_medium=integration&utm_campaign=marketplace) · [View plans](https://leakdata.io/pricing?utm_source=mcp_registry&utm_medium=integration&utm_campaign=marketplace) · [Documentation](https://leakdata.io/docs)

## Connect your account

Use `https://leakdata.io/mcp` as a remote Streamable HTTP server in a supported MCP client. Complete the OAuth sign-in on LeakData and approve the permissions you want to use. Client support and account eligibility vary; a registry entry does not grant access to a client's paid features or directory.

The server uses OAuth with PKCE and grants `search` and `password-check` scopes. No API key or client secret belongs in the connection URL or a prompt. Your LeakData plan, account permissions and usage limits apply separately.

## Available checks

| Tool | Purpose |
| --- | --- |
| `leakdata.search` | Search exposure for the primary email verified on your linked account, or an exact domain whose ownership you verified. |
| `leakdata.password_prefix_check` | Check a five-character prefix of a SHA-1 password hash computed locally. |

For your own verified email, the client can omit the search query. For a domain, provide its exact name; there is no domain-listing tool. Neither tool changes accounts, sends messages or performs remediation.

Never enter a plaintext password or complete password hash. Prefix results describe a group of possible hashes and cannot identify whether one particular password is exposed. A no-match result is limited evidence, not a guarantee that an account or password is safe.

## Privacy and control

Searches are scoped to the assets verified on the linked account. Arbitrary third-party identifiers, usernames, phone numbers, credentials and raw breach rows are outside this tool surface. Revoke the connection in LeakData when you no longer need it.

This repository contains discovery metadata and publishing checks. The hosted service's implementation is maintained separately. MCP Registry publication, client compatibility and marketplace approval are separate statuses; this entry does not imply Google, Microsoft, Anthropic or OpenAI approval.

[Privacy](https://leakdata.io/privacy) · [Terms](https://leakdata.io/terms) · [OAuth guide](https://leakdata.io/auth.md)

For account or setup help, contact [support@leakdata.io](mailto:support@leakdata.io). Send vulnerability reports privately to [security@leakdata.io](mailto:security@leakdata.io).
