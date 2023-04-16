import pandas as pd
######################
#Series#
######################
series2=pd.Series ([10,15,5],index=["Pen","Pencil","Eraser"])#string label for series
print ("Value of pen and eraser\n",series2[["Pen","Eraser"]])
series2.index=["car","bike","spinner"]
print ("changed index label",series2[["bike","spinner"]])#changing index labels
series2.name="Toy Price"#giving name to series
series2.index.name="Toy name"#giving name to index
print ("Is series empty?",series2.empty)#checking if series is empty
print ("Values in series \n",series2.values)#printing elements of series
print (series2)
print ("\n \n")
series2.index=["Pen","Pencil","Eraser"]#changing index labels back to initial
series3=pd.Series ([20,25,5,10],index=["Pencil","Eraser","Pen","Rular"])
print ("addition of two series with + operator \n ",series2+series3)#addition of series with NaN
print ("addition of two series with add function \n ",series2.add(series3,fill_value="0"))#use of add fucntion replace non exsting values to 0
print ("subraction of two series with - operator \n ",series2-series3)
print ("addition of two series with sub function \n ",series2.sub(series3,fill_value="0"))
print ("multiplication of two series with * operator \n ",series2*series3)
print ("addition of two series with mul function \n ",series2.mul(series3,fill_value="0"))
#############################
#dataframe
#############################
seriesA=pd.Series([1,2,3,4,5] , index =['a','b','c','d','e'])
seriesB=pd.Series([1000,2000,-1000,-5000,1000] , index =['a','b','c','d','e'])
seriesC=pd.Series([10,20,-10,-50,100] , index =['z','y','a','c','e'])
dframe7=pd.DataFrame([seriesA,seriesB])#dataframe from series
dframe8=pd.DataFrame([seriesA,seriesC])#dataframe from uneven series
print ("Datafarme using even series \n",dframe7)
print("Datafarme using uneven series \n",dframe8)
ResultSheet={
    "Tom":pd.Series([90,80,87],index=["Eng","hindi","math"]),
    "joy":pd.Series([99,88,80],index=["Eng","hindi","math"]),
    "sim":pd.Series([92,83,81],index=["Eng","hindi","math"]),
    "ricky":pd.Series([93,81,89],index=["Eng","hindi","math"]),
    "vini":pd.Series([91,83,86],index=["Eng","hindi","math"])}
ResultDF=pd.DataFrame(ResultSheet)#dataframe from dictionary of series
print ("Dataframe using dictionary of series \n",ResultDF)
ResultDF["joy"]=[30,20,24]#changing values of a column
print ("Dataframe after changing value of column \n",ResultDF)
ResultDF["vini"]=40#giving same value to complete column
print ("Dataframe after changing value of column to same \n",ResultDF)
ResultDF["Nick"]=[45,32,85]#adding a column
print ("Dataframe after adding a column \n",ResultDF)
ResultDF.loc["SST"]=[20,30,10,90,100,76]#adding a row
print ("Dataframe after adding a row \n",ResultDF)
ResultDF=ResultDF.drop("Eng",axis=0)#deleting a row
print ("Dataframe after droping a row \n",ResultDF)
ResultDF=ResultDF.drop(["joy"],axis=1)#deleting a column
print ("Dataframe after droping a column \n",ResultDF)
ResultDF=ResultDF.rename({"hindi":"Sub2"},axis="index")#renaming an index
print ("Dataframe after renamimg  a row \n",ResultDF)
ResultDF=ResultDF.rename({"ricky":"stu1","vini":"stu2"},axis="columns") #Renaming columns
print ("Dataframe after renaming a column \n",ResultDF)
ResultDF[:]=0 # giving same value to all elements of series
print ("giving same value to complete dataframe \n",ResultDF)
print (ResultDF.loc["SST"])#refering a row
print (ResultDF["sim"])# refering a column 
df=pd.DataFrame(pd.Series([23,34,56],index=[2,3,4]))
print (df.loc[2])#refering an element by numeric index.
