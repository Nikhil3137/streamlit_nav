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
            }
            /* Change font style for the sidebar header */
            .sidebar .header {
                font-family: 'Georgia', serif;
            }
            /* Change font style for the model dropdown */
            .sidebar .selectbox select {
                font-family: 'Verdana', sans-serif;
                background-color: #f4f4f4;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                color: #333;
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
