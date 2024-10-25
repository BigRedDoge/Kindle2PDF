from doctr.io import DocumentFile
from doctr.io import read_img_as_numpy
from doctr.models import ocr_predictor
import cv2


img = cv2.imread(str("page2.png"))
print(img)
pages = read_img_as_numpy('page2.png')


model = ocr_predictor(det_arch='fast-base', pretrained=True)

result = model(pages)

result.show()
print(result)
json_export = result.export()
print(json_export)