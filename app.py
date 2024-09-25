from flask import Flask, render_template, request, redirect
from models import db, Asset
from config import Config

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    asset_number = request.form['asset_number']
    system_name = request.form['system_name']
    status = request.form['status']
    assigned_to = request.form['assigned_to']
    asset_type = request.form['asset_type']
    location = request.form['location']
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    color = request.form['color']
    serial_number = request.form['serial_number']
    mac = request.form['mac']
    purchase_date = request.form['purchase_date']
    issue_date = request.form['issue_date']
    return_date = request.form['return_date']
    warranty_expire_date = request.form['warranty_expire_date']
    condition = request.form['condition']
    notes = request.form['notes']

    # Create a new Asset object
    new_asset = Asset(
        asset_number=asset_number,
        system_name=system_name,
        status=status,
        assigned_to=assigned_to,
        asset_type=asset_type,
        location=location,
        manufacturer=manufacturer,
        model=model,
        color=color,
        serial_number=serial_number,
        mac=mac,
        purchase_date=purchase_date,
        issue_date=issue_date,
        return_date=return_date,
        warranty_expire_date=warranty_expire_date,
        condition=condition,
        notes=notes
    )

    # Add and commit the new asset to the database
    db.session.add(new_asset)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
