from roboflow import Roboflow
rf = Roboflow(api_key="RURUNkefw6jefZRQABl5")
project = rf.workspace().project("obesity")
model = project.version(3).model

# infer on a local image
# file = '2016-09-30-14-49-53-554.jpg'
# pred=list(model.predict(file, confidence=40, overlap=30))
# print(pred[0]['class'])

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
