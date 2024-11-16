from collections.abc import Callable

from cdp import Wallet
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions import CdpAction
from cdp_agentkit_core.actions.aerodrome.constants import (
    GENERIC_TOKEN_METADATA_URI,
    AERODROME_FACTORY_ABI,
    get_factory_address,
)

AERODROME_ADD_LIQUIDITY_PROMPT = """
This tool will add liquidity to the Aerodrome protocol using the specified token pair. 
It requires the token addresses and the amounts you wish to supply for each token. 
The liquidity provision mechanism ensures that your assets are effectively utilized within the Aerodrome ecosystem. 
This operation is supported on both Base Sepolia and Base Mainnet.
"""


class AerodromeAddLiquidityInput(BaseModel):
    """Input argument schema for aerodrome add liquidity action."""

    name: str = Field(
        ...,
        description="The name of the token to create, e.g. WowCoin",
    )
    symbol: str = Field(
        ...,
        description="The symbol of the token to create, e.g. WOW",
    )


def aerodrome_add_liquidity(wallet: Wallet, name: str, symbol: str) -> str:
    """Create a Zora Wow ERC20 memecoin.

    Args:
        wallet (Wallet): The wallet to create the token from.
        name (str): The name of the token to create.
        symbol (str): The symbol of the token to create.

    Returns:
        str: A message containing the token creation details.

    """
    factory_address = get_factory_address(wallet.network_id)

    try:
        invocation = wallet.invoke_contract(
            contract_address=factory_address,
            method="deploy",
            abi=AERODROME_FACTORY_ABI,
            args={
                "_tokenCreator": wallet.default_address.address_id,
                "_platformReferrer": "0x0000000000000000000000000000000000000000",
                "_tokenURI": GENERIC_TOKEN_METADATA_URI,
                "_name": name,
                "_symbol": symbol,
            },
        ).wait()
    except Exception as e:
        return f"Error creating Zora Wow ERC20 memecoin {e!s}"

    return f"Created WoW ERC20 memecoin {name} with symbol {symbol} on network {wallet.network_id}.\nTransaction hash for the token creation: {invocation.transaction.transaction_hash}\nTransaction link for the token creation: {invocation.transaction.transaction_link}"


class AerodromeAddLiquidityAction(CdpAction):
    """Zora Wow create token action."""

    name: str = "aerodrome_add_liquidity"
    description: str = AERODROME_ADD_LIQUIDITY_PROMPT
    args_schema: type[BaseModel] | None = AerodromeAddLiquidityInput
    func: Callable[..., str] = aerodrome_add_liquidity
