import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
def predict_disease(HNR, NHR, JitterDDP):
    input=np.array([[HNR, NHR, JitterDDP]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("PARKINSONS WEB APPLICATION")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">PARKINSONS DISEASE PREDICTION</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    HNR= st.text_input("HNR","Type Here")
    NHR = st.text_input("NHR","Type Here")
    JitterDDP = st.text_input("Jitter:DDP","Type Here")
    safe_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:white;text-align:center;">  You Have Disease</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:black ;text-align:center;">  You Don't Have Disease</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_disease(HNR, NHR, JitterDDP)
        st.success('The Accuracy of getting Disease is: {}'.format(output))

        if output < 0.90:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()