# importing csv module
import csv
import os
import pandas as pd



def list_to_date(date_list):
    date_name = "{}/{}".format(date_list[0],date_list[1])
    return date_name



if __name__ =="__main__":
    filename = "./Weather.csv"

    df = pd.read_csv (filename)   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

    final_list = [{"Date":[1,1990],"Max Temperature":0,"Min Temperature":0,"Precipitation":0,"Wind":0,"Relative Humidity":0,"Solar":0}]

    for index,row in df.iterrows():
        date_string =row['Date'].split('/')
        date_string.remove(date_string[1])
        if(date_string[0]!=final_list[len(final_list)-1]["Date"][0]) and int(date_string[1])>=2004:
            final_list.append({"Date" :date_string,"Max Temperature":row["Max Temperature"],"Min Temperature":row["Min Temperature"],"Precipitation":row["Precipitation"],"Wind":row["Wind"],"Relative Humidity":row["Relative Humidity"],"Solar":row["Solar"]})
        else:
            if final_list[len(final_list)-1]["Max Temperature"]<row['Max Temperature']:
                final_list[len(final_list)-1]["Max Temperature"] = row['Max Temperature']
            if final_list[len(final_list)-1]["Min Temperature"]<row['Min Temperature']:
                final_list[len(final_list)-1]["Min Temperature"] = row['Min Temperature']
            if final_list[len(final_list)-1]["Precipitation"]<row['Precipitation']:
                final_list[len(final_list)-1]["Precipitation"] = row['Precipitation']
            if final_list[len(final_list)-1]["Wind"]<row['Wind']:
                final_list[len(final_list)-1]["Wind"] = row['Wind']
            if final_list[len(final_list)-1]["Relative Humidity"]<row['Relative Humidity']:
                final_list[len(final_list)-1]["Relative Humidity"] = row['Relative Humidity']
            if final_list[len(final_list)-1]["Solar"]<row['Solar']:
                final_list[len(final_list)-1]["Solar"] = row['Solar']

    final_list.remove(final_list[0])

    for row in final_list:
        row["Date"]= list_to_date(row["Date"])
        print(row)


    print(final_list)

    final_df = pd.DataFrame(final_list)

    print(final_df)

    final_df.to_excel(r"./Output.xlsx",index = None, header=True)
    print("Successfully created file")