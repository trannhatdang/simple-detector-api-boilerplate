import os
import shutil

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization  # to create AdamW optimizer

import matplotlib.pyplot as plt

def analyzeText(inputs):
    if(not os.path.isdir("./api/model")):
        return "error, model doesn't exist"


    reloaded_model = tf.saved_model.load("./api/model")

    #def print_my_examples(inputs, results):
    #    result_for_printing = \
    #        [f'input: {inputs[i]:<30} : score: {results[i][0]:.6f}'
    #                            for i in range(len(inputs))]
    #    print(*result_for_printing, sep='\n')
    #    print()

    examples = [
        "Around 40% of the cotton we are using is organic, and we are targeting a 2030 goal of converting all our cotton to organic cotton.",
        "We are currently leading the fashing industry with 80% of our products being sustainable.",
        "I am feeling sick",
        "I love you",
        "I go to school",
        "I go to work",
    ]

    results = tf.sigmoid(reloaded_model(tf.constant([inputs])))

    return results.numpy()[0][0]
