from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.templatetags.static import static
from django.utils.datastructures import MultiValueDictKeyError
from joblib import load
from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.
model=load('./savedModels/fraud(1).joblib')
def index(request):
    
    return render(request,'core/index.html')
def profile(request):
   if request.method == 'POST':
        insurance_type = request.POST.get('insuranceType')
        if insurance_type:
            if insurance_type == 'auto':
                return redirect("core:predict")
            elif insurance_type == 'home':
                return redirect('home_claim_form')
            elif insurance_type == 'health':
                return redirect('health_claim_form')
            else:
                return JsonResponse({'success': False, 'error': 'Invalid insurance type'}, status=400)
        else:
            return JsonResponse({'success': False, 'error': 'No insurance type selected'}, status=400)

   return render(request,'core/profile.html')

def predict(request):
    
    

    return render(request,'core/predict.html')
def formInfo(request):
    months_as_customer=request.GET['months_as_customer']
    policy_deductable=request.GET['policy_deductable']
    umbrella_limit=request.GET['umbrella_limit']
    capital_gains=request.GET['capital_gains']
    capital_loss=request.GET['capital_loss']
    incident_hour_of_the_day=request.GET['incident_hour_of_the_day']
    number_of_vehicles_involved=request.GET['number_of_vehicles_involved']
    bodily_injuries=request.GET['bodily_injuries']
    witnesses=request.GET['witnesses']
    injury_claim=request.GET['injury_claim']
    property_claim=request.GET['property_claim']
    vehicle_claim=request.GET['vehicle_claim']
    policy_csl_250_500=request.GET['policy_csl_250_500']
    policy_csl_500_1000=request.GET['policy_csl_500_1000']
    insured_sex_male=request.GET['insured_sex_male']
    insured_education_level_college=request.GET['insured_education_level_college']
    insured_education_level_high_school=request.GET['insured_education_level_high_school']
    insured_education_level_jd=request.GET['insured_education_level_jd']
    insured_education_level_md=request.GET['insured_education_level_md']
    insured_education_level_masters=request.GET['insured_education_level_masters']
    insured_education_level_phd=request.GET['insured_education_level_phd']
    insured_occupation_armed_forces=request.GET['insured_occupation_armed_forces']
    insured_occupation_craft_repair=request.GET['insured_occupation_craft_repair']
    insured_occupation_exec_managerial=request.GET['insured_occupation_exec-managerial']
    insured_occupation_farming_fishing=request.GET['insured_occupation_farming-fishing']
    insured_occupation_handlers_cleaners=request.GET['insured_occupation_handlers-cleaners']
    insured_occupation_machineopinspct=request.GET['insured_occupation_machine-op-inspct']
    insured_occupation_other_service=request.GET['insured_occupation_other-service']
    insured_occupation_privhouseserv=request.GET['insured_occupation_priv-house-serv']
    insured_occupation_profspecialty=request.GET['insured_occupation_prof-specialty']
    insured_occupation_protectiveserv=request.GET['insured_occupation_protective-serv']
    insured_occupation_sales=request.GET['insured_occupation_sales']
    insured_occupation_techsupport=request.GET['insured_occupation_tech_support']
    insured_occupation_transport_moving=request.GET['insured_occupation_transport-moving']
    insured_relationship_not_in_family=request.GET['insured_relationship_not_in_family']
    insured_relationship__otherrelative=request.GET['insured_relationship_other-relative']
    insured_relationship_own_child=request.GET['insured_relationship_own-child']
    try:
        insured_relationship_unmarried = request.GET['insured_relationship_unmarried']
        # Proceed with processing the 'insured_relationship_unmarried' data
        print("insured_relationship_unmarried:", insured_relationship_unmarried)
    except MultiValueDictKeyError:
        # Handle the case when 'insured_relationship_unmarried' is not present in the request
        print("Insured relationship unmarried data is missing in the request.")
        return HttpResponse("Insured relationship unmarried data is missing in the request.", status=400)

    insured_relationship_wife=request.GET['insured_relationship_wife']
    incident_type_parked_car=request.GET['incident_type_parked_car']
    incident_type_parked_Single_Vehicle_Collision=request.GET['incident_type_parked_Single Vehicle Collision']
    incident_type_Vehicle_Theft=request.GET['incident_type_Vehicle Theft']
    collision_type_rear_collision=request.GET['collision_type_rear_collision']
    collision_type_Side_Collision=request.GET['collision_type_Side Collision']
    incident_severity_minor_damage=request.GET['incident_severity_minor_damage']
    incident_severity_TotalLoss=request.GET['incident_severity_Total Loss']
    incident_severity_TrivialDamage=request.GET['incident_severity_Trivial Damage']
    authorities_contacted_fire=request.GET['authorities_contacted_fire']
    authorities_contacted_None=request.GET['authorities_contacted_None']
    authorities_contacted_Other=request.GET['authorities_contacted_Other']
    authorities_contacted_Police=request.GET['authorities_contacted_Police']
    property_damage_yes=request.GET['property_damage_yes']
    police_report_available_yes=request.GET['police_report_available_yes']
    auto_make_audi=request.GET['auto_make_audi']
    auto_make_bmw=request.GET['auto_make_bmw']
    auto_make_chevrolet=request.GET['auto_make_chevrolet']
    auto_make_dodge=request.GET['auto_make_dodge']
    auto_make_ford=request.GET['auto_make_ford']
    auto_make_Honda=request.GET['auto_make_honda']
    auto_make_jeep=request.GET['auto_make_jeep']
    auto_make_mercedes=request.GET['auto_make_mercedes']
    auto_make_nissan=request.GET['auto_make_nissan']
    auto_make_saab=request.GET['auto_make_saab']
    auto_make_suburu=request.GET['auto_make_suburu']
    auto_make_toyota=request.GET['auto_make_toyota']
    auto_make_volkswagen=request.GET['auto_make_volkswagen']
    
    

    

    y_pred=model.predict([[months_as_customer,policy_deductable,umbrella_limit,capital_gains,capital_loss,incident_hour_of_the_day,number_of_vehicles_involved,bodily_injuries,witnesses,
                  injury_claim,property_claim,vehicle_claim,policy_csl_250_500,policy_csl_500_1000,insured_sex_male,insured_education_level_college, insured_education_level_high_school,
                  insured_education_level_jd,insured_education_level_md,insured_education_level_masters,insured_education_level_phd,insured_occupation_armed_forces,insured_occupation_craft_repair,insured_occupation_exec_managerial,insured_occupation_farming_fishing,insured_occupation_handlers_cleaners,insured_occupation_machineopinspct,insured_occupation_other_service,
                  insured_occupation_privhouseserv,insured_occupation_profspecialty,insured_occupation_protectiveserv,insured_occupation_sales,insured_occupation_techsupport,insured_occupation_transport_moving,insured_relationship_not_in_family,insured_relationship__otherrelative,insured_relationship_own_child,insured_relationship_unmarried,insured_relationship_wife,incident_type_parked_car,incident_type_parked_Single_Vehicle_Collision,
                  incident_type_Vehicle_Theft,collision_type_rear_collision,collision_type_Side_Collision,incident_severity_minor_damage,incident_severity_TotalLoss,incident_severity_TrivialDamage,authorities_contacted_fire,authorities_contacted_None,authorities_contacted_Other,authorities_contacted_Police,property_damage_yes,police_report_available_yes,auto_make_audi,
                  auto_make_bmw,auto_make_chevrolet,auto_make_dodge,auto_make_ford,auto_make_Honda,auto_make_jeep,auto_make_mercedes,auto_make_nissan,auto_make_saab,auto_make_suburu,auto_make_toyota,auto_make_volkswagen,

                  ]])
    if y_pred[0] == 1:
        prediction_text = "The model predicts that insurance fraud is likely."
        mood_image = static("sad.gif")
    else:
        prediction_text = "The model predicts that insurance fraud is unlikely."
        mood_image = static("suc.gif")
    loading_image=static("load.gif")

    context = {
        'prediction_text': prediction_text,
        'mood_image': mood_image,
        'loading_image':loading_image
    }
    return render(request, 'core/result.html', context)




    
 
