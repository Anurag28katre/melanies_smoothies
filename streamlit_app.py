# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
cnx = st.connection("snowflake")
session = cnx.session

# Write directly to the app
st.title(":cup_with_straw:Customize your Smoothie 1 :cup_with_straw:")
st.write(
    """Choose a fruits of which flavour you want your Smoothiee.
    """
)

# option = st.selectbox(
#     "what is your favorite fruit?",
#     ("Banana", "Apple", "Cherry"),
# )

# st.write("You selected:", option)


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruits_option").select(col('FRUITS_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)


ingredient_list = st.multiselect("choose upto 5 ingredients :", my_dataframe)
# st.write(ingredient_list)
# st.text(ingredient_list)

if ingredient_list:
    # st.write(ingredient_list)
    # st.text(ingredient_list)
    
 ingredient_string = ''
for fruit_chosen in ingredient_list:
    ingredient_string += fruit_chosen + ' '
# st.write(ingredient_string)
my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredient_string + """')"""

# st.write(my_insert_stmt)
time_to_insert = st.button("Submit Order")
if time_to_insert:
     session.sql(my_insert_stmt).collect()
     st.success('Your Smoothie is ordered!', icon="✅")
# if ingredient_string:
#     session.sql(my_insert_stmt).collect()
#     st.success('Your Smoothie is ordered!', icon="✅")












