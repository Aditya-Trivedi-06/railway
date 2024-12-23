from web.data import *

def extractData(request):
    data = {}
    # required
    totalCost = 0

    data["JobId"] = request.form["JobId"]
    data["date"] = request.form["date"]
    data["clientName"] = request.form["clientName"]
    data["qty"] = request.form["qty"]
    data["jobName"] = request.form["jobName"]
    data["description"] = request.form["description"]

    # Paper
    data["paperSupplierName"] = request.form["paperSupplierName"]
    data["paperType"] = request.form["paperType"]
    data["gsm"] = request.form["gsm"]
    data["paperLength"] = request.form["paperLength"]
    data["paperWidth"] = request.form["paperWidth"]
    data["paperSize"] = request.form["paperSize"]
    data["paperQty"] = request.form["paperQty"]
    data["paperCost"] = request.form["paperCost"]
    totalCost += 0 if data["paperCost"] == "" else int(data["paperCost"])

    # Printing
    data["printingSupplierName"] = request.form["printingSupplierName"]
    data["color"] = request.form["color"]
    data["printingDescription"] = request.form["printingDescription"]
    data["printSize"] = request.form["printSize"]
    data["printQty"] = request.form["printQty"]
    data["printCost"] = request.form["printCost"]
    totalCost += 0 if data["printCost"] == "" else int(data["printCost"])

    # Corrugation
    data["corrugationSupplierName"] = request.form["corrugationSupplierName"]
    data["ply"] = request.form["ply"]
    data["plyDescription"] = request.form["plyDescription"]
    data["plySize"] = request.form["plySize"]
    data["plyQty"] = request.form["plyQty"]
    data["plyCost"] = request.form["plyCost"]
    totalCost += 0 if data["plyCost"] == "" else int(data["plyCost"])

    # Others
    data["plateSupplierName"] = request.form["plateSupplierName"]
    data["plateQty"] = request.form["plateQty"]
    data["plateCost"] = request.form["plateCost"]
    totalCost += 0 if data["plateCost"] == "" else int(data["plateCost"])

    data["punchSuppliers"] = request.form["punchSupplierName"]
    data["punchQty"] = request.form["punchQty"]
    data["punchCost"] = request.form["punchCost"]
    totalCost += 0 if data["punchCost"] == "" else int(data["punchCost"])

    data["varnishSuppliers"] = request.form["varnishSupplierName"]
    data["varnishQty"] = request.form["varnishQty"]
    data["varnishCost"] = request.form["varnishCost"]
    totalCost += 0 if data["varnishCost"] == "" else int(data["varnishCost"])

    data["laminationSuppliers"] = request.form["laminationSupplierName"]
    data["laminationQty"] = request.form["laminationQty"]
    data["laminationCost"] = request.form["laminationCost"]
    totalCost += 0 if data["laminationCost"] == "" else int(data["laminationCost"])

    data["punchingSuppliers"] = request.form["punchingSupplierName"]
    data["punchingQty"] = request.form["punchingQty"]
    data["punchingCost"] = request.form["punchingCost"]
    totalCost += 0 if data["punchingCost"] == "" else int(data["punchingCost"])

    data["pastingSuppliers"] = request.form["pastingSupplierName"]
    data["pastingQty"] = request.form["pastingQty"]
    data["pastingCost"] = request.form["pastingCost"]
    totalCost += 0 if data["pastingCost"] == "" else int(data["pastingCost"])

    data["jobCost"] = totalCost

    return data
