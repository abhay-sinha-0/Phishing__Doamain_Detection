# Phishing-Domain-Detection
first of all download dataset from kaggle https://www.kaggle.com/datasets/siddharthkumar25/malicious-and-benign-urls <br>
add freature based on 
1. Length based Features
2. Count based Features
3. Binary Features<br>

then we make<br>
**decision tree**
A decision tree is a non-parametric supervised learning algorithm, which is utilized for both classification and regression tasks.

**Random Forest**
Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees.

**Multilayer Perceptron**
A multilayer perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropogation for training the network.

after making model we save this model

# output
**Run Main.py**<br>
<img src="https://github.com/abhay-sinha-0/Phishing__Doamain_Detection/blob/master/__pycache__/assets/Screenshot%202025-04-25%20214304.png">
<br>
go to the url http://127.0.0.1:5000
it will open a window like <br><br>
<img src="https://github.com/abhay-sinha-0/Phishing__Doamain_Detection/blob/master/__pycache__/assets/Screenshot%202025-04-25%20200856.png"><br><br>
enter url then internally it will go to machune learning model and then it test the url that given url is phishing domain or not
<br><br>
<img src="https://github.com/abhay-sinha-0/Phishing__Doamain_Detection/blob/master/__pycache__/assets/Screenshot%202025-04-25%20200923.png">
