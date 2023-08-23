import streamlit as st

def main():
    navigation_options = ["Home", "Results", "Analysis", "Examples"]
    selected_navigation = st.selectbox("Navigation", navigation_options)

    st.title("Multi-Page Streamlit App")

    st.markdown("""
    <style>
    .navigation-bar {
        display: flex;
        justify-content: space-around;
        background-color: #333;
        padding: 10px;
        color: white;
    }
    .navigation-link {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .navigation-link:hover {
        color: #66ccff;
    }
    </style>
    """, unsafe_allow_html=True)

    st.write(f"""
    <div class="navigation-bar">
        <a class="navigation-link" href="?p=Home">Home</a>
        <a class="navigation-link" href="?p=Results">Results</a>
        <a class="navigation-link" href="?p=Analysis">Analysis</a>
        <a class="navigation-link" href="?p=Examples">Examples</a>
    </div>
    """)

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
