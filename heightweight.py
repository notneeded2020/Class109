import statistics 
import pandas as pd 
import csv 

df = pd.read_csv("data3.csv")

height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_std = statistics.stdev(height_list)
weight_std = statistics.stdev(weight_list)

height_first_stdev_start,height_first_stdev_end = height_mean-height_std,height_mean+height_std 
weight_first_stdev_start,weight_first_stdev_end = weight_mean-weight_std,weight_mean+weight_std 

height_second_stdev_start,height_second_stdev_end = height_mean-(2*height_std),height_mean+(2*height_std)
weight_second_stdev_start,weight_second_stdev_end = weight_mean-(2*weight_std),weight_mean+(2*weight_std)

height_third_stdev_start,height_third_stdev_end = height_mean-(3*height_std),height_mean+(3*height_std)
weight_third_stdev_start,weight_third_stdev_end = weight_mean-(3*weight_std),weight_mean+(3*weight_std)

height_list_of_data_within_1stdev = [result for result in height_list if result > height_first_stdev_start and result < height_first_stdev_end]
weight_list_of_data_within_1stdev = [result for result in weight_list if result > weight_first_stdev_start and result < weight_first_stdev_end]

height_list_of_data_within_2stdev = [result for result in height_list if result > height_second_stdev_start and result < height_second_stdev_end]
weight_list_of_data_within_2stdev = [result for result in weight_list if result > weight_second_stdev_start and result < weight_second_stdev_end]

height_list_of_data_within_3stdev = [result for result in height_list if result > height_third_stdev_start and result < height_third_stdev_end]
weight_list_of_data_within_3stdev = [result for result in weight_list if result > weight_third_stdev_start and result < weight_third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3stdev)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3stdev)*100.0/len(weight_list)))


# print("Mean,median and mode of height is: {},{} and {} respectively.".format(height_mean,height_median,height_mode))
# print("Mean,median and mode of weight is: {},{} and {} respectively.".format(weight_mean,weight_median,weight_mode))