
import sys, csv, re
from datetime import datetime

def parse_edi(text):
    # Detect delimiters (simple heuristic)
    seg_term = "~"
    elem_sep = "*"
    # Split into segments and elements
    segments = [s for s in text.strip().split(seg_term) if s.strip()]
    parsed = [seg.split(elem_sep) for seg in segments]
    return parsed

def get_first(parsed, tag):
    for seg in parsed:
        if seg and seg[0] == tag:
            return seg
    return None

def get_n1_name(parsed, qualifier):
    for seg in parsed:
        if seg and seg[0] == "N1" and len(seg) >= 3 and seg[1] == qualifier:
            # N102 is element index 2 (0-based)
            return seg[2]
    return ""

def get_po1_first(parsed):
    for seg in parsed:
        if seg and seg[0] == "PO1":
            return seg
    return None

def find_item_code_from_po1(seg):
    # PO106 qualifier and PO107 value; also supports additional pairs (PO108/PO109, etc.)
    # Indices: PO101 idx=1, PO102 idx=2, PO103 idx=3, PO104 idx=4, PO105 idx=5, PO106 idx=6, PO107 idx=7, and so on
    for i in range(6, len(seg)-1, 2):
        qual = seg[i]
        val = seg[i+1]
        if qual == "VP":
            return val
    return ""

def format_date_ccyymmdd(ccyymmdd):
    if not ccyymmdd:
        return ""
    try:
        return datetime.strptime(ccyymmdd, "%Y%m%d").strftime("%Y-%m-%d")
    except Exception:
        # try YYMMDD
        try:
            return datetime.strptime(ccyymmdd, "%y%m%d").strftime("%Y-%m-%d")
        except Exception:
            return ccyymmdd

def transform_850_to_csv(edi_text, csv_path):
    data = parse_edi(edi_text)
    beg = get_first(data, "BEG")
    po1 = get_po1_first(data)

    order_id = beg[3] if beg and len(beg) > 3 else ""
    order_date_raw = beg[5] if beg and len(beg) > 5 else ""
    order_date = format_date_ccyymmdd(order_date_raw)

    buyer_name = get_n1_name(data, "BY")
    ship_to = get_n1_name(data, "ST")

    qty = po1[2] if po1 and len(po1) > 2 else ""
    price = po1[4] if po1 and len(po1) > 4 else ""

    item_code = find_item_code_from_po1(po1) if po1 else ""

    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["OrderID","OrderDate","BuyerName","ShipToName","ItemCode","Qty","Price"])
        w.writerow([order_id, order_date, buyer_name, ship_to, item_code, qty, price])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transform.py input.edi output.csv")
        sys.exit(1)
    with open(sys.argv[1], "r") as fh:
        edi = fh.read()
    transform_850_to_csv(edi, sys.argv[2])
    print(f"Wrote {sys.argv[2]}")
