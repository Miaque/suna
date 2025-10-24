import json
import logging
from datetime import datetime

import pytest

from core.prompts import prompt_zh
from core.prompts.prompt import get_system_prompt
from core.run import PromptManager

logger = logging.getLogger(__name__)


def test_system_prompt():
    now = datetime.now()
    datetime_info = f"\n\n=== CURRENT DATE/TIME INFORMATION ===\n"
    datetime_info += f"Today's date: {now.strftime('%A, %B %d, %Y')}\n"
    datetime_info += f"Current year: {now.strftime('%Y')}\n"
    datetime_info += f"Current month: {now.strftime('%B')}\n"
    datetime_info += f"Current day: {now.strftime('%A')}\n"
    datetime_info += "Use this information for any time-sensitive tasks, research, or when current date/time context is needed.\n"

    system_content = get_system_prompt()
    system_content += datetime_info

    logger.info(json.dumps(system_content, indent=4, ensure_ascii=False))


@pytest.mark.asyncio
async def test_all():
    prompt = await PromptManager.build_system_prompt(
        model_name="", agent_config=None, thread_id="", mcp_wrapper_instance=None
    )
    print(json.dumps(prompt, indent=2, ensure_ascii=False))

def test_zh_prompt():
    print(json.dumps(prompt_zh.get_system_prompt(), indent=2, ensure_ascii=False))
