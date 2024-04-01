from django.urls import path



from App.views import *

urlpatterns = [
    path('', index),
    path('Hospital-system-management/login', user_login, name='login'),
    path('logout', user_logout, name='logout'), 
    path('dashboard' , dashboard),
    
    
    # DOCTORS URLS
    path('Display/doctor', display_doctor, name='display_doctor'),
    path('<str:doctor_id>/doctor', add_doctor, name='add_doctor'),
    path('Update/doctor/<int:doctor_id>', update_doctor, name='update_doctor'),
    path('Delete/doctor/<int:doctor_id>', delete_doctor, name='delete_doctor'),
    
    
    # PATIENTS URLS
    path('Display/patient/<str:employee_id>' , display_patient, name='display_patient'),
    path('<str:employee_id>/patient', add_patient, name='add_patient'),
    path('download_patient/<int:employee_id>', download_patient, name='download_patient'),
    path('Delete/patient/<int:employee_id>', delete_patient, name='delete_patient'),
    path('Update/patient/<int:employee_id>', update_patient, name='update_patient'),
    
    
    # DRUGS URLS
    path('Display/drug' , display_drug, name='display_drug'),
    path('<str:drug_id>/drug', add_drug, name='add_drug'),
    path('download_drug/', download_drugs, name='download_drug'),
    path('Update/drug/<int:drug_id>', update_drug, name='update_drug'),
    path('Delete/drug/<int:drug_id>', delete_drug, name='delete_drug'),
    
    
    # MEDICAL RECORDS URLS
    path('Display/medical-record/<int:employee_id>' ,display_medical_record,name='display_medical_record'),
    path('search_medical_record/<int:employee_id>' ,search_medical_record, name='search_medical_record'),
    path('back_to_medical_record/<int:record_id>', back_to_medical_record, name='back_to_medical_record'),
    path('Add/medical-record/<int:employee_id>', add_medical_record, name='add_medical_record'),
    path('download-medical-record/<int:record_id>/', download_medical_record, name='download_medical_record'), 
    path('Delete/medical-record/<int:record_id>', delete_medical_record, name='delete_medical_record'),
    path('Update/medical-record/<int:record_id>', change_medical_record, name='update_medical_record'),
    
    
    # APPOINTMENT URLS
    path('Display/appointment/<int:employee_id>/' , display_appointment , name='display_appointment'),
    path('Add/appointment/<int:employee_id>/', add_appointment, name='add_appointment'),
    path('Update/appointment/update/<int:appointment_id>/',update_appointment, name='update_appointment'),
    path('Delete/appointment/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    
    
    # PRESCRIPTIONS URLS
    path('Display/prescription/<int:medical_record_id>/', display_prescription, name='display_prescription'),
    path('Add/prescription/<int:medical_record_id>/', add_prescription, name='add_prescription'),
    path('download_prescription/<int:prescription_id>/', download_prescription, name='download_prescription'),
    path('Update/prescription/<int:prescription_id>/', change_prescription, name='update_prescription'),
    path('Delete/prescription/<int:prescription_id>/', delete_prescription, name='delete_prescription'),
    
    
    # VACCINATION URLS
    path('Display/vaccination/<int:medical_record_id>/', display_vaccination, name='display_vaccination'),
    path('Add/vaccination/<int:medical_record_id>', add_vaccination, name='add_vaccination'),
    path('vaccination/download/<int:vaccination_id>/', download_vaccination, name='download_vaccination'),
    path('Update/vaccination/<int:vaccination_id>/', change_vaccination, name='change_vaccination'),
    path('Delete/vaccination/<int:vaccination_id>/', delete_vaccination, name='delete_vaccination'),
    
    
    
    
    # ENTERPRISE URLS
    path('enterprises/', enterprise_list, name='enterprise_list'),
    path('enterprises/add/', add_enterprise, name='add_enterprise'),
    path('enterprise/delete/<int:enterprise_id>/',delete_enterprise, name='delete_enterprise'),
    
    
    
    # PREVIOUS POST URLS
    path('Display/<int:employee_id>/display/previous_post', display_previous_post, name='display_previous_post'),
    path('Add/<int:employee_id>/add/previous_post', add_previous_post, name='add_previous_post'),
    path('previous_post/download/<int:previous_post_id>/', download_previous_post, name='download_previous_post'),
    path('Update/previous_post/<int:previous_post_id>', update_previous_post, name='update_previous_post'),
    path('Delete/previous_post/<int:previous_post_id>', delete_previous_post, name='delete_previous_post'),
    
    
    
    # ACCIDENT URLS
    path('Display/<int:employee_id>/display/accident', display_accident, name='display_accident'),
    path('Add/<int:employee_id>/add/accident', add_accident, name='add_accident'),
    path('accident/download/<int:accident_id>/', download_accident, name='download_accident'),
    path('Update/accident/<int:accident_id>', update_accident, name='update_accident'),
    path('Delete/accident/<int:accident_id>', delete_accident, name='delete_accident'),
    
    
    # OCCUPATIONAL ILLNESS URLS
    path('Display/occupational-illness/<int:employee_id>', display_occupational_illness, name='display_occupational_illness'),
    path('Add/occupational-illness/<int:employee_id>', add_occupational_illness, name='add_occupational_illness'),
    path('occupational_illness/download/<int:occupational_illness_id>/',download_occupational_illness, name='download_occupational_illness'),
    path('Update/occupational-illness/<int:occupational_illness_id>',update_occupational_illness, name='update_occupational_illness'),
    path('Delete/occupational-illness/<int:occupational_illness_id>',delete_occupational_illness, name='delete_occupational_illness'),
    
    
    # BACKGROUND PATIENT URLS
    path('Display/background/<int:employee_id>', display_background, name='display_background'),
    path('Add/background/<int:employee_id>', add_background, name='add_background'),
    path('download_background_patient/<int:background_patient_id>/', download_background_patient, name='download_background_patient'),
    path('Update/background/<int:background_id>', update_background, name='update_background'),
    path('Delete_background/<int:background_id>',delete_background, name='delete_background'), 
    
    
    # SUMMONS URLS
    path('Display/summons/<int:employee_id>', display_summons, name='display_summons'),
    path('Add/summons/<int:employee_id>', add_summons, name='add_summons'),
    path('download_summons_form/<int:summons_form_id>/', download_summons_form, name='download_summons_form'),
    path('Update/summons/<int:summons_id>', update_summons, name='update_summons'),
    path('Delete/summons/<int:summons_id>', delete_summons, name='delete_summons'),
    
    
    # CURRENT POST URLS
    path('Display/current-post/<int:employee_id>', display_current_post, name='display_current_post'),
    path('Add/current-post/<int:employee_id>', add_current_post, name='add_current_post'),
    path('download_current_post/<int:current_post_id>/', download_current_post, name='download_current_post'),
    path('Update/current-post/<int:current_post_id>', update_current_post, name='update_current_post'),
    path('Delete/current-post/<int:current_post_id>', delete_current_post, name='delete_current_post'),
    
    
    # MEDICAL VISIT URLS
    path('Display/medical_visit/<int:employee_id>', show_medical_visit, name='display_medical_visit'),
    path('Add/medical_visit/<int:employee_id>', add_medical_visit, name='add_medical_visit'),
    path('Download/medical_visit/<int:visit_id>', download_medical_visit, name='download_medical_visit'),
    path('Update/medical_visit/<int:visit_id>', change_medical_visit, name='update_medical_visit'),
    path('Delete/medical_visit/<int:visit_id>', delete_medical_visit, name='delete_medical_visit'),
    
    
    # ABSENTEEISM URLS
    path('Display/absenteeism/<int:employee_id>',display_absenteeism, name='display_absenteeism'),
    path('Add/absenteeism/<int:employee_id>',add_absenteeism, name='add_absenteeism'),
    path('absenteeism/download/<int:absenteeism_id>/', download_absenteeism, name='download_absenteeism'),
    path('Update/absenteeism/<int:absenteeism_id>',update_absenteeism, name='update_absenteeism'),
    path('Delete/absenteeism/<int:absenteeism_id>', delete_absenteeism, name='delete_absenteeism'),
]