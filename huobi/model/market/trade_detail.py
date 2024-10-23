class TradeDetail:
    """
    The trade information with price and amount etc.

    :member
        price: The trading price in quote currency.
        amount: The trading volume in base currency.
        tradeId: The unique trade id of this trade.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        direction: The direction of the taker trade: 'buy' or 'sell'.
    """

    def __init__(self):
        self.price = 0.0
        self.amount = 0.0
        self.tradeId = 0
        self.ts = 0
        self.direction = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.tradeId, format_data + "Trade Id")
        PrintBasic.print_basic(self.ts, format_data + "Trade Time")
        PrintBasic.print_basic(self.price, format_data + "Price")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.direction, format_data + "Direction")
