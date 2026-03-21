from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any

app = FastAPI()

shipments = {
    12701: {
        "weight" : 1.2,
        "content" : "glassware",
        "status" : "placed"
    },
    12702: {
        "weight" : 3.5,
        "content" : "electronics",
        "status" : "in transit"
    },
    12703: {
        "weight" : 0.8,
        "content" : "books",
        "status" : "delivered"
    },
    12704: {
        "weight" : 12.0,
        "content" : "wooden table",
        "status" : "placed"
    },
    12705: {
        "weight" : 2.3,
        "content" : "clothing",
        "status" : "in transit"
    },
    12706: {
        "weight" : 5.7,
        "content" : "kitchenware",
        "status" : "out for delivery"
    },
    12707: {
        "weight" : 0.3,
        "content" : "jewelry",
        "status" : "delivered"
    }
}


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment/")
def get_shipment(id: int) -> dict[str, Any]:

    if not id:
        id = max(shipments.keys())
        return shipments[id]

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist"
        )
    return shipments[id]



@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )