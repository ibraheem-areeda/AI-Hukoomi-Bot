from flask import request
from bot import app
from web_scraping.vehicle_validation import vehicle_validation
from web_scraping.financial_status import financial_status
from web_scraping.violations_lookup import violations_lookup
from web_scraping.roof_tax import roof_tax
from web_scraping.land_location import land_location
from web_scraping.social_secuirty import social_security
from web_scraping.competitive_ranking import competitive_ranking
from web_scraping.to_whom_it_may_concern import to_whom_it_may_concern
from web_scraping.civil_status_and_passports_department_req_status import civil_status_and_passports_department_req_status
from web_scraping.family_registration import family_registration
from web_scraping.clearance import clearance
from web_scraping.OCR4 import image_info_extractor

processes = {"111":["الإستعلام عن المخالفات", 3, [" أمانة عمان الكبرى - الإستعلام عن المخالفات\n\n أدخل رقم المركبة لطفاً", "أدخل الترميز", "أدخل رقم التسجيل"], vehicle_validation], "11":["الإستعلام عن المخالفات", 2, [" أمانة عمان الكبرى - الإستعلام عن المخالفات\n\n أرسل صورة رخصة المركبة من الأمام لطفاً", "أرسل صورة رخصة المركبة من الخلف"], image_info_extractor], "12":["المالية لوزارة المالية", 1, ["الذمم المالية المتحققة بذمتكم لوزارة المالية / مديرية الأموال العامة\n\nأدخل الرقم الوطني لطفاً"], financial_status], "13":["قيم مخالفات السير", 1, ["الاستعلام عن قيم مخالفات السير حسب قانون السير رقم 48\n\n أدخل جزء من وصف المخالفة لطفاً"], violations_lookup], "14":["ضريبة الأبنية والمسقفات", 2, ["ضريبة الأبنية والمسقفات\n\n أدخل الرقم الوطني لطفاً", "أدخل رقم الهوية"], roof_tax], "15":["الاستعلام عن قطعة أرض", 1, ["دائرة الأراضي والمساحة - الاستعلام عن قطعة أرض\n\n أدخل مفتاح القطعة لطفاً"], land_location], "16":["معلومات المشترك في الضمان الاجتماعي", 2, ["المؤسسة العامة للضمان الاجتماعي - لوحة معلومات المشترك\n\n أدخل اسم المستخدم في موقع المؤسسة العامة للضمان الاجتماعي لطفاً", "أدخل الباسوورد"], social_security], "17":["الترتيب التنافسي في ديوان الخدمة المدنية", 2, ["ديوان الخدمة المدنية - الترتيب التنافسي\n\n أدخل الرقم الوطني لطفاً", "أدخل رقم الهوية"], competitive_ranking], "18":["المؤسسة العامة للضمان الإجتماعي - كتب لمن يهمه الأمر", 2, ["المؤسسة العامة للضمان الإجتماعي - كتب لمن يهمه الأمر\n\n أدخل اسم المستخدم في موقع المؤسسة العامة للضمان الاجتماعي لطفاً", "أدخل الباسوورد"], to_whom_it_may_concern], "19":["الأحوال المدنية و الجوازات - متابعة الطلبات", 2, ["الأحوال المدنية و الجوازات - متابعة الطلبات\n\n أدخل اسم المستخدم في موقع دائرة الأحوال المدنية و الجوازات لطفاً", "أدخل الباسوورد"], civil_status_and_passports_department_req_status], "20":["الأحوال المدنية و الجوازات - إصدار شهادة القيد العائلي", 2, ["الأحوال المدنية و الجوازات - إصدار شهادة القيد العائلي\n\n أدخل اسم المستخدم في موقع دائرة الأحوال المدنية و الجوازات لطفاً", "أدخل الباسوورد"], family_registration], "21":["طلب براءة ذمة", 3, ["أمانة عمان الكبرى - طلب براءة ذمة\n\n أدخل الرقم الوطني لطفاً", "أدخل رقم قيد الهوية\t\t( * * * / * * * )  :Ex", "أدخل رقم الهاتف\t( * * * * * * * * 7 0 )  :Ex"], clearance]}
responses = {}  
current_process = "" 

def service(incoming_msg, phone_number):
    global current_process
    global process_values
    global question
    # incoming_msg = request.values['Body']
    # phone_number = request.values['WaId']
    
    if incoming_msg in processes:
        current_process = incoming_msg
        process_values = processes[incoming_msg][0]
        responses[process_values] = []  
        question = 0
        profile_name = request.values["ProfileName"]
        app.send_message(f"أهلاً  {profile_name}", phone_number)
        app.send_message(f"{processes[current_process][2][question]}", phone_number)
        app.send_message("للخروج في أي وقت، فقط اضغط 0", phone_number)
    
    elif incoming_msg == "0":
        del responses[process_values]
        current_process = ""
        app.send_message("تم إلغاء العملية", phone_number)

    elif processes[current_process][0] in responses:
        if len(responses[process_values]) < processes[current_process][1]:  
            responses[process_values].append(incoming_msg)  
            remaining_responses = processes[current_process][1] - len(responses[process_values]) 
            if remaining_responses > 0:
                question += 1
                app.send_message(processes[current_process][2][question], phone_number)
                print(responses)
            else:
                collected_responses = responses[process_values]
                do_service = processes[current_process][3]
                del responses[process_values]
                app.send_message("شكراً لك، انتظر النتيجة", phone_number)
                if current_process == "11":
                    service_result = do_service()
                else:
                    service_result = do_service(*collected_responses)

                if current_process == "111" or current_process == "11" or current_process == "14" or current_process == "15" or current_process == "16" or current_process == "17" or current_process == "18" or current_process == "19" or current_process == "20":
                    if isinstance(service_result, tuple):   
                        for ele in service_result:
                            app.send_media_message(ele, phone_number)
                    else:
                        app.send_media_message(service_result, phone_number)

                elif isinstance(service_result, tuple):       # to handle long twilio's message
                    for ele in service_result:
                        app.send_message(ele, phone_number)
                else:
                    app.send_message(service_result, phone_number)
                current_process = ""
