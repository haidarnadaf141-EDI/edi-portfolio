
# 850 → CSV Mapping (Demo)

**Input:** ANSI X12 850 (Purchase Order)  
**Output:** CSV with fields: `OrderID, OrderDate, BuyerName, ShipToName, ItemCode, Qty, Price`

## Field Map
- BEG03 → OrderID
- BEG05 → OrderDate (format CCYYMMDD → YYYY-MM-DD)
- N1[BY]/N102 → BuyerName
- N1[ST]/N102 → ShipToName
- PO102 → Qty
- PO104 → Price
- PO106='VP' → PO107 → ItemCode

## Sample CSV
```
OrderID,OrderDate,BuyerName,ShipToName,ItemCode,Qty,Price
123456,2025-09-07,ABC Company,John Doe,ITEM001,50,15.00
```

## Notes
- This is a minimal example (single line). Real-world maps must handle multiple PO1 loops, repeats, missing fields, and additional qualifiers (e.g., BP, VN).
