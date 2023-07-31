from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import os
from dummyScript import dummyScript
app = Flask(__name__)


app.config["IMAGE_UPLOADS"] = "E:/polydesign/test/API Flask/static/Images/Input"
#app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

from werkzeug.utils import secure_filename


@app.route('/home',methods = ["GET","POST"])
def upload_image():
	if request.method == "POST":
		image = request.files['UserImage']
		interiorStyle = request.form['InteriorStyle']
		roomStyle = request.form['RoomStyle']
		prompt = request.form['Prompt']
		budgetControl = request.form['BudgetControl']

		now = datetime.now()
		dt_string = str(now.strftime("%Y%m%d%H%M%S%f"))

		# print(image)
		# print(interiorStyle + "::" + roomStyle + "::" + prompt + "::" + budgetControl + "::"+ dt_string)

		if image.filename == '':
			print("Image must have a file name")
			return redirect(request.url)

		# print("og file name::"+str(image.filename))

		filename = secure_filename(image.filename)

		# print("secure file name::"+str(filename))

		filename_wo_extension, file_extesnion = os.path.splitext(filename)
		#print("try 1::::::"+filename_wo_extension + "::" + file_extesnion)
		
		filename_with_datetime = "InputForScriptProcessing_Polydesign_" + filename_wo_extension + "_" + dt_string
		filename_with_datetime_extension = filename_with_datetime + file_extesnion
		#print("try 2::::::"+ filename_with_datetime + "::" + filename_with_datetime_extension)

		basedir = os.path.abspath(os.path.dirname(__file__))
		file_path_and_name = str(os.path.join(basedir,app.config["IMAGE_UPLOADS"], filename_with_datetime_extension))
		# print(filename_with_datetime)

		image.save(file_path_and_name)

		# print("inside flask app")
		# print(str(interiorStyle) + "::" + str(roomStyle) + "::" + str(prompt) + "::" + str(budgetControl) + "::" + str(filename_with_datetime_extension))

		output_filename = dummyScript(interiorStyle, roomStyle, prompt, budgetControl, filename_with_datetime_extension)
		# print("returned value::" + str(output_filename))

		return render_template("main.html",filename=output_filename)



	return render_template('main.html')

# to Display just the file 
@app.route('/display/<filename>',methods = ["GET"])
def display_image(filename):
	return redirect(url_for('static',filename = "/Images/Output/" + filename), code=301)


app.run(debug=True,port=2000)