from pypmml import Model

# The model is from http://dmg.org/pmml/pmml_examples/KNIME_PMML_4.1_Examples/single_iris_dectree.xml
#model = Model.load('single_iris_dectree.xml')
model = Model.load('test_pmml_knime.pmml')

test = model.predict({'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2})
print(test)