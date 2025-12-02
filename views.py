from django.urls import path
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from.models import Building_dtls,Company_dtls,VehicleType,VehicleRate,Parkingdetails
from clientapp.models import Booking,client_reg

# Create your views here.

def index(request):
    context={}
    template=loader.get_template("getstarted.html")
    return HttpResponse(template.render(context,request))
def admin_log(request):
    context={}
    template=loader.get_template("adminlogin.html")
    return HttpResponse(template.render(context,request))
def ad_home(request):
    context={}
    template=loader.get_template("adminpage.html")
    return HttpResponse(template.render(context,request))

def addbuilding(request):
    if request.method == "POST":
        b = Building_dtls()
        bname = request.POST.get("bname")
        area = request.POST.get("area")
        total = request.POST.get("total")
        b.BuildingName = bname
        b.BArea = area
        b.TNoof_vehicles = total
        b.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/addbuilding'</script>")
    else:
        context={}
        template=loader.get_template("addbuilding.html")
        return HttpResponse(template.render(context,request))



# def addcmpn(request):
#     if request.method == "POST":
#         c = Company_dtls()
#         bname = request.POST.get("bname")
#         cname = request.POST.get("cname")
#         c.Buildingid = bname
#         c.CompanyName = cname
#         c.save()
#         return HttpResponse("<script>alert('Added Successfully');window.location='/addcmpn'</script>")
#     else:
#         building = Building_dtls.objects.all()
#         context={'key':building}
#         template=loader.get_template("addcompanies.html")
#         return HttpResponse(template.render(context,request))

def addcmpn(request):
    if request.method == "POST":
        c = Company_dtls()
        bname = request.POST.get("bname")  # This is a string (ID)
        cname = request.POST.get("cname")
        try:
            c.Buildingid = Building_dtls.objects.get(id=bname)  # Get instance
        except Building_dtls.DoesNotExist:
            return HttpResponse("<script>alert('Invalid Building ID');window.location='/addcmpn'</script>")

        c.CompanyName = cname
        c.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/addcmpn'</script>")
    else:
        building = Building_dtls.objects.all()
        context = {'key': building}
        template = loader.get_template("addcompanies.html")
        return HttpResponse(template.render(context, request))

def addvtype(request):
    if request.method == "POST":
        v = VehicleType()
        vehicletype = request.POST.get("vehicletype")
        v.VehicleName = vehicletype
        v.save()
        return HttpResponse("<script>alert('VehicleType Added ');window.location='/addvtype'</script>")
    else:

        context={}
        template=loader.get_template("addvehicletype.html")
        return HttpResponse(template.render(context,request))
# def addvrate(request):
#     if request.method == "POST":
#         v = VehicleRate()
#         vehicleid = request.POST.get("vtype")
#         vehiclerate = request.POST.get("vehiclerate")
#         v.Vehicleid = vehicleid
#         v.VehicleRate = vehiclerate
#         v.save()
#         return HttpResponse("<script>alert('Vehicle Rate Added ');window.location='/addvrate'</script>")
#     else:
#         type = VehicleType.objects.all()
#         context = {'key': type}
#         template=loader.get_template("addvehiclerate.html")
#         return HttpResponse(template.render(context,request))


def addvrate(request):
    if request.method == "POST":
        v = VehicleRate()
        vehicleid = request.POST.get("vtype")  # This is a string ID from the form
        vehiclerate = request.POST.get("vehiclerate")

        try:
            v.Vehicleid = VehicleType.objects.get(id=vehicleid)  # Fetch instance
        except VehicleType.DoesNotExist:
            return HttpResponse("<script>alert('Invalid Vehicle Type');window.location='/addvrate'</script>")

        v.VehicleRate = vehiclerate
        v.save()
        return HttpResponse("<script>alert('Vehicle Rate Added');window.location='/addvrate'</script>")
    else:
        type = VehicleType.objects.all()
        context = {'key': type}
        template = loader.get_template("addvehiclerate.html")
        return HttpResponse(template.render(context, request))


# def addpar_dtls(request):
#     context={}
#     template=loader.get_template("add_parkingdtls.html")
#     return HttpResponse(template.render(context,request))
# def get_companies(request):
#     building_id = request.GET.get("building_id")
#     companies = Company_dtls.objects.filter(Buildingid=building_id)
#
#     # Generate raw HTML options
#     options = '<option value="">--Select--</option>'
#     for company in companies:
#         options += f'<option value="{company.id}">{company.CompanyName}</option>'
#
#     return HttpResponse(options)  # Returning HTML instead of JSON
#
#
# def addpar_dtls(request):
#     buildings = Building_dtls.objects.all()
#     return render(request, "add_parkingdtls.html", {"buildings": buildings})

def get_building_details(request):
    building_id = request.GET.get("building_id")

    try:
        # Get the selected building
        building = get_object_or_404(Building_dtls, id=building_id)

        # Fetch companies related to this building
        companies = Company_dtls.objects.filter(Buildingid=building)

        # Generate HTML for the company dropdown
        company_options = '<option value="">--Select--</option>'
        for company in companies:
            company_options += f'<option value="{company.id}">{company.CompanyName}</option>'

        # Return company options + BArea + TNoof_vehicles
        response_data = f"{company_options}|||{building.BArea}|||{building.TNoof_vehicles}"
        return HttpResponse(response_data)

    except Building_dtls.DoesNotExist:
        return HttpResponse("|||", status=404)  # Empty response if no building found
#


def addpar_dtls(request):
    if request.method == "POST":
        b = Parkingdetails()
        bname = request.POST.get("bname")
        cname = request.POST.get("cname")
        location = request.POST.get("location")
        tparking = request.POST.get("tparking")
        noofvehicles = request.POST.get("noofvehicles")
        vtype = request.POST.get("vtype")
        rate = request.POST.get("rate")
        no_of_veh = request.POST.get("no_of_veh")
        image = request.FILES["vehicle_image"]

        # 🔹 Retrieve Building and Company instances
        building = get_object_or_404(Building_dtls, id=bname)
        company = get_object_or_404(Company_dtls, id=cname)
        vehicle_type = get_object_or_404(VehicleType, id=vtype)

        # 🔹 Assign actual model instances instead of raw IDs
        b.Bid = building
        b.Cid = company
        b.Location = location
        b.T_Park_Area = tparking
        b.T_no_vehicle = noofvehicles
        b.Vehi_type_id = vehicle_type
        b.Veh_rate = rate
        b.No_of_veh = no_of_veh
        b.Veh_image = image
        b.save()

        return HttpResponse("<script>alert('Added Successfully');window.location='/addpar_dtls'</script>")
    else:
        buildings = Building_dtls.objects.all()
        return render(request, "add_parkingdtls.html", {"buildings": buildings})



def get_vehicle_types(request):
    """Returns a list of vehicle types as HTML <option> elements"""
    vehicles = VehicleType.objects.all()
    vehicle_options = ''.join(f'<option value="{vehicle.id}">{vehicle.VehicleName}</option>' for vehicle in vehicles)
    return HttpResponse(vehicle_options)


def get_vehicle_rate(request):
    """Returns the rate of the selected vehicle"""
    vehicle_id = request.GET.get("vehicle_id")
    try:
        vehicle_rate = get_object_or_404(VehicleRate, Vehicleid=vehicle_id)
        return HttpResponse(vehicle_rate.VehicleRate)
    except VehicleRate.DoesNotExist:
        return HttpResponse("", status=404)

def view_all_bookings(request):
    # Fetch all bookings
    bookings = Booking.objects.all()

    # Enrich bookings with related details
    enriched_bookings = []
    for booking in bookings:
        building = Building_dtls.objects.filter(id=booking.building_id).first()
        company = Company_dtls.objects.filter(id=booking.company_id).first()
        vehicle = VehicleType.objects.filter(id=booking.vehicle_id).first()

        enriched_bookings.append({
            'ownername': booking.ownername,
            'email': booking.email,
            'booking_date': booking.booking_date,
            'bname': building.BuildingName if building else "N/A",
            'company_name': company.CompanyName if company else "N/A",
            'location': booking.location,
            'vehicle_name': vehicle.VehicleName if vehicle else "N/A",
            'vehicle_rate': booking.vehicle_rate,
            'payment_mode': booking.payment_mode,
            'status': booking.status,
            'no_ofveh': booking.no_of_vehicles,
            'bookingtime':booking.booking_time,
        })

    return render(request, "viewallbookings.html", {'key': enriched_bookings})
def viewuser(request):
    a=client_reg.objects.all()
    context={"key":a}
    template=loader.get_template("viewusers.html")
    return HttpResponse(template.render(context,request))
# def adminpage(request):
#     context={}
#     template=loader.get_template("adminhome.html")
#     return HttpResponse(template.render(context,request))