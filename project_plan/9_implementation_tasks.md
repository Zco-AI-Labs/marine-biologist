## 📋 9. Implementation Tasks
This checklist maps the precise, step-by-step coding and configuration changes required to implement this agent. Mark tasks as `[ ]` (unstarted), `[/]` (in progress), or `[x]` (completed) as you execute the implementation.

### Phase 1: Configuration & Metadata
- [ ] Update `app/agent.py` to set the `AdkAgent` name parameter to `"marine_biologist_expert"` and write an optimized description detailing its oceanographic and atmospheric resource retrieval capabilities.

### Phase 2: Business Logic & Tool Implementation
- [ ] Update the system instructions inside `app/SKILL.md` to define the Marine Biologist Expert agent persona and instruct it to call `get_noaa_link` for official NOAA inquiries.
- [ ] Implement the tool handler in `app/scripts/get_noaa_link.py` returning `{"url": "https://www.noaa.gov"}`.

### Phase 3: UI/Widgets Definition
- [ ] Scaffold the Lego block widget configuration `noaa_resource_card.json` inside the `app/ui/widgets/` folder.

### Phase 4: Verification & Testing
- [ ] Create a unit test inside `tests/test_get_noaa_link.py` to assert that the `get_noaa_link` tool handler returns the expected URL.
- [ ] Run the test suite with `uv run pytest tests/`.
- [ ] Manually test via local playground execution to verify end-to-end routing.
