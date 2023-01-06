from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:

    def __init__(
        self,
        ref: str,
        sku: str,
        qty: int,
        eta: Optional[date]
    ):

class Hello:

    def __init__(self, bas):




    def allocate(self, order_line: OrderLine):
        self.available_qty -= order_line.qty
