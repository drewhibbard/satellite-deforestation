# a few custom evaluation functions because we're dealing with a unique situation of 17 non-exclusive classes
from sklearn.metrics import confusion_matrix, fbeta_score
import numpy as np
import tensorflow as tf

# the official challenge metric
def challenge_score(y_true,pred):
    return fbeta_score(y_true,pred,beta=2,average='samples')

# treat each class of each image as a separate prediction
def item_accuracy(y_true,pred):
    diffs = tf.cast(tf.math.reduce_sum(abs(y_true-pred)),dtype=tf.int32)
    return 1-(diffs/tf.size(y_true))

# only if all 17 classes are correct for an image, then count that as a correct prediction
def full_accuracy(y_true,pred):
    correct = tf.math.reduce_sum(tf.cast(tf.math.reduce_all(tf.equal(y_true,tf.cast(pred>0.5,tf.float32)),axis=1),dtype=tf.int32))
    return correct/tf.shape(y_true)[0]

# create a separate confusion matrix for each tag
def multi_class_confusion(y_test,pred,tags,thresh=0.2):
    for i in range(17):
        print(tags[i])
        print(confusion_matrix(y_test[:,i],(pred>thresh)[:,i]))
        print('\n')
