import streamlit as st

def main():
    st.title("NTT DATA")
    
    # Create a horizontal layout for the radio buttons
    radio_container = st.container()
    
    # Place the radio buttons in the horizontal layout
    with radio_container:
        col1, col2, col3, col4 = st.columns(4)
        navigation = col1.radio("Navigation", ["Home", "Results", "Analysis", "Models"])

    if navigation == "Home":
        st.header("Home")
        st.write("This is the home page.")

    elif navigation == "Results":
        st.header("Results List")
        for item in range(10):
            st.write(f"Result {item}")

    elif navigation == "Analysis":
        st.header("Analysis")
        x, y = st.number_input("Input X"), st.number_input("Input Y")
        result = x + y
        st.write(f"Result: {result}")

    elif navigation == "Models":
        st.header("Model List")
        model_option = st.selectbox("Select an example", ["Model A", "Model B", "Model C"])
        
        if model_option == "Model A":
            st.write("You selected Model A. Here's some information about it.")
            st.write("For more details, visit the [Model A Page](https://yourdomain.com/model_a)")

        elif model_option == "Model B":
            st.write("You selected Model B. Here's some information about it.")
            st.write("For more details, visit the [Model B Page](https://yourdomain.com/model_b)")

        elif model_option == "Model C":
            st.write("You selected Model C. Here's some information about it.")
            st.write("For more details, visit the [Model C Page](https://yourdomain.com/model_c)")

if __name__ == "__main__":
    main()

# Use HTML and CSS to create a custom footer
custom_footer = """
<div style="background-color: #f4f4f4; padding: 10px; text-align: center;">
    <p>Contact Us: <a href="mailto:contact@example.com">contact@example.com</a></p>
    <p><a href="https://yourdomain.com/about_us">Learn more about us</a></p>
</div>
"""
st.markdown(custom_footer, unsafe_allow_html=True)
