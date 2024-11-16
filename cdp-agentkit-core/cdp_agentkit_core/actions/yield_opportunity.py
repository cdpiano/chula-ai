from collections.abc import Callable

from cdp import Wallet
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions import CdpAction

REQUEST_YIELD_OPPORTUNITY_PROMPT = """
This tool will compare various yield generation to help you select the best yield available. 
By analyzing different protocols and their respective yield rates, this tool provides insights to maximize your returns. 
It considers factors such as risk, liquidity, and duration to ensure you make informed decisions. 
This feature is essential for optimizing your investment strategy and increasing overall profitability.
It is only supported on Base Sepolia and Base Mainnet.
"""


class RequestYieldOpportunityInput(BaseModel):
    """Input argument schema for request yield generation action."""


def request_yield_generation(wallet: Wallet) -> str:
    """Request yield generation for the default address in the wallet.

    Args:
        wallet (Wallet): The wallet to yield generation

    Returns:
        str: Confirmation message with transaction details

    """
    try:
        ""
    except Exception as e:
        return f"Error requesting yield generation {e!s}"

    return f"aave supply"


class RequestYieldOpportunityAction(CdpAction):
    """Request yield generation action."""

    name: str = "request_yield_generation"
    description: str = REQUEST_YIELD_OPPORTUNITY_PROMPT
    args_schema: type[BaseModel] | None = RequestYieldOpportunityInput
    func: Callable[..., str] = request_yield_generation
