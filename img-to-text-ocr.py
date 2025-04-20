import easyocr
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext('input-image.png')

for bbox, text, prob in results:
    print(f"Detected text: {text} (Confidence: {prob:.2f})")
