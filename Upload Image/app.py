from flask import Flask,render_template,request,flash
import os

app=Flask(__name__)
app.secret_key="123"

app.config['UPLOAD_FOLDER']="static/images"

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method=='POST':
        upload_image=request.files['upload_image']

        if upload_image.filename!='':
            filepath=os.path.join(app.config["UPLOAD_FOLDER"],upload_image.filename)
            upload_image.save(filepath)
            path=filepath
            return render_template('UploadImages.html',data=path)
            flash("File Upload Successfully","success")
    return render_template("UploadImages.html")

if __name__ == '__main__':
    app.run(debug=True)