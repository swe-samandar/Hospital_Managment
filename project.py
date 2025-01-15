from os import *
system('clear')

"""
Proyekt mavzusi:   *** Shifoxona Menejment Tizimi ***

Funksiyalari:
    Shifokorlar va bemorlarni ro'yxatga olish.
    Xonalarni boshqarish va bandlik holatini kuzatish.
    Bemorlar uchun uchrashuvlarni rejalashtirish.
    Bemorlar holati va davolanish tarixini ko'rish.
    Shifokorlar, bemorlar va uchrashuvlar ro'yxatini ko'rsatish.

Klasslari:
    Doctor: Shifokorlar haqida ma'lumotni saqlash.
    Patient: Bemorlar haqida ma'lumotni saqlash.
    Appointment: Uchrashuvlar haqida ma'lumotni boshqarish.
    HospitalManager: Shifoxona tizimini boshqaruvchi funksiyalarni o'z ichiga olgan klass.

Project shartlari:
    1.Clean code
    2.magic methodlardan foydalanish kerak
    3.decorator
    4.class atribute
"""

class Doctor:
    def __init__(self, doctor_ismi, doctor_status):
        self.__doctor_ismi = doctor_ismi
        self.__doctor_status = doctor_status

    def __str__(self):
        return f"Shifokorning ismi sharifi {self.__doctor_ismi}, doctor hozirda {self.__doctor_status}"
    
    @property
    def doctor_ismi(self):
        return self.__doctor_ismi
    

class Patient:
    def __init__(self, name, kasalligi, davomiyligi, doctor, narx):
        self.__name = name
        self.__kasalligi = kasalligi
        self.__davomiyligi = davomiyligi
        self.__doctor = doctor
        self.__narx = narx

    def __str__(self):
        return f"Bemorning ismi sharifi {self.__name}, bemorning kasalligi {self.__kasalligi}, davolanish davomiyligi {self.__davomiyligi} bemorni qabul qiluvchi \
doktornig ismi {self.__doctor}, davolaninshning qiymati (necha kun bo'lishidan qat'iy nazar bir xil narx belgilangan) {self.__narx} so'm"
    
    @property
    def name(self):
        return(self)
    
    @property
    def doktor(self):
        return self.__doctor


class Appointment:
    def __init__(self, date, time, doctor_ismi, bemor_ismi):
        self.date = date
        self.time = time
        self.doctor_ismi = doctor_ismi
        self.bemor_ismi = bemor_ismi

    def __str__(self):
        return f"Uchrashuvning vaqti {self.date}, uchrashuvning vaqti {self.time}, {self.doctor_ismi} qabul qiladi, bemorning ismi {self.bemor_ismi}"
    

class Hospital:
    doctors = []
    patients = []
    appointments = []

    @staticmethod
    def doctor_qush(doctor):
        Hospital.doctors.append(doctor)

    @staticmethod
    def patient_qush(patient):
        Hospital.patients.append(patient)

    @staticmethod
    def appointment_qush(appointment):
        Hospital.appointments.append(appointment)

    @staticmethod
    def doctorlar():
        print('\nDoktorlar <<<>>>')
        for doctor in Hospital.doctors:
            print(doctor)

    @staticmethod
    def bemorlar():
        print('\nBemorlar <<<>>>')
        for patient in Hospital.patients:
            print(patient)

    @staticmethod
    def uchrashuvlar():
        print('\nUchrashuvlar <<<>>>')
        for uchrashuv in Hospital.appointments:
            print(uchrashuv)


doctor_1 = Doctor("Abdurauf Islomov", "Ishda")
doctor_2 = Doctor("Ra'no Abdurashidova", "Bemor bilan suhbat olib bormoqda")
doctor_3 = Doctor("Tursunbek Arslonxonov", "Ishda")
# doctor_4 = Doctor("Qodirbek Tursunov", "Ta'tilda")
# doctor_5 = Doctor("Alibek Turdiyev", "Ishda")

patient_1 = Patient("Abduqodir", "Qon bosimi", 12, "Tursunbek Arslonxonov", 1_200_000)
patient_2 = Patient("Farida", "Bosh og'rig'i", 2, "Abdurauf Islomov", 100_000)
# patient_3 = Patient("Ruslan", "Tomoq og'rig'i", 3, "Alibek Turdiyev", 100_000)

appointment_1 = Appointment("2025-yil 18-yanvar", "12:30","Abdurauf Islomov", "Farida")
appointment_2 = Appointment("2025-yil 19-yanvar", "13:00", "Tursunbek Arslonxonov", "Abduqodir")

Hospital.doctor_qush(doctor_1)
Hospital.doctor_qush(doctor_2)
Hospital.doctor_qush(doctor_3)
Hospital.doctor_qush(doctor_4)

Hospital.appointment_qush(appointment_1)
Hospital.appointment_qush(appointment_2)
# Hospital.appointment_qush(appointment_3)

Hospital.patient_qush(patient_1)
Hospital.patient_qush(patient_2)
# Hospital.patient_qush(patient_3)

Hospital.doctorlar()
Hospital.bemorlar()
Hospital.uchrashuvlar()

