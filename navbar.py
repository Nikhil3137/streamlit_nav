import streamlit as st

def main():
    st.title("Multi-Page Streamlit App")

    # Add a navigation dropdown using HTML and Bootstrap
    st.markdown('''
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Examples
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a class="dropdown-item" href="/example1">Example 1</a>
              <a class="dropdown-item" href="/example2">Example 2</a>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    ''', unsafe_allow_html=True)

    navigation = st.sidebar.radio("Navigation", ["Home", "Results", "Analysis"])

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

if __name__ == "__main__":
    main()
