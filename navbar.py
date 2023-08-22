import streamlit as st
import pandas as pd

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" style="height: 95px;">
   <a class="navbar-brand" href="#" style="margin-top: 40px;">
    <img src="data:image/png;base64,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`````````````````````````````````````````````````````````````````````````````0xdL3s6fLnNWAAH8PE9BorJz/nTwAAAABJRU5ErkJggg==" width="30" height="30" class="d-inline-block align-top" alt="">
    NTT Data
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav" style="margin-top:30px;">      
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown('''# **Binance Price App**
A simple cryptocurrency price app pulling price data from *Binance API*.
''')

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
