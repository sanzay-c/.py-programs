import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import tensorflow as tf
from tensorflow import keras
import joblib
import json
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    
    .risk-high {
        background-color: #363333;
        border-left: 5px solid #ff4444;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .risk-low {
        background-color: #363333;
        border-left: 5px solid #44ff44;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .info-box {
        background-color: #383c3d82;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #0288d1;
    }
    
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background-color: #0d47a1;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model_components(): # load all models 
    """Load all model components"""
    # Get the directory of the current script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    try:
        model_path = os.path.join(BASE_DIR, "models", "diabetes_model.keras")
        scaler_path = os.path.join(BASE_DIR, "models", "scaler.joblib")
        numerical_cols_path = os.path.join(BASE_DIR, "models", "numerical_cols.joblib")
        feature_columns_path = os.path.join(BASE_DIR, "models", "feature_columns.joblib")
        metadata_path = os.path.join(BASE_DIR, "models", "metadata.json")

        model = keras.models.load_model(model_path)
        scaler = joblib.load(scaler_path)
        numerical_cols = joblib.load(numerical_cols_path)
        feature_columns = joblib.load(feature_columns_path)
        
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
            
        return model, scaler, numerical_cols, feature_columns, metadata
    except FileNotFoundError:
        st.error(f"Model files not found! Looking in: {BASE_DIR}/models/")
        return None, None, None, None, None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None, None, None, None

def predict_diabetes(patient_data, model, scaler, numerical_cols, feature_columns): 
    """Make diabetes prediction"""
    try:
       
        df_sample = pd.DataFrame([patient_data])
        
  
        if "Age" in df_sample.columns:
            age = df_sample["Age"].iloc[0]
            df_sample["Age_group_Middle"] = 1 if 30 <= age < 45 else 0
            df_sample["Age_group_Senior"] = 1 if 45 <= age < 60 else 0
            df_sample["Age_group_Elder"] = 1 if age >= 60 else 0
        

        if "BMI" in df_sample.columns:
            bmi = df_sample["BMI"].iloc[0]
            df_sample["BMI_category_Normal"] = 1 if 18.5 <= bmi < 25 else 0
            df_sample["BMI_category_Overweight"] = 1 if 25 <= bmi < 30 else 0
            df_sample["BMI_category_Obese"] = 1 if bmi >= 30 else 0
        
      
        if {"BMI", "Age"}.issubset(df_sample.columns):
            df_sample["BMI_Age_interaction"] = df_sample["BMI"] * df_sample["Age"]
        
     
        if "Glucose" in df_sample.columns:
            glucose = df_sample["Glucose"].iloc[0]
            df_sample["Glucose_category_Prediabetic"] = 1 if 100 <= glucose < 125 else 0
            df_sample["Glucose_category_Diabetic"] = 1 if glucose >= 125 else 0
        
       
        for col in feature_columns:
            if col not in df_sample.columns:
                df_sample[col] = 0
        
      
        df_sample = df_sample[feature_columns]
        

        df_sample_scaled = df_sample.copy()
        df_sample_scaled[numerical_cols] = scaler.transform(df_sample[numerical_cols])
        
        probability = model.predict(df_sample_scaled, verbose=0).ravel()[0]
        
        return {
            "probability": float(probability),
            "risk_percentage": float(probability * 100),
            "risk_level": "High Risk" if probability >= 0.5 else "Low Risk",
            # "confidence": float(max(probability, 1-probability) * 100),
            "label": int(probability >= 0.5)
        }
        
    except Exception as e:
        return {"error": str(e)}

def create_risk_gauge(probability):
    """Create a risk gauge chart"""
    risk_percentage = probability * 100
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = risk_percentage,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Diabetes Risk"},
        delta = {'reference': 50,  
                 'increasing': {'color': "red"},   # High Risk
                 'decreasing': {'color': "green"}  # Low Risk
                }, # reference point to show how far you are from the risk
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 25], 'color': "lightgreen"},
                {'range': [25, 50], 'color': "yellow"},
                {'range': [50, 75], 'color': "orange"},
                {'range': [75, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(height=300)
    return fig

def create_feature_importance_chart(): # that creats chart in model alalysis
    """Create feature importance visualization"""

    features = ['Glucose', 'BMI', 'Age', 'Pregnancies', 'DiabetesPedigreeFunction', 
               'BloodPressure', 'Insulin', 'SkinThickness']
    importance = [0.35, 0.25, 0.18, 0.10, 0.05, 0.03, 0.02, 0.02]
    
    fig = px.bar(
        x=importance, 
        y=features, 
        orientation='h',
        title="Feature Importance in Diabetes Prediction",
        labels={'x': 'Importance Score', 'y': 'Features'},
        color=importance,
        color_continuous_scale='viridis'
    )
    fig.update_layout(height=400)
    return fig

def main():
  
    st.markdown('<h1 class="main-header">🏥 Diabetes Risk Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>AI-Powered Health Assessment:</strong> Get instant diabetes risk prediction based on your health parameters using advanced machine learning.</div>', unsafe_allow_html=True)
    
 
    model, scaler, numerical_cols, feature_columns, metadata = load_model_components()
    
    if model is None:
        st.stop()
    

    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Choose a page:", 
                           ["🏠 Home & Prediction", "📊 Model Analytics", "ℹ️ About Diabetes"])
    
    if page == "🏠 Home & Prediction":
      
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown('<h2 class="sub-header">Enter Your Health Information</h2>', unsafe_allow_html=True)
            
    
            with st.form("prediction_form"):
       
                st.subheader("👤 Personal Information")
                col1_1, col1_2 = st.columns(2)
                
                with col1_1:
                    age = st.slider("Age (years)", min_value=18, max_value=100, value=30)
                    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
                
                with col1_2:
                    glucose = st.slider("Glucose Level (mg/dL)", min_value=50, max_value=300, value=120)
                    blood_pressure = st.slider("Blood Pressure (mmHg)", min_value=40, max_value=200, value=80)
                
          
                st.subheader("🏃 Health Metrics")
                col2_1, col2_2 = st.columns(2)
                
                with col2_1:
                    bmi = st.slider("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
                    skin_thickness = st.slider("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
                
                with col2_2:
                    insulin = st.slider("Insulin Level (μU/mL)", min_value=0, max_value=900, value=100)
                    diabetes_pedigree = st.slider("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
                
          
                submit_button = st.form_submit_button(label="🔍 Analyze Risk", use_container_width=True)
                
 
            st.subheader("💡 Health Status Overview")
            col3_1, col3_2, col3_3 = st.columns(3)
            
            with col3_1:
                bmi_status = "Normal" if 18.5 <= bmi < 25 else "Overweight" if 25 <= bmi < 30 else "Obese" if bmi >= 30 else "Underweight"
                bmi_color = "green" if bmi_status == "Normal" else "orange" if bmi_status in ["Overweight", "Underweight"] else "red"
                st.metric("BMI Status", bmi_status)
                
            with col3_2:
                glucose_status = "Normal" if glucose < 100 else "Prediabetic" if glucose < 125 else "Diabetic"
                glucose_color = "green" if glucose_status == "Normal" else "orange" if glucose_status == "Prediabetic" else "red"
                st.metric("Glucose Status", glucose_status)
                
            with col3_3:
                bp_status = "Normal" if blood_pressure < 120 else "Elevated" if blood_pressure < 130 else "High"
                bp_color = "green" if bp_status == "Normal" else "orange" if bp_status == "Elevated" else "red"
                st.metric("BP Status", bp_status)
        
        with col2:
            st.markdown('<h2 class="sub-header">Prediction Results</h2>', unsafe_allow_html=True)
            
            if submit_button:
               
                patient_data = {
                    "Pregnancies": pregnancies,
                    "Glucose": glucose,
                    "BloodPressure": blood_pressure,
                    "SkinThickness": skin_thickness,
                    "Insulin": insulin,
                    "BMI": bmi,
                    "DiabetesPedigreeFunction": diabetes_pedigree,
                    "Age": age
                }
                
                with st.spinner("Analyzing your health data..."):
                    result = predict_diabetes(patient_data, model, scaler, numerical_cols, feature_columns)
                
                if "error" not in result:
                    
                    st.plotly_chart(create_risk_gauge(result["probability"]), use_container_width=True)
                
                    risk_class = "risk-high" if result["label"] == 1 else "risk-low"
                    risk_emoji = "⚠️" if result["label"] == 1 else "✅"
                    
                    st.markdown(f'''
                    <div class="{risk_class}">
                        <h3>{risk_emoji} Risk Assessment</h3>
                        <p><strong>Risk Level:</strong> {result["risk_level"]}</p>
                        <p><strong>Risk Probability:</strong> {result["risk_percentage"]:.1f}%</p>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                        # <p><strong>Confidence:</strong> {result["confidence"]:.1f}%</p>
                    
                    st.subheader("📋 Recommendations")
                    if result["label"] == 1:
                        st.error("""
                        **High Risk - Please take action:**
                        - Consult with a healthcare professional immediately
                        - Monitor blood glucose levels regularly
                        - Maintain a healthy diet and regular exercise
                        - Consider lifestyle modifications
                        """)
                    else:
                        st.success("""
                        **Low Risk - Keep up the good work:**
                        - Continue healthy lifestyle choices
                        - Regular health check-ups
                        - Maintain current weight and activity level
                        - Monitor periodically
                        """)
                        
                    
                    if "prediction_history" not in st.session_state:
                        st.session_state.prediction_history = []
                    
                    st.session_state.prediction_history.append({
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "patient_data": patient_data,
                        "result": result
                    })
                    
                else:
                    st.error(f"Error making prediction: {result['error']}")
            else:
                st.info("👆 Fill in your health information and click 'Analyze Risk' to get your diabetes risk assessment.")
        
        
        if hasattr(st.session_state, 'prediction_history') and st.session_state.prediction_history:
            st.markdown("---")
            st.subheader("📈 Prediction History")
            
            history_df = pd.DataFrame([
                {
                    "Date": entry["timestamp"],
                    "Risk Level": entry["result"]["risk_level"],
                    "Risk %": f"{entry['result']['risk_percentage']:.1f}%",
                    "Age": entry["patient_data"]["Age"],
                    "BMI": entry["patient_data"]["BMI"],
                    "Glucose": entry["patient_data"]["Glucose"]
                }
                for entry in st.session_state.prediction_history[-10:]  # Last 10 predictions
            ])
            
            st.dataframe(history_df, use_container_width=True)



    
    elif page == "📊 Model Analytics":
        st.markdown('<h2 class="sub-header">Model Performance & Analytics</h2>', unsafe_allow_html=True)
        
        # Model metadata
        if metadata:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Model Accuracy", f"{metadata['model_metrics']['accuracy']:.3f}")
            with col2:
                st.metric("ROC AUC Score", f"{metadata['model_metrics']['roc_auc']:.3f}")
            with col3:
                st.metric("Model Type", metadata['model_type'].title())
        
        # Feature importance chart
        st.subheader("🎯 Feature Importance")
        st.plotly_chart(create_feature_importance_chart(), use_container_width=True)
        

    
    elif page == "ℹ️ About Diabetes":
        st.markdown('<h2 class="sub-header">Understanding Diabetes</h2>', unsafe_allow_html=True)
        
        # Diabetes information
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### What is Diabetes?
            Diabetes is a chronic condition that affects how your body processes blood glucose (sugar). 
            When you have diabetes, your body either doesn't make enough insulin or can't effectively use the insulin it makes.
            
            ### Types of Diabetes:
            - **Type 1**: Body doesn't produce insulin
            - **Type 2**: Body doesn't use insulin properly
            - **Gestational**: Develops during pregnancy
            
            ### Risk Factors:
            - Age (45 and older)
            - Overweight or obesity
            - Family history
            - Physical inactivity
            - High blood pressure
            - Previous gestational diabetes
            """)
        
        with col2:
            st.markdown("""
            ### Symptoms to Watch:
            - Increased thirst and urination
            - Unexplained weight loss
            - Fatigue and weakness
            - Blurred vision
            - Slow-healing wounds
            - Frequent infections
            
            ### Prevention Tips:
            - Maintain healthy weight
            - Regular physical activity
            - Healthy diet (low sugar, high fiber)
            - Regular health screenings
            - Avoid smoking
            - Limit alcohol consumption
            
            ### When to See a Doctor:
            Consult healthcare professionals if you have risk factors or symptoms.
            """)
        
        # Feature explanations
        st.subheader("🔍 Understanding the Health Metrics")
        
        feature_explanations = {
            "Glucose": "Blood sugar level - Normal: <100 mg/dL, Prediabetic: 100-125 mg/dL, Diabetic: >125 mg/dL",
            "BMI": "Body Mass Index - Normal: 18.5-24.9, Overweight: 25-29.9, Obese: ≥30",
            "Blood Pressure": "Systolic pressure - Normal: <120 mmHg, Elevated: 120-129 mmHg, High: ≥130 mmHg",
            "Insulin": "Hormone that regulates blood sugar - Normal: 2.6-24.9 μU/mL",
            "Age": "Risk increases with age, especially after 45",
            "Pregnancies": "Number of pregnancies - Gestational diabetes increases future risk",
            "Skin Thickness": "Triceps skin fold thickness - Indicates body fat percentage",
            "Diabetes Pedigree Function": "Genetic predisposition based on family history"
        }
        
        for feature, explanation in feature_explanations.items():
            with st.expander(f"📊 {feature}"):
                st.write(explanation)
        
        # Disclaimer
        st.markdown("---")
        # st.markdown("""
        # ### ⚠️ Important Disclaimer
        # This tool is for educational purposes only and should not replace professional medical advice. 
        # The predictions are based on machine learning models and may not be 100% accurate. 
        # Always consult with healthcare professionals for proper diagnosis and treatment.
        # """)

if __name__ == "__main__":
    main()