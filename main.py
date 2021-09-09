import os
import time
from controller import convert_video
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, after_this_request

UPLOAD_FOLDER = "./uploads"
OUTPUT_FOLDER = "./outputs"

app = Flask(__name__)
app.secret_key = "$3cR3t_K3y"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

if not os.path.exists(app.config["UPLOAD_FOLDER"]) :
    os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route('/')
def home() :
    return render_template("home.html")

@app.route('/convert', methods=["GET", "POST"])
def convert() :
    if request.method == "POST" :
        # Save the video file from user input
        input_video = request.files["input-video"]
        if input_video.filename == '' :
            flash("Please upload a video file to be converted!")
            return redirect(url_for('home'))
        input_video_path = os.path.join(app.config["UPLOAD_FOLDER"], os.path.splitext(input_video.filename)[0] + '_' + str(int(time.time())) + os.path.splitext(input_video.filename)[1])
        input_video.save(input_video_path)

        # Get the desired output from "output-format" dropdown options
        output_format = request.form.get("output-format")

        # Convert video using the function in controller module
        output_video_path = convert_video(input_video_path, output_format)

        # Remove all old uploaded videos
        os.unlink(input_video_path)

        @after_this_request
        def remove_file(response) :
            try :
                os.unlink(output_video_path)
            except Exception as error :
                app.logger.error("Error removing or closing downloaded file handle", error)
            return response
        return send_file(output_video_path, as_attachment=True)