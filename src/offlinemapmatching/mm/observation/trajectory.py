from .observation import *
from qgis.core import *

class Trajectory:
	
	def __init__(self, point_layer, id_field):
		self.observations = []
		
		#extract all points from the QGIS layer
		features = point_layer.getFeatures()
		for feature in feattures:
			point = feature.geometry()
			id = feature[id_field]
			
			#create a new observation object and add them to our observation list
			obs = observation(point, id)
			self.observations.append(obs)
	
