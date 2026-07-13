## 📂 3. Feature Checklist & Interaction Modes
Break down the features. For each feature, outline how the user interacts with the agent under both visual (UI-enabled) and non-visual (SMS, voice/phone) conditions.

### Feature 1: Retrieve NOAA Link
*   **Description:** Retrieves the official website link for NOAA (https://www.noaa.gov).
*   **Visual Interaction Mode:**
    *   *Trigger:* User asks "Give me the NOAA link" or "Where can I find NOAA resources?" in chat.
    *   *UI Rendered:* Standard Chat UI message with a clickable hyperlink to NOAA, or a clean Link Card.
    *   *Form Actions:* None.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:* SMS user texts "NOAA link". Agent responds with: "Here is the official NOAA website link: https://www.noaa.gov"
    *   *Voice/Phone Flow:* Caller asks "What is the NOAA website?". Agent responds with: "You can find NOAA online at triple-w dot noaa dot gov."
    *   *Natural Language Parameters Extracted:* None.
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the agent is active and running.
        *   **WHEN** the user asks to get the NOAA website link.
        *   **THEN** the agent calls the tool `get_noaa_link` and returns the official URL.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** the agent is active.
        *   **WHEN** the user asks an unrelated question (e.g. "What is the capital of France?").
        *   **THEN** the agent politely explains it is a Marine Biologist Expert and redirects the user back to marine biology resources and the NOAA tool.
