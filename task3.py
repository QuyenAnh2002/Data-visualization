import pyreadr
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pyreadr.read_r("C:/Users/quyen/Downloads/births2006.smpl.rda")
#DOB_MM Month of date of birth
#DOB_WK Day of week of birth
#MAGER Mother's age
#TBO_REC Total birth order
#WTGAIN Weight gain by mother
#SEX a factor with levels F M, representing the sex of the child
#APGAR5 APGAR score
#DMEDUC Mother's education level
#UPREVIS Number of prenatal visits
#ESTGEST Estimated weeks of gestation
#DMETH_REC Delivery Method
#DPLURAL "Plural Births;" levels include 1 Single, 2 Twin, 3 Triplet, 4 Quadruplet, and 5 Quintuplet or higher
#DBWT Birth weight, in grams

#task1
 

df = data['births2006.smpl']
df.head(10)
df.describe()



#task2

df['DOB_WK'].value_counts().plot(kind='bar')
plt.show()

births_per_day_of_week = df.groupby("DOB_WK").size()
print(births_per_day_of_week)


#task3


births_per_day_method = df.groupby(["DOB_WK", "DMETH_REC"]).size()
print(births_per_day_method)

births_per_day_method.plot(kind='barh', figsize = (16,9) )
plt.show()


#task4  


single_births = df[df["DPLURAL"] == '1 Single']['DBWT']
single_births
multiple_births  = df[df["DPLURAL"] != '1 Single']['DBWT']
multiple_births

plt.hist(single_births, bins=20, alpha=0.5, label="Single Births", color ="black")
plt.hist(multiple_births, bins=20, alpha=0.5, label="Multiple Births", color ="red")

plt.xlabel("Birth Weight")
plt.ylabel("Frequency")
plt.title("Histogram of Birth Weight based on Single/Multiple Births")
plt.legend()
plt.show()


#task5


births_vaginal = df[df["DMETH_REC"] == "Vaginal"]
births_Csection = df[df["DMETH_REC"] == "C-section"]
births_Unknown = df[df["DMETH_REC"] == "Unknown"]


plt.hist(births_vaginal["DBWT"], bins=60, alpha=0.5, label="Vaginal Delivery")
plt.hist(births_Csection["DBWT"], bins=60, alpha=0.5, label="Cesarean Delivery")
plt.hist(births_Unknown["DBWT"], bins=60, alpha=0.5, label="Unknown", color = "red")

plt.xlabel("Birth Weight")
plt.ylabel("Frequency")
plt.title("Histogram of Birth Weight based on Delivery Method")
plt.legend()
plt.show()


#task6


sns.boxplot(x="APGAR5", y="DBWT", data=df)

plt.xlabel('Apgar Score')
plt.ylabel('Birth Weight')
plt.title('Box Plot of Birth Weight Per Apgar Score')
plt.show()


#task7


sns.boxplot(x="DOB_WK", y="DBWT", data=df)

plt.xlabel('Day of week')
plt.ylabel('Birth Weight')
plt.title('Box Plot of Birth Weight Per Day of Week')
plt.show()


#task8

multiple_births_per_gender = df[df["DPLURAL"] != '1 Single'].groupby("SEX")["DBWT"].mean()
print(multiple_births_per_gender)


multiple_births_per_gender.plot(kind = "barh")
plt.show()

#x