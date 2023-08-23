def main():
    st.title("NTT DATA")
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

    # Use st.markdown to create a custom footer

    st.markdown("Contact Us: contact@example.com | Learn more about us at [About Us](https://yourdomain.com/about_us)")

if __name__ == "__main__":
    main()    
