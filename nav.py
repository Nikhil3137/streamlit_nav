import streamlit as st

# Define the navigation bar style
st.markdown(
    """
    <style>
    .navbar {
        background-color: #343a40;
        padding: 10px 0;
    }
    .navbar-brand {
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    .nav-item {
        padding: 0 15px;
    }
    .nav-link {
        color: white;
        font-size: 18px;
    }
    </style>
    """
, unsafe_allow_html=True)

# Create the navigation bar
st.markdown(
    """
    <nav class="navbar">
        <div class="container">
            <a class="navbar-brand" href="#">NTT Data</a>
            <ul class="nav">
                <li class="nav-item">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item dropdown">
                    <span class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Dropdown
                    </span>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
    """
, unsafe_allow_html=True)

# Main content
st.title("NTT DATA")
st.write("A simple cryptocurrency price app pulling price data from Binance API.")
