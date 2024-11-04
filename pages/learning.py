import streamlit as st

def show():
    st.markdown('<div class="title">Learning Content</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Explore the weekly breakdown of learning modules, assignments, and additional resources in this course.</div>', unsafe_allow_html=True)

    # Week 1
    with st.expander("Week 1: Introduction to Coding"):
        st.markdown("""
        **Learning Objectives**: Introduce foundational coding concepts, setting up Python, and using Google Colab.
        
        ### Content
        - **Video**: *Week 1 Presentation: Learning Python with Hawkar* – Introduction to Python basics.
        - **Page**: *What is in the Python Script?* – Explanation of Python script components.
        - **Page**: *Introduction to Python Libraries* – Overview of essential Python libraries and how they enhance coding efficiency.
        - **Page**: *Getting Started with Coding in Google Colab* – Guide on setting up and coding in Google Colab.
        - **Page**: *Accessing Google Sheets Data in Google Colab* – Demonstration of data access from Google Sheets.

        ### Assignments
        - **Assignment**: *Week 1 – Mapping Coordinates* – Write a script to plot geographic coordinates and calculate distances.
        - **Assignment**: *Analyzing Real-Time Earthquake Data* – Using APIs to gather and visualize earthquake data.

        ### One-on-One Session
        - **Session**: *Introduction to Python - One-on-One Session* – Live session to cover Week 1 basics and individual questions.

        ### Additional Resources
        - **Page**: *Automate Your Tasks with Google Apps Script* – Introduction to Apps Script for task automation.
        - **Page**: *Top 10 Powerful ChatGPT Prompts for Google Apps Script* – Prompt suggestions for automation.
        - **Discussion**: *Do you have any preferences for the next lecture?* – Opportunity to request specific topics or focus areas.
        """)

    # Week 2
    with st.expander("Week 2: Generate Comprehensive Codings"):
        st.markdown("""
        **Learning Objectives**: Build multi-functional scripts, integrate automation, and work with spatial data in Google Earth Engine.
        
        ### Content
        - **Video**: *Presentation 2 One-on-One Session* – Deeper exploration of Week 2 topics.
        - **Page**: *Merging and Reversing Scripts: Essential Skills for Python* – Guidance on combining and breaking down scripts.
        - **Page**: *The Importance of Google Apps Script* – Why Google Apps Script is valuable for automation and workflows.
        - **Page**: *Understanding Google Earth Engine for Spatial Data Access* – Introduction to using Google Earth Engine for data retrieval.

        ### Assignments
        - **Assignment**: *Image Analysis and Rectangle Detection in Python* – Image analysis project focusing on identifying and analyzing rectangles.
        - **Assignment**: *Urban Analysis with Geospatial Data in Python* – Analyzing urban data with Python.

        ### Additional Resources
        - **Page**: *About Google Earth Engine* – Overview of Earth Engine capabilities.
        - **Page**: *Top 10 Essential Prompts for Accessing Data in Google Earth Engine* – Key prompts for using Earth Engine.
        - **Page**: *Create Google Form by One Click* – Guide to automating Google Forms.
        - **Page**: *Introduction to Using GitHub* – Basics of GitHub for project management.
        - **Discussion**: *Week Discussion: Multi-Function Python Scripts, App Script, and Earth Engine* – Open discussion on combining Python, Apps Script, and Earth Engine.
        """)

    # Week 3
    with st.expander("Week 3: Deploy App through GitHub and Streamlit"):
        st.markdown("""
        **Learning Objectives**: Set up a project for deployment, use GitHub for version control, and create interactive applications with Streamlit.
        
        ### Content
        - **Page**: *Building Interactive Data Apps with GitHub & Streamlit* – How to create and deploy data applications.
        - **Page**: *Do You Know You Can Do a Lot with Streamlit?* – Exploring the capabilities of Streamlit for interactive apps.
        - **Page**: *Top 10 Prompt Engineering Techniques for ChatGPT to Optimize GitHub Scripting* – Using ChatGPT prompts for efficient coding.
        - **Survey**: *Pre-Class 4 Survey: Project Requirements and Checklist* – Gather information on your project’s scope and needs.

        ### Assignments
        - **Assignment**: *Building an Interactive Urban Analysis Dashboard Using Streamlit* – Develop a Streamlit dashboard for visualizing urban analysis data.

        ### Discussion
        - **Discussion**: *GitHub & Streamlit: How Are You Using Them to Elevate Your Project?* – Share experiences on GitHub and Streamlit.
        """)

    # Week 4
    with st.expander("Week 4: Draft Submission of Your Personalized Project"):
        st.markdown("""
        **Learning Objectives**: Develop a personalized project based on skills learned, draft submission for feedback.
        
        ### Content
        - **Page**: *Your Personalized Project* – Guidelines for creating and customizing a project.

        ### Assignment
        - **Assignment**: *Submission of Draft Version for Your Personalized Project* – Submit your draft project for review and feedback.
        """)

    # Week 5
    with st.expander("Week 5: Finalizing and Showcasing Your Personalized Project"):
        st.markdown("""
        **Learning Objectives**: Complete the final version of the personalized project, create a portfolio, and prepare a coding portfolio.
        
        ### Content
        - **Page**: *Finalizing and Showcasing Your Personalized Project* – Steps for finalizing and presenting your project.

        ### Assignment
        - **Assignment**: *Final Project Submission and Portfolio Creation* – Submit the finalized project and develop a portfolio page to showcase work.
        """)
