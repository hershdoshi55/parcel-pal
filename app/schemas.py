from random import randint
from pydantic import BaseModel, Field
from enum import Enum

def random_destination():
    return randint(11000,11999)

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class Shipment(BaseModel):
    content: str = Field(
        description="Contents of the shipment",
        max_length=30,
    )
    weight: float = Field(
        description="Weight of the shipment in kilograms (kg)",
        le=25, 
        ge=1,
    )
    destination: int | None = Field(
        description="Destination Zipcode",
        default_factory=random_destination,
    )
    status: ShipmentStatus
