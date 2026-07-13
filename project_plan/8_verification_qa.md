## 🧪 8. Verification & QA Plan
Outline how the agent's functionality will be tested.

*   **Automated Tests:** `uv run pytest tests/`
*   **Manual Verification Checklist:**
    1.  `[ ]` Invoke the `get_noaa_link` tool in the Holodeck playground or vertex engine and confirm it returns `{"url": "https://www.noaa.gov"}`.
    2.  `[ ]` Ask the agent in the chat playground "Can you give me the NOAA website?" and verify the agent successfully resolves the query by calling `get_noaa_link` and providing the link.
    3.  `[ ]` Verify visual presentation on Chat UI (ensuring standard markdown link is correctly rendered as a hyperlink).
    4.  `[ ]` Test speech output simulated responses to confirm no markdown blocks are spoken.
