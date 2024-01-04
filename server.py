from flask import Flask, render_template,url_for,redirect,request, send_file
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_form', methods = ['GET','POST'] )
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'Form Submitted, We will get in touch with you shortly!!'
            return render_template('thankyou.html',message=message)
        except:
            message = "DID NOT SAVE DATA TO DATABASE."
            return render_template('thankyou.html',message=message)
    else:
        message = "FORM NOT SUBMITTED"
        return render_template('thankyou.html',message=message)


@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')
    
@app.route('/download_pdf')
def download_pdf():
    pdf_path = 'static/downloads/VaisakhK_Resume.pdf'
    return send_file(pdf_path, as_attachment=True)

@app.route('/download_docx')
def download_docx():
    pdf_path = 'static/downloads/VaisakhK_Resume.docx'
    return send_file(pdf_path, as_attachment=True)



def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

if __name__ == '__main__':  
   app.run(debug=True) 