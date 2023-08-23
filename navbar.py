import streamlit as st

def main():
    navigation_options = ["Home", "Analysis", "Examples"]
    selected_navigation = st.radio("Navigation", navigation_options)

    navigation_bar = """
    <style>
    .navigation-bar {
        display: flex;
        justify-content: space-around;
        background-color: #333;
        padding: 10px;
        color: white;
    }
    .nav-link {
        text-decoration: none;
        color: white;
    }
    </style>
    <div class="navigation-bar">
        <a class="nav-link" href="?p=home">Home</a>
        <a class="nav-link" href="?p=analysis">Analysis</a>
        <a class="nav-link" href="?p=examples">Examples</a>
    </div>
    """

    st.markdown(navigation_bar, unsafe_allow_html=True)

    st.title("Multi-Page Streamlit App")

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
