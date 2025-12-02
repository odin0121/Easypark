from django.db import models
# Create your models here.
class Building_dtls(models.Model):
    BuildingName = models.CharField(max_length=100)
    BArea = models.CharField(max_length=100)
    TNoof_vehicles = models.CharField(max_length=100)
class Company_dtls(models.Model):
    Buildingid = models.ForeignKey(Building_dtls, on_delete=models.CASCADE)  # Ensure it's ForeignKey!
    CompanyName = models.CharField(max_length=100)
class VehicleType(models.Model):
    VehicleName = models.CharField(max_length=100)
class VehicleRate(models.Model):
    Vehicleid = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    VehicleRate = models.CharField(max_length=100)
class Parkingdetails(models.Model):
    Veh_image = models.FileField(upload_to="file",default="")
    Bid = models.ForeignKey(Building_dtls, on_delete=models.CASCADE)  # 🔹ForeignKey to Building
    Cid = models.ForeignKey(Company_dtls, on_delete=models.CASCADE)  # 🔹 ForeignKey to Company
    Location = models.CharField(max_length=100)
    T_Park_Area = models.CharField(max_length=100)
    T_no_vehicle = models.CharField(max_length=100)
    Vehi_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    Veh_rate = models.CharField(max_length=100)
    No_of_veh = models.CharField(max_length=100)
class bookingpayment(models.Model):
    Veh_Owner_Name=models.CharField(max_length=100)
    Veh_Owner_Emailid=models.CharField(max_length=100)
    Booking_id= models.CharField(max_length=100,default='')
    Parking_id=models.CharField(max_length=100)
    Paymnt_date=models.DateField()
    Paymntamount=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)




