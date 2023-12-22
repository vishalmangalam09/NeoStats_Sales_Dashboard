import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Neostats sales Prospect", page_icon=":chart_with_upwards_trend:",layout="wide")

st.sidebar.image("neostats.jpg", caption="NeoStats Analytics Solutions PVT LTD")

st.subheader("Neostats Sales Prospect")
st.markdown('',unsafe_allow_html=False)


df = pd.read_csv("Sales_Prospect.csv")



# Sidebar layout
st.sidebar.title("Filter Data")

col1, col2 ,col3 , col4 = st.columns((4))

with col1:
# Create for Industry
    Industry = st.sidebar.multiselect("Industry", df["Industry"].unique())
if not Industry:
    df2 = df.copy()
else:
    df2 = df[df["Industry"].isin(Industry)]

with col2:
# Create for Organization
    Organization = st.sidebar.multiselect("Organization", df2["Organization"].unique())
if not Organization:
      df3 = df2.copy()
else:
    df3 = df2[df2["Organization"].isin(Organization)]


with col3:
# Create for Location
    Location = st.sidebar.multiselect("Location", df3["Location"].unique())
if not Location:
      df4 = df3.copy()
else:
    df4 = df3[df3["Location"].isin(Location)]


with col4:
# Create for Owner
    Owner = st.sidebar.multiselect("Owner ", df4["Owner "].unique())
if not Owner :
      df5 = df4.copy()
else:
    df5 = df4[df4["Owner "].isin(Owner )]




if not Industry and not Organization and not Location and not Owner :
    filtered_df = df
elif not Organization and not Location and not Owner :
    filtered_df = df[df["Industry"].isin(Industry)]
elif not Industry and not Location and not Owner :
    filtered_df = df2[df2["Organization"].isin(Organization)]
elif not Industry and not Organization and not Owner :
    filtered_df = df3[df3["Location"].isin(Location)]
elif not Industry and not Organization and not Location:
    filtered_df = df4[df4["Owner "].isin(Owner )]
elif Industry and Organization and Location:
    filtered_df = df5[
        df["Industry"].isin(Industry)
        & df2["Organization"].isin(Organization)
        & df3["Location"].isin(Location)
    ]
elif Industry and Location and Owner :
    filtered_df = df5[
        df["Industry"].isin(Industry)
        & df3["Location"].isin(Location)
        & df4["Owner "].isin(Owner )
    ]
elif Industry and Organization and Owner :
    filtered_df = df5[
        df["Industry"].isin(Industry)
        & df2["Organization"].isin(Organization)
        & df4["Owner "].isin(Owner )
    ]
elif Organization and Location and Owner :
    filtered_df = df5[
        df2["Organization"].isin(Organization)
        & df3["Location"].isin(Location)
        & df4["Owner "].isin(Owner )
    ]
elif Industry and Organization:
    filtered_df = df5[
        df["Industry"].isin(Industry) & df2["Organization"].isin(Organization)
    ]
elif Industry and Location:
    filtered_df = df5[df["Industry"].isin(Industry) & df3["Location"].isin(Location)]
elif Industry and Owner :
    filtered_df = df5[df["Industry"].isin(Industry) & df4["Owner"].isin(Owner )]
elif Organization and Location:
    filtered_df = df5[
        df2["Organization"].isin(Organization) & df3["Location"].isin(Location)
    ]
elif Organization and Owner :
    filtered_df = df5[
        df2["Organization"].isin(Organization) & df4["Owner "].isin(Owner )
    ]
elif Location and Owner :
    filtered_df = df5[df3["Location"].isin(Location) & df4["Owner "].isin(Owner )]
else:
    filtered_df = df5[
        df["Industry"].isin(Industry)
        & df3["Location"].isin(Location)
        & df4["Owner "].isin(Owner )
    ]



col1, col2, col3= st.columns((1,1,2))

with col1:
    total_organizations = filtered_df['Organization'].nunique()
    st.markdown(f"<p style='font-size: small; font-weight: bold;'>Total Number of Organizations:</p>", unsafe_allow_html=True)
    st.info(f"{total_organizations}")



with col2:
    total_Prospect_Name = filtered_df['Prospect_Name'].nunique()
    st.markdown(f"<p style='font-size: small; font-weight: bold;'>Total Number of Prospects:</p>", unsafe_allow_html=True)
    st.info(f"{total_Prospect_Name}")


with col3:

    st.markdown(f"<p style='font-size: small; font-weight: bold;'>Interest Count:</p>", unsafe_allow_html=True)

    # Count the occurrences and create a table
    Interest_level_counts = pd.crosstab(index=filtered_df['Interest_Level'], columns='count')
    Interest_level_transposed_counts = Interest_level_counts.transpose()

    # Specify the desired order of Interest_Level categories
    interest_order = ['High', 'Medium', 'Low']
    Interest_level_transposed_counts_sorted = Interest_level_transposed_counts.reindex(columns=interest_order, fill_value=0)



    Interest_Level = st.sidebar.multiselect("Interest Level", df5["Interest_Level"].unique())
    if not Interest_Level:
      df6 = df5.copy()
    else:
      df6 = df5[df5["Interest_Level"].isin(Interest_Level)]    

    st.markdown(Interest_level_transposed_counts_sorted.to_markdown(index=False), unsafe_allow_html=True)


filtered_df = df6


col1, col2 = st.columns((5,1))

with col1:
    st.markdown(f"<p style='font-size: small; font-weight: bold;'>Status Count:</p>", unsafe_allow_html=True)

    # Count the occurrences and create a table
    Status_counts = pd.crosstab(index=filtered_df['Status'], columns='count')
    Status_transposed_counts = Status_counts.transpose()

    # Specify the desired order of Status categories
    Status_order = ['New Lead', 'Active Discussions', 'Closed (Won)', 'Qualified', 'Proposal', 'On Hold', 'Not Responding', 'Not Applicable', 'Closed (Lost)']
    Status_transposed_counts_sorted = Status_transposed_counts.reindex(columns=Status_order, fill_value=0)

    # Display the Status Count table
    st.markdown(f"<p style='font-size: small; font-weight: bold;'>Status Count:</p>", unsafe_allow_html=True)
    st.markdown(Status_transposed_counts_sorted.to_markdown(index=False), unsafe_allow_html=True)

# Sidebar filter for Status
    Status = st.sidebar.multiselect("Status", df6["Status"].unique())

# Apply the filter to the DataFrame
    if not Status:
       df7 = df6.copy()
    else:
       df7 = df6[df6["Status"].isin(Status)]


 

import streamlit as st

# Assuming filtered_df is already defined

st.subheader(":point_right: Sales Summary")
with st.expander("Summary_Table"):
    df_sample = filtered_df

    # Display the DataFrame using st.dataframe with horizontal scrolling
    st.dataframe(df_sample, height=400, width=1200)


#form
st.subheader(":point_right: Add new Entry")
option_form = st.form("Option Form")

# Create three columns inside the form
col1, col2, col3 = option_form.columns(3)

# First Column
with col1:
    Prospect_ID = st.text_input("Prospect_ID")
    Industry = st.text_input("Industry")
    Location = st.text_input("Location")
    Organization = st.text_input("Organization")
    Notes  = st.text_input("Notes ")
    Owner = st.selectbox("Owner", {"","Gino", "Sachin", "Felci", "Jestna", "Arjun"})

# Second Column
with col2:
    Source_of_Lead = st.selectbox("Source of Lead", {"","Self", "Employee", "Partner", "Event", "Client Initiated"})
    Contacted = st.selectbox("Contacted", {"","Yes", "No"})
    Prospect_Name = st.text_input("Prospect Name")
    Prospect_Title = st.text_input("Prospect Title")
    Prospect_Phone = st.text_input("Prospect Phone")
    Prospect_Email = st.text_input("Prospect Email")
    Decision_Rights = st.selectbox("Decision Right", {"","Decision Maker", "Influencer", "Passive", "Junior", "Not Applicable"})

# Third Column
with col3:
    Responded = st.selectbox("Responded", {"","Yes", "No"})
    Interest_Level = st.selectbox("Interest Level", {'','High', 'Medium', 'Low'})
    Status = st.selectbox("Status", {'','New Lead​', 'Active Discussions​', 'Closed (Won)​', 'Qualified​', 'Proposal​', 'On Hold​', 'Not Responding​', 'Not Applicable​', 'Closed (Lost)​'})
    Follow_Up = st.selectbox("Follow Up", {"","Yes", "No"})
    Follow_Up_Date = st.text_input("Follow up date")
    Pain_Points = st.text_input("Pain Point")
    add_data = option_form.form_submit_button(label="Add new Record")

# Process the form submission if the button is clicked
if add_data and len(Prospect_Phone) >= 10 and Prospect_Phone.isdigit():
    # Process the form data here
    st.success("New record added successfully!")



#when Button is clicked
if add_data:
  if Prospect_ID !="":
   df=pd.concat([df,pd.DataFrame.from_records([{
      'Prospect_ID':Prospect_ID,
      'Industry':Industry,
      'Location':Location,
      'Organization':Organization,
      'Notes ':Notes ,
      'Owner ':Owner ,
      'Source_of_Lead':Source_of_Lead,
      'Contacted':Contacted,
      'Prospect_Name':Prospect_Name,
      'Prospect_Title':Prospect_Title,
      'Prospect_Phone':Prospect_Phone,
      'Prospect_Email':Prospect_Email,
      'Decision_Rights':Decision_Rights,
      'Responded':Responded,
      'Interest_Level':Interest_Level,
      'Status':Status,
      'Follow_Up':Follow_Up,
      'Follow_Up_Date':Follow_Up_Date,
      'Pain_Points':Pain_Points}])])
   df.to_csv("Sales_Prospect.csv",index=False)
  else:
    st.error("Propect id Required")
  if len(Prospect_Phone) < 10 or not Prospect_Phone.isdigit():
        st.warning("Please add a valid phone number with at least 10 digits.")
  if '@' not in Prospect_Email:
        st.warning("Please enter a valid email ID.")
  if Industry=="":
        st.warning("Please enter Industry")
  if Location=="":
        st.warning("Please enter Location")
  if Organization=="":
        st.warning("Please enter Organization")
  if Owner =="":
        st.warning("Please enter Owner ")
  if Source_of_Lead=="":
        st.warning("Please enter Source of Lead ")
  if Contacted=="":
        st.warning("Please enter Contacted ")
  if Prospect_Name=="":
        st.warning("Please enter Prospect Name")
  if Decision_Rights=="":
        st.warning("Please enter Decision Right")
  if Responded=="":
        st.warning("Please enter Responded")
  if Interest_Level=="":
        st.warning("Please enter Interest Level")
  if Responded=="":
        st.warning("Please enter Responded")
  if Status=="":
        st.warning("Please enter Status")
  if Follow_Up=="":
        st.warning("Please enter Follow Up")
  st.experimental_rerun()
