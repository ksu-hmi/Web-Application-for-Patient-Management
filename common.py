#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrive the patient,doctor and appointment count for the dashboard page"""

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM appointment").fetchone()
        getInsuranceCount = conn.execute("SELECT COUNT(*) AS insurance FROM insurance").fetchone()
        getBillingCount = conn.execute("SELECT COUNT(*) AS billing FROM billing").fetchone()
        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        getPatientCount.update(getInsuranceCount)
        getPatientCount.update(getBillingCount)
        return getPatientCount