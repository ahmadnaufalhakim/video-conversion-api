import os
from controller import convert_video
from flask import Flask, render_template, request, flash, redirect, url_for, send_file

UPLOAD_FOLDER = "./uploads"
app = Flask(__name__)
app.secret_key = "$3cR3t_K3y"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
        
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
        input_video_path = os.path.join(app.config["UPLOAD_FOLDER"], input_video.filename)
        input_video.save(input_video_path)

        output_format = request.form.get("output-format")
        output_video = convert_video(input_video_path, output_format)
        return send_file(output_video)
    else :
        return render_template("home.html")

if __name__ == "__main__" :
    app.run()