import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")

    navigation_options = ["Home", "Results", "Analysis", "Examples"]
    selected_navigation = st.radio("Navigation", navigation_options, index=0, format_func=lambda x: "")

    st.write(" | ".join(navigation_options))  # Display navigation horizontally

    if selected_navigation == "Home":
        st.header("Home")
        st.write("This is the home page.")

    elif selected_navigation == "Results":
        st.header("Results List")
        for item in range(25):
            st.write(f"Result {item}")

    elif selected_navigation == "Analysis":
        st.header("Analysis")
        x, y = st.number_input("Input X"), st.number_input("Input Y")
        result = x + y
        st.write(f"Result: {result}")

    elif selected_navigation == "Examples":
        st.header("Examples Menu")
        st.write("Select an example.")

if __name__ == "__main__":
    main()
