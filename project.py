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

# class Doctor:
#     pass


# class Patient:
#     pass


# class Appointment:
#     pass


# class HospitalManager:
#     pass


class Doctor:
    def __init__(self, doctor_name, doctor_status):
        self.__doctor_name = doctor_name
        self.__doctor_status = doctor_status
    
    def __str__(self):
        return f"Shifokorning ism sharifi: {self.__doctor_name}, hozirda doktor {self.__doctor_status} da"


class Patient:
    def __init__(self, ismi, kasalligi, davolanish, doktor_nazorati, narx):
        self.__ismi = ismi
        self.__kasalligi = kasalligi
        self.__davolanish = davolanish
        self.doktor_nazorati = doktor_nazorati
        self.narx = narx
    
    def __str__(self):
        return f"Bemorning ismi: {self.__ismi}, bemorning bezovta qilayotgan kasalligi {self.__kasalligi} va ushbu bemorninig /
          davolanish davomiyligi {self.__davolanish}. Ushbu bemorni {self.doktor_nazorati} / davolayapdi"

    # def 


class Appointment:
    pass


class HospitalManager:
    pass


doctor = Doctor("ruslan master")
