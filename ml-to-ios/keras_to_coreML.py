# Keras to CoreML
# To convert your model from Keras to CoreML, we need to do few more additional steps. Our deep learning model expects a 28×28 normalized grayscale image, and gives probabilities for the class predictions as output. 

import coremltools
output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
scale = 1/255.

coreml_model = coremltools.converters.keras.convert('./handWritten.h5',
													input_names='image',
													image_input_names='image',
													output_names='output',
													class_labels= output_labels,
													image_scale=scale)

coreml_model.author = 'Gerardo Lopez Falcon'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Model to classify hand written digit'
coreml_model.input_description['image'] = 'Grayscale image of hand written digit'
coreml_model.output_description['output'] = 'Predicted digit'

coreml_model.save('handWritten.mlmodel')

# python kears_to_coreML.py