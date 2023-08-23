import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")

    # Navigation bar using HTML and Bootstrap styles
    navbar = """
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">App Logo</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#results">Results</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#analysis">Analysis</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="examplesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Examples
                    </a>
                    <div class="dropdown-menu" aria-labelledby="examplesDropdown">
                        <a class="dropdown-item" href="#example1">Example 1</a>
                        <a class="dropdown-item" href="#example2">Example 2</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
    """

    st.markdown(navbar, unsafe_allow_html=True)

    # Content based on navigation
    if st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Examples"]) == "Home":
        st.header("Home")
        st.write("This is the home page.")

    elif st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Examples"]) == "Results":
        st.header("Results List")
        for item in range(25):
            st.write(f"Result {item}", key=f"result_{item}")

    elif st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Examples"]) == "Analysis":
        st.header("Analysis")
        x, y = st.number_input("Input X"), st.number_input("Input Y")
        result = x + y
        st.write(f"Result: {result}")

    elif st.sidebar.radio("Navigation", ["Home", "Results", "Analysis", "Examples"]) == "Examples":
        st.header("Examples Menu")
        example_selection = st.selectbox("Select an example", ["Example 1", "Example 2"])
        if example_selection == "Example 1":
            st.write("This is Example 1.")
        elif example_selection == "Example 2":
            st.write("This is Example 2.")

if __name__ == "__main__":
    main()
