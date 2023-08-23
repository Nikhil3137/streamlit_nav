import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")
    navigation = st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Examples"])

    if navigation == "Home":
        st.header("Home")
        st.write("This is the home page.")

    elif navigation == "Results":
        st.header("Results List")
        for item in range(25):
            st.write(f"Result {item}")

    elif navigation == "Analysis":
        st.header("Analysis")
        x, y = st.number_input("Input X"), st.number_input("Input Y")
        result = x + y
        st.write(f"Result: {result}")

    elif navigation == "Examples":
        st.header("Examples Menu")
        st.write("Select an example.")

if __name__ == "__main__":
    main()
