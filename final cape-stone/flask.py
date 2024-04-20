{"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":74938,"status":"ok","timestamp":1713561615493,"user":{"displayName":"Project 606","userId":"17607937635991066044"},"user_tz":240},"id":"pV8zT_F-k_d_","outputId":"51e6c67d-3b6d-4ea6-cb55-00abf54ef4c7"},"outputs":[{"name":"stdout","output_type":"stream","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"]}],"source":["from google.colab import drive\n","drive.mount('/content/drive')"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"TCjblUwGk_Tz"},"outputs":[],"source":["model_path = '/content/drive/MyDrive/final cape-stone/my_model/saved_model.pb'"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"l_C4ax8gk_Bw"},"outputs":[],"source":["# Importing required libs\n","import numpy as np\n","import pickle\n","from flask import Flask, flash, request, redirect, url_for, render_template\n","import urllib.request\n","import os\n","from werkzeug.utils import secure_filename\n","from keras.utils import img_to_array\n","from PIL import Image\n"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":9980,"status":"ok","timestamp":1713561632644,"user":{"displayName":"Project 606","userId":"17607937635991066044"},"user_tz":240},"id":"srhgSCu8ZbEJ","outputId":"b30b7b61-ed4e-4063-ddab-c97a3193fe06"},"outputs":[{"name":"stdout","output_type":"stream","text":["Model: \"sequential_19\"\n","_________________________________________________________________\n"," Layer (type)                Output Shape              Param #   \n","=================================================================\n"," conv2d_91 (Conv2D)          (None, 256, 256, 32)      320       \n","                                                                 \n"," max_pooling2d_41 (MaxPooli  (None, 128, 128, 32)      0         \n"," ng2D)                                                           \n","                                                                 \n"," conv2d_92 (Conv2D)          (None, 128, 128, 64)      18496     \n","                                                                 \n"," max_pooling2d_42 (MaxPooli  (None, 64, 64, 64)        0         \n"," ng2D)                                                           \n","                                                                 \n"," conv2d_93 (Conv2D)          (None, 64, 64, 128)       73856     \n","                                                                 \n"," max_pooling2d_43 (MaxPooli  (None, 32, 32, 128)       0         \n"," ng2D)                                                           \n","                                                                 \n"," conv2d_94 (Conv2D)          (None, 32, 32, 256)       295168    \n","                                                                 \n"," max_pooling2d_44 (MaxPooli  (None, 16, 16, 256)       0         \n"," ng2D)                                                           \n","                                                                 \n"," flatten_19 (Flatten)        (None, 65536)             0         \n","                                                                 \n"," dense_55 (Dense)            (None, 512)               33554944  \n","                                                                 \n"," dropout_1 (Dropout)         (None, 512)               0         \n","                                                                 \n"," dense_56 (Dense)            (None, 4)                 2052      \n","                                                                 \n","=================================================================\n","Total params: 33944836 (129.49 MB)\n","Trainable params: 33944836 (129.49 MB)\n","Non-trainable params: 0 (0.00 Byte)\n","_________________________________________________________________\n","None\n"]}],"source":["\n","from tensorflow.keras.models import load_model\n","\n","\n","# Save the model\n","saved_model_path = '/content/drive/MyDrive/final cape-stone/my_model'\n","\n","#Loading model\n","model = load_model(saved_model_path)\n","print(model.summary())\n"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":107,"status":"ok","timestamp":1713561645455,"user":{"displayName":"Project 606","userId":"17607937635991066044"},"user_tz":240},"id":"P6zNzL6nFSE0","outputId":"df6af4db-db6b-400e-d45b-8573ffae7df0"},"outputs":[{"data":{"text/plain":["(None, 256, 256, 1)"]},"execution_count":5,"metadata":{},"output_type":"execute_result"}],"source":["model.input_shape"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"NjL4mftj7IW1"},"outputs":[],"source":["\n","# Preparing and pre-processing the image\n","# Modify the preprocess_img function to resize the image to the correct size\n","def preprocess_img(img_path):\n","    op_img = Image.open(img_path)\n","    if op_img is None:\n","        print(f\"Failed to load image: {img_path}\")\n","        return\n","    img_resize = op_img.resize((256, 256))    # Resize original image\n","    img2arr = img_to_array(img_resize) / 255.0    # Normalize image\n","    img_reshape = img2arr.reshape(-1, 256 , 256, 1)    # Resise image for model input\n","    return img_reshape\n","\n","# Predicting function\n","def predict_result(predict):\n","    pred = model.predict(predict)\n","    print(\"Prediction\", pred)\n","    return np.argmax(pred[0], axis=-1)\n"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":35},"executionInfo":{"elapsed":527,"status":"ok","timestamp":1713570995483,"user":{"displayName":"Project 606","userId":"17607937635991066044"},"user_tz":240},"id":"wlWW21iMfiko","outputId":"279e7a96-266e-4f3d-ac39-bd9cec88425d"},"outputs":[{"name":"stdout","output_type":"stream","text":["https://9zmi0t7hhsc-496ff2e9c6d22116-5000-colab.googleusercontent.com/\n"]}],"source":["from google.colab.output import eval_js\n","print(eval_js(\"google.colab.kernel.proxyPort(5000)\"))"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"sWFFEn1vZ96H","outputId":"49d12802-c385-461f-9e15-f9bb0d685d66"},"outputs":[{"metadata":{"tags":null},"name":"stdout","output_type":"stream","text":[" * Serving Flask app '__main__'\n"," * Debug mode: off\n"]},{"metadata":{"tags":null},"name":"stderr","output_type":"stream","text":["INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n"," * Running on http://127.0.0.1:5000\n","INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:14] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:15] \"\u001b[33mGET /static/css/custom.css HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:15] \"\u001b[33mGET /static/js/image_upload.js HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:15] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:15] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"]},{"metadata":{"tags":null},"name":"stdout","output_type":"stream","text":["Hello Request Received.....\n","Image <PIL.JpegImagePlugin.JpegImageFile image mode=L size=768x496 at 0x7C8ED48E3DF0>\n","Image Array [[[0.07058824]\n","  [0.05098039]\n","  [0.10196079]\n","  ...\n","  [0.05490196]\n","  [0.00392157]\n","  [0.00784314]]\n","\n"," [[0.11764706]\n","  [0.05490196]\n","  [0.11372549]\n","  ...\n","  [0.01176471]\n","  [0.01960784]\n","  [0.01568628]]\n","\n"," [[0.05098039]\n","  [0.07058824]\n","  [0.07450981]\n","  ...\n","  [0.01960784]\n","  [0.08627451]\n","  [0.03921569]]\n","\n"," ...\n","\n"," [[0.01960784]\n","  [0.01176471]\n","  [0.00784314]\n","  ...\n","  [0.00392157]\n","  [0.01960784]\n","  [0.02745098]]\n","\n"," [[0.00784314]\n","  [0.01568628]\n","  [0.01568628]\n","  ...\n","  [0.01960784]\n","  [0.01960784]\n","  [0.02352941]]\n","\n"," [[0.00392157]\n","  [0.01960784]\n","  [0.03137255]\n","  ...\n","  [0.03921569]\n","  [0.01568628]\n","  [0.03529412]]]\n","Image Reshape [[[[0.07058824]\n","   [0.05098039]\n","   [0.10196079]\n","   ...\n","   [0.05490196]\n","   [0.00392157]\n","   [0.00784314]]\n","\n","  [[0.11764706]\n","   [0.05490196]\n","   [0.11372549]\n","   ...\n","   [0.01176471]\n","   [0.01960784]\n","   [0.01568628]]\n","\n","  [[0.05098039]\n","   [0.07058824]\n","   [0.07450981]\n","   ...\n","   [0.01960784]\n","   [0.08627451]\n","   [0.03921569]]\n","\n","  ...\n","\n","  [[0.01960784]\n","   [0.01176471]\n","   [0.00784314]\n","   ...\n","   [0.00392157]\n","   [0.01960784]\n","   [0.02745098]]\n","\n","  [[0.00784314]\n","   [0.01568628]\n","   [0.01568628]\n","   ...\n","   [0.01960784]\n","   [0.01960784]\n","   [0.02352941]]\n","\n","  [[0.00392157]\n","   [0.01960784]\n","   [0.03137255]\n","   ...\n","   [0.03921569]\n","   [0.01568628]\n","   [0.03529412]]]]\n","1/1 [==============================] - 0s 75ms/step\n"]},{"metadata":{"tags":null},"name":"stderr","output_type":"stream","text":["INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:31] \"POST /prediction HTTP/1.1\" 200 -\n"]},{"metadata":{"tags":null},"name":"stdout","output_type":"stream","text":["Prediction [[0.00388972 0.19767636 0.00200635 0.7964276 ]]\n"]},{"metadata":{"tags":null},"name":"stderr","output_type":"stream","text":["INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:31] \"\u001b[33mGET /static/css/custom.css HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:31] \"\u001b[33mGET /static/js/image_upload.js HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:31] \"\u001b[31m\u001b[1mGET /prediction HTTP/1.1\u001b[0m\" 405 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:31] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:34] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:34] \"\u001b[33mGET /static/js/image_upload.js HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:34] \"\u001b[33mGET /static/css/custom.css HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:34] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:34] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"]},{"metadata":{"tags":null},"name":"stdout","output_type":"stream","text":["Hello Request Received.....\n","Image <PIL.JpegImagePlugin.JpegImageFile image mode=L size=768x496 at 0x7C8ED50F2FE0>\n","Image Array [[[0.07058824]\n","  [0.05098039]\n","  [0.10196079]\n","  ...\n","  [0.05490196]\n","  [0.00392157]\n","  [0.00784314]]\n","\n"," [[0.11764706]\n","  [0.05490196]\n","  [0.11372549]\n","  ...\n","  [0.01176471]\n","  [0.01960784]\n","  [0.01568628]]\n","\n"," [[0.05098039]\n","  [0.07058824]\n","  [0.07450981]\n","  ...\n","  [0.01960784]\n","  [0.08627451]\n","  [0.03921569]]\n","\n"," ...\n","\n"," [[0.01960784]\n","  [0.01176471]\n","  [0.00784314]\n","  ...\n","  [0.00392157]\n","  [0.01960784]\n","  [0.02745098]]\n","\n"," [[0.00784314]\n","  [0.01568628]\n","  [0.01568628]\n","  ...\n","  [0.01960784]\n","  [0.01960784]\n","  [0.02352941]]\n","\n"," [[0.00392157]\n","  [0.01960784]\n","  [0.03137255]\n","  ...\n","  [0.03921569]\n","  [0.01568628]\n","  [0.03529412]]]\n","Image Reshape [[[[0.07058824]\n","   [0.05098039]\n","   [0.10196079]\n","   ...\n","   [0.05490196]\n","   [0.00392157]\n","   [0.00784314]]\n","\n","  [[0.11764706]\n","   [0.05490196]\n","   [0.11372549]\n","   ...\n","   [0.01176471]\n","   [0.01960784]\n","   [0.01568628]]\n","\n","  [[0.05098039]\n","   [0.07058824]\n","   [0.07450981]\n","   ...\n","   [0.01960784]\n","   [0.08627451]\n","   [0.03921569]]\n","\n","  ...\n","\n","  [[0.01960784]\n","   [0.01176471]\n","   [0.00784314]\n","   ...\n","   [0.00392157]\n","   [0.01960784]\n","   [0.02745098]]\n","\n","  [[0.00784314]\n","   [0.01568628]\n","   [0.01568628]\n","   ...\n","   [0.01960784]\n","   [0.01960784]\n","   [0.02352941]]\n","\n","  [[0.00392157]\n","   [0.01960784]\n","   [0.03137255]\n","   ...\n","   [0.03921569]\n","   [0.01568628]\n","   [0.03529412]]]]\n","1/1 [==============================] - 0s 67ms/step\n"]},{"metadata":{"tags":null},"name":"stderr","output_type":"stream","text":["INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:53] \"POST /prediction HTTP/1.1\" 200 -\n"]},{"metadata":{"tags":null},"name":"stdout","output_type":"stream","text":["Prediction [[0.00388972 0.19767636 0.00200635 0.7964276 ]]\n"]},{"metadata":{"tags":null},"name":"stderr","output_type":"stream","text":["INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:53] \"\u001b[33mGET /static/css/custom.css HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:53] \"\u001b[33mGET /static/js/image_upload.js HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:53] \"\u001b[31m\u001b[1mGET /prediction HTTP/1.1\u001b[0m\" 405 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:54] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:59] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:59] \"\u001b[33mGET /static/css/custom.css HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:59] \"\u001b[33mGET /static/js/image_upload.js HTTP/1.1\u001b[0m\" 404 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:04:59] \"GET / HTTP/1.1\" 200 -\n","INFO:werkzeug:127.0.0.1 - - [20/Apr/2024 04:05:00] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"]}],"source":["from flask import Flask, render_template\n","app = Flask(__name__, template_folder='drive/MyDrive/final cape-stone/template')\n","UPLOAD_FOLDER = 'drive/MyDrive/final cape-stone/template'\n","\n","app.secret_key = \"secret key\"\n","app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER\n","app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024\n","\n","ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])\n","\n","def allowed_file(filename):\n","    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS\n","\n","\n","\n","\n","# Home route\n","@app.route(\"/\")\n","def main():\n","    return render_template(\"index1.html\")\n","\n","# Prediction route\n","@app.route('/prediction', methods=['POST'])\n","def predict_image_file():\n","    try:\n","\n","\n","\n","        # your prediction\n","        if request.method == 'POST':\n","            #filename = secure_filename(file.filename)\n","            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))\n","            #print('upload_image filename: ' + filename)\n","            print(\"Hello Request Received.....\")\n","            file = request.files['file']\n","            # filename = secure_filename(file.filename)\n","            # print('upload_image filename: ' + filename)\n","            img = preprocess_img(request.files['file'].stream)\n","            pred = predict_result(img)\n","\n","            # print(\"Result Pred\", type(int(pred)))\n","\n","            return render_template(\"index1.html\", predictions=str(pred))\n","\n","    except:\n","        error = \"File cannot be processed, Sorry Try again.\"\n","        return render_template(\"index1.html\", err=error)\n","\n","\n","# Driver code\n","if __name__ == \"__main__\":\n","    app.run()\n"]},{"cell_type":"markdown","metadata":{"id":"nGgnl-6p5poq"},"source":["op_img = Image.open(img_path)\n","    print(\"Image\", op_img)\n","    img_resize = op_img.resize((256, 256))\n","    print(\"Image Resize\", img_resize)\n","    img2arr = img_to_array(img_resize) / 255.0\n","    print(\"Image Array\", img2arr)\n","    img_reshape = img2arr.reshape(1, 224, 224, 3)\n","    #print(\"Image Reshape\", img_reshape)\n","    return img_reshape"]}],"metadata":{"colab":{"provenance":[],"mount_file_id":"1ELYuMg8RKLwHBnVwMFpQLkj3eNz-qUkE","authorship_tag":"ABX9TyMLYGVmANnyT6Nq9PdyoCJ9"},"kernelspec":{"display_name":"Python 3","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":0}