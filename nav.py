import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")
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
        elif model_option == "Model B":
            st.write("You selected Model B. Here's some information about it.")
        elif model_option == "Model C":
            st.write("You selected Model C. Here's some information about it.")

if __name__ == "__main__":
    st.image(""C:\Users\Nikhil\Downloads\pngwing.com.png"", use_column_width=True)
    col1, col2 = st.beta_columns([1, 3])
    with col1:
        st.write("")
    with col2:
        st.title("NTT DATA")
    main()
