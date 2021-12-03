import csv 
import pandas as pd 
import random 
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv("School1.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data],["Math Scores"],show_hist = False)
fig.show()

std_deviation = statistics.stdev(data)
mean = statistics.mean(data)

print("Mean of this data is {}".format(mean))
print("Standard deviation of this data is {}".format(std_deviation))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
print("The mean of sampling distribution is: ", mean)

std_deviation = statistics.stdev(mean_list)
print("The standard deviation of sample is: ", std_deviation)

fig = ff.create_distplot([mean_list],["Math Scores"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20], mode = "lines", name = "MEAN"))
fig.show()

first_sd_start,first_sd_end = mean - std_deviation, mean + std_deviation
second_sd_start,second_sd_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_sd_start,third_sd_end = mean - (3*std_deviation), mean + (3*std_deviation)

df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of this data 1 is {}".format(mean_of_sample1))
fig = ff.create_distplot([mean_list],["Math Scores"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1],y = [0,0.17], mode = "lines", name = "students ipad"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.show()

df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of this data 2 is {}".format(mean_of_sample2))
fig = ff.create_distplot([mean_list],["Math Scores"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2],y = [0,0.17], mode = "lines", name = "students extra classes"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.show()

df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("Mean of this data 3 is {}".format(mean_of_sample3))
fig = ff.create_distplot([mean_list],["Math Scores"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample3, mean_of_sample3],y = [0,0.17], mode = "lines", name = "students with funsheets"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.show()

z_score = (mean_of_sample1 - mean)/std_deviation
print("The z score of sample 1 is: ", z_score)

z_score = (mean_of_sample2 - mean)/std_deviation
print("The z score of sample 2 is: ", z_score)

z_score = (mean_of_sample3 - mean)/std_deviation
print("The z score of sample 3 is: ", z_score)