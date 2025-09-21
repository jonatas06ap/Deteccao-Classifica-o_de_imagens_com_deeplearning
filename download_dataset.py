from roboflow import Roboflow

rf = Roboflow(api_key="jDMFH8bInpzf3zYAXwgP")
project = rf.workspace("patinholilica").project("detection-and-classification-itseo")
version = project.version(3)
dataset = version.download("yolov5")
