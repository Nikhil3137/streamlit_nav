import streamlit as st

# Define CSS styles for the navigation bar
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        padding: 1rem;
        background-color: #333;
    }
    .nav-button {
        margin: 0 10px;
        color: white;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Multi-Page Streamlit App")

    navigation_options = ["Home", "Results", "Analysis", "Examples"]

    # Create a horizontal navigation bar using CSS styles
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    for option in navigation_options:
        if st.button(option, class_="nav-button"):
            selected_navigation = option
    st.markdown('</div>', unsafe_allow_html=True)

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
