
import pickle
from turtle import color
import streamlit as st
from streamlit_option_menu import option_menu
import hydralit_components as hc


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/clean-medical-background_53876-116875.jpg?w=1060&t=st=1665926250~exp=1665926850~hmac=0d90c6771da6df4f4af9aeb318fd72ff05e4bef3c68cc7719d36bfe6a1d7c25f");
             background-attachment: fixed;
             
             background-size: cover;
             
   
         }}
         
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)


   

# loading the saved models

diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

menu_data = [
        {'icon': "far fa-clone", 'label':"Info Page"},
        {'icon': "bi bi-activity", 'label':"Diabetes Prediction"},
        {'icon': "bi bi-heart", 'label':"Heart Disease Prediction"},#no tooltip message
        {'icon': "bi bi-person", 'label':"Parkinsons Prediction"},
     
       
        {'icon': "bi bi-calendar2-check-fill", 'label':"Treatment",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
       
]
# we can override any part of the primary colors of the menu
over_theme= {'txc_inactive': 'Black','menu_background':'#8FDDDF','txc_active':'black','option_active':'white'}
#over_theme = {'txc_inactive': 'black'}
selected = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

#get the id of the menu item clicked
#st.info(f"{selected=}")


if (selected == 'Home'):
    st.title("Multiple disease prediction system ")
   
    new_title = '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to our webapp!!!!!   </p>'
    st.markdown(new_title, unsafe_allow_html=True)
   
   
    #title = '<
    #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
            This is an integrated webApp which predicts the selected disease when the user gives an input for each asked attributes .

The system can predict 3 types of diseases

-Diabetes

-Heart disease

-Parkinson's disease

User can get to know about these diseases in the Info page.

If user is affected by any of the diseases then they can also check out the possible treatment on our Treatments page.


           
            ''')


if (selected == 'Info Page'):
    st.title("Multiple disease prediction system ")
   
    new_title1= '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Diabetes  </p>'
    st.markdown(new_title1, unsafe_allow_html=True)
   
    #title = '<
    #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
            Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.
            Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.

            Over time, having too much glucose in your blood can cause health problems. Although diabetes has no cure, you can take steps to manage your diabetes and stay healthy with home remedies provided in the treatmnet section.
            ''')

    new_title2 = '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Heart Disease  </p>'
    st.markdown(new_title2, unsafe_allow_html=True)
     
     #title = '<
     #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
             Coronary artery disease is a common heart condition that affects the major blood vessels that supply the heart muscle. Cholesterol deposits (plaques) in the heart arteries are usually the cause of coronary artery disease. The buildup of these plaques is called atherosclerosis (ath-ur-o-skluh-ROE-sis). Atherosclerosis reduces blood flow to the heart and other parts of the body. It can lead to a heart attack, chest pain (angina) or stroke.

Coronary artery disease symptoms may be different for men and women. For instance, men are more likely to have chest pain. Women are more likely to have other symptoms along with chest discomfort, such as shortness of breath, nausea and extreme fatigue.

Symptoms of coronary artery disease can include:

Chest pain, chest tightness, chest pressure and chest discomfort (angina)
Shortness of breath
Pain in the neck, jaw, throat, upper belly area or back
Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in those body areas are narrowed
            ''')
       
    new_title3 = '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Parkinsons Disease  </p>'
    st.markdown(new_title3, unsafe_allow_html=True)
     
     #title = '<
     #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
             Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.

In the early stages of Parkinson's disease, your face may show little or no expression. Your arms may not swing when you walk. Your speech may become soft or slurred. Parkinson's disease symptoms worsen as your condition progresses over time.

Although Parkinson's disease can't be cured, medications might significantly improve your symptoms. Occasionally, your health care provider may suggest surgery to regulate certain regions of your brain and improve your symptoms.
Tremor.
Slowed movement (bradykinesia).
Rigid muscles.
Impaired posture and balance.
Loss of automatic movements.
            ''')

   
if (selected == 'Treatment'):
    st.title("Multiple disease prediction system ")
   
    new_title1= '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Heart Disease  </p>'
    st.markdown(new_title1, unsafe_allow_html=True)
   
    #title = '<
    #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
            Home Remedies: Some Lifestyle changes can help your heart health
           
-Stop smoking: Smoking is a major risk factor for heart disease, especially atherosclerosis.

-Control your blood pressure.

-Check your cholesterol.

-Keep diabetes under control.

-Excercise

-Eat healthy foods.

-Maintain a healthy weight.

-Manage stress.
            ''')
           

    new_title2= '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Diabetes  </p>'
    st.markdown(new_title2, unsafe_allow_html=True)
   
    #title = '<
    #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
-Eat a consistent diet.

-Get consistent exercise.

-Reduce stress.

-Stay hydrated.

-Get a good night's rest.

-See your doctor.

-Maintain a healthy weight.

-Stick to your medication and insulin regimen.
           
            ''')
           
    new_title3= '<p style="font-family: sans-serif; color:Black; font-size: 30px;"> Parkinsons Disease  </p>'
    st.markdown(new_title3, unsafe_allow_html=True)
   
    #title = '<
    #p style="font-family: sans-serif; color:Black; font-size: 30px;"> Welcome to this webapp   </p>'
    st.info('''
Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.

In the early stages of Parkinson's disease, your face may show little or no expression. Your arms may not swing when you walk. Your speech may become soft or slurred. Parkinson's disease symptoms worsen as your condition progresses over time.

Although Parkinson's disease can't be cured, medications might significantly improve your symptoms. Occasionally, your health care provider may suggest surgery to regulate certain regions of your brain and improve your symptoms.

These treatments include:

Supportive therapies,
Medication,
surgery (for some people)

Supportive therapy:
   
Physiotherapy,
Occupational therapy,
Speech and language therapy,

            ''')
           
           
           

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
   
    # page title
    #st.title('')

   
    st.title('Diabetes Prediction')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
   
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
       
    with col2:
        Glucose = st.text_input('Glucose Level')
   
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
   
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
   
    with col2:
        Insulin = st.text_input('Insulin Level')
   
    with col3:
        BMI = st.text_input('BMI value')
   
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
    with col2:
        Age = st.text_input('Age of the Person')
   
   
    # code for Prediction
    diab_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
       
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
   
   
   
    # page title
    st.title('Heart Disease Prediction')
   
    col1, col2, col3 = st.columns(3)
   
    with col1:
        age = st.number_input('Age')
       
    with col2:
        sex = st.number_input ('Sex')
       
    with col3:
        cp = st.number_input ('Chest Pain types')
       
    with col1:
        trestbps = st.number_input ('Resting Blood Pressure')
       
    with col2:
        chol = st.number_input ('Serum Cholestoral in mg/dl')
       
    with col3:
        fbs = st.number_input ('Fasting Blood Sugar > 120 mg/dl')
       
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
       
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
       
    with col3:
        exang = st.number_input ('Exercise Induced Angina')
       
    with col1:
        oldpeak = st.number_input ('ST depression induced by exercise')
       
    with col2:
        slope = st.number_input ('Slope of the peak exercise ST segment')
       
    with col3:
        ca = st.number_input ('Major vessels colored by flourosopy')
       
    with col1:
        thal = st.number_input ('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
       
       
     
     
    # code for Prediction
    heart_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
       
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
       
    st.success(heart_diagnosis)
       
   
   

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
   
    # page title
    st.title("Parkinson's Disease Prediction ")
   
    col1, col2, col3, col4, col5 = st.columns(5)  
   
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
       
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
       
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
       
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
       
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
       
    with col1:
        RAP = st.text_input('MDVP:RAP')
       
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
       
    with col3:
        DDP = st.text_input('Jitter:DDP')
       
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
       
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
       
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
       
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
       
    with col3:
        APQ = st.text_input('MDVP:APQ')
       
    with col4:
        DDA = st.text_input('Shimmer:DDA')
       
    with col5:
        NHR = st.text_input('NHR')
       
    with col1:
        HNR = st.text_input('HNR')
       
    with col2:
        RPDE = st.text_input('RPDE')
       
    with col3:
        DFA = st.text_input('DFA')
       
    with col4:
        spread1 = st.text_input('spread1')
       
    with col5:
        spread2 = st.text_input('spread2')
       
    with col1:
        D2 = st.text_input('D2')
       
    with col2:
        PPE = st.text_input('PPE')
       
   
   
    # code for Prediction
    parkinsons_diagnosis = ''
   
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
       
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
         
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
       
    st.success(parkinsons_diagnosis)