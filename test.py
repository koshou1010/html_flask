import os
meta_data = '{"name":"file_meta","raw_dumper_ver":"raw_dumper_v1_2","project_ver":"ESRTSD_bcus_v1_2","machine_sn":"FT3WLPSW","fw_ver":"fw_sextant_1.0.0","hw_ver":"hw_sextant_1.0.0","sw_ver":"0.1.3-alpha-1","app_name":"Enosim ESRTSD","user_sn":"9366d0eb90a06ff067dfdef6c3eca8f339f72ddd4fa21cf6e376177f3ed1a547","organization":"enosim","reference_time":null,"l_date":"2021-05-19T11:44:06.076+08:00","channel_name":["_#ec_i#0","_#ec_i#0","_#ec_i#0","_#ec_i#0","_#tm_c#0","_#rh_p#0","_#fm_sccm#0"]}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.125+08:00","status_flag":"on_start","subject_flag":"user","step_flag":null}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","status_flag":"on_first_preset_voltage","subject_flag":"auto","step_flag":null}\n'+'{"name":"preset_meta","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","len_channel":7,"device_cfg":{"supply_voltage":5.0,"channel_biasing_resistance":[1,1,1,1,1,1,1],"channel_reference_c":[null,null,null,null,null,null,null],"channel_reference_voltage":[null,null,null,null,null,null,null],"preset_flow":[5],"channel_actual_gain":[1.0,1.0,1.0,1.0,1.0,1.0,1.0],"channel_preset_voltage":[1.5,1.5,1.5,1.5,1.5,1.5,1.5]},"critical":{"first_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":1800.0,"during":1.0},"second_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":10.0,"during":1.0},"round_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"baseline":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":60.0,"during":1.0},"stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":120.0,"during":1.0},"reacting":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"recovery":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":600.0,"during":1.0},"auto_stop_valve":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":4.0,"during":1.0},"slope_window_size":10,"threshold_ref_channel_indexes":[0,1]}}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:14.264+08:00","status_flag":"on_first_waiting_initial","subject_flag":"auto","valve":0,"pump":1,"step_flag":null}\n'
# with open(r'C:\SPEC\readme.txt', 'w') as f:
#     f.write(meta_data)

filename = r'C:\SPEC\Experiment\SXT2SPECECE010010\test.txt'
print(os.path.isfile(filename))
if not os.path.isfile(filename):
    f = open(filename, "w")
    f.write(meta_data)
    f.close()
print(os.path.isfile(filename))