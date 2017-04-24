import numpy as np
import tensorflow as tf

def ReadImage(filename):
    """ 
    IN filenames: string - read file names
    OUT (***int, int[3]) - image, size of image
    """
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    decode_img = tf.image.decode_png(value, channels=3)

    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_op)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        image = decode_img.eval()
        coord.request_stop()
        coord.join(threads)

        shape = [len(image), len(image[0]), len(image[0][0])]
        return (image, shape)


