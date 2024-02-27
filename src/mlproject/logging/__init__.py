# NOT USING THIS APPROACH, INSTEAD USING mlproject construct for simpler coding 
# import os
# import sys
# import logging

# # save the info ..

# logging_str = "[%(asctime)s: %(levelname)s : %(module)s : %(message)s]"

# # levelname -> if rnning code from root folder will return root 

# #log folder

# log_dir  ="logs"

# # creating log file :
# log_filepath = os.path.join(log_dir , "running_log.log")

# os.makedirs(log_dir , exist_ok =True)
# # exist_of = True , if folder already created then will not create again

# #defining my logging string 
# logging.basicConfig(
#     level = logging.INFO, # info level log 
#     format = logging_str,
#     handlers=[
#         logging.FileHandler(log_filepath),
#         logging.StreamHandler(sys.stdout)
#     ]
# )

# #creating the object 

# logger = logging.getLogger("mlprojectLogger") # can provide any kind of names 