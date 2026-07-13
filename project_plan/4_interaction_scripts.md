## 💬 4. Interaction Scripts & Conversational Flows
Provide exact transcript logs showing how users interact with the agent. These scripts will serve as prompt references and unit testing paths. 

### 📐 Guidelines for Design:
1. **Interface Modality Adaptation:** Every interaction scenario must explicitly state the behavior and expected output depending on the user's active interface:
   - **Visual Path (Chat UI):** Outlines how the agent renders UI widgets, cards, or custom layouts.
   - **Non-Visual Paths (SMS/Voice):** Outlines how the agent replies using clean, plain text (without markdown, formatting, or JSON placeholders) suitable for text-only messages or voice synthesizers.

---

### Scenario 1: Requesting the NOAA Website Link

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** Can you give me the link to NOAA?
*   **Agent (Behind the Scenes):** Calls `consultAgent` -> calls tool `get_noaa_link`
*   **Agent Message:** "Here is the link to the official NOAA website: [NOAA Website](https://www.noaa.gov)"

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** Get NOAA link
*   **Agent (Behind the Scenes):** Calls tool `get_noaa_link`
*   **Agent Text Reply:** "Here is the official NOAA website link: https://www.noaa.gov"

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** Can you tell me the NOAA web address?
*   **Agent (Behind the Scenes):** Calls tool `get_noaa_link`
*   **Agent Speech Reply:** "You can access the official National Oceanic and Atmospheric Administration website at triple double-u dot noaa dot gov."
