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

        # Dropdown menu using HTML, CSS, and Bootstrap
        st.markdown('''
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" id="examplesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Select an example
          </button>
          <div class="dropdown-menu" aria-labelledby="examplesDropdown">
            <a class="dropdown-item" href="#">Example 1</a>
            <a class="dropdown-item" href="#">Example 2</a>
            <a class="dropdown-item" href="#">Example 3</a>
          </div>
        </div>
        ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
