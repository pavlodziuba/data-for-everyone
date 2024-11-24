import requests

url = "http://127.0.0.1:5000/process"

advanced_slovakia_questions = [
    # Advanced Economic Questions
    "What is the current inflation rate in Slovakia, and how has it changed over the last 5 years?",
    "What are the key factors contributing to Slovakia’s trade balance, and how has it evolved in the past decade?",
    "What is Slovakia's public debt as a percentage of GDP, and how does it compare to the EU average?",
    "How much foreign direct investment (FDI) has Slovakia attracted in the past 5 years, and which sectors have seen the most investment?",
    "What is the unemployment rate among highly educated workers in Slovakia, and how does it compare to other EU countries?",
    "What is Slovakia's current account balance, and what impact does it have on the country’s economic stability?",

    # Health and Social Development
    "What is the impact of Slovakia’s healthcare system on the overall life expectancy and infant mortality rates compared to other EU countries?",
    "What are the socio-economic determinants of health in Slovakia, and how do they affect different population groups (e.g., rural vs urban, men vs women)?",
    "What is the rate of chronic diseases (e.g., diabetes, heart disease) in Slovakia, and what policies are in place to address them?",
    "How does Slovakia's mental health care system compare to other EU countries in terms of access, affordability, and quality?",
    "What is the prevalence of non-communicable diseases in Slovakia, and how does it impact the country's healthcare expenditures?",

    # Environmental and Sustainability Questions
    "How does Slovakia’s carbon footprint compare to other Central European countries, and what steps is it taking to meet EU climate targets?",
    "What is the current rate of biodiversity loss in Slovakia, and what policies are being implemented to protect endangered species and ecosystems?",
    "What percentage of Slovakia’s agricultural land is dedicated to organic farming, and how does this compare to the EU average?",
    "What is the state of Slovakia’s water resources in terms of availability, quality, and usage, and what challenges does the country face in water management?",
    "How is Slovakia addressing waste management and recycling, and what percentage of its waste is currently being recycled?",

    # Education and Innovation
    "How does Slovakia rank in terms of educational outcomes (e.g., PISA scores) compared to other EU countries?",
    "What is the gap in educational attainment between urban and rural areas in Slovakia, and what policies are being implemented to address it?",
    "What is the current state of research and development (R&D) in Slovakia, and how does it compare to other EU countries in terms of investment and output?",
    "How many Slovak students pursue higher education abroad, and what are the key factors influencing this trend?",
    "What is Slovakia's position in the global innovation index, and what initiatives are driving technological development in the country?",

    # Poverty and Inequality
    "What is the poverty gap in Slovakia, and how does it compare to other EU countries in terms of income inequality?",
    "How has Slovakia’s wealth distribution changed over the last 20 years, and what are the key factors contributing to this shift?",
    "What are the living conditions of the Roma population in Slovakia, and what government policies exist to improve their social inclusion?",
    "What is the rate of child poverty in Slovakia, and what social programs are in place to address it?",
    "How does Slovakia’s income inequality (measured by the Gini coefficient) compare to other EU countries, and what has been the trend in recent years?",

    # International Relations and Global Influence
    "What role does Slovakia play in the European Union's foreign policy, and how has its position evolved in the context of recent global geopolitical changes?",
    "How does Slovakia’s participation in international trade agreements (e.g., EU, WTO) impact its economic performance and growth?",
    "What is Slovakia's foreign aid contribution, and how does it compare to other EU countries in terms of per capita donations?",
    "What are Slovakia's key partnerships in Central Europe, and how do these partnerships influence its regional and global standing?",
    "How does Slovakia’s membership in NATO affect its defense policy and international relations with neighboring countries?",

    # Technology and Digitalization
    "How is Slovakia adopting digital technologies in public services, and what is the level of digital literacy across different age groups?",
    "What percentage of Slovak businesses are engaged in e-commerce, and how does this compare to the EU average?",
    "What is the state of 5G network development in Slovakia, and how is it expected to impact economic and social development in the coming years?",
    "How does Slovakia rank in terms of cybersecurity preparedness, and what are the main challenges the country faces in securing its digital infrastructure?",
    "What initiatives are being implemented to promote the digitalization of Slovakia’s education system, and how effective have these efforts been?"
]


slovakia_questions = [
    # Population and Demographics
    "How many people live in Slovakia right now?",
    "What’s the population growth rate in Slovakia?",
    "What percentage of the population in Slovakia lives in cities?",
    "What’s the average age of people in Slovakia?",
    "How has the population of Slovakia changed over the past 10 years?",

    # Economy
    "What’s the GDP of Slovakia?",
    "How does Slovakia rank in terms of economic size compared to other European countries?",
    "What is the average income per person in Slovakia?",
    "How much of the economy in Slovakia comes from agriculture, industry, or services?",
    "What’s the unemployment rate in Slovakia?",

    # Health
    "What’s the life expectancy in Slovakia?",
    "How many doctors or healthcare workers are there per 1,000 people in Slovakia?",
    "What are the leading causes of death in Slovakia?",
    "What percentage of children in Slovakia are vaccinated against common diseases?",
    "What’s the rate of access to clean water or sanitation in Slovakia?",

    # Education
    "How many people in Slovakia can read and write?",
    "What’s the average number of years people in Slovakia go to school?",
    "How many children are currently enrolled in primary or secondary school in Slovakia?",
    "What percentage of government spending in Slovakia goes to education?",
    "What’s the literacy rate for women in Slovakia compared to men?",



    # Poverty and Inequality
    "What percentage of people in Slovakia live below the poverty line?",
    "How does the income of the richest 10% compare to the poorest 10% in Slovakia?",
    "What’s the unemployment rate among young people in Slovakia?",
    "How much international aid does Slovakia receive each year?",
    "What’s the Gini index for income inequality in Slovakia?",

    # Global Comparisons
    "What is Slovakia’s GDP compared to other countries in Central Europe?",
    "What’s Slovakia’s life expectancy compared to other EU countries?",
    "How has Slovakia made progress in reducing poverty in recent years?",
    "How does Slovakia compare to the global average in education spending?",
    "How is Slovakia performing in terms of adopting renewable energy?"
]

for question in advanced_slovakia_questions:
    data = {"message": question}

    # Send the POST request
    response = requests.post(url, json=data)

    # Print the question
    print('The question is: ' + data["message"])
    max_attempts = 10
    attempt_count = 0
    # Check for critical errors and resend the request if necessary
    while "critical error" in response.text.lower() and attempt_count < max_attempts:
        attempt_count += 1
        response = requests.post(url, json=data)

    print(response.json())