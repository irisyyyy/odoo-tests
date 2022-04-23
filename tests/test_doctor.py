from odoo.tests import common

class TestDoctor(common.TransactionCase):
    def setUp(self):
        super(TestDoctor, self).setUp()
        self.doctor = self.env['hospital.doctor']

        self.doctor1 = self.doctor.create({
            'doctor_name': 'Chris',
            'age': '50',
            'gender': 'male',
            
        })

        self.doctor2 = self.doctor.create({
            'doctor_name': 'Doctor',
            'age': '50',
            'gender': 'male',
        })



    def test_doctor_name(self):
        self.assertEqual(self.doctor1.doctor_name, 'Chris')
        self.assertEqual(self.doctor2.doctor_name, 'Doctor')

    def test_doctor_age(self):
        self.assertEqual(self.doctor1.age, 50)


    #add tests for functions 