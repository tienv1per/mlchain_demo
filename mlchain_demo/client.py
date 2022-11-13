from mlchain.client import Client
import cv2
import pdb;

model = Client(api_address='http://0.0.0.0:8001').model()
img = cv2.imread('/home/tienviper/Pictures/Screenshot from 2022-10-16 16-48-40.png')
pred = model.predict(img)
print(pred)
pdb.set_trace()