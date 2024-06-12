from web.data import *

def extractData(request):
    data = {}
    # required
    data['JobId'] = request.form['JobId']
    data['date'] = request.form['date']
    data['clientName'] = request.form['clientName']
    data['qty'] = request.form['qty']
    data['jobName'] = request.form['jobName']
    data['description'] = request.form['description']

    # Paper
    data['paperSupplierName'] = request.form['paperSupplierName']
    data['paperType'] = request.form['paperType']
    data['gsm'] = request.form['gsm']
    data['paperLength'] = request.form['paperLength']
    data['paperWidth'] = request.form['paperWidth']
    data["paperSize"] = request.form["paperSize"]
    data['paperQty'] = request.form['paperQty']

    # Printing
    data['printingSupplierName'] = request.form['printingSupplierName']
    data['color'] = request.form['color']
    data['printingDescription'] = request.form['printingDescription']
    data['printSize'] = request.form['printSize']
    data['printQty'] = request.form['printQty']

    # Corrugation
    data['corrugationSupplierName'] = request.form['corrugationSupplierName']
    data['ply'] = request.form['ply']
    data['plyDescription'] = request.form['plyDescription']
    data['plySize'] = request.form['plySize']
    data['plyQty'] = request.form['plyQty']

    # Others
    data['plateSupplierName'] = request.form['plateSupplierName']
    data['plateQty'] = request.form['plateQty']
    data['punchSuppliers'] = request.form['punchSupplierName']
    data['punchQty'] = request.form['punchQty']
    data['varnishSuppliers'] = request.form['varnishSupplierName']
    data['varnishQty'] = request.form['varnishQty']
    data['laminationSuppliers'] = request.form['laminationSupplierName']
    data['laminationQty'] = request.form['laminationQty']
    data['punchingSuppliers'] = request.form['punchingSupplierName']
    data['punchingQty'] = request.form['punchingQty']
    data['pastingSuppliers'] = request.form['pastingSupplierName']
    data['pastingQty'] = request.form['pastingQty']

    return data
