# Import Libraries
import streamlit as st
from pandas_profiling import ProfileReport
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from PIL import Image
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report



#Set title of our Front web app
image = Image.open('image.png')
st.image(image,use_column_width=True)
st.title('Easy way to Data Analysis')

#Set Slide bar to chose between EDA and Visualization
def main():
	activities=['EDA' , 'Visualisation']
	option=st.sidebar.selectbox('Selection option:',activities)

	#EDA Tab
	if option =='EDA':
		st.subheader("Exploratory Data Analysis")

		#File Upload
		data=st.file_uploader("Upload you CSV or Excel File:",type=['csv','xlsx'])
		

		if data is not None:
			file=pd.read_csv(data)
			st.success("File Upload Success")
			st.dataframe(file.head(10))

			if st.checkbox("Show Data Columns"):
				st.write(file.columns)

			if st.checkbox("Show data Shape"):
				st.write(file.shape)

			if st.checkbox("Data Description"):
				st.write(file.describe())

			#Subset the data
			if st.checkbox("Select columns you want to work with"):

				selected_columns = st.multiselect('Select preferred columns:',file.columns)
				sub_file = file[selected_columns]
				st.dataframe(sub_file)

			if st.checkbox("Show Missing Value"):
				st.write(sub_file.isnull().sum())

			if st.checkbox("Show data types of each columns"):
				st.write(sub_file.dtypes)

			if st.checkbox("Want to change pre-assigned data types? "):

				#For numerical columns
				num_columns=st.multiselect("Select all the columns that you want as a numerical type",sub_file.columns)
				for column in num_columns:
					sub_file[column]=sub_file[column].astype('int64')
					st.success('Columns changed to numerical type')

				#For float column
				float_columns=st.multiselect("Select all the columns that you want as a float type",sub_file.columns)
				for column in float_columns:
					sub_file[column]=sub_file[column].astype('float64')
					st.success('Columns changed to float type')

				#For categorical column
				cat_columns=st.multiselect("Select all the columns that you want as a categorical type",sub_file.columns)
				for column in cat_columns:
					sub_file[column]=sub_file[column].astype('category')
					st.success('Columns changed to category type')

				st.write(sub_file.dtypes)

				if st.checkbox('Show Correlation of various columns'):

					st.write(sub_file.corr())


			if st.checkbox("Would you like to implement AutoEDA library: Pandas Profiling on you data?"):
				profile = ProfileReport(file)
				st_profile_report(profile)
				#prof = ProfileReport(sub_file, explorative=True, minimal=True)

				#output = prof.to_file('output.html', silent=False)
				#st.write(prof)

				#st.success("Success! Check the Page in your other tab.")




	#Visulization
	elif option == 'Visualisation':
		st.subheader("Visualization using Python")

		#File Upload
		data=st.file_uploader("Upload you CSV or Excel File:",type=['csv','xlsx'])
		st.success("File Upload Success")

		if data is not None:
			file=pd.read_csv(data)
			st.dataframe(file.head(10))

			if st.checkbox("Select columns to visualize"):

				selected_columns=st.multiselect("Select your columns",file.columns)
				sub_dataV=file[selected_columns]
				st.dataframe(sub_dataV)
			if st.checkbox("Show data types of each columns"):
				st.write(sub_dataV.dtypes)

			if st.checkbox("Want to change pre-assigned data types? "):

				#For numerical columns
				num_columns=st.multiselect("Select all the columns that you want as a numerical type", sub_dataV.columns)
				for column in num_columns:
					sub_dataV[column]=sub_dataV[column].astype('int64')
					st.success('Columns changed to numerical type')

				#For float column
				float_columns=st.multiselect("Select all the columns that you want as a float type",sub_dataV.columns)
				for column in float_columns:
					sub_dataV[column]=sub_dataV[column].astype('float64')
					st.success('Columns changed to float type')

				#For categorical column
				cat_columns=st.multiselect("Select all the columns that you want as a categorical type",sub_dataV.columns)
				for column in cat_columns:
					sub_dataV[column]=sub_dataV[column].astype('category')
					st.success('Columns changed to category type')

				st.write(sub_dataV.dtypes)
			if st.checkbox('Display Pairplot'):
				fig, ax = plt.subplots()
				st.write(sns.pairplot(sub_dataV, diag_kind='kde'))
				st.set_option('deprecation.showPyplotGlobalUse', False)
				st.pyplot()

			if st.checkbox('Display Pie Chart'):
				all_columns=sub_dataV.columns.to_list()
				pie_columns=st.selectbox("select column to display",all_columns)
				pieChart=sub_dataV[pie_columns].value_counts().plot.pie(autopct="%1.1f%%")
				st.write(pieChart)
				st.pyplot()

			if st.checkbox('Display Correlation heatmap'):
				heatmap=sns.heatmap(sub_dataV.corr(), annot=True,cbar_kws= {'orientation': 'horizontal'})
				st.write(heatmap)
				st.pyplot()

			if st.checkbox('Display Scattered plot'):
				x_axis = st.selectbox("Select  x-axis for scattered plot",sub_dataV.columns)
				y_axis= st.selectbox("Select  y-axis for scattered plot",sub_dataV.columns)
				scattered_plot=sns.scatterplot(x=x_axis, y=y_axis, data=sub_dataV)
				st.write(scattered_plot)
				st.pyplot()

			if st.checkbox('Display line plot'):
				x_axisl = st.selectbox("Select x-axis for line plot",sub_dataV.columns)
				y_axisl = st.selectbox("Select y-axis for line plot",sub_dataV.columns)
				Lineplot = sns.relplot(x=x_axisl, y=y_axisl, kind="line", data=sub_dataV)
				Lineplot.fig.autofmt_xdate()
				st.write(Lineplot)
				st.pyplot()




















if __name__ == '__main__':
	main()

