"""Check public metadata before registry publishing; never handles account tokens."""
import json
import os
import urllib.request
from pathlib import Path


def read_public_json(url):
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "LeakData-Registry-Publisher/1.0 (+https://leakdata.io/docs)"})
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise SystemExit("Public metadata is unavailable")
        return json.load(response)


server = json.loads(Path("server.json").read_text())
expected = os.environ.get("EXPECTED_MCP_VERSION", "")
if not expected or server["version"] != expected:
    raise SystemExit("Requested version must exactly match server.json")
if server["name"] != "io.github.leakdatahq/leakdata-mcp":
    raise SystemExit("Unexpected registry namespace")
if server["remotes"] != [{"type": "streamable-http", "url": "https://leakdata.io/mcp"}]:
    raise SystemExit("Unexpected remote endpoint")
card = read_public_json("https://leakdata.io/.well-known/mcp/server-card.json")
if card.get("serverInfo", {}).get("version") != expected:
    raise SystemExit("Live MCP version does not match the requested registry version")
if card.get("transport") != {"type": "streamable-http", "endpoint": "https://leakdata.io/mcp"}:
    raise SystemExit("Live transport differs from the registry entry")
tools = card.get("tools", [])
if {item.get("name") for item in tools} != {"leakdata.search", "leakdata.password_prefix_check"}:
    raise SystemExit("Live tool surface changed; review before publishing")
if not all(item.get("annotations", {}).get("readOnlyHint") is True for item in tools):
    raise SystemExit("Tool read-only contract changed; review before publishing")
resource = read_public_json("https://leakdata.io/.well-known/oauth-protected-resource")
if resource.get("resource") != "https://leakdata.io/mcp":
    raise SystemExit("OAuth resource mismatch")
if set(resource.get("scopes_supported", [])) != {"search", "password-check"}:
    raise SystemExit("OAuth scopes changed; review before publishing")
print("Exact live MCP version, endpoint, tools and OAuth scopes verified")
