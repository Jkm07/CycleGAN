from flask import Flask, render_template, Blueprint, request, make_response
import gan_handler

root = Blueprint('root', __name__)

@root.route("/")
def main():
    return render_template("main.html")

@root.route("/convert", methods=['POST'])
def convert_to_monet():
    image = request.files['image'].stream.read()
    image_conv = gan_handler.convert_to_monet(image)
    response = make_response(image_conv)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='gen.jpg')
    return response

@root.route("/unconvert", methods=['POST'])
def unconvert_to_monet():
    image = request.files['image'].stream.read()
    image_conv = gan_handler.unconvert_to_monet(image)
    response = make_response(image_conv)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='gen.jpg')
    return response


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(root, url_prefix='/')
    app.run(host="0.0.0.0", port=8080)