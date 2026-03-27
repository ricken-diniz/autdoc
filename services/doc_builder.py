from docxtpl import DocxTemplate
from sysvars import SysVars as svar

def gen_doc(context):

    doc = DocxTemplate(svar.DATA_ROOT / "model.docx")
    doc.render(context)
    output = svar.DATA_ROOT / "document.docx"
    doc.save(output)
    return
