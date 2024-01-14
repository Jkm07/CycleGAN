import tensorflow as tf

IMAGE_SIZE = [256, 256]
model = tf.keras.models.load_model('cycleGAN')

def convert_to_monet(image):
    image = tf.image.decode_image(image)
    image = (tf.cast(image, tf.float32) / 127.5) - 1
    image = tf.expand_dims(image, 0)
    image = tf.image.resize(image, IMAGE_SIZE)
    prediction = model(image, training=False)[0]
    prediction = tf.cast(prediction * 127.5 + 127.5, tf.uint8)
    return tf.image.encode_jpeg(prediction).numpy()

def unconvert_to_monet(image):
    image = tf.image.decode_image(image)
    image = (tf.cast(image, tf.float32) / 127.5) - 1
    image = tf.expand_dims(image, 0)
    image = tf.image.resize(image, IMAGE_SIZE)
    prediction = model(image, training=False)[1]
    prediction = tf.cast(prediction * 127.5 + 127.5, tf.uint8)
    return tf.image.encode_jpeg(prediction).numpy()