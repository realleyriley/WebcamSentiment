# This file converts a .h5 tensorflow model to a .pb format
# OpenVino only works with .pb according to https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html#Convert_From_TF
#
# Original model obtained from https://github.com/jaydeepthik/facial-expression-recognition-webcam
#
# Tensorflow 2.1 yields error while trying to load .h5 model, but tf2.0 works fine
#
# The script will produce a "saved_model.pb" file and two folders.

# After attempting to deploy the model with OpenVino using this command
# python mo_tf.py --saved_model_dir "C:\Users\rptal\Documents\GitHub\WebcamSentiment\Machine Learning\emotion model 2"
# We are presented with an error:
'''
[ ERROR ]  Shape [-1 48 48  1] is not fully defined for output 0 of "conv2d_21_input". Use --input_shape with positive integers to override model input shapes.
[ ERROR ]  Cannot infer shapes or values for node "conv2d_21_input".
[ ERROR ]  Not all output shapes were inferred or fully defined for node "conv2d_21_input".
 For more information please refer to Model Optimizer FAQ, question #40. (https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_Model_Optimizer_FAQ.html?question=40#question-40)
[ ERROR ]
[ ERROR ]  It can happen due to bug in custom shape infer function <function Parameter.infer at 0x000002093E4495E0>.
[ ERROR ]  Or because the node inputs have incorrect values/shapes.
[ ERROR ]  Or because input shapes are incorrect (embedded to the model or passed via --input_shape).
[ ERROR ]  Run Model Optimizer with --log_level=DEBUG for more information.
[ ERROR ]  Exception occurred during running replacer "REPLACEMENT_ID" (<class 'extensions.middle.PartialInfer.PartialInfer'>): Stopped shape/value propagation at "conv2d_21_input" node.
 For more information please refer to Model Optimizer FAQ, question #38. (https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_Model_Optimizer_FAQ.html?question=38#question-38)
 '''

import os
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("model_35_91_61.h5")

print('model loaded')

tf.saved_model.save(model, '.')

print('model saved')
