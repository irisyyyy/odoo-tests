from odoo.tests import common

class TestPatient(common.TransactionCase):
    def setUp(self):
        super(TestPatient, self).setUp()
        self.patient = self.env['hospital.patient']

        self.patient1 = self.patient.create({
            'name': 'Jess',
            'gender': 'female',
            'age': 25
        })
        self.patient2 = self.patient.create({
            'name': 'Abby',
            'gender': 'female',
            'age': 30
        })

        
    def test_patient_age(self):
        self.assertEqual(self.patient1.age, 25)

    def test_patient_appointment(self):
        self.assertEqual(self.patient1.appointment_count, 0)
        self.patient1.write({
            'appointment_count': 1,
        })
        self.assertEqual(self.patient1.appointment_count, 1)
        self.assertEqual(self.patient2.appointment_count, 0)


    #add tests for functions