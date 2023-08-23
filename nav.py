import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")
    
    # Apply custom CSS styles to the Streamlit app
    st.markdown(
        """
        <style>
            /* Change font style for the whole app */
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
            /* Change background color of the header */
            .header {
                background-color: #007BFF;
                color: white;
                padding: 20px;
                text-align: center;
                font-size: 24px;
            }
            /* Change background color of the sidebar */
            .sidebar .sidebar-content {
                background-color: #333;
                color: white;
                padding: 20px;
            }
            /* Change style of the radio buttons in the sidebar */
            .sidebar .stRadio > label > div {
                background-color: transparent;
                border: 2px solid white;
                color: white;
                padding: 10px 20px;
                margin-bottom: 10px;
                cursor: pointer;
                transition: background-color 0.3s, border-color 0.3s, color 0.3s;
            }
            .sidebar .stRadio > label > div:hover {
                background-color: white;
                color: #333;
                border-color: #333;
            }
            /* Change style of the model dropdown */
            .sidebar .stSelectbox select {
                font-family: 'Verdana', sans-serif;
                background-color: #333; /* Change the background color */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                color: white; /* Change the font color */
                width: 100%;
            }
            /* Change style of dropdown options */
            .stSelectbox option {
                background-color: #333; /* Change the background color of options */
                color: white; /* Change the font color of options */
                border: none;
                padding: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar navigation
    navigation = st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Models"])

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
        st.sidebar.header("Model List")
        
        # Create a container for the selectbox
        model_container = st.sidebar.container()
        
        # Apply custom CSS style to the model container
        model_container.markdown(
            """
            <style>
                /* Change background color of the model container */
                .widget.stContainer {
                    background-color: #444;
                    padding: 10px;
                    border-radius: 5px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
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

    # Custom footer
    st.markdown("---")
    st.markdown("Contact Us: contact@example.com | Learn more about us at [About Us](https://yourdomain.com/about_us)")

if __name__ == "__main__":
    main()
