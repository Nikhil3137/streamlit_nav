import streamlit as st

def main():
    navigation_options = ["Home", "Results", "Analysis", "Examples"]
    selected_navigation = st.selectbox("Navigation", navigation_options)

    # Custom CSS
    st.markdown("""
    <style>
        .navigation-bar {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            background-color: #333;
            color: white;
        }
        .navigation-bar a {
            text-decoration: none;
            color: white;
            margin-right: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Multi-Page Streamlit App")

    # Custom HTML for navigation bar
    st.markdown('<div class="navigation-bar">' + ''.join(f'<a href="#">{option}</a>' for option in navigation_options) + '</div>', unsafe_allow_html=True)

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
