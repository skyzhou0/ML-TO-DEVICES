1. What is Core ML.
Core ML is new machine learning framework from Apple. It brings machine learning models to Apple devices and makes it easy for developers to take an advantage of ML. We can use a dozen of models prepared by Apple or convert the open-sourced model from popular ML frameworks like Keras, Caffe or scikit-learn.

2. How does it work.
a- You need to create a data model using some ML Framework like Caffe, turi, Keras, etc.
b- To install the Python framework called Core ML Tools, it converts the data model to Core ML format. The result of the conversion is a file with a mlmodel extension.
c- That is it, you take the model created by Core ML Tools and use it withit your mobile app.


3. Installation.
conda install pandas matplotlib jupyter notebook scipy opencv
pip install -U scikit-learn==0.15
pip install -U coremltools
pip install tensorflow==1.1
pip install keras==2.0.6
pip install h5py