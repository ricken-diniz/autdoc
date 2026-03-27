from ultralytics import YOLO

def extract_document(image):
    """
    Crop the image to remove the background

    args:
    - image: image in PIL format
    """
    
    model = YOLO('yolo11n.pt')

    if image is None:
        raise ValueError("Não foi possível carregar a imagem")

    results = model(image)
    
    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            croped_image = image.crop((x1, y1, x2, y2))

        if croped_image and croped_image.width > 0 and croped_image.height > 0:
            return croped_image
    
    return image