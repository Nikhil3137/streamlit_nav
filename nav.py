import streamlit as st

def main():
    st.title("Custom UI Streamlit App")
    
    # Apply custom CSS styles to the Streamlit app
    st.markdown(
        """
        <style>
            /* Set custom font for the whole app */
            body {
                font-family: 'Arial', sans-serif;
            }
            /* Style the title */
            .title-container {
                text-align: center;
                padding: 20px;
                background-color: #333;
                color: #fff;
                border-bottom: 3px solid #555;
            }
            /* Style the sidebar */
            .sidebar .sidebar-content {
                background-color: #555;
                color: #fff;
            }
            /* Style the sidebar header */
            .sidebar .header {
                font-family: 'Georgia', serif;
                color: #f0f0f0;
                padding-top: 20px;
                padding-bottom: 10px;
            }
            /* Style the model dropdown */
            .sidebar .selectbox select {
                font-family: 'Verdana', sans-serif;
                background-color: #f4f4f4;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                color: #333;
                width: 100%;
            }
            /* Style the navigation links */
            .sidebar .stRadio {
                margin-top: 15px;
                margin-left: 10px;
            }
            /* Style the main content */
            .main-container {
                padding: 20px;
            }
            /* Style the custom footer */
            .footer {
                text-align: center;
                padding: 10px;
                background-color: #333;
                color: #fff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title container
    st.markdown('<div class="title-container"><h1>Custom UI Streamlit App</h1></div>', unsafe_allow_html=True)
    
    # Sidebar navigation
    navigation = st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Models"])
    
    # Main content
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
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
        st.markdown('<div class="header">Model List</div>', unsafe_allow_html=True)
        
        # Create a container for the selectbox
        model_container = st.container()
        
        # Place the selectbox in the container
        with model_container:
            model_option = st.selectbox("Select a model", ["Model A", "Model B", "Model C"], key="model_select")

        if model_option == "Model A":
            st.write("You selected Model A. Here's some information about it.")
            st.write("For more details, visit the [Model A Page](https://yourdomain.com/model_a)")

        elif model_option == "Model B":
            st.write("You selected Model B. Here's some information about it.")
            st.write("For more details, visit the [Model B Page](https://yourdomain.com/model_b)")

        elif model_option == "Model C":
            st.write("You selected Model C. Here's some information about it.")
            st.write("For more details, visit the [Model C Page](https://yourdomain.com/model_c)")
    
    # Close main content container
    st.markdown('</div>', unsafe_allow_html=True)

    # Custom footer
    st.markdown('<div class="footer">Contact Us: contact@example.com | Learn more about us at [About Us](https://yourdomain.com/about_us)</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
