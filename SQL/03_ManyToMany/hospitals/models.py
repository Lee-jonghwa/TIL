from django.db import models

# Create your models here.


# Doctor 모델에서 Patient에 접근하려면
# ManyToManyField가 없으므로 역참조
# patient_set 활용
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
    
# Patient 모델에서 Doctor 모델에 접근하려면
# ManyToManyField가 있으므로 참조
# doctors 속성 활용
class Patient(models.Model):
    # Doctor과 Patient가 M:N의 관계를 갖게 됨
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    

# # ORM 코드
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol')
# patient2 = Patient.objects.create(name='duke')

# # 1번 patient1에 doctor1 추가
# patient1.doctors.add(doctor1)
# # 2번 doctor1에 patient2 추가
# doctor1.patient_set.add(patient2)
# # 3번 doctor1에 patient1 제거
# doctor1.patient_set.remove(patient1)

# # ORM 코드
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol')
# patient2 = Patient.objects.create(name='duke')

# 1. alice가 carol을 headache로 예약
# => reservation class를 통한 예약
# reservation1 = Reservation(doctor=doctor1,patient=patient2,symptom='headache')
# 2. duke가 alice에게 flu로 예약
# => patient 객체 활용
# patient2.doctors.add(doctor1,through_defaults={'symptom':'flu'})
# 3. alice가 예약 취소
# doctor1.patient_set.remove(patient1)