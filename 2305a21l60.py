import streamlit as st
import math as m

st.markdown('<h1>2305A21L60-PS7 O.C.T.E.C</h1>', unsafe_allow_html=True)
st.markdown('## INPUT PARAMETERS:')
st.markdown('---')

# Create a form for input
with st.form(key='input_form'):
    col1, col2 = st.columns(2)

    with col1:
        V0 = st.number_input('V0(V)', min_value=0.0) 
        I0 = st.number_input('I0(A)', min_value=0.0)  
        W0 = st.number_input('W0(W)', min_value=0.0)  

    
    submitted = st.form_submit_button('Submit')


if submitted:
    with col2:
        if V0 == 0 and I0 == 0:
            st.write('Invalid inputs: V0 and I0 cannot both be zero.')
        else:
            st.markdown('## OUTPUT PARAMETERS:')
            st.markdown('---')
            cos0 = W0 / (V0 * I0) if V0 * I0 != 0 else 0
            sin0 = m.sqrt(1 - cos0**2) if cos0 < 1 else 0 
            Iw = I0 * cos0
            Iu = I0 * sin0
        
       
        if Iw != 0:
            R0 = V0 / Iw
            st.write('Open circuit Resistance:', R0, 'ohm')
        else:
            st.write('Open circuit Resistance: Undefined (Iw is zero)')
        
        if Iu != 0:
            X0 = V0 / Iu
            st.write('Open circuit Reactance:', X0, 'ohm')
        else:
            st.write('Open circuit Reactance: Undefined (Iu is zero)')