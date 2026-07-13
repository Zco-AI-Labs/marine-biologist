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

import unittest
from app.scripts.get_noaa_link import get_noaa_link

class TestGetNoaaLink(unittest.IsolatedAsyncioTestCase):
    async def test_get_noaa_link_unittest(self):
        # Invoke tool with None context as it's not needed for this tool
        result = await get_noaa_link(None)
        self.assertEqual(result, {"url": "https://www.noaa.gov"})

try:
    import pytest
    @pytest.mark.asyncio
    async def test_get_noaa_link_pytest():
        result = await get_noaa_link(None)
        assert result == {"url": "https://www.noaa.gov"}
except ImportError:
    pass
