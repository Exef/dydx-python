from decimal import Decimal

# ------------ Universal Constants ------------
NETWORK_ID = 1
MAX_SOLIDITY_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935  # noqa: E501
FOUR_WEEKS_IN_SECONDS = 2419200

# ------------ Addresses ------------
TAKER_ACCOUNT_OWNER = '0xf809e07870dca762B9536d61A4fBEF1a17178092'

# ------------ Contract Addresses ------------
CANONICAL_ORDERS_ADDRESS = '0xCd81398895bEa7AD9EFF273aeFFc41A9d83B4dAD'
SOLO_MARGIN_ADDRESS = '0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e'
PAYABLE_PROXY_ADDRESS = '0xa8b39829cE2246f89B31C013b8Cde15506Fb9A76'
WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
SAI_ADDRESS = '0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359'
USDC_ADDRESS = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
DAI_ADDRESS = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
WETH_PROXY_ADDRESS = '0x17ac4cC32696987CEa1737343188716b1D827E7B'
BTC_P1_ORDERS_ADDRESS = '0x3ea6F88eC8F7b24Bb3Ad206fa80124210e8e28F3'
BTC_PERPETUAL_ADDRESS = '0x07aBe965500A49370D331eCD613c7AC47dD6e547'
LINK_P1_ORDERS_ADDRESS = '0xaC14B70adBf42bedE4E4c7Ef67E8CB618b0D4506'
LINK_PERPETUAL_ADDRESS = '0x1c50c582c7066049C560Bca20416b1d9E0dfb003'
ETH_P1_ORDERS_ADDRESS = '0x1d3ccceEE6d9f9c3b79ed5fAdD98E32B5d48b22E'
ETH_PERPETUAL_ADDRESS = '0x09403FD14510F8196F7879eF514827CD76960B5d'
CURRENCY_CONVERTER_PROXY_ADDRESS = '0xA0d885316Be23dE8bB19E7C53F6d483279E3467D'

# ------------ Protocol Enums ------------
ACTION_TYPE_DEPOSIT = 0
ACTION_TYPE_WITHDRAW = 1

REFERENCE_DELTA = 0
REFERENCE_TARGET = 1

# ------------ Markets ------------
MARKET_ETH = 0
MARKET_WETH = 0
MARKET_SAI = 1
MARKET_USDC = 2
MARKET_DAI = 3
MARKET_INVALID = 4

# ------------ Pairs ------------
PAIR_WETH_DAI = 'WETH-DAI'
PAIR_WETH_USDC = 'WETH-USDC'
PAIR_DAI_USDC = 'DAI-USDC'
PAIR_PBTC_USDC = 'PBTC-USDC'
PAIR_PLINK_USDC = 'PLINK-USDC'
PAIR_WETH_PUSD = 'WETH-PUSD'

DECIMALS_WETH = 18
DECIMALS_SAI = 18
DECIMALS_USDC = 6
DECIMALS_DAI = 18
DECIMALS_PBTC = 8
DECIMALS_PLINK = 6
DECIMALS_PUSD = 6

# ------------ Sides ------------
SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

# ------------ Fees ------------
FROM_BIPS = Decimal('1e-4')
DEFAULT_LIMIT_FEE = Decimal(100) * FROM_BIPS
FEE_ZERO = Decimal(0)

# ------------ Transaction Constants ------------
DEFAULT_GAS_AMOUNT = 250000
DEFAULT_GAS_MULTIPLIER = 1.5
DEFAULT_GAS_PRICE = 4000000000
DEFAULT_GAS_PRICE_ADDITION = 3

# ------------ Protocol ------------
MINIMUM_COLLATERALIZATION = 1.15
PRICE_ORACLE_USD_MULTIPLIER = 10 ** 36

# ------------ Math ------------
BASE_DECIMAL = Decimal(10 ** 18)

# ------------ Account Numbers ------------
ACCOUNT_NUMBERS_SPOT = 78249916358380492593314239409032173911741268194868200833150293576330928686520  # NOQA
ACCOUNT_NUMBERS_MARGIN = 0
