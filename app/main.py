from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any

app = FastAPI()

shipments = {
    12701: {"weight": 1.2, "content": "glassware", "status": "placed"},
    12702: {"weight": 3.5, "content": "electronics", "status": "in transit"},
    12703: {"weight": 0.8, "content": "books", "status": "delivered"},
    12704: {"weight": 12.0, "content": "wooden table", "status": "placed"},
    12705: {"weight": 2.3, "content": "clothing", "status": "in transit"},
    12706: {"weight": 5.7, "content": "kitchenware", "status": "out for delivery"},
    12707: {"weight": 0.3, "content": "jewelry", "status": "delivered"},
}


@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    # check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist"
        )
    return shipments[id]


@app.post("/shipment")
def submit_shipment(content: str, weight: float) -> dict[str, int]:

    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25 kgs",
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed",
    }

    return {"id": new_id}

@app.put("/shipment")
def shipment_update(
    id: int, content: str, weight: float, status: str
) -> dict[str, Any]:
    shipments[id] = {
        "weight": weight, 
        "content": content, 
        "status": status,
    }

    return shipments[id]

@app.patch("/shipment")
def patch_shipment(id: int, body: dict[str, Any]):
    shipment = shipments[id]
    shipment.update(body)
    shipments[id] = shipment

    return shipment

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    shipments.pop(id)
    return {"detail": f"shipment with id #{id} is deleted!"}







@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )