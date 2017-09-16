import time
from os import path
from RNN import *
from init import *


#**************************************************************************
# np.random.seed(10)
# model = RNN(vocabulary_size)
# o, s = model.forward_propagation(X_train[10])
# print o.shape
# print o

# predictions = model.predict(X_train[10])
# print predictions.shape
# print predictions

# print "actual loss for 1000 samples", model.calculate_loss(X_train[:1], y_train[:1])

X_train = pickle.load(open("X_train.p", 'rb'))
y_train = pickle.load(open("y_train.p", 'rb'))
print "Data loaded"
# np.random.seed(10)
# model = RNN(vocabulary_size)
start_time = time.time()
# model.sgd_step(X_train[10], y_train[10], 0.005)


np.random.seed(10)
# Train on a small subset of the data to see what happens
if path.exists("output.p"):
    model = load("output.p")
else:
    model = RNN(vocabulary_size)

print "Model loaded"
print "Starting training .."

losses = train_with_sgd(model, X_train, y_train, nepoch=5, evaluate_loss_after=5)

print time.time()-start_time

print "Training Complete !!"

save(model, "output.p")

print "Model saved"


