# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.tools import ToolContext

async def get_noaa_link(tool_context: ToolContext) -> dict:
    """
    Retrieves the official website link for NOAA (National Oceanic and Atmospheric Administration).

    Returns:
        dict: A dictionary containing the official NOAA link.
    """
    return {"url": "https://www.noaa.gov"}
