import pandas
import devices

"""
data = pandas.read_csv("Standard_template.xlsx")
# print(data)
dict = data.to_dict("list")
# print(dict)
# data_frame = pandas.DataFrame(dict)
# print(data_frame)
# Making CSV
# data_frame.to_csv("new_Data.csv")
"('dict', list, 'series', 'split', 'records', 'index')"
dev = devices.GeneralTransmitterHW(channel_name="CH001", plc_name="IEWPLC01", tag="IEW_EWP1", description="Pump 2",
                        alarm_area="TBDALMXX")
frame_list = dev.gen_hw_trans_frame_list()
for item in frame_list:
    item.to_csv("gentrasHW.csv", mode='a', index=False)

print(dev.runtime_hours.tag)
"""
# low = signals.AI()
# vfd = signals.generate_header(low.ai_header_attributes)
"""
print(vfd)
vfd.to_csv("new_Data.csv", index=False)
"""
