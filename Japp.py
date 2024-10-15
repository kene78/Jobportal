import random
import streamlit as st

# Industries and example job titles
industries = {
    "Information Technology": ["Software Developer", "Data Scientist", "Network Engineer", "IT Support"],
    "Healthcare": ["Nurse", "Doctor", "Pharmacist", "Healthcare Assistant"],
    "Education": ["Teacher", "Professor", "Librarian", "Tutor"],
    "Finance": ["Accountant", "Financial Analyst", "Bank Teller", "Investment Banker"],
    "Marketing": ["Marketing Manager", "SEO Specialist", "Content Creator", "Brand Strategist"],
    "Construction": ["Civil Engineer", "Architect", "Construction Worker", "Surveyor"],
    "Retail": ["Store Manager", "Cashier", "Merchandiser", "Sales Assistant"],
    "Legal": ["Lawyer", "Paralegal", "Legal Assistant", "Compliance Officer"],
    "Hospitality": ["Chef", "Hotel Manager", "Waiter", "Event Planner"],
    "Manufacturing": ["Production Manager", "Quality Control", "Assembly Line Worker", "Machine Operator"],
}

# List of degrees and experience levels
degrees = ["High School", "Diploma", "Bachelor's", "Master's", "PhD"]
locations = ["Cape Town", "Johannesburg", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein"]
companies = ["Company A", "Company B", "Company C", "Company D", "Company E", "Company F"]

# Function to generate mock jobs
def generate_mock_jobs(num_jobs=1000):
    jobs = []
    
    for _ in range(num_jobs):
        # Randomly choose an industry and a job title from that industry
        industry = random.choice(list(industries.keys()))
        job_title = random.choice(industries[industry])
        
        # Randomly choose a degree, experience level, and other job attributes
        degree_required = random.choice(degrees)
        experience_required = random.randint(0, 15)  # Experience range from 0 to 15 years
        location = random.choice(locations)
        company = random.choice(companies)
        
        # Create the job dictionary
        job = {
            "title": job_title,
            "company": company,
            "industry": industry,
            "degree_required": degree_required,
            "experience_required": experience_required,
            "location": location
        }
        
        # Add the job to the list of jobs
        jobs.append(job)
    
    return jobs

# Generate 1000 mock jobs
mock_jobs = generate_mock_jobs()

# Function to display the mock jobs in Streamlit
def job_listing_page(mock_jobs, degree, experience_years):
    st.header("Available Jobs Matching Your Profile")

    # Filter job listings based on degree and experience
    matching_jobs = [job for job in mock_jobs if job['degree_required'] == degree and experience_years >= job['experience_required']]
    
    if matching_jobs:
        for idx, job in enumerate(matching_jobs[:50]):  # Show top 50 jobs to avoid overload
            st.subheader(f"{job['title']} at {job['company']} ({job['industry']})")
            st.text(f"Location: {job['location']}")
            st.text(f"Degree Required: {job['degree_required']}")
            st.text(f"Experience Required: {job['experience_required']} years")
            if st.button(f"Apply to {job['title']}", key=idx):
                st.success(f"Applied to {job['title']} successfully!")
    else:
        st.info("No jobs matching your profile were found.")

# Page 1: Collect personal information
def personal_info_form():
    st.header("Job Application Portal")
    
    # Collect personal and education details
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    degree = st.selectbox("Academic Degree", degrees)
    experience_years = st.slider("Years of Experience", 0, 30)
    
    if st.button("Submit"):
        st.session_state['degree'] = degree
        st.session_state['experience_years'] = experience_years
        st.success("Information submitted successfully!")
    else:
        return None, None

# Main App Logic
def main():
    st.sidebar.title("Navigation")
    pages = ["Personal Information", "Available Jobs"]
    choice = st.sidebar.selectbox("Go to", pages)
    
    if choice == "Personal Information":
        personal_info_form()
    elif choice == "Available Jobs":
        if 'degree' in st.session_state and 'experience_years' in st.session_state:
            job_listing_page(mock_jobs, st.session_state['degree'], st.session_state['experience_years'])
        else:
            st.warning("Please fill out the Personal Information form first.")

# Initialize session state variables if they don't exist
if __name__ == "__main__":
    if 'degree' not in st.session_state:
        st.session_state['degree'] = None
    if 'experience_years' not in st.session_state:
        st.session_state['experience_years'] = None
    
    main()

