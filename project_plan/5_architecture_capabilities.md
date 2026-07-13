## 🛠️ 5. Architecture & Capabilities

### System Instructions (`app/SKILL.md`)
```text
You are the Marine Biologist Expert agent. You specialize in providing oceanographic resources and official information about oceans, marine life, and the atmosphere. 

When users ask for official resources, external information, or links regarding NOAA (National Oceanic and Atmospheric Administration), you must call the `get_noaa_link` tool to retrieve the correct official website URL.

Guidelines:
1. Provide helpful, concise marine biology context when asked.
2. Present the NOAA URL clearly.
3. Keep all responses brief and factual.
```

### Tool Implementations (`app/scripts/`)
Define the Python function signatures, docstrings, type-hints, and return types for each tool inside the package's `app/scripts/` folder as individual `{tool_name}.py` files. The ADK automatically parses these to build Gemini function declarations.

```python
# app/scripts/get_noaa_link.py
from google.adk.tools import ToolContext

async def get_noaa_link(tool_context: ToolContext) -> dict:
    """
    Retrieves the official website link for NOAA (National Oceanic and Atmospheric Administration).

    Returns:
        dict: A dictionary containing the official NOAA link.
    """
    # Tool implementation logic...
```

### 🔑 Tool Privileges Matrix
Defines which platform-level privileges grant access to which specific capabilities and tools.

| Privilege Name | Description of Granted Capabilities / Tools |
| :--- | :--- |
| None | The `get_noaa_link` tool does not require specialized privileges and is accessible to all users. |

### Model Context Protocol (MCP) & Agent-to-Agent (A2A) Connections
Define any external connections (MCP servers, custom OAuth providers, or external agents).

*   **MCP Servers:** None
*   **External Agents (A2A):** None
*   **Custom OAuth2 Providers:** None

### Required Secrets (Agent Secrets Vault)
Define any external API keys or client secrets that must be configured and uploaded to the platform Secrets Vault.

| Secret Name | Description | Required? (True/False) |
| :--- | :--- | :--- |
| None | N/A | False |
