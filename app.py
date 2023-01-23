import pandas as pd
import streamlit as st
from markdownlit import mdlit
from ranking_restaurants import get_highest_rated_restaurants

# starting streamlit
st.set_page_config(layout="wide", page_title = 'Restaurants')
st.markdown("<h1 style='text-align: center;'>Bangalore Restaurant Analysis</h1>", unsafe_allow_html=True)

# metrics Section
st.cache(show_spinner = False)
def first_section():
    st.markdown("""---""")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Number of Restaurants in **Bangalore**', value = 20808)
    c1.write(' ')
    c1.write(' ')
    c1.metric('One of the most expensive area to eat in **Bangalore**', value = 'Brigade Road')
    c1.write(' ')

    c2.metric('Number of Restaurants with **more than one Outlet**', value = 4684)
    c2.write(' ')
    c2.write(' ')
    c2.metric('Restaurant with the **highest** number of outlets', value = 'Cafe Coffee Day')
    c2.write(' ')

    c3.metric('Number of Restaurants who provide **Online Delivery**', value = 16434)
    c3.write(' ')
    c3.write(' ')
    c3.metric('Most Common Restaurant Type in **Bangalore**', value = 'Quick Bites')
    c3.write(' ')

    c4.metric('Number of Restaurants who has **Online Table Booking**', value = 4719)
    c4.write(' ')
    c4.write(' ')
    c4.metric('Most Common Cuisine in **Bangalore**', value = 'North Indian Food')
    c4.write(' ')

first_section()


# analysis section
st.markdown("""---""")
st.image('image/visualizations/outlets.png')
mdlit("This bar graph represents the number of outlets for various restaurants in Bangalore. The x-axis displays the names of the restaurants, and the y-axis displays the number of outlets for each restaurant. As per the bar chart, [violet]**it is observed that Cafe Coffee Day has the highest number of outlets in Bangalore with 73 outlets, followed by 'Five Star Chicken' with 61 outlets**[/violet]. This highlights the dominance of Cafe Coffee Day in the city's coffee retail market and Five Star Chicken in the quick service restaurant. This data is helpful for anyone looking to understand the restaurant industry in Bangalore and the popularity of different types of restaurants in the city.")
st.write("The graph is useful for anyone interested in understanding the restaurant industry in Bangalore, such as restaurant owners, investors, or city planners. By understanding which restaurants are the most successful in terms of number of outlets, they can gain insight into what types of restaurants are in high demand in the city. Additionally, this graph can also help in identifying the popular localities for restaurants. It's important to note that the data represented in this graph is specific to a certain point in time, and the number of outlets for these restaurants may have changed since the data was collected. Additionally, it is also important to note that the number of outlets is not necessarily indicative of the overall success of a restaurant, as it does not take into account factors such as revenue or customer satisfaction.")

st.markdown("""---""")
st.image('image/visualizations/rating_vs_cost.png')
st.write("This scatter plot represents the relationship between the rating of a restaurant and the cost of dining at that restaurant. Each point on the plot represents a single restaurant, with the x-coordinate representing the cost of dining at that restaurant and the y-coordinate representing the rating of that restaurant.")
mdlit("The graph shows that more expensive restaurants tend to have higher ratings. [green]**This suggests that there may be a positive correlation between the cost of dining at a restaurant and the rating of that restaurant.**[/green] Restaurants with higher prices may offer better quality food, service, or atmosphere. However, it's important to note that this graph is based on a sample of restaurants and the data used to create the plot might not be representative of all restaurants. Additionally, the cost of dining and rating are both affected by various other factors, so it should be used as a general guide and not as a definitive statement about all restaurants.")

st.markdown("""---""")
st.image('image/visualizations/location_vs_cost.png')
st.write("This box plot displays the approximate cost for two people at various locations in a city. The x-axis displays the different locations, and the y-axis displays the approximate cost for two people. Each box on the plot represents the data for a specific location, with the box showing the range of costs, and the line inside the box representing the median cost.")
mdlit("The plot highlights that the locations of [red]**Indranagar**[/red], [violet]**Lavelle Road**[/violet], [blue]**Malleshwaram**[/blue], [red]**Brigade Road**[/red], [orange]**Church Street**[/orange] and [green]**Airport Road**[/green] have the highest cost for two people. This indicates that these areas might be considered as [blue]**premium locations**[/blue] in terms of dining out. The box plot also gives an idea of the spread of the data, and if there are any outliers, or extreme values that are far from the rest of the data. It can be used as a tool for diners looking to budget their meals or restaurant owners looking to understand the pricing trends in the different areas of the city. The plot highlights that the locations of Indranagar, Lavelle Road, Malleshwaram, Brigade Road, Church Street and Airport Road have the highest cost for two people. This indicates that these areas might be considered as premium locations in terms of dining out. The box plot also gives an idea of the spread of the data, and if there are any outliers, or extreme values that are far from the rest of the data. It can be used as a tool for diners looking to budget their meals or restaurant owners looking to understand the pricing trends in the different areas of the city.")

st.markdown("""---""")
st.image('image/visualizations/cost_of_online_vs_inhotel.png')
st.write("This bar plot represents the approximate cost for two people at various locations in a city, with the availability of online ordering as a parameter. The x-axis displays the different locations, and the y-axis displays the approximate cost for two people. The bars on the plot are separated by the availability of online ordering, with one color representing the cost for ordering online and another color representing the cost for ordering in-person.")
mdlit("The plot highlights that ordering online is cheaper in almost all locations. [red]**This suggests that there may be a positive correlation between the availability of online ordering and the cost of dining at a restaurant.**[/red] But what to do if you live in an expensive area like Brigade Road and wants to go out? Well, you can always go to Freazer Town where cost of dining in is less than that of ordering online from Brigde Road.")

st.markdown("""---""")
c1, c2 = st.columns(2)
c1.image('image/visualizations/relation_between_service_and_ratings.png')
c2.write("This box plot represents the relationship between the availability of online ordering and table booking, and the ratings of restaurants. The x-axis displays the different options of online ordering and table booking, with one box representing restaurants that offer both options, another box representing restaurants that offer online ordering only, and another box representing restaurants that offer neither option. The y-axis displays the ratings of the restaurants, with each box representing the range of ratings and the line inside the box representing the median rating.")
with c2:
    mdlit('The plot [blue]**supports the hypothesis that restaurants that offer both online ordering and table booking have higher ratings on average.**[/blue] By comparing the heights of the boxes, it is clear that the box representing the restaurants that offer both options is higher than the other two boxes, indicating that these restaurants have higher ratings. This suggests that offering these convenient options may be positively associated with customer satisfaction. The box plot also gives an idea of the spread of the data, and if there are any outliers, or extreme values that are far from the rest of the data. This information can be useful for restaurant owners looking to improve their ratings by providing convenient options like online ordering and table booking.')
c2.write("It's important to note that this graph is based on a sample of restaurants and the data used to create the plot might not be representative of all restaurants. Additionally, the rating of the restaurant can be based on various factors such as the quality of food, customer service, ambiance and so on. Therefore, it should be used as a general guide and not as a definitive statement about all restaurants.")

st.markdown("""---""")
st.image('image/visualizations/common_rest_types.png')
mdlit('[orange]**The plot shows that the most common type of restaurant in each area is "Quick Bites" while "Food Court", "Meat Shop" and "Beverage Shop" are the least common type of restaurants in Bangalore.**[/orange] This indicates that quick service restaurants are more popular in the city than other types of restaurants. The graph gives an idea of the distribution of different types of restaurants in the different areas of the city. This information can be useful for restaurant owners looking to open a new restaurant in a specific area, as well as for diners looking to find a specific type of restaurant in a specific area.')

st.markdown("""---""")
tab1_viz, tab2_viz = st.tabs(['Areas with Highest number of restaurants', 'Areas with Highest number of expensive restaurants'])
tab1_viz.image('image/visualizations/areas_and_rest_count.png')
tab2_viz.image('image/visualizations/areas_and_exp_rest_count.png')

st.markdown("""---""")
st.image('image/visualizations/favorite_cusines.png')
st.write("This tree map plot, created using the squarify library, represents the top 15 most common cuisines in Bangalore. The size of each rectangle on the plot represents the proportion of restaurants serving that cuisine in the city, with the largest rectangles representing the most common cuisines. The rectangles are color-coded to indicate the different cuisines.")
mdlit("The plot shows that the most common cuisine in Bangalore is [blue]**North Indian**[/blue], followed by [blue]**Chinese**[/blue] cuisine. [violet]**This is an interesting finding as Bangalore is located in South India, where the traditional cuisine is different from North Indian cuisine.**[/violet] This indicates that there is a high demand for North Indian cuisine in the city, possibly due to the large number of migrants from other parts of India, and also the popularity of North Indian food in different parts of the country. The tree map plot also gives an idea of the distribution of different types of cuisines in the city. This information can be useful for restaurant owners looking to open a new restaurant, as well as for diners looking to find a specific type of cuisine.")
st.markdown("""---""")

st.markdown("<h1 style='text-align: center;'>Conclusion</h1>", unsafe_allow_html=True)
mdlit("In conclusion, the collection of plots presented in this project provide a detailed analysis of the restaurant industry in Bangalore. The bar graph of restaurants name (x) and number of outlets (y) showed that 'Cafe Coffee Day' has the highest number of outlets in Bangalore with 73 outlets, followed by 'Five Star Chicken' with 61 outlets. The scatter plot of rating of restaurant and cost of restaurant demonstrated a positive correlation between the cost of dining at a restaurant and the rating of that restaurant. The location wise box plot of approximate cost for two people in that location revealed that Indranagar, Lavelle Road, Malleshwaram, brigade road, church street, Airport Road has the highest cost for two people. The scatter plot of approximate cost for two people, location and online_order demonstrated that ordering online is cheaper in almost all locations. The box plot of online ordering and table booking versus ratings supported the hypothesis that restaurants that offer both online ordering and table booking have higher ratings on average. The bar plot of most common restaurants type in each area showed that the most common type of restaurant in each area is Quick Bites while Food Court, Meat Shop and Beverage Shop are the least common type of restaurants in Bangalore.")
mdlit("The tree map plot of top 15 most common cuisines in bangalore, using squarify, showed that the most common cuisine in Bangalore is North Indian, followed by Chinese cuisine. This is an interesting finding as Bangalore is located in South India, where the traditional cuisine is different from North Indian cuisine.")
mdlit("Overall, the data presented in this project provides valuable insights into the restaurant industry in Bangalore, including the popularity of different types of restaurants, cuisines, and locations, as well as the relationship between cost, rating, online ordering, and table booking. The findings can be used by restaurant owners, investors, and city planners to gain a better understanding of the industry and make informed decisions. Additionally, it can also be used by diners to make informed choices about where and what to eat.")

st.markdown("<h1 style='text-align: center;'>About Me</h1>", unsafe_allow_html=True)
mdlit("My name is [violet]**Adarsh Wase**[/violet]. I am currently pursuing a Master's degree in [blue]**Data Science and Management**[/blue] from [violet]**IIM Indore**[/violet], where I am building on my existing knowledge of Math, Programming, Machine Learning, and MLOps, and learning about key management subjects such as Economics, Operations, Marketing, and Organizational Behavior.")
