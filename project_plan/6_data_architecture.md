## 💾 6. Data Architecture & DB Schemas
Define the collections, subcollections, fields, and indexes. Strictly adhere to ADK scoping paths:
*   **User Scope:** `platform_users/{user_id}/agent_data/{agent_id}/{collection_name}`
*   **Hub Scope:** `organizations/{org_id}/hubs/{hub_id}/agent_data/{agent_id}/{collection_name}`
*   **Org Scope:** `organizations/{org_id}/agent_data/{agent_id}/{collection_name}`
*   **User Tokens:** `platform_users/{user_id}/tokens/{agent_id}/{token_name}`

> [!NOTE]
> The Marine Biologist Expert agent is entirely stateless and does not read, write, or persist any data in Firestore. No collections, subcollections, or user tokens are defined or required for this agent.
