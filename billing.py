#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn




class Billings(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        patients = conn.execute("SELECT * FROM billing  ORDER BY bill_id").fetchall()
        return patients



class Billing(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient = conn.execute("SELECT * FROM billing WHERE bill_id=?",(id,)).fetchall()
        return patient

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM billing WHERE bill_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}