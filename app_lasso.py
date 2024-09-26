
# Load the trained Lasso model
filename_lasso = 'lasso_regression_model.sav'
lasso_model = pickle.load(open(filename_lasso, 'rb'))

st.title("Lasso Regression Revenue Prediction App")

st.write("Enter monthly revenue to predict other variables using Lasso Regression:")

monthly_revenue = st.number_input("Monthly Revenue", min_value=0.0)

if st.button("Predict"):
  # Reshape the input to a 2D array
  input_data = [[monthly_revenue]]

  # Make a prediction using the loaded model
  prediction = lasso_model.predict(input_data)[0]

  st.write("Predicted Values:")
  # You might want to format or display the prediction more nicely
  # depending on the output of your model
  st.write(prediction)

# You can add more elements and features to your Streamlit app as needed.
# For example, you could display charts, tables, or upload your own data.


!streamlit run app_lasso.py & npx localtunnel --port 8501
