#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[2]:


url = "http://api.weatherapi.com/v1/current.json?key=912b824aadd9412889d230027221306&q=07652&aqi=no"

response = requests.get(url)

data = response.json()


# In[3]:


print(data)


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[4]:


print("The current wind speed in", data['location']['name'], "is", data['current']['wind_mph'], "mph.")


# In[5]:


temp = data['current']['temp_f']
feels = data['current']['feelslike_f']

# print(temp)
# print(feels)

if temp > feels:
    print("It feels", round(temp - feels, 1), "degrees colder.") 
else:
    print("It feels", round(feels - temp, 1), "degrees warmer.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[6]:


# http://api.weatherapi.com/v1/astronomy.json?key={key}={zipcode}={yyyy-mm-dd}


# In[7]:


url = "http://api.weatherapi.com/v1/astronomy.json?key=912b824aadd9412889d230027221306&q=07652&dt=2022-06-14"

response = requests.get(url)

data = response.json()

print(data)


# In[8]:


print(data['astronomy']['astro']['moon_illumination'], "percent of the moon will be visible in", data['location']['name'], "tonight.")


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[22]:


url = "http://api.weatherapi.com/v1/forecast.json?key=912b824aadd9412889d230027221306&q=07652&days=1&aqi=no&alerts=no"

response = requests.get(url)

data = response.json()

dates = (data['forecast']['forecastday'])

high = (date['day']['maxtemp_f'])

low = (date['day']['mintemp_f'])

for date in dates:
    print("The difference between the high and low temperatures in", data['location']['name'], "today is", round(high - low,2), "degrees.")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


# rename url, response, and both sides of forecast_data


# In[ ]:


# forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=912b824aadd9412889d230027221306&q=07652&days=1&aqi=no&alerts=no"

# forecast_response = requests.get(url)

# forecast_data = forecast_response.json()


# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[13]:


url = "http://api.weatherapi.com/v1/forecast.json?key=912b824aadd9412889d230027221306&q=07652&days=3&aqi=no&alerts=no"

response = requests.get(url)

data = response.json()

dates = (data['forecast']['forecastday'])

for date in dates:
    if (date['day']['maxtemp_f']) > 80:
        print("The high on", date['date'], "will be", (date['day']['maxtemp_f']), "degrees; it'll be hot!")
    elif (date['day']['maxtemp_f']) > 70:
        print("The high on", date['date'], "will be", (date['day']['maxtemp_f']), "degrees; it'll be warm.")
    else: 
        print("The high on", date['date'], "will be", (date['day']['maxtemp_f']), "degrees; it'll be cold.")    


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[ ]:


# The API parameter value is for the three days, not seven; so code requires a new url


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[15]:


high = 0

for date in dates:
    if (date['day']['maxtemp_f']) > high:
        high = (date['day']['maxtemp_f'])

for date in dates:    
    if (date['day']['maxtemp_f']) == high:
        print("The three day forecast high on", date['date'], "will be", high, "degrees.")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[27]:


url = "http://api.weatherapi.com/v1/forecast.json?key=912b824aadd9412889d230027221306&q=Miami&days=1&aqi=no&alerts=no"

response = requests.get(url)

data = response.json()

dates = (data['forecast']['forecastday'])

for date in dates:
    for temp_f in date['hour']:
        if temp_f['cloud'] < 50:
            print(temp_f['temp_f'], "on", temp_f['time'])
        else:
            print(temp_f['temp_f'], "on", temp_f['time'], "and cloudy")

#temp_hours = date['hour'][0]['temp_f']

#print(temp_hours)


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[33]:


url = "http://api.weatherapi.com/v1/forecast.json?key=912b824aadd9412889d230027221306&q=Miami&days=1&aqi=no&alerts=no"

response = requests.get(url)

data = response.json()

dates = (data['forecast']['forecastday'])

count = 0

for date in dates:
    for temp_f in date['hour']:
        if temp_f['temp_f'] > 85:
            count = count + 1
            
print("The temp will be over 85 degrees", (count/24)*100, "percent of the time.")


# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


# $4 per month


# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


# share keys

