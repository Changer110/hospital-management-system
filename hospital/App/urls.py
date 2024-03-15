from django.urls import path



from App.views import *

urlpatterns = [
    path('homepage', index),
    path('login', user_login, name='login'),
    path('dashboard' , dashboard),
    path('doctor' , display_doctors, name='doctor'),
    path('search_doctor/', search_doctor, name='search_doctor'),
    path('show_all_doctors/', show_all_doctors, name='show_all_doctors'),
    path('patient' , display_patient, name='patient'),
    
    path('search_patient', search_patient, name='search_patient'),
    path('patients/', show_all_patient, name='show_all_patient'),
    path('patient_information/<int:employee_id>/', patient_information, name='patient_information'),
    
    
    path('drugs' , display_drugs, name='drugs'),
    path('search_drug/', search_drug, name='search_drug'),
    path('show_drugs/', show_all_drugs, name='show_all_drugs'),
    
    path('medicalrecord/<int:employee_id>/' ,display_medical_record,name='medical_record' ),
    path('search_medical_record/<int:employee_id>' ,search_medical_record, name='search_medical_record'),
    path('back_to_medical_record/<int:record_id>/', back_to_medical_record, name='back_to_medical_record'),
    
   path('prescription/<int:medical_record_id>/', display_prescription, name='prescription'),
    path('appointment/<int:employee_id>/' , appointment , name='appointment'),
    path('add_patient', add_patient, name='add_patient'),
    # path('patient_list', patient_list, name='patient_list'),
    path('add_drug', add_drug, name='add_drug'),
    path('delete_patient/<int:employee_id>/', delete_patient, name='delete_patient'),
    path('change_patient/<int:employee_id>', update_patient, name='change_patient'),
    path('drug_list/', drug_list, name='drug_list'),
    path('delete-drug/<int:drug_id>', delete_drug, name='delete_drug'),
    path('change_drug/<int:drug_id>', change_drug, name='change_drug'),
    path('add_doctor', add_doctor, name='add_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
    path('change_doctor/<int:doctor_id>', change_doctor, name='change_doctor'),
    path('doctor_list', doctor_list, name='doctor_list'),
    path('add_medical_record/<int:employee_id>/', add_medical_record, name='add_medical_record'),
    # path('medical_record_list', medical_record_list, name='medical_record_list'),
    path('medical_records/<int:employee_id>/', show_all_medical_records, name='show_all_medical_records'),
    
    
    
    path('medical-record/delete/<int:record_id>/', delete_medical_record, name='delete_medical_record'),
    path('medical-record/change/<int:record_id>/', change_medical_record, name='change_medical_record'),
    
    path('add_appointment/<int:employee_id>/', add_appointment, name='add_appointment'),
    path('appointment/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('appointment/change/<int:appointment_id>/',change_appointment, name='change_appointment'),
    path('add_prescription/<int:medical_record_id>/', add_prescription, name='add_prescription'),
    path('change-prescription/<int:prescription_id>/', change_prescription, name='change_prescription'),
    path('delete-prescription/<int:prescription_id>/', delete_prescription, name='delete_prescription'),
    
    path('vaccination/<int:medical_record_id>/', vaccination, name='vaccination'),
    path('add_vaccination/<int:medical_record_id>', add_vaccination, name='add_vaccination'),
    path('vaccination/delete/<int:vaccination_id>/', delete_vaccination, name='delete_vaccination'),
    path('vaccination/change/<int:vaccination_id>/', change_vaccination, name='change_vaccination'),
    
    
    
    
    path('enterprises/', enterprise_list, name='enterprise_list'),
    path('enterprises/add/', add_enterprise, name='add_enterprise'),
    path('enterprise/delete/<int:enterprise_id>/',delete_enterprise, name='delete_enterprise'),


    path('previous_post/<int:employee_id>/', previous_post, name='previous_post'),
    path('add-previous-post/<int:employee_id>/', add_previous_post, name='add_previous_post'),
    path('previous_post/change/<int:previous_post_id>/', change_previous_post, name='change_previous_post'),
    path('previous_post/delete/<int:previous_post_id>/', delete_previous_post, name='delete_previous_post'),
    
    
    
    path('accident/<int:employee_id>/', accident, name='accident'),
    path('add_accident/<int:employee_id>/', add_accident, name='add_accident'),
    path('accident/change/<int:accident_id>/', change_accident, name='change_accident'),
    path('accident/delete/<int:accident_id>/', delete_accident, name='delete_accident'),
    
    
    path('occupational_illness/<int:employee_id>/', display_occupational_illness, name='occupational_illness'),
    path('add-occupational-illness/<int:employee_id>/', add_occupational_illness, name='add_occupational_illness'),
    path('occupational_illness/delete/<int:occupational_illness_id>/',delete_occupational_illness, name='delete_occupational_illness'),
    path('occupational_illness/change/<int:occupational_illness_id>/',change_occupational_illness, name='change_occupational_illness'),
    
    
    path('background_patient/<int:employee_id>/', display_background_patient, name='background_patient'),
    path('background_patient/add/<int:employee_id>/', add_background_patient, name='add_background_patient'),
    path('change_background_patient/<int:background_patient_id>/', change_background_patient, name='change_background_patient'),
    path('delete_background_patient/<int:background_patient_id>/',delete_background_patient, name='delete_background_patient'), 




    path('summons_form/<int:employee_id>/', display_summons_form, name='summons_form'), 
    path('add_summons_form/<int:employee_id>/', add_summons_form, name='add_summons_form'),
    path('change_summons_form/<int:summons_form_id>/', change_summons_form, name='change_summons_form'),
    path('delete_summons_form/<int:summons_form_id>/', delete_summons_form, name='delete_summons_form'),
    
    
    
    path('current_post/<int:employee_id>/', display_current_post, name='current_post'),
    path('add_current_post/<int:employee_id>/', add_current_post, name='add_current_post'),
    path('update_current_post/<int:current_post_id>/', update_current_post, name='update_current_post'),
    path('delete_current_post/<int:current_post_id>/', delete_current_post, name='delete_current_post'),
    
    
    
    path('medical_visit/<int:employee_id>/', show_medical_visit, name='medical_visit'),
    path('add_medical_visit/<int:employee_id>/', add_medical_visit, name='add_medical_visit'),
    # path('update_current_post/<int:employee_id>/', update_current_post, name='update_current_post'),
    # path('delete_add_current_post/<int:employee_id>/', delete_current_post, name='delete_current_post'),
]