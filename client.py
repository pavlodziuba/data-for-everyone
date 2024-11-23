import requests

url = "http://127.0.0.1:5000/process"


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

    # Environment
    "How much of Slovakia is covered by forests?",
    "What’s the carbon dioxide emission per person in Slovakia?",
    "What percentage of energy in Slovakia comes from renewable sources?",
    "How much freshwater is available per person in Slovakia?",
    "What’s the air quality index in Slovakia or major cities?",

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

for question in slovakia_questions:
    data = {"message": question}

    # Send the POST request
    response = requests.post(url, json=data)

    # Print the question
    print('The question is: ' + data["message"])

    # Check for critical errors and resend the request if necessary
    while "critical error" in response.text.lower():
        response = requests.post(url, json=data)

    print(response.json())