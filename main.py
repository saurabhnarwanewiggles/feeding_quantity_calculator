# IMPORTING LIBRARIES


import streamlit as st
import pandas as pd
from fpdf import FPDF





# CUSTOM FUNCTIONS


def gap():

    st.write("")


def thank_you():

    st.markdown(f" #### <center> 🙏🏻 Thank you {customer_name}, for using our Feeding Quantity Calculator.</center>", unsafe_allow_html = True)

    st.markdown(" ##### <center> ⟳ Refresh the page to check again.</center>", unsafe_allow_html = True)


def generate_pdf():

    pdf = FPDF()



    # PAGE 1 ------------------------------------------------------------------------------



    pdf.add_page()



    # IMAGE -------------------------------------------------------------------------------



    page_width = pdf.w

    image_width = 80

    image_height = 20

    x = (page_width - image_width) / 2

    pdf.image("https://i.ibb.co/j5zt9J8/Top.png", x=x, y=10, w=image_width, h=image_height)



    # BREAK 1 -------------------------------------------------------------------------------



    pdf.ln(40)



    # GAP LINE 1 -------------------------------------------------------------------------------



    pdf.line(25,40,185,40)


    pdf.set_font("Arial", style="B", size=15)

    content_heading = "Feeding Quantity Calculator Report"

    pdf.cell(190, -10, txt=content_heading, ln=True, align="C")


    pdf.line(25,50,185,50)



    # HEADER 1 -------------------------------------------------------------------------------



    pdf.ln(10)

    col_width = 80

    row_height = 6


    page_width = pdf.w - (2 * pdf.l_margin)

    x_start = pdf.l_margin + (page_width - 2 * col_width) / 2


    pdf.set_font("Arial", style="B", size=12)

    table_heading = "1. Basic Information"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["Pet name", str(pet_name)],
        ["Type", str(pet_type)],
        ["Body weight (in kgs)", str(pet_weight)],
        ["Gender", str(pet_gender)],
        ["Breed", str(pet_breed)],
        ["BCS (Body Condition Score)", str(pet_activity)],
        ["Age (in years)", str(pet_age)]
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # HEADER 2 -------------------------------------------------------------------------------



    pdf.set_font("Arial", style="B", size=12)

    table_heading = "2. Medical History"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["Present illnesses or diseases", str(pet_current_disease)],
        ["Last deworming date", str(ldd)],
        ["Appetite status", str(pet_appetite)],
        ["Gastrointestinal health status", str(pet_gastro)],
        ["Renal health status", str(pet_renal)],
        ["Past treatment", str(pet_past_treatment)],
        ["Past illnesses or diseases", str(pet_past_disease)]
    ]

    for row in data:
        
        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # HEADER 3 -------------------------------------------------------------------------------



    pdf.set_font("Arial", style="B", size=12)

    table_heading = "3. RER (Resting Energy Requirements)"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["RER (in kcal/day)", str(round( a, 2))],
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # HEADER 4 -------------------------------------------------------------------------------



    pdf.set_font("Arial", style="B", size=12)

    table_heading = "4. Liquid Food Information"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["Cocotail Rx / Moist Food Pack size (in ml)", str(b)],
        ["Kcal value as per the label information (in kcal)", str(c)],
        ["Warm water is required for blending with food (in ml)", str(d)],
        ["Moisture content in Cocotail Rx (in %)", str(f_percentage)],
        ["Method of food delivery", str(pet_food_delivery)]
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)





    # PAGE 2 ------------------------------------------------------------------------------



    pdf.add_page()



    # IMAGE -------------------------------------------------------------------------------



    page_width = pdf.w

    

    image_width = 80
    
    image_height = 20

    
    x = (page_width - image_width) / 2

    pdf.image("https://i.ibb.co/j5zt9J8/Top.png", x=x, y=10, w=image_width, h=image_height)



    # BREAK 1 -------------------------------------------------------------------------------



    pdf.ln(40)



    # GAP LINE 1 -------------------------------------------------------------------------------



    pdf.line(25,40,185,40)


    pdf.set_font("Arial", style="B", size=15)

    content_heading = "Feeding Quantity Calculator Report - Continued"

    pdf.cell(190, -10, txt=content_heading, ln=True, align="C")


    pdf.line(25,50,185,50)



    # HEADER 5 -------------------------------------------------------------------------------



    pdf.ln(10)

    
    col_width = 80

    row_height = 6


    page_width = pdf.w - (2 * pdf.l_margin)

    x_start = pdf.l_margin + (page_width - 2 * col_width) / 2


    pdf.set_font("Arial", style="B", size=12)

    table_heading = "5. Water Requirement"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["Required daily fluid volume per day (in ml)", str(round( i, 2))]
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # HEADER 6 -------------------------------------------------------------------------------



    pdf.set_font("Arial", style="B", size=12)

    table_heading = "6. Feeding Frequency"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    pdf.cell(page_width, 5, txt="For Dogs: 4 meals/day (Every 6 hr)", ln=True, align="C")
    pdf.cell(page_width, 5, txt="For Cats: 6 meals/day (Every 4 hr)", ln=True, align="C")


    pdf.set_font("Arial", size=9)

    data = [
        ["For day 1, (in ml/meal)", str(round( m_day_1, 2))],
        ["For day 2, (in ml/meal)", str(round( m_day_2, 2))],
        ["For day 3, (in ml/meal)", str(round( m_day_3, 2))]
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # HEADER 7 -------------------------------------------------------------------------------



    pdf.set_font("Arial", style="B", size=12)

    table_heading = "7. Additional Water Requirement (to meet daily fluid volume)"

    pdf.cell(page_width, 25, txt=table_heading, ln=True, align="C")


    pdf.set_font("Arial", size=9)

    pdf.cell(page_width, 5, txt=f"Flush required after every food delivery (in ml/flush) : {n}", ln=True, align="C")
    

    pdf.set_font("Arial", size=9)

    data = [
        ["For day 1, (in ml)", str(round( r_day_1, 2))],
        ["For day 2, (in ml)", str(round( r_day_2, 2))],
        ["For day 3, (in ml)", str(round( r_day_3, 2))]
    ]

    for row in data:

        pdf.set_x(x_start)

        for item in row:

            pdf.cell(col_width, row_height, txt=item, border=1, align="C")

        pdf.ln(row_height)



    # END -------------------------------------------------------------------------------

    pdf.line(25,195,185,195)



    pdf.set_font("Arial", style="B", size=12)

    pdf.cell(page_width, 50, txt= f"Thank you {customer_name}, for using our Feeding Quantity Calculator.", ln=True, align="C")

    pdf.set_font("Arial", style="I", size=10)

    pdf.cell(page_width, -25, txt="Click here to check again.", ln=True, align="C", link="https://wiggles-feedingquantitycalculator.streamlit.app/")


    # OUTPUT -------------------------------------------------------------------------------


    pdf.output(r"Report.pdf")





# PAGE CONFIGURATION


st.set_page_config(
    page_title = "Wiggles I Feeding Quantity Calculator",
    page_icon="data:image/png;base64,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",
    layout="centered"
)





# CUSTOM CSS


hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

reduce_header_and_footer_height_style = """
<style>
    div.block-container {padding-top:2rem;}
    div.block-container {padding-bottom:2rem;}
</style>
"""
st.markdown(reduce_header_and_footer_height_style, unsafe_allow_html=True)

st.markdown(f"""
    <style>
    @import url("style/style.css");
    </style>
""", unsafe_allow_html = True)





# BACKGROUND


st.image(image = "https://i.ibb.co/j5zt9J8/Top.png")

gap()





# QUESTIONNAIRE TITLE


st.markdown("<center><b><font size='5'> 📋 Wiggles I</font> <font size='3'> Pet Feeding Quantity Calculator </font></b></center>", unsafe_allow_html = True   )

st.divider()

gap()





# QUESTIONS





# Section 1. Basic Information





st.markdown("##### 1. Basic Information")

gap()

customer_name = st.text_input("###### ⚫ What is your name?")

gap()

pet_name = st.text_input("###### ⚫ What is your pet's name?")

gap()

pet_type = st.radio(f"###### ⚫ Is the pet a dog or a cat?",["Dog","Cat"], horizontal = True)

gap()

pet_weight = float(st.text_input(f"###### ⚫ What is the pet's body weight? (in kgs)", value = 0, placeholder = "Type the number in kgs..."))

gap()

pet_gender = st.radio(f"###### ⚫ What is the pet's gender?",["Male","Female"], horizontal = True)

gap()

pet_breed = st.text_input(f"###### ⚫ What is the pet's breed?")

gap()

pet_activity = st.slider("###### ⚫ What is the pet's BCS (Body Condition Score)? (1 - Extremely Underweight, 9 - Extremely Obese)", min_value = 1, max_value = 9, value = 1)

gap()

pet_age = st.number_input(f"###### ⚫ What is the pet's age? (in years)", value = None, placeholder = "Type the number in years...")

gap()

st.divider()





# Section 2. Medical History





st.markdown("##### 2. Medical history")

gap()

pet_current_disease = st.text_input("###### ⚫ What illnesses or diseases does the pet have?")

gap()

ldd = st.date_input(f"###### ⚫ What was the pet's last deworming date?", value = None, format = "DD/MM/YYYY")

gap()

pet_appetite = st.text_input("###### ⚫ How is the pet's appetite?")

gap()

pet_gastro = st.text_input("###### ⚫ What is the status of the pet's gastrointestinal health?")

gap()

pet_renal = st.text_input("###### ⚫ What is the status of the pet's renal health?")

gap()

pet_past_treatment = st.text_input("###### ⚫ What was the past treatment provided to the pet? (If any)")

gap()

pet_past_disease = st.text_input("###### ⚫ What illnesses or diseases did the pet have in past? (If any)")

gap()

st.divider()





# Section 3. RER (Resting Energy Requirements) Calculation





st.markdown("##### 3. RER (Resting energy requirements)")

gap()

if pet_type == "Dog":

    if (pet_weight <= 25) and (pet_weight > 2):

        a = 70 + (30 * pet_weight)
    
    elif (pet_weight <= 2 ) or (pet_weight > 25):

        a = 70 * (pet_weight ** 0.75)

elif pet_type == "Cat":

    a = 70 * (pet_weight ** 0.67)

st.write(f" - The RER for the pet is <font size='5'>{round( a, 2)}</font> kcal/day.", unsafe_allow_html = True)

st.divider()





# Section 4. Liquid Food Information





st.markdown("##### 4. Liquid food information")

gap()

st.write("Determine the caloric density of the food or food blend. Liquid foods have a predetermined caloric density (kcal/ml) as stated on the product information sheet. If your food needs to be blended with a liquid (water or liquid food) to create a gruel (food blend) for delivery through a feeding tube or syringe, note that Cocotail Rx does not require additional water or liquid food.")

gap()

b = st.number_input("###### ⚫ What is the Cocotail Rx / Moist Food Pack size? (in ml)", value = 100, placeholder = "Type the number in ml/g...")

gap()

c = st.number_input("###### ⚫ What is the kcal value as per the label information? (in kcal)", value = 120, placeholder = "Type the number in kcal...")

gap()

d = st.number_input("###### ⚫ How much warm water is required for blending with food? (in ml)", placeholder = "Type the number in ml/liter...")

gap()

e = c / ( b + d )

# st.write(f" - The caloric density of fluid is <font size='5'>{e}</font> kcal/ml.", unsafe_allow_html = True)

# gap()

f_percentage = 70

# f_percentage = st.number_input("###### ⚫ What is the moisture content in Cocotail Rx? (in %)", value = 70, placeholder = "Type the number in %...")

# gap()

g = ( b * f_percentage) / 100

# st.write(f" - Therefore, the total water content in Cocotail Rx is <font size='5'>{g}</font> ml.", unsafe_allow_html = True)

# gap()

f_hash = ( g + d ) * 100 / ( b + d )

# st.write(f" - And thus, moisture content after, if <font size='5'>{d}</font> ml warm water added is <font size='5'>{f_hash} %</font>.", unsafe_allow_html = True)

# gap()

h = 100 - g

# st.write(f" - And the total solid content in Cocotail Rx / Moist Food is <font size='5'>{h}</font> gram/s.", unsafe_allow_html = True)

# gap()

methods = ("Bolus Feeding", "Constant Rate Infusion", "Other")

pet_food_delivery = st.selectbox("###### ⚫ What is the method of food delivery?", options = methods, index = None)

gap()

if pet_food_delivery == "Other":

    pet_food_delivery = st.text_input("###### ⚫ Which other method?")

    gap()

st.divider()





# Section 5. The quantity of water in Cocotail Rx / Moist Food Blend





st.markdown("##### 5. Water requirement")

gap()

# st.write(f" - Water content in Cocotail Rx is <font size='5'>{g}</font> ml.", unsafe_allow_html = True)

# gap()

# st.write(f" - Additional water added to the blend is <font size='5'>{d}</font> ml.", unsafe_allow_html = True)

# gap()

i = 60 * pet_weight

st.write(f" - Required daily fluid volume per day is <font size='5'>{round( i, 2)}</font> ml.", unsafe_allow_html = True)

gap()

j = g + d

# st.write(f" - And, total water coming from Cocotail Rx / Moist Food is <font size='5'>{j}</font> ml.", unsafe_allow_html = True)

st.divider()





# Section 6. Provide a feeding protocol






st.markdown("##### 6. Feeding frequency")

gap()

# st.write("##### 6.1 Initial feeding rate.")

# gap()

k_day_1 = ( 30 * a ) / 100

k_day_2 = ( 50 * a ) / 100

k_day_3 = ( 100 * a ) / 100

# st.write(f" - For day 1, the daily caloric intake goal per day is <font size='5'>{k_day_1}</font> kcal.", unsafe_allow_html = True)

# st.write(f" - For day 2, the daily caloric intake goal per day is <font size='5'>{k_day_2}</font> kcal.", unsafe_allow_html = True)

# st.write(f" - For day 3, the daily caloric intake goal per day is <font size='5'>{k_day_3}</font> kcal.", unsafe_allow_html = True)

# gap()

# st.write("##### 6.2 Daily feeding volume.")

# gap()

l_day_1 = k_day_1 / e

l_day_2 = k_day_2 / e

l_day_3 = k_day_3 / e

# st.write(f" - For day 1, the daily feeding volume is <font size='5'>{l_day_1}</font> kcal.", unsafe_allow_html = True)

# st.write(f" - For day 2, the daily feeding volume is <font size='5'>{l_day_2}</font> kcal.", unsafe_allow_html = True)

# st.write(f" - For day 3, the daily feeding volume is <font size='5'>{l_day_3}</font> kcal.", unsafe_allow_html = True)

# gap()

# st.write("##### 6.3 Feeding Frequency")

st.write("For Dogs: 4 meals/day (Every 6 hr)")

st.write("For Cats: 6 meals/day (Every 4 hr)")

if pet_type == "Dog":

    m = 4

elif pet_type == "Cat":

    m = 6

m_day_1 = l_day_1 / m

m_day_2 = l_day_2 / m

m_day_3 = l_day_3 / m

st.write(f" - For day 1, it is <font size='5'>{round( m_day_1, 2)}</font> ml/meal.", unsafe_allow_html = True)

st.write(f" - For day 2, it is <font size='5'>{round( m_day_2, 2)}</font> ml/meal.", unsafe_allow_html = True)

st.write(f" - For day 3, it is <font size='5'>{round( m_day_3, 2)}</font> ml/meal.", unsafe_allow_html = True)

st.divider()

gap()

n = st.slider("###### ⚫ What is the flush required after every food delivery? (in ml/flush)", min_value = 2, max_value = 20, value = 10)

gap()

o = n * m

# st.write(f" - Therefore, the total water used in flushing is <font size='5'>{o}</font> ml", unsafe_allow_html = True)

st.divider()

# gap()

# st.write("##### 6.4 Total water from food.")

p_day_1 = ( l_day_1 * f_hash ) / 100

p_day_2 = ( l_day_2 * f_hash ) / 100

p_day_3 = ( l_day_3 * f_hash ) / 100

# st.write(f" - For day 1, it is <font size='5'>{p_day_1}</font> ml.", unsafe_allow_html = True)

# st.write(f" - For day 2, it is <font size='5'>{p_day_2}</font> ml.", unsafe_allow_html = True)

# st.write(f" - For day 3, it is <font size='5'>{p_day_3}</font> ml.", unsafe_allow_html = True)

# gap()

# st.write("##### 6.5 Total water from food and flushing.")

q_day_1 = o + p_day_1

q_day_2 = o + p_day_2

q_day_3 = o + p_day_3

# st.write(f" - For day 1, it is <font size='5'>{q_day_1}</font> ml.", unsafe_allow_html = True)

# st.write(f" - For day 2, it is <font size='5'>{q_day_2}</font> ml.", unsafe_allow_html = True)

# st.write(f" - For day 3, it is <font size='5'>{q_day_3}</font> ml.", unsafe_allow_html = True)

# gap()

st.write("##### 7. Additional water requirement (To meet daily fluid volume)")

r_day_1 = i - q_day_1

r_day_2 = i - q_day_2

r_day_3 = i - q_day_3

st.write(f" - For day 1, it is <font size='5'>{round( r_day_1, 2)}</font> ml.", unsafe_allow_html = True)

st.write(f" - For day 2, it is <font size='5'>{round( r_day_2, 2)}</font> ml.", unsafe_allow_html = True)

st.write(f" - For day 3, it is <font size='5'>{round( r_day_3, 2)}</font> ml.", unsafe_allow_html = True)

st.divider()

gap()

generate_pdf()

with open("Report.pdf", "rb") as file:

    pdf_bytes = file.read()

if st.download_button("Click here to download the report.", data=pdf_bytes, file_name="Report.pdf", mime="application/pdf", use_container_width = True):

    st.success("Report successfully downloaded.")


st.divider()

thank_you()